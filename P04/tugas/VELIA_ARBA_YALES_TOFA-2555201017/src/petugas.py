class Petugas:
    """Kelas untuk merepresentasikan petugas pengelola kios."""

    def __init__(self, nama: str, id_petugas: str) -> None:
        self._nama = nama
        self._id_petugas = id_petugas

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def id_petugas(self) -> str:
        return self._id_petugas

    def get_info(self) -> str:
        return f"Petugas {self._nama} ({self._id_petugas})"