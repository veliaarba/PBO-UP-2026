from enum import Enum


class StatusSewa(Enum):
    """Status dalam transaksi penyewaan."""

    DIPESAN = "dipesan"
    BERJALAN = "berjalan"
    SELESAI = "selesai"
    BATAL = "batal"

    def boleh_diubah(self) -> bool:
        """Menentukan apakah transaksi masih boleh diubah."""
        return self in (
            StatusSewa.DIPESAN,
            StatusSewa.BERJALAN,
        )