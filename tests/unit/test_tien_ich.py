"""Kiểm thử cho tầng hạ tầng: `loi`, `tien_ich`, `dich_vu`."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import sys
import unittest

import numpy as np

# Đảm bảo import được `mlmath` từ `src/` ngay cả khi chưa `pip install -e .`
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from mlmath.dich_vu import DANG_KY, MucThuatToan, ThamSo, chay, dang_ky_thuat_toan, liet_ke
from mlmath.loi import LoiDieuKien, LoiDuLieu, LoiHoiTu, LoiKichThuoc, LoiMaTranSuyBien
from mlmath.tien_ich import (
    DaThuc,
    NhatKyTinhToan,
    dinh_dang_ma_tran,
    dinh_dang_so,
    gan_bang,
    ghi_json,
    ghi_txt,
    sai_so_tuong_doi,
    sai_so_tuyet_doi,
    tim_nghiem,
    xac_thuc_ma_tran,
    xac_thuc_nhan_duoc,
    xac_thuc_vec_to,
    xac_thuc_vuong,
)


class TestLoiVaTienIch(unittest.TestCase):
    def test_phan_cap_ngoai_le(self) -> None:
        self.assertTrue(issubclass(LoiKichThuoc, ValueError))
        self.assertTrue(issubclass(LoiMaTranSuyBien, ValueError))
        self.assertTrue(issubclass(LoiDieuKien, ValueError))
        self.assertTrue(issubclass(LoiDuLieu, ValueError))
        self.assertTrue(issubclass(LoiHoiTu, RuntimeError))

    def test_xac_thuc_du_lieu(self) -> None:
        A_raw = [[1, 2], [3, 4]]
        A = xac_thuc_vuong(A_raw)
        self.assertEqual(A.shape, (2, 2))
        self.assertEqual(A.dtype, np.float64)

        F = xac_thuc_ma_tran([[Fraction(1, 2), 1], [0, Fraction(3, 4)]])
        self.assertEqual(F.dtype, object)
        self.assertEqual(F[0, 0], Fraction(1, 2))

        with self.assertRaises(LoiDuLieu):
            xac_thuc_ma_tran([[1.0, float("nan")]])
        with self.assertRaises(LoiKichThuoc):
            xac_thuc_vuong([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(LoiKichThuoc):
            xac_thuc_nhan_duoc(np.zeros((2, 3)), np.zeros((2, 2)))
        v = xac_thuc_vec_to([1, 2, 3])
        self.assertEqual(v.shape, (3,))

    def test_nhat_ky_va_sao_chep(self) -> None:
        nk = NhatKyTinhToan("test")
        mat = np.array([[1.0, 2.0], [3.0, 4.0]])
        nk.ghi_buoc("Buoc 1", "A", trang_thai=mat)
        mat[0, 0] = 999.0
        self.assertEqual(nk.cac_buoc[0].trang_thai[0, 0], 1.0)

        rong = NhatKyTinhToan.rong()
        rong.ghi_buoc("Khong ghi", trang_thai=mat)
        self.assertEqual(len(rong.cac_buoc), 0)

    def test_dinh_dang_va_sai_so(self) -> None:
        self.assertEqual(dinh_dang_so(Fraction(1, 3)), "1/3")
        s = dinh_dang_ma_tran(np.array([[1, 2], [3, 4]]))
        self.assertIn("[", s)
        self.assertAlmostEqual(sai_so_tuyet_doi([1.0, 0.0], [1.0, 3.0]), 3.0)
        self.assertLess(sai_so_tuong_doi([1.0, 2.0], [1.0, 2.0 + 1e-10]), 1e-9)
        self.assertTrue(gan_bang([1.0, 2.0], [1.0, 2.0]))

    def test_da_thuc_va_tim_nghiem(self) -> None:
        # (λ - 1)(λ - 2) = λ^2 - 3λ + 2 -> hệ số bậc thấp đến cao: [2, -3, 1]
        p = DaThuc([2, -3, 1])
        self.assertEqual(p.bac, 2)
        self.assertEqual(p(1), 0)
        self.assertEqual(p(2), 0)
        nghiem = tim_nghiem(p)
        gia_tri = sorted(float(r) for r, _ in nghiem)
        self.assertEqual(len(gia_tri), 2)
        self.assertAlmostEqual(gia_tri[0], 1.0)
        self.assertAlmostEqual(gia_tri[1], 2.0)

    def test_dich_vu_va_xuat_ket_qua(self) -> None:
        def _cong_demo(A: np.ndarray, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
            if nhat_ky is not None:
                nhat_ky.ghi_buoc("Nhan doi", "2*A", trang_thai=A, ket_qua=2 * A)
            return 2 * A

        ma_demo = "test.demo_nhan_doi"
        dang_ky_thuat_toan(
            MucThuatToan(
                ma=ma_demo,
                chuong=1,
                ten_hien_thi="Demo nhân đôi",
                ham=_cong_demo,
                tham_so=[ThamSo("A", "ma_tran", "Ma trận đầu vào")],
            )
        )
        try:
            self.assertTrue(any(m.ma == ma_demo for m in liet_ke(chuong=1)))
            kq = chay(ma_demo, A=np.array([[1.0, 2.0], [3.0, 4.0]]))
            self.assertEqual(len(kq.cac_buoc), 1)
            self.assertTrue(gan_bang(kq.ket_qua, np.array([[2.0, 4.0], [6.0, 8.0]])))

            tmp_dir = ROOT / "tests" / "_tmp_out"
            txt_p = ghi_txt(kq, tmp_dir)
            json_p = ghi_json(kq, tmp_dir)
            self.assertTrue(txt_p.exists())
            data = json.loads(json_p.read_text(encoding="utf-8"))
            self.assertEqual(data["ten_thuat_toan"], "Demo nhân đôi")
            txt_p.unlink()
            json_p.unlink()
            tmp_dir.rmdir()
        finally:
            DANG_KY.pop(ma_demo, None)


if __name__ == "__main__":
    unittest.main()
