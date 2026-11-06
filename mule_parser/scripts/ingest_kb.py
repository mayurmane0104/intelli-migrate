import sys
import os
from pathlib import Path

# Add the parent directory to Python path so we can import mule_parser
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from mule_parser.kb.local_registry import get_registry

def main():
    print("Connecting to ChromaDB...")
    try:
        reg = get_registry()
    except Exception as e:
        print(f"Failed to connect to ChromaDB: {e}")
        print("Please ensure your ChromaDB Docker container is running and .env variables are set.")
        sys.exit(1)

    if hasattr(reg, "collection"):
        try:
            existing = reg.collection.count()
            if existing > 0:
                print(f"KB already populated ({existing} documents). Skipping ingest.")
                return
        except Exception:
            pass

    kb_dir = project_root / "kb"
    print(f"Scanning for knowledge base files in: {kb_dir}")
    
    if not kb_dir.exists():
        print(f"Error: Knowledge base directory {kb_dir} does not exist.")
        sys.exit(1)
        
    print("Ingesting files into vector database...")
    reg.ingest_kb(str(kb_dir))
    print("Done! Your RAG pipeline is fully populated.")

if __name__ == "__main__":
    main()
