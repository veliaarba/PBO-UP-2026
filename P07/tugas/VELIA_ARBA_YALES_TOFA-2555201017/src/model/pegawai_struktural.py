from __future__ import annotations

from src.model.pegawai import Pegawai


class PegawaiStruktural(Pegawai):
    """Pegawai yang memiliki jabatan struktural."""

    TUNJANGAN_PER_TINGKAT: int = 300_000

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tingkat_jabatan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)
        if tingkat_jabatan <= 0:
            raise ValueError("Tingkat jabatan harus lebih dari nol")
        self._tingkat_jabatan = tingkat_jabatan

    @property
    def tingkat_jabatan(self) -> int:
        return self._tingkat_jabatan

    def hitung_penghasilan(self, tambahan: int = 0) -> int:
        tambahan_jabatan = (
            tambahan + self._tingkat_jabatan * self.TUNJANGAN_PER_TINGKAT
        )
        return super().hitung_penghasilan(tambahan_jabatan)
