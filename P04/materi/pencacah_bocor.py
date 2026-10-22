"""Kesalahan yang disengaja nomor 1: pencacah ditulis lewat self.

Niatnya menaikkan pencacah milik kelas. Yang terjadi: Python membuatkan
atribut BARU milik objek yang menutupi atribut kelas. Pencacah kelas tidak
pernah bergerak, dan setiap alat mengaku dirinya alat pertama.
"""


class AlatTani:
    """Alat pertanian dengan pencacah yang tidak pernah bekerja."""

    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str) -> None:
        self._kode = kode
        self._jumlah_terdaftar += 1        # SALAH: self, bukan AlatTani

    def laporan(self) -> str:
        return f"{self._kode} melaporkan jumlah = {self._jumlah_terdaftar}"


def main() -> None:
    a = AlatTani("TR-01")
    b = AlatTani("TR-02")
    c = AlatTani("PA-01")
    print(a.laporan())
    print(b.laporan())
    print(c.laporan())
    print("Pencacah milik kelas :", AlatTani._jumlah_terdaftar)
    print("Isi objek a          :", list(vars(a)))


if __name__ == "__main__":
    main()
