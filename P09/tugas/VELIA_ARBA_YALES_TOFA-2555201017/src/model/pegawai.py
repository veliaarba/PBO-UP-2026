from __future__ import annotations


class Pegawai:
    """Kelas induk untuk pegawai instansi di Kabupaten Kampar."""

    def __init__(self, nip: str, nama: str, gaji_pokok: int) -> None:
        if not nip or not nip.strip():
            raise ValueError("NIP tidak boleh kosong")
        if not nama or not nama.strip():
            raise ValueError("Nama pegawai tidak boleh kosong")
        if gaji_pokok <= 0:
            raise ValueError("Gaji pokok harus lebih dari nol")

        self._nip = nip
        self._nama = nama
        self._gaji_pokok = gaji_pokok

    @property
    def nip(self) -> str:
        return self._nip

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def gaji_pokok(self) -> int:
        return self._gaji_pokok

    def hitung_penghasilan(self, tambahan: int = 0) -> int:
        """Menghitung penghasilan dasar ditambah komponen tambahan."""
        if tambahan < 0:
            raise ValueError("Tambahan penghasilan tidak boleh negatif")
        return self._gaji_pokok + tambahan

    def __str__(self) -> str:
        return f"{self._nip} - {self._nama}"

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(nip={self._nip!r}, "
            f"nama={self._nama!r}, gaji_pokok={self._gaji_pokok!r})"
        )

    def __eq__(self, lain: object) -> bool:
        if not isinstance(lain, Pegawai):
            return NotImplemented
        return self._nip == lain._nip

    def __hash__(self) -> int:
        return hash(self._nip)
