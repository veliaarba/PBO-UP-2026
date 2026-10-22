# pbo-sipala-CONTOH — Pertemuan 4

Kode acuan Pertemuan 4 — Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai

## Empat jenis anggota kelas yang diterapkan

| Jenis | Contoh di `AlatTani` |
|---|---|
| Konstanta kelas | `TARIF_MINIMUM`, `TARIF_MAKSIMUM`, `PERSEN_DENDA_HARIAN`, `PEMISAH_BARIS` |
| Atribut kelas | `_jumlah_terdaftar` — dinaikkan lewat **nama kelas**, bukan `self` |
| `@classmethod` | `dari_baris_csv()` konstruktor alternatif, `jumlah_terdaftar()` |
| `@staticmethod` | `tarif_wajar()`, `format_rupiah()` — dipanggil tanpa objek |

## Tiga gerbang

```
python periksa_pbo.py src --profil p04
python -m mypy
python -m pytest
python -m src.main
```

Keluaran yang diharapkan:

```
LOLOS. Tidak ada pelanggaran disiplin berorientasi objek.
Success: no issues found in 10 source files
21 passed

Sebelum pendataan, alat terdaftar: 0
  [TR-01] Traktor Roda Dua Kubota — Rp150.000/hari
  [PA-01] Pompa Air 3 Inci — Rp75.000/hari
Sesudah pendataan, alat terdaftar: 4

--- Memeriksa tarif tanpa membuat objek ---
         Rp5.000  →  ditolak
       Rp150.000  →  wajar
     Rp6.000.000  →  ditolak
```

## Dua kesalahan yang sengaja ditanam

**① Pencacah ditulis lewat `self`** — `python pencacah_bocor.py`:

```
TR-01 melaporkan jumlah = 1
TR-02 melaporkan jumlah = 1
PA-01 melaporkan jumlah = 1
Pencacah milik kelas : 0
Isi objek a          : ['_kode', '_jumlah_terdaftar']
```

`self._jumlah_terdaftar += 1` sesungguhnya berarti
`self._jumlah_terdaftar = self._jumlah_terdaftar + 1`.
Sisi kanan **membaca dari kelas** (nol); sisi kiri **menulis ke objek**.
Lahirlah atribut baru milik objek yang menutupi atribut kelas.

**② Parameter berdefault yang dapat diubah** — `python default_berbagi.py`:

```
Budi: ['TR-01', 'PA-01']
Siti: ['TR-01', 'PA-01']        ← Siti belum menyewa apa pun
Daftar yang sama? True
```

Nilai default dibuat **satu kali** saat baris `def` dijalankan, bukan tiap kali
objek dibuat. Perbaikannya: `riwayat: list[str] | None = None`, lalu
`self._riwayat = list(riwayat) if riwayat else []`.

## Yang tertangkap alat dan yang tidak

```
python -m ruff check default_berbagi.py
→ B006 Do not use mutable data structures for argument defaults

python -m ruff check pencacah_bocor.py
→ All checks passed!
```

Kesalahan ② tertangkap Ruff. Kesalahan ① lolos dari **seluruh** perkakas yang
dipakai mata kuliah ini. Tidak ada alat yang menangkap segalanya — itulah
sebabnya pemahaman dan pengujian tetap tidak tergantikan.

## Catatan versi

`pyproject.toml` memakai `python_version = "3.14"`. Sesuaikan pada berkas milik
dosen bila laboratorium memakai versi lain — bukan pada berkas milik mahasiswa.
