from __future__ import annotations
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class PeriodeTugas:
    """Objek nilai periode tugas yang tidak dapat diubah."""
    tanggal_mulai: str
    tanggal_selesai: str

    def __post_init__(self) -> None:
        try:
            date.fromisoformat(self.tanggal_mulai)
            date.fromisoformat(self.tanggal_selesai)
        except ValueError:
            raise ValueError("Format tanggal harus YYYY-MM-DD")