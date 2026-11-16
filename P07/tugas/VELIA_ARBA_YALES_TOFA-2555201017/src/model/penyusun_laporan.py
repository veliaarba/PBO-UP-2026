from __future__ import annotations

from src.model.pegawai import Pegawai


class PenyusunLaporan:
    """Mengelola rekapitulasi penghasilan berbagai jenis pegawai."""

    def __init__(self, pegawai: list[Pegawai]) -> None:
        if not pegawai:
            raise ValueError("Daftar pegawai tidak boleh kosong")
        self._pegawai = list(pegawai)

    def rekap_penghasilan(self) -> list[tuple[str, int]]:
        return [
            (pegawai.nama, pegawai.hitung_penghasilan())
            for pegawai in self._pegawai
        ]

    def penghasilan_tertinggi(self) -> tuple[str, int]:
        pegawai_tertinggi = max(
            self._pegawai,
            key=lambda pegawai: pegawai.hitung_penghasilan(),
        )
        return (
            pegawai_tertinggi.nama,
            pegawai_tertinggi.hitung_penghasilan(),
        )

    def penghasilan_terendah(self) -> tuple[str, int]:
        pegawai_terendah = min(
            self._pegawai,
            key=lambda pegawai: pegawai.hitung_penghasilan(),
        )
        return (
            pegawai_terendah.nama,
            pegawai_terendah.hitung_penghasilan(),
        )

    def total_penghasilan(self) -> int:
        return sum(
            pegawai.hitung_penghasilan()
            for pegawai in self._pegawai
        )
