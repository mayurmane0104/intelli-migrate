from __future__ import annotations

from pathlib import Path

from mule_parser.knowledge_base.chunking import split_text
from mule_parser.knowledge_base.ingest import ingest_knowledge_base, load_default_kb
from mule_parser.knowledge_base.opensearch import build_opensearch_index_mappings
from mule_parser.knowledge_base.registry import KnowledgeBaseRegistry
from mule_parser.knowledge_base.retrieval import SearchRequest, get_index_mappings, list_domains, search


def test_split_text_respects_chunk_size_and_overlap():
    text = " ".join(["mule"] * 500)
    chunks = split_text(text, chunk_size=1000, overlap=200)

    assert chunks
    assert all(len(chunk) <= 1000 for chunk in chunks)
    assert len(chunks) >= 2
    assert set(chunks[0].split()[-20:]).intersection(chunks[1].split())


def test_ingestion_builds_artifacts(tmp_path: Path):
    samples = Path(__file__).resolve().parents[1] / "knowledge_base" / "samples"
    sources = [str(path) for path in sorted(samples.glob("*")) if path.is_file()]

    result = ingest_knowledge_base(sources, output_dir=tmp_path)

    assert result.report.document_count >= 10
    assert result.report.chunk_count >= 10
    assert result.index_mappings["mappings"]["properties"]["embedding"]["type"] == "knn_vector"
    assert (tmp_path / "documents.json").exists()
    assert (tmp_path / "chunks.json").exists()
    assert (tmp_path / "manifest.json").exists()
    assert (tmp_path / "opensearch_index_mappings.json").exists()


def test_default_kb_registry_search_returns_relevant_mappings(tmp_path: Path):
    artifact = load_default_kb(output_dir=tmp_path)
    registry = KnowledgeBaseRegistry.from_chunks(artifact.chunks)

    http_results = registry.search("HTTP Listener mapping", kb_type="aws_mapping_kb", top_k=3)
    scheduler_results = registry.search("Scheduler EventBridge", kb_type="aws_mapping_kb", top_k=3)

    assert http_results
    assert scheduler_results
    assert any("API Gateway" in result.text for result in http_results)
    assert any("EventBridge" in result.text for result in scheduler_results)


def test_opensearch_mappings_include_kb_fields():
    mappings = build_opensearch_index_mappings(dimensions=384)

    props = mappings["mappings"]["properties"]
    assert props["chunk_id"]["type"] == "keyword"
    assert props["domain"]["type"] == "keyword"
    assert props["tags"]["type"] == "keyword"
    assert mappings["settings"]["index"]["knn"] is True


def test_retrieval_api_exposes_domains_and_search():
    assert "mule_component_kb" in list_domains()["domains"]

    response = search(SearchRequest(query="HTTP Listener API Gateway", kb_type="aws_mapping_kb", top_k=3))
    assert response.results
    assert any("API Gateway" in item["text"] for item in response.results)
    assert get_index_mappings()["mappings"]["properties"]["embedding"]["type"] == "knn_vector"
