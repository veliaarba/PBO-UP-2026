"""Pengujian untuk kelas Kios."""

import pytest
from src.kios import Kios


def test_membuat_produk_valid() -> None:
    produk = Kios("BR01", "Beras", 10000, 12000)
    assert produk.ringkasan().startswith("BR01")


def test_harga_jual_memenuhi_margin() -> None:
    produk = Kios("GL01", "Gula", 10000, 12000)
    assert "Gula" in produk.ringkasan()


def test_format_rupiah() -> None:
    assert Kios.format_rupiah(150000) == "Rp150.000"


def test_harga_wajar() -> None:
    assert Kios.harga_wajar(150000)


def test_harga_tidak_wajar_di_bawah_minimum() -> None:
    assert not Kios.harga_wajar(0)


def test_harga_tidak_wajar_di_atas_maksimum() -> None:
    assert not Kios.harga_wajar(100000001)


def test_menolak_kode_kosong() -> None:
    with pytest.raises(ValueError):
        Kios(" ", "Beras", 10000, 12000)


def test_menolak_nama_kosong() -> None:
    with pytest.raises(ValueError):
        Kios("BR01", " ", 10000, 12000)


def test_menolak_harga_modal_nol() -> None:
    with pytest.raises(ValueError):
        Kios("BR01", "Beras", 0, 12000)


def test_menolak_harga_jual_di_bawah_modal() -> None:
    with pytest.raises(ValueError):
        Kios("BR01", "Beras", 10000, 10500)


def test_menolak_baris_csv_tidak_lengkap() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("BR01,Beras,10000")


def test_membuat_produk_dari_baris_csv() -> None:
    produk = Kios.dari_baris_csv("BR02,Beras,10000,12000")
    assert produk.ringkasan().startswith("BR02")


def test_menolak_harga_csv_bukan_angka() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("BR01,Beras,modal,12000")


def test_pencacah_bertambah_satu() -> None:
    sebelum = Kios.jumlah_terdaftar()
    Kios("BR03", "Beras Premium", 10000, 12000)
    sesudah = Kios.jumlah_terdaftar()
    assert sesudah - sebelum == 1


def test_ringkasan_memuat_harga() -> None:
    produk = Kios("MG01", "Minyak Goreng", 15000, 18000)
    assert "Rp18.000" in produk.ringkasan()
