from __future__ import annotations

import pytest

from src.model.pegawai import Pegawai
from src.model.pegawai_lapangan import PegawaiLapangan
from src.model.pegawai_penyuluh import PegawaiPenyuluh
from src.model.pegawai_struktural import PegawaiStruktural
from src.model.penyusun_laporan import PenyusunLaporan


def buat_daftar_pegawai() -> list[Pegawai]:
    return [
        Pegawai("001", "Budi", 5_000_000),
        PegawaiLapangan("002", "Andi", 5_000_000, "Bangkinang"),
        PegawaiPenyuluh("003", "Siti", 5_000_000, 2),
        PegawaiStruktural("004", "Doni", 5_000_000, 2),
    ]


def test_penyusun_laporan_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        PenyusunLaporan([])


def test_penyusun_laporan_menerima_daftar_pegawai() -> None:
    laporan = PenyusunLaporan(buat_daftar_pegawai())
    assert laporan is not None


def test_rekap_penghasilan_semua_jenis_pegawai() -> None:
    laporan = PenyusunLaporan(buat_daftar_pegawai())
    assert laporan.rekap_penghasilan() == [
        ("Budi", 5_000_000),
        ("Andi", 5_500_000),
        ("Siti", 5_300_000),
        ("Doni", 5_600_000),
    ]


def test_penghasilan_tertinggi() -> None:
    laporan = PenyusunLaporan(buat_daftar_pegawai())
    assert laporan.penghasilan_tertinggi() == ("Doni", 5_600_000)


def test_penghasilan_terendah() -> None:
    laporan = PenyusunLaporan(buat_daftar_pegawai())
    assert laporan.penghasilan_terendah() == ("Budi", 5_000_000)


def test_total_penghasilan_semua_pegawai() -> None:
    laporan = PenyusunLaporan(buat_daftar_pegawai())
    assert laporan.total_penghasilan() == 21_400_000


def test_rekap_penghasilan_daftar_tidak_berubah() -> None:
    pegawai = buat_daftar_pegawai()
    laporan = PenyusunLaporan(pegawai)
    pegawai.clear()
    assert len(laporan.rekap_penghasilan()) == 4


def test_penghasilan_tertinggi_dengan_satu_pegawai() -> None:
    laporan = PenyusunLaporan([Pegawai("001", "Budi", 5_000_000)])
    assert laporan.penghasilan_tertinggi() == ("Budi", 5_000_000)


def test_penghasilan_terendah_dengan_satu_pegawai() -> None:
    laporan = PenyusunLaporan([Pegawai("001", "Budi", 5_000_000)])
    assert laporan.penghasilan_terendah() == ("Budi", 5_000_000)


def test_penyusun_laporan_mendukung_jenis_pegawai_baru() -> None:
    class PegawaiKontrak(Pegawai):
        def hitung_penghasilan(self, tambahan: int = 0) -> int:
            return super().hitung_penghasilan(tambahan) + 750_000

    pegawai = [
        Pegawai("001", "Budi", 5_000_000),
        PegawaiKontrak("005", "Rina", 4_000_000),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.rekap_penghasilan() == [
        ("Budi", 5_000_000),
        ("Rina", 4_750_000),
    ]
    assert laporan.total_penghasilan() == 9_750_000
