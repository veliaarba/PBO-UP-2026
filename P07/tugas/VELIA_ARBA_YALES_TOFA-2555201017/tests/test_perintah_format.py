from __future__ import annotations

from src.ui.perintah_konsol import terjemahkan_perintah
from src.format_nilai import format_nilai


# ==================================================
# PENGUJIAN MATCH-CASE
# ==================================================

def test_perintah_tambah_traktor() -> None:
    assert terjemahkan_perintah("tambah traktor TR-01") == (
        "Tambah alat traktor dengan kode TR-01"
    )


def test_perintah_tambah_pompa() -> None:
    assert terjemahkan_perintah("tambah pompa PA-01") == (
        "Tambah alat pompa dengan kode PA-01"
    )


def test_perintah_tambah_perontok() -> None:
    assert terjemahkan_perintah("tambah perontok PR-01") == (
        "Tambah alat perontok dengan kode PR-01"
    )


def test_perintah_daftar() -> None:
    assert terjemahkan_perintah("daftar") == "Tampilkan daftar alat"


def test_perintah_harga() -> None:
    assert terjemahkan_perintah("harga TR-01") == (
        "Tampilkan harga alat dengan kode TR-01"
    )


def test_perintah_sewa() -> None:
    assert terjemahkan_perintah("sewa TR-01 3") == (
        "Sewa alat TR-01 selama 3 hari"
    )


def test_perintah_batal() -> None:
    assert terjemahkan_perintah("batal TR-01") == (
        "Batalkan penyewaan alat TR-01"
    )


def test_perintah_tidak_dikenali() -> None:
    assert terjemahkan_perintah("hapus TR-01") == (
        "Perintah tidak dikenali"
    )


def test_perintah_tambah_jenis_tidak_valid() -> None:
    assert terjemahkan_perintah("tambah cangkul C-01") == (
        "Perintah tidak dikenali"
    )


def test_perintah_format_tidak_valid() -> None:
    assert terjemahkan_perintah("sewa TR-01") == (
        "Perintah tidak dikenali"
    )


def test_perintah_kosong() -> None:
    assert terjemahkan_perintah("") == "Perintah tidak dikenali"


def test_perintah_mengabaikan_huruf_besar() -> None:
    assert terjemahkan_perintah("DAFTAR") == "Tampilkan daftar alat"


def test_perintah_mengabaikan_spasi() -> None:
    assert terjemahkan_perintah("  daftar  ") == "Tampilkan daftar alat"


# ==================================================
# PENGUJIAN SINGLE DISPATCH
# ==================================================

def test_format_nilai_integer() -> None:
    assert format_nilai(150000) == "Rp 150.000"


def test_format_nilai_float() -> None:
    assert format_nilai(0.15) == "15.00%"


def test_format_nilai_string() -> None:
    assert format_nilai("Traktor") == "Traktor"


def test_format_nilai_list_integer() -> None:
    assert format_nilai([1000, 2000]) == "[Rp 1.000, Rp 2.000]"


def test_format_nilai_list_berbagai_tipe() -> None:
    assert format_nilai([1000, 0.25, "Alat"]) == (
        "[Rp 1.000, 25.00%, Alat]"
    )


def test_format_nilai_list_kosong() -> None:
    assert format_nilai([]) == "[]"


def test_format_nilai_list_bersarang() -> None:
    assert format_nilai([[1000, 2000], 0.5]) == (
        "[[Rp 1.000, Rp 2.000], 50.00%]"
    )


def test_format_nilai_integer_nol() -> None:
    assert format_nilai(0) == "Rp 0"


def test_format_nilai_float_nol() -> None:
    assert format_nilai(0.0) == "0.00%"
