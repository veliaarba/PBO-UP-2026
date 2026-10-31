"""Model alat pertanian yang disewakan."""
from typing import Final

class AlatTani:
    """Mewakili alat pertanian yang disewakan."""
    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"
    JUMLAH_KOLOM_CSV: Final[int] = 3
    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise ValueError("kode alat tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama alat tidak boleh kosong")
        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian
        AlatTani._jumlah_terdaftar += 1

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
        if not AlatTani.tarif_wajar(nilai):
            raise ValueError(
                f"tarif harus antara "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)} dan "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)}, "
                f"diterima {nilai}"
            )
        self._tarif_harian = nilai

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "AlatTani":
        """Membuat alat dari satu baris pendataan."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)
        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError(
                f"baris harus berisi {cls.JUMLAH_KOLOM_CSV} bagian, "
                f"diterima {len(bagian)}: '{baris}'"
            )
        kode, nama, tarif = bagian
        if not tarif.strip().isdigit():
            raise ValueError(f"tarif harus berupa angka, diterima '{tarif}'")
        return cls(kode.strip(), nama.strip(), int(tarif))

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return self._tarif_harian * jumlah_hari

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        if hari_terlambat < 0:
            raise ValueError(
                f"hari terlambat tidak boleh minus, diterima {hari_terlambat}"
            )
        per_hari = (
            self._tarif_harian * AlatTani.PERSEN_DENDA_HARIAN // 100
        )
        return per_hari * hari_terlambat

    def keterangan(self) -> str:
        return (
            f"[{self._kode}] {self._nama} — "
            f"{self.format_rupiah(self._tarif_harian)}/hari"
        )