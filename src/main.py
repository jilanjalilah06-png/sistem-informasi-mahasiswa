import pytest
from src.models import Mahasiswa, DaftarMahasiswa


class TestMahasiswa:

    def test_buat_mahasiswa_valid(self):
        mhs = Mahasiswa(
            "20241320039",
            "Jilan Jalilah",
            "Sistem Informasi",
            2024,
            3.50
        )

        assert mhs.nim == "20241320039"
        assert mhs.ipk == 3.50

    def test_nim_tidak_valid(self):
        with pytest.raises(ValueError):
            Mahasiswa(
                "abc",
                "Test",
                "Sistem Informasi",
                2024,
                3.0
            )

    def test_ipk_diluar_range(self):
        with pytest.raises(ValueError):
            Mahasiswa(
                "20241320040",
                "Test",
                "Sistem Informasi",
                2024,
                5.0
            )


class TestDaftarMahasiswa:

    def test_tambah_dan_cari(self):
        db = DaftarMahasiswa()

        mhs = Mahasiswa(
            "20241320039",
            "Jilan",
            "Sistem Informasi",
            2024,
            3.50
        )

        db.tambah(mhs)

        assert db.cari("20241320039") == mhs
        assert db.jumlah == 1

    def test_nim_duplikat(self):
        db = DaftarMahasiswa()

        m1 = Mahasiswa(
            "20241320039",
            "Jilan",
            "Sistem Informasi",
            2024,
            3.50
        )

        m2 = Mahasiswa(
            "20241320039",
            "Budi",
            "Sistem Informasi",
            2024,
            3.00
        )

        db.tambah(m1)

        with pytest.raises(ValueError):
            db.tambah(m2)