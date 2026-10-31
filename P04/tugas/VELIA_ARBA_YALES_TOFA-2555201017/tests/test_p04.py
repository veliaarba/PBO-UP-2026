import pytest
from src.model.alat_tani import AlatTani

def test_alat_tani_inisialisasi_valid() -> None:
    alat = AlatTani("TR-01", "Traktor Sawah", 150000)
    assert alat.kode == "TR-01"
    assert alat.nama == "Traktor Sawah"
    assert alat.tarif_harian == 150000

def test_kode_kosong_raises_value_error() -> None:
    with pytest.raises(ValueError):
        AlatTani("", "Traktor", 100000)

def test_nama_kosong_raises_value_error() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "", 100000)

def test_tarif_dibawah_minimum_raises_value_error() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 5000)

def test_tarif_diatas_maksimum_raises_value_error() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 6000000)

def test_tarif_wajar_validasi() -> None:
    assert AlatTani.tarif_wajar(50000) is True
    assert AlatTani.tarif_wajar(5000) is False
    assert AlatTani.tarif_wajar(6000000) is False

def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150000) == "Rp150.000"

def test_jumlah_terdaftar() -> None:
    awal = AlatTani.jumlah_terdaftar()
    AlatTani("A-1", "Alat 1", 20000)
    assert AlatTani.jumlah_terdaftar() == awal + 1

def test_dari_baris_csv_valid() -> None:
    alat = AlatTani.dari_baris_csv("TR-02;Traktor Mini;200000")
    assert alat.kode == "TR-02"
    assert alat.nama == "Traktor Mini"
    assert alat.tarif_harian == 200000

def test_dari_baris_csv_kolom_salah() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-02;Traktor Mini")

def test_dari_baris_csv_tarif_bukan_angka() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-02;Traktor Mini;dua-ratus-ribu")

def test_biaya_sewa() -> None:
    alat = AlatTani("TR-01", "Traktor", 100000)
    assert alat.biaya_sewa(5) == 500000

def test_denda_keterlambatan_normal() -> None:
    alat = AlatTani("TR-01", "Traktor", 100000)
    # Denda 10% dari 100.000 = 10.000 per hari, terlambat 2 hari = 20.000
    assert alat.denda_keterlambatan(2) == 20000

def test_denda_keterlambatan_minus_raises_error() -> None:
    alat = AlatTani("TR-01", "Traktor", 100000)
    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)

def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.keterangan() == "[TR-01] Traktor — Rp150.000/hari"