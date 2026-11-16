from __future__ import annotations

import pytest

from src.model.pegawai import Pegawai
from src.model.pegawai_lapangan import PegawaiLapangan
from src.model.pegawai_penyuluh import PegawaiPenyuluh
from src.model.pegawai_struktural import PegawaiStruktural


def test_pegawai_menyimpan_data() -> None:
    pegawai = Pegawai("123", "Budi", 5_000_000)
    assert pegawai.nip == "123"
    assert pegawai.nama == "Budi"
    assert pegawai.gaji_pokok == 5_000_000


def test_pegawai_menolak_nip_kosong() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Budi", 5_000_000)


def test_pegawai_menolak_nama_kosong() -> None:
    with pytest.raises(ValueError):
        Pegawai("123", "", 5_000_000)


def test_pegawai_menolak_gaji_nol() -> None:
    with pytest.raises(ValueError):
        Pegawai("123", "Budi", 0)


def test_pegawai_menghitung_penghasilan() -> None:
    pegawai = Pegawai("123", "Budi", 5_000_000)
    assert pegawai.hitung_penghasilan(500_000) == 5_500_000


def test_pegawai_menolak_tambahan_negatif() -> None:
    pegawai = Pegawai("123", "Budi", 5_000_000)
    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(-100_000)


def test_pegawai_memiliki_str() -> None:
    pegawai = Pegawai("123", "Budi", 5_000_000)
    assert str(pegawai) == "123 - Budi"


def test_pegawai_memiliki_repr() -> None:
    pegawai = Pegawai("123", "Budi", 5_000_000)
    assert "Pegawai(" in repr(pegawai)


def test_pegawai_dibandingkan_berdasarkan_nip() -> None:
    pertama = Pegawai("123", "Budi", 5_000_000)
    kedua = Pegawai("123", "Andi", 6_000_000)
    assert pertama == kedua


def test_pegawai_dengan_nip_berbeda_tidak_sama() -> None:
    pertama = Pegawai("123", "Budi", 5_000_000)
    kedua = Pegawai("456", "Budi", 5_000_000)
    assert pertama != kedua


def test_pegawai_dapat_menjadi_kunci_dictionary() -> None:
    pegawai = Pegawai("123", "Budi", 5_000_000)
    data = {pegawai: "Pegawai tetap"}
    assert data[pegawai] == "Pegawai tetap"


def test_pegawai_lapangan_menghitung_tunjangan() -> None:
    pegawai = PegawaiLapangan("123", "Budi", 5_000_000, "Bangkinang")
    assert pegawai.hitung_penghasilan() == 5_500_000


def test_pegawai_lapangan_menolak_lokasi_kosong() -> None:
    with pytest.raises(ValueError):
        PegawaiLapangan("123", "Budi", 5_000_000, "")


def test_pegawai_penyuluh_menghitung_honor_kegiatan() -> None:
    pegawai = PegawaiPenyuluh("123", "Budi", 5_000_000, 2)
    assert pegawai.hitung_penghasilan() == 5_300_000


def test_pegawai_penyuluh_menolak_jumlah_kegiatan_negatif() -> None:
    with pytest.raises(ValueError):
        PegawaiPenyuluh("123", "Budi", 5_000_000, -1)


def test_pegawai_struktural_menghitung_tunjangan_jabatan() -> None:
    pegawai = PegawaiStruktural("123", "Budi", 5_000_000, 2)
    assert pegawai.hitung_penghasilan() == 5_600_000


def test_pegawai_struktural_menolak_tingkat_jabatan_nol() -> None:
    with pytest.raises(ValueError):
        PegawaiStruktural("123", "Budi", 5_000_000, 0)
