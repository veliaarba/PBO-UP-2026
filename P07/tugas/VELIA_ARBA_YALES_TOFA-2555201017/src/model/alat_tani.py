from __future__ import annotations
from typing import Final

class AlatTani:
    """Kelas induk untuk seluruh alat tani di UPJA."""

    _total_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode or not kode.strip():
            raise ValueError("Kode alat tidak boleh kosong")
        if not nama or not nama.strip():
            raise ValueError("Nama alat tidak boleh kosong")
        if tarif_harian <= 0:
            raise ValueError(f"Tarif harian harus lebih dari nol, diterima {tarif_harian}")
        
        self._kode: Final[str] = kode
        self._nama: Final[str] = nama
        self._tarif_harian: int = tarif_harian
        AlatTani._total_terdaftar += 1

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError(f"Tarif harian harus lebih dari nol, diterima {nilai}")
        self._tarif_harian = nilai

    @property
    def tarif(self) -> int:
        """Alias untuk tarif_harian agar kompatibel dengan tes P05."""
        return self._tarif_harian

    @tarif.setter
    def tarif(self, nilai: int) -> None:
        self.tarif_harian = nilai

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah alat tani yang terdaftar."""
        return cls._total_terdaftar

    @staticmethod
    def format_rupiah(nominal: int) -> str:
        """Format angka ke bentuk rupiah."""
        return f"Rp {nominal:,}".replace(",", ".")

    def keterangan(self) -> str:
        return f"[{self._kode}] {self._nama}"

    def biaya_sewa(self, jumlah_hari: int) -> int:
        if jumlah_hari <= 0:
            raise ValueError(f"Jumlah hari harus lebih dari nol, diterima {jumlah_hari}")
        return self._tarif_harian * jumlah_hari

    def __str__(self) -> str:
        """Untuk dibaca manusia: dipakai print() dan f-string."""
        return self.keterangan()

    def __repr__(self) -> str:
        """Untuk dibaca pemrogram: dipakai saat menampilkan isi koleksi."""
        return (f"{type(self).__name__}(kode={self._kode!r}, "
                f"nama={self._nama!r}, tarif_harian={self._tarif_harian!r})")

    def __eq__(self, lain: object) -> bool:
        """Dua alat dianggap sama bila kodenya sama, karena kode itu identitas."""
        if not isinstance(lain, AlatTani):
            return NotImplemented
        return self._kode == lain._kode

    def __hash__(self) -> int:
        """Wajib ditulis bersama __eq__ agar alat tetap dapat dimasukkan set."""
        return hash(self._kode)