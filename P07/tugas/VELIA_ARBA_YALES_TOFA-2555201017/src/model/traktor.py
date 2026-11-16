from __future__ import annotations

from typing import Final

from src.model.alat_tani import AlatTani


class Traktor(AlatTani):
    """Traktor roda dua. Wajib dioperasikan petugas UPJA."""

    ONGKOS_OPERATOR_HARIAN: Final[int] = 100_000

    def __init__(
        self, kode: str, nama: str, tarif_harian: int, tenaga_kuda: int
    ) -> None:
        super().__init__(kode, nama, tarif_harian)
        if tenaga_kuda <= 0:
            raise ValueError(
                f"tenaga kuda harus lebih dari nol, diterima {tenaga_kuda}"
            )
        self._tenaga_kuda = tenaga_kuda

    @property
    def tenaga_kuda(self) -> int:
        return self._tenaga_kuda

    @classmethod
    def from_baris_csv(cls, baris: str) -> Traktor:
        bagian = [nilai.strip() for nilai in baris.split(",")]
        if len(bagian) != 4:
            raise ValueError("Baris CSV Traktor harus memiliki 4 kolom")

        kode, nama, tarif, tenaga_kuda = bagian
        return cls(kode, nama, int(tarif), int(tenaga_kuda))

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Biaya dasar ditambah ongkos operator untuk setiap hari sewa."""
        dasar = super().biaya_sewa(jumlah_hari)
        return dasar + (self.ONGKOS_OPERATOR_HARIAN * jumlah_hari)
