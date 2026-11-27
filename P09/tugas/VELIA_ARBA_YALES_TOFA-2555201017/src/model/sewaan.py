from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Sewaan(Protocol):
    """Kontrak untuk objek yang dapat disewakan."""

    @property
    def kode(self) -> str:
        ...

    @property
    def nama(self) -> str:
        ...

    def biaya_sewa(self, jumlah_hari: int) -> int:
        ...

    def keterangan(self) -> str:
        ...