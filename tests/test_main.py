from src.models import DaftarMahasiswa, Mahasiswa


class TestDaftarMahasiswa:
    def test_hapus_mahasiswa(self):
        db = DaftarMahasiswa()
        mhs = Mahasiswa(
            "20241320039",
            "Jilan Jalilah",
            "Sistem Informasi",
            2024,
            3.50,
        )
        db.tambah(mhs)

        assert db.hapus("20241320039") is True
        assert db.jumlah == 0
        assert db.cari("20241320039") is None

    def test_hapus_nim_tidak_ditemukan(self):
        db = DaftarMahasiswa()

        assert db.hapus("20249999999") is False
