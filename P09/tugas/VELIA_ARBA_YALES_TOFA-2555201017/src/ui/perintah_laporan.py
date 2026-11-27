from __future__ import annotations

from src.model.penyusun_laporan import PenyusunLaporan


class PerintahLaporan:
    """Menerjemahkan perintah konsol untuk laporan penghasilan pegawai."""

    def __init__(self, laporan: PenyusunLaporan) -> None:
        self._laporan = laporan

    def jalankan(self, perintah: str) -> str:
        bagian = perintah.strip().lower().split()

        match bagian:
            case ["rekap"]:
                hasil = self._laporan.rekap_penghasilan()
                return "\n".join(
                    f"{nama}: Rp{penghasilan:,}"
                    for nama, penghasilan in hasil
                )

            case ["tertinggi"]:
                nama, penghasilan = self._laporan.penghasilan_tertinggi()
                return f"{nama}: Rp{penghasilan:,}"

            case ["terendah"]:
                nama, penghasilan = self._laporan.penghasilan_terendah()
                return f"{nama}: Rp{penghasilan:,}"

            case ["total"]:
                return f"Total penghasilan: Rp{self._laporan.total_penghasilan():,}"

            case ["bantuan"]:
                return (
                    "Perintah tersedia: rekap, tertinggi, "
                    "terendah, total, bantuan"
                )

            case [nama_perintah, *_] if nama_perintah:
                return f"Perintah tidak dikenal: {nama_perintah}"

            case _:
                return "Perintah tidak boleh kosong."
