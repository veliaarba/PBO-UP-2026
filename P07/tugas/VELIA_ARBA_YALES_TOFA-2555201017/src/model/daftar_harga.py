from __future__ import annotations

from src.model.alat_tani import AlatTani


class DaftarHarga:
    """Mengelola daftar biaya sewa berbagai jenis alat tani."""

    def __init__(self, alat: list[AlatTani]) -> None:
        if not alat:
            raise ValueError("Daftar alat tidak boleh kosong")
        self._alat = list(alat)

    def biaya_semua(self, jumlah_hari: int) -> list[tuple[str, int]]:
        return [
            (alat.nama, alat.biaya_sewa(jumlah_hari))
            for alat in self._alat
        ]

    def termurah(self, jumlah_hari: int) -> tuple[str, int]:
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol")

        alat_termurah = min(
            self._alat,
            key=lambda alat: alat.biaya_sewa(jumlah_hari),
        )
        return (
            alat_termurah.nama,
            alat_termurah.biaya_sewa(jumlah_hari),
        )

    def total_bila_semua_disewa(self, jumlah_hari: int) -> int:
        return sum(
            alat.biaya_sewa(jumlah_hari)
            for alat in self._alat
        )
