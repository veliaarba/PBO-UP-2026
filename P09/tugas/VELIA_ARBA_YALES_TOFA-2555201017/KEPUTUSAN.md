# Keputusan Perancangan P09

## Pemilihan ABC

Saya memilih abc.ABC untuk kelas AlatTani karena kelas ini merupakan induk dari jenis alat tani yang memiliki kesamaan dasar. Kelas AlatTani tidak boleh dibuat objeknya secara langsung karena masih bersifat umum. Dengan menggunakan ABC dan abstractmethod, setiap kelas turunan diwajibkan menyediakan method biaya_tambahan() dan syarat_pemakaian(). Cara ini membuat kontrak lebih jelas dan kesalahan dapat diketahui sejak objek dibuat.

## Pemilihan Protocol

Saya memilih typing.Protocol untuk kontrak Sewaan karena tidak semua objek yang dapat disewakan harus berasal dari keluarga AlatTani. Contohnya GerobakDorong yang dapat memenuhi kontrak Sewaan tanpa harus mewarisi AlatTani. Protocol memungkinkan kelas memenuhi kontrak berdasarkan method dan atribut yang dimilikinya. Dengan demikian, program menjadi lebih fleksibel tanpa memaksakan hubungan pewarisan yang tidak sesuai.
