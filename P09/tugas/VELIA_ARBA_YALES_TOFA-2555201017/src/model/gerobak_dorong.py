class GerobakDorong:
    """Gerobak dorong yang dapat disewakan tanpa mewarisi AlatTani."""

    def __init__(
        self, kode: str, nama: str, tarif_harian: int
    ) -> None:
        if not kode or not kode.strip():
            raise ValueError("Kode alat tidak boleh kosong")

        if not nama or not nama.strip():
            raise ValueError("Nama alat tidak boleh kosong")

        if tarif_harian <= 0:
            raise ValueError("Tarif harian harus lebih dari nol")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    def biaya_sewa(self, jumlah_hari: int) -> int:
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol")

        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        return f"[{self._kode}] {self._nama}"