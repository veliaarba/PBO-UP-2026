from __future__ import annotations

import pytest

from src.model.alat_tani import AlatTani
from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir
from src.model.perontok import Perontok
from src.model.daftar_harga import DaftarHarga


def buat_daftar() -> DaftarHarga:
    return DaftarHarga([
        Traktor("TR-01", "Traktor Kubota", 150_000, 8),
        PompaAir("PA-01", "Pompa Air", 75_000, 100),
        Perontok("PR-01", "Perontok Padi", 200_000, 500),
    ])


def test_daftar_harga_menerima_beberapa_jenis_alat() -> None:
    daftar = buat_daftar()
    assert len(daftar.biaya_semua(2)) == 3


def test_daftar_harga_menggunakan_biaya_polimorfis() -> None:
    daftar = buat_daftar()
    hasil = daftar.biaya_semua(2)

    assert hasil == [
        ("Traktor Kubota", 500_000),
        ("Pompa Air", 192_000),
        ("Perontok Padi", 400_000),
    ]


def test_daftar_harga_mencari_termurah() -> None:
    daftar = buat_daftar()
    assert daftar.termurah(2) == ("Pompa Air", 192_000)


def test_daftar_harga_menghitung_total() -> None:
    daftar = buat_daftar()
    assert daftar.total_bila_semua_disewa(2) == 1_092_000


def test_daftar_harga_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        DaftarHarga([])


def test_daftar_harga_menolak_nol_hari() -> None:
    daftar = buat_daftar()
    with pytest.raises(ValueError):
        daftar.termurah(0)


def test_daftar_harga_menolak_hari_negatif() -> None:
    daftar = buat_daftar()
    with pytest.raises(ValueError):
        daftar.termurah(-2)


def test_daftar_harga_menolak_hari_tidak_valid_pada_semua_alat() -> None:
    daftar = buat_daftar()
    with pytest.raises(ValueError):
        daftar.biaya_semua(0)


def test_daftar_harga_menolak_hari_tidak_valid_pada_total() -> None:
    daftar = buat_daftar()
    with pytest.raises(ValueError):
        daftar.total_bila_semua_disewa(0)


def test_daftar_harga_menggunakan_polimorfisme_subkelas_baru() -> None:
    class Penggiling(AlatTani):
        def biaya_sewa(self, jumlah_hari: int) -> int:
            return super().biaya_sewa(jumlah_hari) + 25_000

    penggiling = Penggiling("PG-01", "Mesin Penggiling", 100_000)
    daftar = DaftarHarga([penggiling])

    assert daftar.biaya_semua(2) == [
        ("Mesin Penggiling", 225_000)
    ]
    assert daftar.termurah(2) == ("Mesin Penggiling", 225_000)
    assert daftar.total_bila_semua_disewa(2) == 225_000


def test_daftar_harga_menyimpan_salinan_daftar() -> None:
    alat: list[AlatTani] = [Traktor("TR-02", "Traktor", 150_000, 8)]
    daftar = DaftarHarga(alat)

    alat.clear()

    assert daftar.biaya_semua(1) == [("Traktor", 250_000)]

