def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    # Invalid configuration
    if chunk_size <= 0:
        raise ValueError(f"chunk_size must be > 0, got {chunk_size}")
    if overlap < 0:
        raise ValueError(f"overlap must be >= 0, got {overlap}")
    if overlap >= chunk_size:
        raise ValueError(
            f"overlap ({overlap}) must be strictly less than chunk_size ({chunk_size})"
        )

    # Return empty list for enpty text
    if not text:
        return []

    chunks = []
    step = chunk_size - overlap
    start = 0
    text_length = len(text)

    while start < text_length:
        chunk = text[start : start + chunk_size]
        chunks.append(chunk)

        start += step

    return chunks
