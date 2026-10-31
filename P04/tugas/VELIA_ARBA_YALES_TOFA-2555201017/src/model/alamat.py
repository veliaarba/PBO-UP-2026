"""Model alamat untuk penyewa."""
from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)
class Alamat:
    """Mewakili informasi alamat tempat tinggal."""
    jalan: str
    desa: str
    kecamatan: str

    def __post_init__(self) -> None:
        if not self.desa.strip():
            raise ValueError("desa tidak boleh kosong")
        if not self.kecamatan.strip():
            raise ValueError("kecamatan tidak boleh kosong")

    def singkat(self) -> str:
        return f"{self.desa}, {self.kecamatan}"