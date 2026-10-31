"""Model penyewa alat pertanian."""
from src.model.alamat import Alamat

class Penyewa:
    """Mewakili data penyewa alat pertanian."""
    PANJANG_NIK: int = 16

    def __init__(self, nik: str, nama: str, alamat: Alamat, telepon: str = "") -> None:
        if len(nik.strip()) != self.PANJANG_NIK:
            raise ValueError(f"NIK harus sepanjang {self.PANJANG_NIK} digit")
        if not nama.strip():
            raise ValueError("nama penyewa tidak boleh kosong")
        
        self._nik = nik.strip()
        self._nama = nama.strip()
        self._alamat = alamat
        self._telepon = telepon.strip()

    @property
    def nik(self) -> str:
        return self._nik

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def alamat(self) -> Alamat:
        return self._alamat

    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        if nilai.strip() and not nilai.strip().isdigit():
            raise ValueError("nomor telepon harus berupa angka")
        self._telepon = nilai.strip()

    def identitas(self) -> str:
        return f"Penyewa: {self._nama} (NIK: {self._nik})"

    def kontak(self) -> str:
        telp = self._telepon if self._telepon else "-"
        return f"Alamat: {self._alamat.singkat()} | Telp: {telp}"