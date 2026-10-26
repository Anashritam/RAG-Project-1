from knowledgebase_ai.domain.models import TextChunk
from knowledgebase_ai.ingestion.chunker import chunk_text


def build_chunks(
    text: str,
    document_id: str,
    source: str,
    chunk_size: int,
    overlap: int,
) -> list[TextChunk]:

    raw_chunks = chunk_text(text, chunk_size, overlap)

    if not raw_chunks:
        return []

    step = chunk_size - overlap
    text_chunks = []

    for i, raw_text in enumerate(raw_chunks):
        start_char = i * step
        text_chunks.append(
            TextChunk(
                document_id=document_id,
                chunk_index=i,
                text=raw_text,
                source=source,
                start_char=start_char,
                page_number=None,
            )
        )

    return text_chunks
