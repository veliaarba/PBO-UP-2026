"""Kesalahan yang disengaja nomor 2: parameter berdefault yang dapat diubah.

Nilai default dibuat SATU KALI saat def dijalankan, bukan setiap kali
method dipanggil. Akibatnya seluruh objek yang tidak mengisi parameter itu
memakai daftar yang sama persis.
"""


class Penyewa:
    """Penyewa dengan riwayat sewa yang tanpa sengaja dibagi bersama."""

    def __init__(self, nama: str, riwayat: list[str] = []) -> None:   # SALAH
        self._nama = nama
        self._riwayat = riwayat

    def sewa(self, kode_alat: str) -> None:
        self._riwayat.append(kode_alat)

    def laporan(self) -> str:
        return f"{self._nama}: {self._riwayat}"


def main() -> None:
    budi = Penyewa("Budi")
    siti = Penyewa("Siti")

    budi.sewa("TR-01")
    budi.sewa("PA-01")

    print(budi.laporan())
    print(siti.laporan())          # Siti belum menyewa apa pun
    print("Daftar yang sama?", budi._riwayat is siti._riwayat)


if __name__ == "__main__":
    main()
