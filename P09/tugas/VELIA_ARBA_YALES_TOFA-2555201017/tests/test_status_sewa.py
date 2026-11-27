"""Pengujian status dan aturan perubahan transaksi penyewaan."""

import pytest

from src.model.alamat import Alamat
from src.model.penyewa import Penyewa
from src.model.traktor import Traktor
from src.model.sewa import Sewa
from src.model.status_sewa import StatusSewa


def buat_sewa() -> Sewa:
    penyewa = Penyewa(
        "1234567890123456",
        "Budi",
        Alamat("Dusun Maju", "Bangkinang", "Suka Maju"),
    )
    return Sewa("SW-01", penyewa)


def buat_traktor() -> Traktor:
    return Traktor("TR-01", "Traktor Kubota", 150_000, 8)


def test_status_awal_sewa_dipesan() -> None:
    sewa = buat_sewa()
    assert sewa.status == StatusSewa.DIPESAN


def test_status_sewa_dapat_diubah() -> None:
    sewa = buat_sewa()
    sewa.ubah_status(StatusSewa.BERJALAN)
    assert sewa.status == StatusSewa.BERJALAN


def test_status_selesai_tidak_boleh_diubah() -> None:
    assert not StatusSewa.SELESAI.boleh_diubah()


def test_status_batal_tidak_boleh_diubah() -> None:
    assert not StatusSewa.BATAL.boleh_diubah()


def test_status_dipesan_boleh_diubah() -> None:
    assert StatusSewa.DIPESAN.boleh_diubah()


def test_status_berjalan_boleh_diubah() -> None:
    assert StatusSewa.BERJALAN.boleh_diubah()


def test_status_sewa_menolak_status_tidak_valid() -> None:
    sewa = buat_sewa()
    with pytest.raises(TypeError):
        sewa.ubah_status("selesai")  # type: ignore[arg-type]


def test_status_sewa_menolak_nilai_enum_tidak_dikenal() -> None:
    with pytest.raises(ValueError):
        StatusSewa("seleai")


def test_sewa_dapat_menambahkan_alat_saat_dipesan() -> None:
    sewa = buat_sewa()
    sewa.tambah_alat(buat_traktor(), 2)
    assert sewa.jumlah_alat() == 1


def test_sewa_dapat_menambahkan_alat_saat_berjalan() -> None:
    sewa = buat_sewa()
    sewa.ubah_status(StatusSewa.BERJALAN)
    sewa.tambah_alat(buat_traktor(), 2)
    assert sewa.jumlah_alat() == 1


def test_sewa_tidak_dapat_menambahkan_alat_saat_selesai() -> None:
    sewa = buat_sewa()
    sewa.ubah_status(StatusSewa.SELESAI)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_traktor(), 2)


def test_sewa_tidak_dapat_menambahkan_alat_saat_batal() -> None:
    sewa = buat_sewa()
    sewa.ubah_status(StatusSewa.BATAL)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_traktor(), 2)