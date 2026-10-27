
"""Kelas Kios untuk pendataan produk UMKM."""

from typing import Final


class Kios:
    """Mewakili satu produk yang dijual oleh kios UMKM."""

    MARGIN_MINIMUM: Final[float] = 0.10
    HARGA_MINIMUM: Final[int] = 1
    HARGA_MAKSIMUM: Final[int] = 100_000_000
    JUMLAH_KOLOM_BARIS: Final[int] = 4

    _jumlah_terdaftar: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_modal: int,
        harga_jual: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("Kode produk tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama produk tidak boleh kosong.")
        if harga_modal < self.HARGA_MINIMUM:
            raise ValueError("Harga modal harus lebih dari nol.")
        if not self.harga_wajar(harga_jual):
            raise ValueError("Harga jual tidak wajar.")
        if harga_jual < harga_modal * (
            1 + self.MARGIN_MINIMUM
        ):
            raise ValueError("Harga jual belum memenuhi margin minimum.")

        self._kode = kode
        self._nama = nama
        self._harga_modal = harga_modal
        self._harga_jual = harga_jual

        Kios._jumlah_terdaftar += 1

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Kios:
        """Membuat produk dari baris teks berkoma."""
        bagian = [nilai.strip() for nilai in baris.split(",")]

        if len(bagian) != cls.JUMLAH_KOLOM_BARIS:
            raise ValueError("Baris harus berisi empat bagian.")

        try:
            harga_modal = int(bagian[2])
            harga_jual = int(bagian[3])
        except ValueError as exc:
            raise ValueError("Harga harus berupa bilangan bulat.") from exc

        return cls(bagian[0], bagian[1], harga_modal, harga_jual)

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah produk yang berhasil didaftarkan."""
        return cls._jumlah_terdaftar

    @staticmethod
    def harga_wajar(harga: int) -> bool:
        """Memeriksa apakah harga berada dalam rentang yang wajar."""
        return Kios.HARGA_MINIMUM <= harga <= Kios.HARGA_MAKSIMUM

    @staticmethod
    def format_rupiah(harga: int) -> str:
        """Mengubah angka menjadi teks berformat rupiah."""
        return f"Rp{harga:,.0f}".replace(",", ".")

    def ringkasan(self) -> str:
        """Menghasilkan ringkasan produk dengan kolom harga rata."""
        return (
            f"{self._kode:<10} {self._nama:<24} "
            f"{self.format_rupiah(self._harga_jual):>15}"
        )
