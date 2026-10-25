from dataclasses import dataclass


@dataclass(frozen=True)
class TextChunk:
    document_id: str
    chunk_index: int
    text: str
    source: str
    start_char: int
    page_number: int | None = None

    @property
    def end_char(self) -> int:
        return self.start_char + len(self.text)
