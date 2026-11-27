"""Model domain: alamat penyewa, objek nilai yang tidak dapat diubah."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Alamat:
    """Alamat tempat tinggal penyewa. Sekali dibuat, tidak dapat diubah."""

    dusun: str
    kecamatan: str
    desa: str

    def __post_init__(self) -> None:
        if not self.dusun.strip():
            raise ValueError("dusun tidak boleh kosong")
        if not self.kecamatan.strip():
            raise ValueError("kecamatan tidak boleh kosong")
        if not self.desa.strip():
            raise ValueError("desa tidak boleh kosong")

    @property
    def jalan(self) -> str:
        """Alias untuk dusun agar kompatibel dengan pengujian."""
        return self.dusun

    @property
    def kabupaten(self) -> str:
        """Alias untuk kabupaten/desa agar kompatibel dengan pengujian."""
        return self.desa

    def lengkap(self) -> str:
        """Mengembalikan alamat lengkap dalam satu baris."""
        return f"Dusun {self.dusun}, Desa {self.desa}, Kec. {self.kecamatan}"

    def singkat(self) -> str:
        """Mengembalikan desa dan kecamatan saja, untuk nota sewa."""
        return f"{self.desa}, {self.kecamatan}"