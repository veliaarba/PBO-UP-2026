from __future__ import annotations

from src.model.pegawai import Pegawai


class PegawaiLapangan(Pegawai):
    """Pegawai yang bertugas langsung di lapangan."""

    TUNJANGAN_LAPANGAN: int = 500_000

    def __init__(
        self, nip: str, nama: str, gaji_pokok: int, lokasi_tugas: str
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)
        if not lokasi_tugas or not lokasi_tugas.strip():
            raise ValueError("Lokasi tugas tidak boleh kosong")
        self._lokasi_tugas = lokasi_tugas

    @property
    def lokasi_tugas(self) -> str:
        return self._lokasi_tugas

    def hitung_penghasilan(self, tambahan: int = 0) -> int:
        dasar = super().hitung_penghasilan(tambahan)
        return dasar + self.TUNJANGAN_LAPANGAN
