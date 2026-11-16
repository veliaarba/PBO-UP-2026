"""Program utama P07: Polimorfisme dan pemrosesan perintah."""

from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir
from src.model.perontok import Perontok
from src.model.daftar_harga import DaftarHarga
from src.ui.perintah_konsol import terjemahkan_perintah
from src.format_nilai import format_nilai


def main() -> None:
    alat = [
        Traktor("TR-01", "Traktor Kubota", 150_000, 8),
        PompaAir("PA-01", "Pompa Air", 75_000, 100),
        Perontok("PR-01", "Perontok Padi", 200_000, 500),
    ]

    daftar = DaftarHarga(alat)

    print("=== DAFTAR BIAYA SEWA ALAT TANI ===")
    for nama, biaya in daftar.biaya_semua(2):
        print(f"{nama}: {format_nilai(biaya)}")

    nama, biaya = daftar.termurah(2)
    print(f"\nAlat termurah: {nama} ({format_nilai(biaya)})")
    print(
        "Total jika semua disewa: "
        f"{format_nilai(daftar.total_bila_semua_disewa(2))}"
    )

    print("\n=== PENERJEMAH PERINTAH ===")
    print(terjemahkan_perintah("tambah traktor TR-01"))
    print(terjemahkan_perintah("daftar"))
    print(terjemahkan_perintah("harga PA-01"))

    print("\n=== FORMAT NILAI ===")
    print(format_nilai(150_000))
    print(format_nilai(0.25))
    print(format_nilai([100_000, 200_000, 300_000]))


if __name__ == "__main__":
    main()
