from __future__ import annotations

from typing import Final

from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok padi. Biaya angkutnya besar, jadi ada minimum sewa."""

    MINIMUM_HARI_SEWA: Final[int] = 2

    def __init__(
        self, kode: str, nama: str, tarif_harian: int, kapasitas: int
    ) -> None:
        super().__init__(kode, nama, tarif_harian)
        if kapasitas <= 0:
            raise ValueError(
                f"kapasitas harus lebih dari nol, diterima {kapasitas}"
            )
        self._kapasitas = kapasitas

    @property
    def kapasitas(self) -> int:
        return self._kapasitas

    @classmethod
    def from_baris_csv(cls, baris: str) -> Perontok:
        bagian = [nilai.strip() for nilai in baris.split(",")]
        if len(bagian) != 4:
            raise ValueError("Baris CSV Perontok harus memiliki 4 kolom")

        kode, nama, tarif, kapasitas = bagian
        return cls(kode, nama, int(tarif), int(kapasitas))

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Hari yang benar-benar ditagih, memperhitungkan batas minimum."""
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol")
        return max(jumlah_hari, self.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menagih sekurang-kurangnya dua hari, meski disewa lebih singkat."""
        return super().biaya_sewa(self.hari_ditagih(jumlah_hari))
