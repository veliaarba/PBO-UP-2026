from __future__ import annotations

from typing import Any, cast

import pytest

from src.model.alat_tani import AlatTani
from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir
from src.model.perontok import Perontok


class AlatTaniUji(AlatTani):
    """Kelas konkret untuk menguji fitur yang diwariskan dari AlatTani."""

    def biaya_tambahan(self, jumlah_hari: int) -> int:
        return 0

    def syarat_pemakaian(self) -> str:
        return "Tidak ada syarat khusus."


def buat_alat(
    kode: str = "A01",
    nama: str = "Cangkul",
    tarif: int = 50_000,
) -> AlatTaniUji:
    return AlatTaniUji(kode, nama, tarif)


# ==================================================
# PENGUJIAN KELAS TRAKTOR
# ==================================================

def test_traktor_init() -> None:
    traktor = Traktor("TR-01", "Traktor Kubota", 150_000, 8)
    assert traktor.kode == "TR-01"
    assert traktor.nama == "Traktor Kubota"
    assert traktor.tarif_harian == 150_000
    assert traktor.tenaga_kuda == 8


def test_traktor_tenaga_kuda_nol() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-02", "Traktor", 150_000, 0)


def test_traktor_tenaga_kuda_negatif() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-03", "Traktor", 150_000, -5)


def test_traktor_biaya_sewa() -> None:
    traktor = Traktor("TR-04", "Traktor", 150_000, 8)
    assert traktor.biaya_sewa(2) == 500_000


def test_traktor_tarif_induk_tidak_valid() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-05", "Traktor", 0, 8)


# ==================================================
# PENGUJIAN KELAS POMPA AIR
# ==================================================

def test_pompa_air_init() -> None:
    pompa = PompaAir("PA-01", "Pompa Air", 75_000, 100)
    assert pompa.kode == "PA-01"
    assert pompa.nama == "Pompa Air"
    assert pompa.debit == 100


def test_pompa_air_debit_nol() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-02", "Pompa Air", 75_000, 0)


def test_pompa_air_debit_negatif() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-03", "Pompa Air", 75_000, -10)


def test_pompa_air_konsumsi_solar() -> None:
    pompa = PompaAir("PA-04", "Pompa Air", 75_000, 100)
    assert pompa.konsumsi_solar_harian() == 3


def test_pompa_air_biaya_sewa() -> None:
    pompa = PompaAir("PA-05", "Pompa Air", 75_000, 100)
    assert pompa.biaya_sewa(2) == 192_000


# ==================================================
# PENGUJIAN KELAS PERONTOK
# ==================================================

def test_perontok_init() -> None:
    perontok = Perontok("PR-01", "Perontok Padi", 200_000, 500)
    assert perontok.kode == "PR-01"
    assert perontok.nama == "Perontok Padi"
    assert perontok.kapasitas == 500


def test_perontok_kapasitas_nol() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-02", "Perontok Padi", 200_000, 0)


def test_perontok_kapasitas_negatif() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-03", "Perontok Padi", 200_000, -100)


def test_perontok_minimum_hari() -> None:
    perontok = Perontok("PR-04", "Perontok Padi", 200_000, 500)
    assert perontok.hari_ditagih(1) == 2
    assert perontok.biaya_sewa(1) == 400_000


def test_perontok_biaya_sewa_normal() -> None:
    perontok = Perontok("PR-05", "Perontok Padi", 200_000, 500)
    assert perontok.biaya_sewa(3) == 600_000


# ==================================================
# PENGUJIAN KELAS INDUK ABSTRAK ALAT TANI
# ==================================================

def test_alat_tani_merupakan_kelas_abstrak() -> None:
    with pytest.raises(TypeError):
        cast(Any, AlatTani)("A00", "Cangkul", 50_000)


def test_alat_tani_str() -> None:
    alat = buat_alat("A01", "Cangkul")
    assert str(alat) == "[A01] Cangkul"


def test_alat_tani_repr() -> None:
    alat = buat_alat("A02", "Cangkul")
    assert "AlatTaniUji" in repr(alat)
    assert "A02" in repr(alat)


def test_alat_tani_eq_kode_sama() -> None:
    alat1 = buat_alat("A03", "Cangkul")
    alat2 = buat_alat("A03", "Cangkul Besar", 75_000)
    assert alat1 == alat2


def test_alat_tani_eq_kode_berbeda() -> None:
    alat1 = buat_alat("A04", "Cangkul")
    alat2 = buat_alat("A05", "Cangkul")
    assert alat1 != alat2


def test_alat_tani_dibandingkan_dengan_objek_lain() -> None:
    alat = buat_alat("A06", "Cangkul")
    assert alat != "Cangkul"


def test_alat_tani_hash_dapat_digunakan_sebagai_kunci_dict() -> None:
    alat = buat_alat("A07", "Cangkul")
    data = {alat: "Tersedia"}
    assert data[alat] == "Tersedia"


def test_alat_tani_hash_sama_untuk_kode_sama() -> None:
    alat1 = buat_alat("A08", "Cangkul")
    alat2 = buat_alat("A08", "Cangkul Baru", 60_000)
    assert hash(alat1) == hash(alat2)


# ==================================================
# PENGUJIAN VALIDASI ALAT TANI
# ==================================================

def test_alat_tani_kode_kosong() -> None:
    with pytest.raises(ValueError):
        buat_alat("", "Cangkul")


def test_alat_tani_nama_hanya_spasi() -> None:
    with pytest.raises(ValueError):
        buat_alat("A09", "   ")


def test_alat_tani_tarif_negatif() -> None:
    with pytest.raises(ValueError):
        buat_alat("A10", "Cangkul", -10_000)


def test_alat_tani_setter_tarif_valid() -> None:
    alat = buat_alat("A11", "Cangkul")
    alat.tarif_harian = 75_000
    assert alat.tarif_harian == 75_000


def test_alat_tani_setter_tarif_nol() -> None:
    alat = buat_alat("A12", "Cangkul")
    with pytest.raises(ValueError):
        alat.tarif_harian = 0


def test_alat_tani_alias_tarif() -> None:
    alat = buat_alat("A13", "Cangkul")
    assert alat.tarif == 50_000


def test_alat_tani_setter_alias_tarif() -> None:
    alat = buat_alat("A14", "Cangkul")
    alat.tarif = 100_000
    assert alat.tarif_harian == 100_000


def test_alat_tani_jumlah_terdaftar_bertambah() -> None:
    sebelum = AlatTani.jumlah_terdaftar()
    buat_alat("A15", "Cangkul")
    sesudah = AlatTani.jumlah_terdaftar()
    assert sesudah == sebelum + 1


def test_alat_tani_format_rupiah() -> None:
    assert AlatTani.format_rupiah(1_234_567) == "Rp 1.234.567"


def test_alat_tani_keterangan() -> None:
    alat = buat_alat("A16", "Cangkul")
    assert alat.keterangan() == "[A16] Cangkul"


def test_alat_tani_biaya_sewa_satu_hari() -> None:
    alat = buat_alat("A17", "Cangkul")
    assert alat.biaya_sewa(1) == 50_000


def test_alat_tani_biaya_sewa_nol_hari() -> None:
    alat = buat_alat("A18", "Cangkul")
    with pytest.raises(ValueError):
        alat.biaya_sewa(0)


def test_alat_tani_biaya_sewa_hari_negatif() -> None:
    alat = buat_alat("A19", "Cangkul")
    with pytest.raises(ValueError):
        alat.biaya_sewa(-2)


def test_alat_tani_set_menghapus_objek_dengan_kode_sama() -> None:
    alat1 = buat_alat("A20", "Cangkul")
    alat2 = buat_alat("A20", "Cangkul Besar", 75_000)
    kumpulan = {alat1, alat2}
    assert len(kumpulan) == 1


# ==================================================
# PENGUJIAN TAMBAHAN
# ==================================================

def test_traktor_biaya_sewa_satu_hari() -> None:
    traktor = Traktor("TR-06", "Kubota", 150_000, 8)
    assert traktor.biaya_sewa(1) == 250_000


def test_traktor_csv_menolak_kolom_berlebih() -> None:
    with pytest.raises(ValueError):
        Traktor.from_baris_csv("TR-07, Kubota, 200000, 8, ekstra")


def test_pompa_air_csv_menolak_data_angka_salah() -> None:
    with pytest.raises(ValueError):
        PompaAir.from_baris_csv("PA-06, Pompa Air, abc, 100")


def test_pompa_air_konsumsi_solar_di_bawah_seratus() -> None:
    pompa = PompaAir("PA-07", "Pompa Air", 75_000, 99)
    assert pompa.konsumsi_solar_harian() == 2


def test_pompa_air_biaya_sewa_satu_hari() -> None:
    pompa = PompaAir("PA-08", "Pompa Air", 75_000, 100)
    assert pompa.biaya_sewa(1) == 96_000


def test_perontok_menolak_nol_hari() -> None:
    perontok = Perontok("PR-06", "Perontok Padi", 200_000, 500)
    with pytest.raises(ValueError):
        perontok.hari_ditagih(0)


def test_perontok_csv_menolak_data_angka_salah() -> None:
    with pytest.raises(ValueError):
        Perontok.from_baris_csv("PR-07, Perontok Padi, abc, 500")