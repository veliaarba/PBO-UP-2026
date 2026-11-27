"""Model domain: rincian baris penyewaan alat."""

from src.model.sewaan import Sewaan


class BarisSewa:
    """Satu objek sewaan dalam satu transaksi."""

    def __init__(self, alat: Sewaan, jumlah_hari: int) -> None:
        if jumlah_hari <= 0:
            raise ValueError(
                f"jumlah hari harus lebih dari nol, diterima {jumlah_hari}"
            )

        self._alat = alat
        self._jumlah_hari = jumlah_hari
        self._kode_alat = alat.kode
        self._nama_alat = alat.nama

    def subtotal(self) -> int:
        """Menghitung subtotal berdasarkan biaya sewa objek."""
        return self._alat.biaya_sewa(self._jumlah_hari)

    @property
    def kode_alat(self) -> str:
        return self._kode_alat

    @property
    def nama_alat(self) -> str:
        return self._nama_alat

    @property
    def durasi_hari(self) -> int:
        return self._jumlah_hari

    @durasi_hari.setter
    def durasi_hari(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError("Durasi hari harus lebih dari nol")
        self._jumlah_hari = nilai

    def baris_nota(self) -> str:
        biaya = self.subtotal()
        return (
            f"{self._nama_alat} "
            f"{self._jumlah_hari} hr "
            f"x Rp{biaya:,}".replace(",", ".")
        )