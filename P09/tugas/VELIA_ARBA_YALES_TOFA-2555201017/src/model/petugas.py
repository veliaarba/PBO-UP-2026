from __future__ import annotations

class Petugas:
    """Kelas untuk merepresentasikan data petugas penyewaan alat."""

    def __init__(self, id_petugas: str, nama: str) -> None:
        self.__id_petugas: str = id_petugas
        self.__nama: str = nama

    @property
    def id_petugas(self) -> str:
        return self.__id_petugas

    @property
    def nama(self) -> str:
        return self.__nama