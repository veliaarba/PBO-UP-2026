from __future__ import annotations

from typing import Final

from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Pompa air bermesin. Penyewa dikenakan biaya solar sesuai debitnya."""

    HARGA_SOLAR_PER_LITER: Final[int] = 7_000
    LITER_PER_SERATUS_DEBIT: Final[int] = 3

    def __init__(
        self, kode: str, nama: str, tarif_harian: int, debit: int
    ) -> None:
        super().__init__(kode, nama, tarif_harian)
        if debit <= 0:
            raise ValueError(
                f"debit harus lebih dari nol, diterima {debit}"
            )
        self._debit = debit

    @property
    def debit(self) -> int:
        return self._debit

    @classmethod
    def from_baris_csv(cls, baris: str) -> PompaAir:
        bagian = [nilai.strip() for nilai in baris.split(",")]
        if len(bagian) != 4:
            raise ValueError("Baris CSV PompaAir harus memiliki 4 kolom")

        kode, nama, tarif, debit = bagian
        return cls(kode, nama, int(tarif), int(debit))

    def konsumsi_solar_harian(self) -> int:
        """Perkiraan pemakaian solar dalam liter untuk satu hari."""
        return (
            self._debit * self.LITER_PER_SERATUS_DEBIT
        ) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Biaya dasar ditambah biaya solar selama hari sewa."""
        dasar = super().biaya_sewa(jumlah_hari)
        solar = (
            self.konsumsi_solar_harian()
            * jumlah_hari
            * self.HARGA_SOLAR_PER_LITER
        )
        return dasar + solar
