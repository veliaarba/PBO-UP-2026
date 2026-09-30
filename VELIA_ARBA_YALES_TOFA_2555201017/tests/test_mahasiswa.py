"""Pengujian untuk kelas Mahasiswa."""

from src.mahasiswa import Mahasiswa


def test_perkenalan_memuat_nama() -> None:
    saya = Mahasiswa("Velia Arba Yales Tofa", "2555201017", "Bangkinang")
    assert "Velia Arba Yales Tofa" in saya.perkenalan()


def test_atribut_dibaca_lewat_property() -> None:
    saya = Mahasiswa("Velia Arba Yales Tofa", "2555201017", "Bangkinang")
    assert saya.nama == "Velia Arba Yales Tofa"
    assert saya.asal_desa == "Bangkinang"