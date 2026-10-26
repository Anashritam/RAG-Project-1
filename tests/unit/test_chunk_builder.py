# tests/unit/test_chunk_builder.py
import pytest

from knowledgebase_ai.domain.models import TextChunk
from knowledgebase_ai.ingestion.chunk_builder import build_chunks


def test_build_chunks_returns_correct_number_of_chunks():
    chunks = build_chunks(
        text="ABCDEFGHIJKLMNO",
        document_id="doc-1",
        source="test.txt",
        chunk_size=6,
        overlap=2,
    )
    assert len(chunks) == 4
    assert all(isinstance(c, TextChunk) for c in chunks)


def test_build_chunks_assigns_correct_indices():
    chunks = build_chunks(
        text="ABCDEFGHIJKLMNO",
        document_id="doc-1",
        source="test.txt",
        chunk_size=6,
        overlap=2,
    )
    indices = [c.chunk_index for c in chunks]
    assert indices == [0, 1, 2, 3]


def test_build_chunks_calculates_correct_start_offsets():
    chunks = build_chunks(
        text="ABCDEFGHIJKLMNO",
        document_id="doc-1",
        source="test.txt",
        chunk_size=6,
        overlap=2,
    )
    starts = [c.start_char for c in chunks]
    assert starts == [0, 4, 8, 12]


def test_build_chunks_calculates_correct_end_offsets():
    chunks = build_chunks(
        text="ABCDEFGHIJKLMNO",
        document_id="doc-1",
        source="test.txt",
        chunk_size=6,
        overlap=2,
    )
    # end_char is a derived property on the TextChunk model
    ends = [c.end_char for c in chunks]
    # 0+6=6, 4+6=10, 8+6=14, 12+3=15 (last chunk is only 3 chars long)
    assert ends == [6, 10, 14, 15]


def test_build_chunks_propagates_invalid_parameters():
    # overlap >= chunk_size should raise ValueError
    with pytest.raises(ValueError):
        build_chunks(
            text="ABCDEFGHIJKLMNO",
            document_id="doc-1",
            source="test.txt",
            chunk_size=6,
            overlap=6,
        )

    # chunk_size <= 0 should raise ValueError
    with pytest.raises(ValueError):
        build_chunks(
            text="ABCDEFGHIJKLMNO",
            document_id="doc-1",
            source="test.txt",
            chunk_size=0,
            overlap=0,
        )
