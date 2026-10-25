import pytest

from knowledgebase_ai.ingestion.chunker import chunk_text


def test_chunk_text_with_overlap():
    result = chunk_text(
        "ABCDEFGHIJKLMNO",
        chunk_size=6,
        overlap=2,
    )
    assert result == [
        "ABCDEF",
        "EFGHIJ",
        "IJKLMN",
        "MNO",
    ]


def test_returns_empty_list_for_empty_text():
    assert chunk_text("", chunk_size=6, overlap=2) == []


def test_returns_one_chunk_for_short_text():
    assert chunk_text("Hello", chunk_size=10, overlap=2) == ["Hello"]


def test_returns_exact_chunks_with_zero_overlap():
    result = chunk_text("ABCDEF", chunk_size=3, overlap=0)
    assert result == ["ABC", "DEF"]


@pytest.mark.parametrize(
    ("chunk_size", "overlap"),
    [
        (0, 0),  # chunk_size is 0
        (-1, 0),  # chunk_size is negative
        (6, -1),  # overlap is negative
        (6, 6),  # overlap equals chunk_size (step size would be 0)
        (6, 7),  # overlap is greater than chunk_size
    ],
)
def test_rejects_invalid_configuration(chunk_size, overlap):
    with pytest.raises(ValueError):
        chunk_text("ABCDEFGHIJKLMNO", chunk_size=chunk_size, overlap=overlap)
