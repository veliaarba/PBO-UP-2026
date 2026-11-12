from __future__ import annotations

from src.model.pegawai import Pegawai


class PegawaiPenyuluh(Pegawai):
    """Pegawai yang bertugas melakukan kegiatan penyuluhan."""

    HONOR_PER_KEGIATAN: int = 150_000

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        jumlah_kegiatan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)
        if jumlah_kegiatan < 0:
            raise ValueError("Jumlah kegiatan tidak boleh negatif")
        self._jumlah_kegiatan = jumlah_kegiatan

    @property
    def jumlah_kegiatan(self) -> int:
        return self._jumlah_kegiatan

    def hitung_penghasilan(self, tambahan: int = 0) -> int:
        honor = self._jumlah_kegiatan * self.HONOR_PER_KEGIATAN
        return super().hitung_penghasilan(tambahan) + honor
