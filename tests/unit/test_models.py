from dataclasses import FrozenInstanceError

import pytest

from knowledgebase_ai.domain.models import TextChunk


def test_end_char_calculated_correctly():
    chunk = TextChunk(
        document_id="doc-001",
        chunk_index=0,
        text="A database transaction ensures...",
        source="database-guide.pdf",
        start_char=10,
        page_number=3,
    )
    # start_char (10) + len(text) (33) = 43
    assert chunk.end_char == 43


def test_empty_chunk_has_same_start_and_end_offsets():
    chunk = TextChunk(
        document_id="doc-002", chunk_index=1, text="", source="empty.txt", start_char=50
    )
    assert chunk.start_char == chunk.end_char
    assert chunk.end_char == 50


def test_page_number_defaults_to_none():
    chunk = TextChunk(
        document_id="doc-003",
        chunk_index=0,
        text="Some text from a txt file.",
        source="notes.txt",
        start_char=0,
    )
    assert chunk.page_number is None


def test_reassigning_field_raises_error():
    chunk = TextChunk(
        document_id="doc-004",
        chunk_index=0,
        text="Immutable text.",
        source="test.txt",
        start_char=0,
    )

    # Attempting to mutate a frozen dataclass should raise FrozenInstanceError
    with pytest.raises(FrozenInstanceError):
        chunk.text = "Mutated text!"
