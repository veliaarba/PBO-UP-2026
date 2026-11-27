from __future__ import annotations


def terjemahkan_perintah(perintah: str) -> str:
    bagian = perintah.strip().split()

    if bagian:
        bagian[0] = bagian[0].lower()

    if len(bagian) > 1 and bagian[0] == "tambah":
        bagian[1] = bagian[1].lower()

    match bagian:
        case ["tambah", jenis, kode] if jenis in ("traktor", "pompa", "perontok"):
            return f"Tambah alat {jenis} dengan kode {kode}"

        case ["daftar"]:
            return "Tampilkan daftar alat"

        case ["harga", kode]:
            return f"Tampilkan harga alat dengan kode {kode}"

        case ["sewa", kode, hari]:
            return f"Sewa alat {kode} selama {hari} hari"

        case ["batal", kode]:
            return f"Batalkan penyewaan alat {kode}"

        case _:
            return "Perintah tidak dikenali"
