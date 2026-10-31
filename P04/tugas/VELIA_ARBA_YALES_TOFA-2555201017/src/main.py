"""Program utama pendataan dan penyewaan alat pertanian."""
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    print("=== PROGRAM PENYEWAAN ALAT PERTANIAN ===")
    
    # Membuat objek alamat
    alamat_pembeli = Alamat("Pulau Jambu", "Kuok", "Kampar")
    
    # Membuat objek penyewa
    penyewa = Penyewa("1401011234567890", "Budi Santoso", alamat_pembeli, "081234567890")
    print(penyewa.identitas())
    print(penyewa.kontak())
    
    print("-" * 40)
    
    # Membuat objek alat tani
    alat1 = AlatTani("TR-01", "Traktor Sawah", 150000)
    print(alat1.keterangan())
    
    # Menghitung biaya sewa dan denda
    lama_sewa = 4
    biaya = alat1.biaya_sewa(lama_sewa)
    print(f"Biaya sewa untuk {lama_sewa} hari: {AlatTani.format_rupiah(biaya)}")
    
    terlambat = 2
    denda = alat1.denda_keterlambatan(terlambat)
    print(f"Denda keterlambatan {terlambat} hari: {AlatTani.format_rupiah(denda)}")


if __name__ == "__main__":
    main()