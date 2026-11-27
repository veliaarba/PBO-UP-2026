from __future__ import annotations

from src.model.pegawai import Pegawai
from src.model.penyusun_laporan import PenyusunLaporan
from src.ui.perintah_laporan import PerintahLaporan


def buat_penerjemah() -> PerintahLaporan:
    pegawai = [
        Pegawai("001", "Budi", 5_000_000),
        Pegawai("002", "Andi", 6_000_000),
    ]
    return PerintahLaporan(PenyusunLaporan(pegawai))


def test_perintah_rekap() -> None:
    hasil = buat_penerjemah().jalankan("rekap")
    assert "Budi: Rp5,000,000" in hasil
    assert "Andi: Rp6,000,000" in hasil


def test_perintah_tertinggi() -> None:
    hasil = buat_penerjemah().jalankan("tertinggi")
    assert hasil == "Andi: Rp6,000,000"


def test_perintah_terendah() -> None:
    hasil = buat_penerjemah().jalankan("terendah")
    assert hasil == "Budi: Rp5,000,000"


def test_perintah_total() -> None:
    hasil = buat_penerjemah().jalankan("total")
    assert hasil == "Total penghasilan: Rp11,000,000"


def test_perintah_bantuan() -> None:
    hasil = buat_penerjemah().jalankan("bantuan")
    assert "rekap" in hasil
    assert "tertinggi" in hasil


def test_perintah_asing_ditolak() -> None:
    hasil = buat_penerjemah().jalankan("hapus")
    assert hasil == "Perintah tidak dikenal: hapus"


def test_perintah_asing_dengan_argumen_ditolak() -> None:
    hasil = buat_penerjemah().jalankan("cetak laporan")
    assert hasil == "Perintah tidak dikenal: cetak"


def test_perintah_kosong_ditolak() -> None:
    hasil = buat_penerjemah().jalankan("")
    assert hasil == "Perintah tidak boleh kosong."


def test_perintah_spasi_ditolak() -> None:
    hasil = buat_penerjemah().jalankan("   ")
    assert hasil == "Perintah tidak boleh kosong."


def test_perintah_dengan_huruf_besar() -> None:
    hasil = buat_penerjemah().jalankan("REKAP")
    assert "Budi: Rp5,000,000" in hasil


def test_perintah_asing_keluar_ditolak() -> None:
    hasil = buat_penerjemah().jalankan("keluar")
    assert hasil == "Perintah tidak dikenal: keluar"
