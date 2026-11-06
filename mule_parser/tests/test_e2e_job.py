import os
import time
import urllib.request
import json

def main():
    print("Starting E2E Job Verification...")
    
    # 1. Create dummy project
    project_path = '/tmp/test-mule-app'
    os.makedirs(f'{project_path}/src/main/mule', exist_ok=True)
    with open(f'{project_path}/src/main/mule/runtime.xml', 'w') as f:
        f.write('''<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core" xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.mulesoft.org/schema/mule/core http://www.mulesoft.org/schema/mule/core/current/mule.xsd">
  <flow name="test-e2e-flow">
    <logger message="Hello E2E" level="INFO" />
  </flow>
</mule>''')

    # 2. Trigger POST /internal/projects/test-project-e2e/analysis
    url = 'http://localhost:8000/internal/projects/test-project-e2e/analysis'
    payload = {'sourcePath': project_path, 'requestedBy': 'e2e-verifier'}
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            job = json.loads(resp.read().decode())
            print(f"POST {url} response: {job}")
            job_id = job.get('jobId')
            if not job_id:
                print("Error: No jobId returned!")
                return
    except Exception as exc:
        print(f"Failed to post analysis job: {exc}")
        return

    # 3. Poll /internal/projects/test-project-e2e/analysis/latest until completed
    latest_url = 'http://localhost:8000/internal/projects/test-project-e2e/analysis/latest'
    print(f"Polling job status via {latest_url}...")
    for i in range(20):
        time.sleep(2)
        try:
            with urllib.request.urlopen(latest_url) as get_resp:
                latest = json.loads(get_resp.read().decode())
                status = latest.get('status')
                progress = latest.get('progressPct')
                error = latest.get('error')
                print(f"Poll #{i+1}: status={status}, progress={progress}%, error={error}")
                if status in ('completed', 'failed'):
                    print(f"Job finished with status: {status}")
                    break
        except Exception as exc:
            print(f"Error polling job status: {exc}")

if __name__ == '__main__':
    main()
