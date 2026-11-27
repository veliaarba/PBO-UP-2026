from __future__ import annotations

import pytest

from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir
from src.model.perontok import Perontok


def test_traktor_dari_csv() -> None:
    alat = Traktor.from_baris_csv("TR-01, Kubota, 200000, 8")
    assert alat.kode == "TR-01"
    assert alat.nama == "Kubota"
    assert alat.tarif_harian == 200000
    assert alat.tenaga_kuda == 8


def test_traktor_csv_menolak_kolom_kurang() -> None:
    with pytest.raises(ValueError):
        Traktor.from_baris_csv("TR-01, Kubota, 200000")


def test_traktor_csv_menolak_data_angka_salah() -> None:
    with pytest.raises(ValueError):
        Traktor.from_baris_csv("TR-01, Kubota, abc, 8")


def test_pompa_air_dari_csv() -> None:
    alat = PompaAir.from_baris_csv("PA-01, Pompa Air, 150000, 300")
    assert alat.kode == "PA-01"
    assert alat.debit == 300


def test_pompa_air_csv_menolak_kolom_kurang() -> None:
    with pytest.raises(ValueError):
        PompaAir.from_baris_csv("PA-01, Pompa Air, 150000")


def test_pompa_air_csv_menolak_debit_nol() -> None:
    with pytest.raises(ValueError):
        PompaAir.from_baris_csv("PA-01, Pompa Air, 150000, 0")


def test_perontok_dari_csv() -> None:
    alat = Perontok.from_baris_csv("PR-01, Perontok Padi, 250000, 500")
    assert alat.kode == "PR-01"
    assert alat.kapasitas == 500


def test_perontok_csv_menolak_kolom_kurang() -> None:
    with pytest.raises(ValueError):
        Perontok.from_baris_csv("PR-01, Perontok Padi, 250000")


def test_perontok_csv_menolak_kapasitas_nol() -> None:
    with pytest.raises(ValueError):
        Perontok.from_baris_csv("PR-01, Perontok Padi, 250000, 0")
