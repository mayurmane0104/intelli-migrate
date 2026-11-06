# Security - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/security](https://docs.aws.amazon.com/powertools/python/latest/security)

---

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Allowed

Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice.

Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our Cookie Notice.

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form here.

For more information about how AWS handles your information, read the AWS Privacy Notice.

Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Within our releases page, you will notice a new metadata file: multiple.intoto.jsonl. It's metadata to describe where, when, and how our build artifacts were produced - or simply, attestation in SLSA terminology.

For this to be useful, we need a verification tool - SLSA Verifier. SLSA Verifier decodes attestation to confirm the authenticity, identity, and the steps we took in our release pipeline (e.g., inputs, git commit/branch, GitHub org/repo, build SHA256, etc.).

#!/bin/bashset-uopipefail# prevent accessing unset env vars, prevent masking pipeline errors to the next command#docs#title :verify_provenance.sh#description :This script will download and verify a signed Powertools for AWS Lambda (Python) release build with SLSA Verifier#author :@heitorlessa#date :July 1st 2023#version :0.1#usage :bash verify_provenance.sh {release version}#notes :Meant to use in GitHub Actions or locally (MacOS, Linux, WSL).#os_version :Ubuntu 22.04.2 LTS#==============================================================================# Check if RELEASE_VERSION is provided as a command line argumentif[[$#-eq1]];thenexportreadonlyRELEASE_VERSION="$1"elseecho"ERROR: Please provider Powertools release version as a command line argument."echo"Example: bash verify_provenance.sh 2.20.0"exit1fiexportreadonlyARCHITECTURE=$(uname-m|sed's/x86_64/amd64/g')# arm64, x86_64 ->amd64exportreadonlyOS_NAME=$(uname-s|tr'[:upper:]''[:lower:]')# darwin, linuxexportreadonlySLSA_VERIFIER_VERSION="2.3.0"exportreadonlySLSA_VERIFIER_CHECKSUM_FILE="SHA256SUM.md"exportreadonlySLSA_VERIFIER_BINARY="./slsa-verifier-${OS_NAME}-${ARCHITECTURE}"exportreadonlyRELEASE_BINARY="aws_lambda_powertools-${RELEASE_VERSION}-py3-none-any.whl"exportreadonlyORG="aws-powertools"exportreadonlyREPO="powertools-lambda-python"exportreadonlyPROVENANCE_FILE="multiple.intoto.jsonl"exportreadonlyFILES=("${SLSA_VERIFIER_BINARY}""${SLSA_VERIFIER_CHECKSUM_FILE}""${PROVENANCE_FILE}""${RELEASE_BINARY}")functiondebug(){TIMESTAMP=$(date-u"+%FT%TZ")# 2023-05-10T07:53:59Zecho""${TIMESTAMP}" DEBUG - [*] $1"}functionerror(){cleanup
TIMESTAMP=$(date-u"+%FT%TZ")# 2023-05-10T07:53:59Zecho""${TIMESTAMP}" ERROR - [!] $1"echo""${TIMESTAMP}" ERROR - [!] exiting"exit1}functiondownload_slsa_verifier(){readonlySLSA_URL="https://github.com/slsa-framework/slsa-verifier/releases/download/v${SLSA_VERIFIER_VERSION}/slsa-verifier-${OS_NAME}-${ARCHITECTURE}"# debug "Downloading SLSA Verifier for - Binary: slsa-verifier-${OS_NAME}-${ARCHITECTURE}"debug"Downloading SLSA Verifier binary: ${SLSA_URL}"curl\--location\--fail\--silent\-O"${SLSA_URL}"||error"Failed to download SLSA Verifier binary"readonlySLSA_CHECKSUM_URL="https://raw.githubusercontent.com/slsa-framework/slsa-verifier/f59b55ef2190581d40fc1a5f3b7a51cab2f4a652/${SLSA_VERIFIER_CHECKSUM_FILE}"debug"Downloading SLSA Verifier checksums"curl\--location\--fail\--silent\-O"${SLSA_CHECKSUM_URL}"||error"Failed to download SLSA Verifier binary checksum file"debug"Verifying SLSA Verifier binary integrity"CURRENT_HASH=$(sha256sum"${SLSA_VERIFIER_BINARY}"|awk'{print $1}')if[[$(grep"${CURRENT_HASH}""${SLSA_VERIFIER_CHECKSUM_FILE}")]];thendebug"SLSA Verifier binary integrity confirmed"chmod+x"${SLSA_VERIFIER_BINARY}"elseerror"Failed integrity check for SLSA Verifier binary: ${SLSA_VERIFIER_BINARY}"fi}functiondownload_provenance(){readonlyPROVENANCE_URL="https://github.com/${ORG}/${REPO}/releases/download/v${RELEASE_VERSION}/${PROVENANCE_FILE}"debug"Downloading attestation: ${PROVENANCE_URL}"curl\--location\--fail\--silent\-O${PROVENANCE_URL}||error"Failed to download provenance. Does the release already exist?"}functiondownload_release_artifact(){debug"Downloading ${RELEASE_VERSION} release from PyPi"python-mpipdownload\--only-binary=:all:\--no-deps\--quiet\aws-lambda-powertools=="${RELEASE_VERSION}"}functionverify_provenance(){debug"Verifying attestation with slsa-verifier""${SLSA_VERIFIER_BINARY}"verify-artifact\--provenance-path"${PROVENANCE_FILE}"\--source-urigithub.com/${ORG}/${REPO}\${RELEASE_BINARY}}functioncleanup(){debug"Cleaning up previously downloaded files"rm-f"${SLSA_VERIFIER_BINARY}"rm-f"${SLSA_VERIFIER_CHECKSUM_FILE}"rm-f"${PROVENANCE_FILE}"rm-f"${RELEASE_BINARY}"echo"${FILES[@]}"|xargs-n1echo"Removed file: "}functionmain(){download_slsa_verifier
download_provenance
download_release_artifact
verify_provenance
cleanup
}
main
# Lessons learned## 1. If source doesn't match provenance## FAILED: SLSA verification failed: source used to generate the binary does not match provenance: expected source 'awslabs/aws-lambda-powertools-python', got 'heitorlessa/aws-lambda-powertools-test'## 2. Avoid building deps during download in Test registry endpoints## FAILED: Could not find a version that satisfies the requirement poetry-core>=1.3.2 (from versions: 1.2.0)#