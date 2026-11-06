import os
from pathlib import Path
from typing import List, Dict, Any, Optional

import yaml

try:
    import chromadb
    from chromadb.config import Settings
    from chromadb.utils import embedding_functions

    CHROMADB_AVAILABLE = True
except ImportError:
    chromadb = None  # type: ignore[assignment,misc]
    Settings = None  # type: ignore[assignment,misc]
    embedding_functions = None  # type: ignore[assignment,misc]
    CHROMADB_AVAILABLE = False

# Use Chroma's built-in ONNX MiniLM embedder (no sentence-transformers / PyTorch).
def _default_embedding_function():
    if not CHROMADB_AVAILABLE or embedding_functions is None:
        return None
    try:
        return embedding_functions.DefaultEmbeddingFunction()
    except Exception:
        try:
            return embedding_functions.ONNXMiniLM_L6_V2()
        except Exception:
            try:
                return embedding_functions.SentenceTransformerEmbeddingFunction(
                    model_name="all-MiniLM-L6-v2",
                )
            except Exception:
                return None


hf_ef = _default_embedding_function()


class NoOpKBRegistry:
    """Fallback when ChromaDB is not installed or unreachable (e.g. slim Docker image)."""

    def search(self, query: str, top_k: int = 3, domain: Optional[str] = None) -> List[Dict[str, Any]]:
        return []

    def ingest_kb(self, kb_dir: str) -> None:
        print("Skipping KB ingest: ChromaDB not available")


class LocalKBRegistry:
    """
    Connects to an externally managed ChromaDB instance using credentials
    from the environment. Embeddings are generated locally using SentenceTransformers
    to save API costs and improve privacy.
    """

    def __init__(self):
        if not CHROMADB_AVAILABLE or chromadb is None or Settings is None:
            raise RuntimeError("ChromaDB is not installed")

        host = os.environ.get("CHROMA_HOST", "localhost")
        port = os.environ.get("CHROMA_PORT", "8000")
        auth_token = os.environ.get("CHROMA_AUTH_TOKEN")

        settings = Settings()
        if auth_token:
            settings.chroma_client_auth_provider = "chromadb.auth.token.TokenAuthClientProvider"
            settings.chroma_client_auth_credentials = auth_token

        self.client = chromadb.HttpClient(
            host=host,
            port=port,
            settings=settings,
        )

        self.collection = self.client.get_or_create_collection(
            name="mule_migration_kb",
            embedding_function=hf_ef,
        )

    def search(self, query: str, top_k: int = 3, domain: Optional[str] = None) -> List[Dict[str, Any]]:
        where_clause = {}
        if domain:
            where_clause = {"domain": domain}

        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
            where=where_clause if where_clause else None,
        )

        formatted_results = []
        if results and results.get("documents") and len(results["documents"]) > 0:
            docs = results["documents"][0]
            metas = results["metadatas"][0] if results.get("metadatas") else [{}] * len(docs)
            for doc, meta in zip(docs, metas):
                formatted_results.append({
                    "content": doc,
                    "metadata": meta,
                })
        return formatted_results

    def ingest_kb(self, kb_dir: str):
        base_path = Path(kb_dir)
        documents = []
        metadatas = []
        ids = []

        files = []
        for ext in ["*.md", "*.yaml", "*.yml"]:
            files.extend(base_path.rglob(ext))

        total_files = len(files)
        print(f"Found {total_files} files. Reading contents...")

        for file_path in files:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if not content.strip():
                continue

            domain = file_path.parent.name
            doc_id = f"{domain}_{file_path.name}"

            documents.append(content)
            metadatas.append({
                "source": str(file_path.name),
                "domain": domain,
                "type": file_path.suffix.lstrip("."),
            })
            ids.append(doc_id)

        if not documents:
            print("No valid documents found to ingest.")
            return

        total_docs = len(documents)
        batch_size = 50
        print(f"Starting ingestion of {total_docs} documents (Batch size: {batch_size})...")

        for i in range(0, total_docs, batch_size):
            end_idx = min(i + batch_size, total_docs)
            batch_docs = documents[i:end_idx]
            batch_metas = metadatas[i:end_idx]
            batch_ids = ids[i:end_idx]

            print(f"  -> Ingesting {i + 1} to {end_idx} of {total_docs} ({(end_idx / total_docs) * 100:.1f}%) ...")
            self.collection.upsert(
                documents=batch_docs,
                metadatas=batch_metas,
                ids=batch_ids,
            )

        print(f"Successfully ingested {total_docs} documents into ChromaDB.")


_registry = None


def get_registry() -> LocalKBRegistry | NoOpKBRegistry:
    global _registry
    if _registry is None:
        if CHROMADB_AVAILABLE:
            try:
                _registry = LocalKBRegistry()
            except Exception as exc:
                print(f"ChromaDB unavailable ({exc}); KB search disabled.")
                _registry = NoOpKBRegistry()
        else:
            _registry = NoOpKBRegistry()
    return _registry
