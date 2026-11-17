"""Đa thức một biến (λ) và giải nghiệm đa thức (theo hợp đồng §0.7)."""

from __future__ import annotations

from fractions import Fraction
import math
from typing import Sequence, Union

from .dinh_dang_ma_tran import dinh_dang_so

So = Union[int, float, complex, Fraction]


def _rut_gon_he_so(he_so: Sequence[So]) -> tuple[So, ...]:
    """Loại bỏ các hệ số 0 ở bậc cao nhất (giữ lại ít nhất 1 phần tử)."""
    ds = list(he_so) if len(he_so) > 0 else [0]
    while len(ds) > 1 and ds[-1] == 0:
        ds.pop()
    return tuple(ds)


class DaThuc:
    """Đa thức một biến với hệ số lưu từ bậc thấp đến bậc cao."""

    def __init__(self, he_so: Sequence[So]) -> None:
        if len(he_so) == 0:
            self.he_so: tuple[So, ...] = (0,)
        else:
            self.he_so = _rut_gon_he_so(he_so)

    @property
    def bac(self) -> int:
        """Bậc của đa thức (đa thức 0 có bậc 0)."""
        return len(self.he_so) - 1

    def __call__(self, x: So) -> So:
        """Tính P(x) bằng sơ đồ Horner."""
        kq: So = 0
        for c in reversed(self.he_so):
            kq = kq * x + c
        return kq

    def __neg__(self) -> DaThuc:
        return DaThuc([-c for c in self.he_so])

    def __add__(self, other: DaThuc | So) -> DaThuc:
        if isinstance(other, DaThuc):
            n = max(len(self.he_so), len(other.he_so))
            kq = [
                (self.he_so[i] if i < len(self.he_so) else 0)
                + (other.he_so[i] if i < len(other.he_so) else 0)
                for i in range(n)
            ]
            return DaThuc(kq)
        if isinstance(other, (int, float, complex, Fraction)):
            kq = list(self.he_so)
            kq[0] = kq[0] + other
            return DaThuc(kq)
        return NotImplemented

    def __radd__(self, other: So) -> DaThuc:
        return self.__add__(other)

    def __sub__(self, other: DaThuc | So) -> DaThuc:
        if isinstance(other, (DaThuc, int, float, complex, Fraction)):
            return self.__add__(-other)
        return NotImplemented

    def __rsub__(self, other: So) -> DaThuc:
        if isinstance(other, (int, float, complex, Fraction)):
            return (-self).__add__(other)
        return NotImplemented

    def __mul__(self, other: DaThuc | So) -> DaThuc:
        if isinstance(other, DaThuc):
            kq: list[So] = [0] * (len(self.he_so) + len(other.he_so) - 1)
            for i, a in enumerate(self.he_so):
                for j, b in enumerate(other.he_so):
                    kq[i + j] = kq[i + j] + a * b
            return DaThuc(kq)
        if isinstance(other, (int, float, complex, Fraction)):
            return DaThuc([c * other for c in self.he_so])
        return NotImplemented

    def __rmul__(self, other: So) -> DaThuc:
        return self.__mul__(other)

    def __pow__(self, n: int) -> DaThuc:
        if not isinstance(n, int) or n < 0:
            raise ValueError(f"Số mũ của đa thức phải là số nguyên >= 0, nhận được {n!r}.")
        kq = DaThuc([1])
        co_so = self
        mu = n
        while mu > 0:
            if mu % 2 == 1:
                kq = kq * co_so
            co_so = co_so * co_so
            mu //= 2
        return kq

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DaThuc):
            return False
        if self.bac != other.bac:
            return False
        return all(a == b for a, b in zip(self.he_so, other.he_so))

    def __str__(self) -> str:
        if all(c == 0 for c in self.he_so):
            return "0"
        cac_hang_tu: list[str] = []
        for bac in range(self.bac, -1, -1):
            c = self.he_so[bac]
            if c == 0:
                continue
            la_am = isinstance(c, (int, float, Fraction)) and c < 0
            tri = -c if la_am else c
            dau = " - " if la_am else (" + " if cac_hang_tu else "")
            if not cac_hang_tu and la_am:
                dau = "-"

            if bac == 0:
                phan_bien = dinh_dang_so(tri)
            else:
                phan_he_so = "" if tri == 1 else dinh_dang_so(tri)
                phan_bien = f"{phan_he_so}λ" if bac == 1 else f"{phan_he_so}λ^{bac}"
            cac_hang_tu.append(f"{dau}{phan_bien}")
        return "".join(cac_hang_tu) or "0"

    def __repr__(self) -> str:
        return f"DaThuc({list(self.he_so)!r})"


def tim_nghiem(P: DaThuc, dung_sai: float = 1e-10) -> list[tuple[So, int]]:
    """Tìm nghiệm của đa thức P(λ) = 0, trả về danh sách (nghiệm, bội đại số).

    Bước 1: Thử nghiệm hữu tỉ nếu mọi hệ số đều là int/Fraction.
    Bước 2: Dùng thuật toán Durand–Kerner cho phần còn lại (không dùng np.roots).
    """
    if P.bac == 0:
        return []

    cac_nghiem: list[So] = []
    he_so = list(P.he_so)

    # Khử nghiệm λ = 0 nếu có
    while len(he_so) > 1 and he_so[0] == 0:
        cac_nghiem.append(Fraction(0) if all(isinstance(c, (int, Fraction)) for c in he_so) else 0.0)
        he_so.pop(0)

    if len(he_so) <= 1:
        return _gop_nghiem(cac_nghiem, dung_sai)

    # Bước 1: Thử nghiệm hữu tỉ khi mọi hệ số hữu tỉ
    if all(isinstance(c, (int, Fraction)) for c in he_so):
        he_so, nghiem_huu_ti = _tim_nghiem_huu_ti(he_so)
        cac_nghiem.extend(nghiem_huu_ti)

    # Bước 2: Durand-Kerner cho đa thức còn lại (nếu bậc >= 1)
    if len(he_so) > 1:
        cac_nghiem.extend(_durand_kerner(he_so, dung_sai=dung_sai))

    return _gop_nghiem(cac_nghiem, dung_sai)


def _uoc_duong(n: int) -> list[int]:
    n = abs(n)
    if n == 0:
        return [1]
    uoc = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            uoc.add(i)
            uoc.add(n // i)
    return sorted(uoc)


def _chia_hoocner(he_so: list[Fraction], r: Fraction) -> tuple[list[Fraction], Fraction]:
    """Chia đa thức (bậc thấp -> cao) cho (λ - r)."""
    n = len(he_so) - 1
    thuong = [Fraction(0)] * n
    du = he_so[n]
    for i in range(n - 1, -1, -1):
        thuong[i] = du
        du = he_so[i] + du * r
    return thuong, du


def _tim_nghiem_huu_ti(he_so: Sequence[int | Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    fracs = [Fraction(c) for c in he_so]
    nghiem: list[Fraction] = []
    while len(fracs) > 1:
        mau_chung = 1
        for c in fracs:
            mau_chung = math.lcm(mau_chung, c.denominator)
        nguyen = [int(c * mau_chung) for c in fracs]
        p_uoc = _uoc_duong(nguyen[0])
        q_uoc = _uoc_duong(nguyen[-1])
        tim_thay = None
        for p in p_uoc:
            for q in q_uoc:
                for dau in (1, -1):
                    r = Fraction(dau * p, q)
                    thuong, du = _chia_hoocner(fracs, r)
                    if du == 0:
                        tim_thay = (r, thuong)
                        break
                if tim_thay is not None:
                    break
            if tim_thay is not None:
                break
        if tim_thay is None:
            break
        r, fracs = tim_thay
        nghiem.append(r)
    return fracs, nghiem


def _durand_kerner(he_so: Sequence[So], dung_sai: float = 1e-10, max_iter: int = 2000) -> list[complex | float]:
    n = len(he_so) - 1
    an = complex(he_so[-1])
    chuan_hoa = [complex(c) / an for c in he_so]

    def eval_p(z: complex) -> complex:
        kq = 0j
        for c in reversed(chuan_hoa):
            kq = kq * z + c
        return kq

    # Bán kính ước lượng Cauchy
    ban_kinh = 1.0 + max((abs(c) for c in chuan_hoa[:-1]), default=0.0)
    z = [
        ban_kinh * 0.5 * complex(math.cos(2 * math.pi * k / n + 0.123), math.sin(2 * math.pi * k / n + 0.123))
        for k in range(n)
    ]

    for _ in range(max_iter):
        max_buoc = 0.0
        for i in range(n):
            mau = 1.0 + 0j
            for j in range(n):
                if i != j:
                    diff = z[i] - z[j]
                    mau *= diff if abs(diff) > 1e-15 else 1e-15
            delta = eval_p(z[i]) / mau
            z[i] -= delta
            max_buoc = max(max_buoc, abs(delta))
        if max_buoc < dung_sai * 1e-2:
            break

    kq: list[complex | float] = []
    for val in z:
        if abs(val.imag) <= dung_sai:
            kq.append(float(val.real))
        else:
            kq.append(complex(val))
    return kq


def _gop_nghiem(cac_nghiem: list[So], dung_sai: float) -> list[tuple[So, int]]:
    nhom: list[tuple[So, int]] = []
    for r in cac_nghiem:
        gan = False
        for idx, (dai_dien, boi) in enumerate(nhom):
            if abs(complex(r) - complex(dai_dien)) <= dung_sai:
                nhom[idx] = (dai_dien, boi + 1)
                gan = True
                break
        if not gan:
            nhom.append((r, 1))
    return nhom
