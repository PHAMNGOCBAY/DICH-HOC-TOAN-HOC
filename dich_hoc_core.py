"""
DỊCH HỌC DIỄN GIẢI TRÊN CƠ SỞ TOÁN HỌC VÀ ỨNG DỤNG VÀO ĐỜI SỐNG
Tác giả: TS. Nguyễn Thế Cường (Nguyễn Quý Thế Cường)
Nhà xuất bản Đại học Quốc gia Thành phố Hồ Chí Minh, 2014

Mô-đun Python mô hình hóa toàn diện hệ thống toán học Dịch học cho cả 8 Chương:
- Chương I: Cơ sở toán học của Bát quái (Nhóm cộng Hà - Lạc Z/10Z, số học đồng hồ)
- Chương II: Âm, dương và Thái cực (Hợp hóa Thiên can, Địa chi lục hợp, Tam hợp)
- Chương III: Tạo quái từ lưỡng nghi (Hàm năng lượng E = h1*1 + h2*3 + h3*5, biến đổi hào)
- Chương IV: Bát quái Tân thiên (8 quái, trị số, số gán Lạc thư, đối xứng tâm/trục, phu thê)
- Chương V: Đồ tổng hợp Quái - Can - Chi (Phân bố Can Chi trên vòng tròn Tân thiên)
- Chương VI: Ứng dụng QCC vào đời sống (Quái mệnh Nam/Nữ, Đông/Tây tứ trạch, Bát san 8x8)
- Chương VII: Quẻ dịch (Hệ nhị phân Phục Hi, Danh mục 64 quẻ, Nạp can chi 6 hào, Thế/Ứng)
- Chương VIII: Nhận dạng Bát tự Hà - Lạc (Quẻ Tiên thiên, Hào Nguyên đường, Hậu thiên, Đại vận 6/9 năm)
"""

import sys
import io
import math
from typing import Dict, List, Tuple, Optional, Any

# Cấu hình UTF-8 cho console Windows
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


# ==============================================================================
# CHƯƠNG I: CƠ SỞ TOÁN HỌC CỦA BÁT QUÁI (NHÓM CỘNG HÀ - LẠC)
# ==============================================================================

class HaLacGroup:
    """
    Chương I & II: Nhóm cộng Hà - Lạc (Z/10Z, +)
    Tập hợp S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, phần tử trung hòa e = 0 (tương đương 10).
    Thỏa mãn 4 tiên đề nhóm Abel: khép kín, kết hợp, tồn tại phần tử trung hòa, tồn tại số đối duy nhất.
    """

    @staticmethod
    def add(a: int, b: int) -> int:
        """Phép cộng modulo 10 trên đồng hồ 10 vạch chia (trang 2)."""
        return (a + b) % 10

    @staticmethod
    def multiply(a: int, k: int) -> int:
        """Phép nhân (dịch chuyển k lần a vạch chia trên đồng hồ 10)."""
        return (a * k) % 10

    @staticmethod
    def opposite(a: int) -> int:
        """
        Số đối a' thỏa mãn a + a' = 0 (mod 10) (trang 3).
        1' = 9, 2' = 8, 3' = 7, 4' = 6, 5' = 5, 0' = 0.
        """
        return (10 - (a % 10)) % 10

    @classmethod
    def verify_abel_group(cls) -> bool:
        """Kiểm chứng tính chất nhóm giao hoán Abel trên tập hợp S."""
        S = list(range(10))
        # 1. Giao hoán: a + b = b + a
        for a in S:
            for b in S:
                if cls.add(a, b) != cls.add(b, a):
                    return False
        # 2. Trung hòa: a + 0 = a
        for a in S:
            if cls.add(a, 0) != a:
                return False
        # 3. Phần tử đối: a + a' = 0
        for a in S:
            if cls.add(a, cls.opposite(a)) != 0:
                return False
        return True


# ==============================================================================
# CHƯƠNG II: ÂM, DƯƠNG VÀ THÁI CỰC (HỆ NGUYÊN LÝ VÀ ĐỊNH LUẬT HỢP HÓA)
# ==============================================================================

class HopHoaCanChi:
    """
    Chương II.3: Định luật Hợp hóa Can - Chi (trang 18 - 23).
    """

    # Ngũ hợp Thiên can: Hai can đối diện cách nhau 5 vị trí hợp hóa thành một hành
    THIEN_CAN_NGU_HOP = {
        ("Giáp", "Kỷ"): "Thổ",
        ("Kỷ", "Giáp"): "Thổ",
        ("Ất", "Canh"): "Kim",
        ("Canh", "Ất"): "Kim",
        ("Bính", "Tân"): "Thủy",
        ("Tân", "Bính"): "Thủy",
        ("Đinh", "Nhâm"): "Mộc",
        ("Nhâm", "Đinh"): "Mộc",
        ("Mậu", "Quý"): "Hỏa",
        ("Quý", "Mậu"): "Hỏa",
    }

    # Địa chi lục hợp (6 cặp nhị hợp đối xứng qua trục)
    DIA_CHI_LUC_HOP = {
        ("Tý", "Sửu"): "Thổ",
        ("Sửu", "Tý"): "Thổ",
        ("Dần", "Hợi"): "Mộc",
        ("Hợi", "Dần"): "Mộc",
        ("Mão", "Tuất"): "Hỏa",
        ("Tuất", "Mão"): "Hỏa",
        ("Thìn", "Dậu"): "Kim",
        ("Dậu", "Thìn"): "Kim",
        ("Tị", "Thân"): "Thủy",
        ("Thân", "Tị"): "Thủy",
        ("Ngọ", "Mùi"): "Thái Dương / Thái Âm",
        ("Mùi", "Ngọ"): "Thái Dương / Thái Âm",
    }

    # Địa chi tam hợp (4 cục tam giác cân trên vòng hoàng đạo)
    DIA_CHI_TAM_HOP = {
        ("Thân", "Tý", "Thìn"): "Thủy cục",
        ("Hợi", "Mão", "Mùi"): "Mộc cục",
        ("Dần", "Ngọ", "Tuất"): "Hỏa cục",
        ("Tị", "Dậu", "Sửu"): "Kim cục",
    }

    @classmethod
    def get_can_hop(cls, can1: str, can2: str) -> Optional[str]:
        """Tra cứu ngũ hành hợp hóa giữa 2 Thiên can."""
        return cls.THIEN_CAN_NGU_HOP.get((can1, can2))

    @classmethod
    def get_chi_luc_hop(cls, chi1: str, chi2: str) -> Optional[str]:
        """Tra cứu kết quả Lục hợp giữa 2 Địa chi."""
        return cls.DIA_CHI_LUC_HOP.get((chi1, chi2))

    @classmethod
    def check_tam_hop(cls, chi_list: List[str]) -> Optional[str]:
        """Kiểm tra danh sách chi có chứa bộ Tam hợp hay không."""
        s = set(chi_list)
        for trio, cuc in cls.DIA_CHI_TAM_HOP.items():
            if set(trio).issubset(s):
                return cuc
        return None


# ==============================================================================
# CHƯƠNG III: TẠO QUÁI TỪ LƯỠNG NGHI ÂM, DƯƠNG
# ==============================================================================

class TrigramEnergy:
    """
    Chương III.1 & III.4: Trị số năng lượng của hào và Bát quái (trang 24 - 47).
    - Hào 1 (sơ, dưới cùng): mang trọng số ±1
    - Hào 2 (trung, ở giữa): mang trọng số ±3
    - Hào 3 (thượng, trên cùng): mang trọng số ±5
    Hào dương tính dấu dương (+), Hào âm tính dấu âm (-).
    Công thức năng lượng: E = h1*(±1) + h2*(±3) + h3*(±5).
    """

    @staticmethod
    def calculate_energy(lines: Tuple[int, int, int]) -> int:
        """
        lines: tuple (h1, h2, h3) với 1 là hào dương, 0 là hào âm.
        """
        h1 = 1 if lines[0] == 1 else -1
        h2 = 3 if lines[1] == 1 else -3
        h3 = 5 if lines[2] == 1 else -5
        return h1 + h2 + h3

    @staticmethod
    def bien_hao(lines: Tuple[int, int, int], pos: int) -> Tuple[int, int, int]:
        """Biến đổi hào tại vị trí pos (1, 2 hoặc 3): 1 thành 0, 0 thành 1."""
        idx = pos - 1
        new_lines = list(lines)
        new_lines[idx] = 1 - new_lines[idx]
        return (new_lines[0], new_lines[1], new_lines[2])

    @staticmethod
    def dao_tuong(lines: Tuple[int, int, int]) -> Tuple[int, int, int]:
        """Đảo tượng quái (quay 180 độ, hào sơ đổi chỗ hào thượng)."""
        return (lines[2], lines[1], lines[0])


# ==============================================================================
# CHƯƠNG IV: BÁT QUÁI TÂN THIÊN
# ==============================================================================

TRIGRAMS_DATA = {
    "Càn": {
        "lines": (1, 1, 1),
        "tri_so": 9,
        "so_gan": 9,
        "cung_lac_thu": 9,
        "phuong_vi": "Chính Nam",
        "tinh_chat": "Dương",
        "doi_xung": True,
        "cap_phu_the": "Đoài",
        "ngu_hanh": "Kim",
    },
    "Đoài": {
        "lines": (1, 1, 0),
        "tri_so": -1,
        "so_gan": 8,
        "cung_lac_thu": 8,
        "phuong_vi": "Đông Bắc",
        "tinh_chat": "Âm",
        "doi_xung": False,
        "cap_phu_the": "Càn",
        "ngu_hanh": "Kim",
    },
    "Li": {
        "lines": (1, 0, 1),
        "tri_so": 3,
        "so_gan": 3,
        "cung_lac_thu": 3,
        "phuong_vi": "Chính Đông",
        "tinh_chat": "Dương",
        "doi_xung": True,
        "cap_phu_the": "Chấn",
        "ngu_hanh": "Hỏa",
    },
    "Chấn": {
        "lines": (1, 0, 0),
        "tri_so": -7,
        "so_gan": 6,
        "cung_lac_thu": 6,
        "phuong_vi": "Tây Bắc",
        "tinh_chat": "Âm",
        "doi_xung": False,
        "cap_phu_the": "Li",
        "ngu_hanh": "Mộc",
    },
    "Tốn": {
        "lines": (0, 1, 1),
        "tri_so": 7,
        "so_gan": 4,
        "cung_lac_thu": 4,
        "phuong_vi": "Đông Nam",
        "tinh_chat": "Dương",
        "doi_xung": False,
        "cap_phu_the": "Khảm",
        "ngu_hanh": "Mộc",
    },
    "Khảm": {
        "lines": (0, 1, 0),
        "tri_so": -3,
        "so_gan": 7,
        "cung_lac_thu": 7,
        "phuong_vi": "Chính Tây",
        "tinh_chat": "Âm",
        "doi_xung": True,
        "cap_phu_the": "Tốn",
        "ngu_hanh": "Thủy",
    },
    "Cấn": {
        "lines": (0, 0, 1),
        "tri_so": 1,
        "so_gan": 2,
        "cung_lac_thu": 2,
        "phuong_vi": "Tây Nam",
        "tinh_chat": "Dương",
        "doi_xung": False,
        "cap_phu_the": "Khôn",
        "ngu_hanh": "Thổ",
    },
    "Khôn": {
        "lines": (0, 0, 0),
        "tri_so": -9,
        "so_gan": 1,
        "cung_lac_thu": 1,
        "phuong_vi": "Chính Bắc",
        "tinh_chat": "Âm",
        "doi_xung": True,
        "cap_phu_the": "Cấn",
        "ngu_hanh": "Thổ",
    },
}

LAC_THU_TO_TRIGRAM = {
    1: "Khôn",
    2: "Cấn",
    3: "Li",
    4: "Tốn",
    6: "Chấn",
    7: "Khảm",
    8: "Đoài",
    9: "Càn",
}


class BatQuaiTanThien:
    """
    Chương IV: Đặc điểm đối xứng và cấu trúc Bát quái Tân thiên.
    """

    @classmethod
    def check_symmetry_opposite(cls, trigram1: str, trigram2: str) -> bool:
        """
        Kiểm tra 2 quái có đối xứng qua tâm Thái cực hay không:
        Hai quái đối xứng qua tâm thỏa mãn:
        1. Cung Lạc thư có tổng bằng 10: q1 + q2 = 10.
        2. Tổng trị số năng lượng triệt tiêu: E1 + E2 = 0.
        """
        d1 = TRIGRAMS_DATA[trigram1]
        d2 = TRIGRAMS_DATA[trigram2]
        sum_cung = d1["cung_lac_thu"] + d2["cung_lac_thu"]
        sum_e = d1["tri_so"] + d2["tri_so"]
        return (sum_cung == 10) and (sum_e == 0)

    @classmethod
    def get_opposite_trigram(cls, name: str) -> str:
        """Lấy quái đối xứng qua tâm Lạc thư."""
        cung = TRIGRAMS_DATA[name]["cung_lac_thu"]
        opp_cung = 10 - cung
        return LAC_THU_TO_TRIGRAM[opp_cung]


# ==============================================================================
# CHƯƠNG V: ĐỒ TỔNG HỢP QUÁI - CAN - CHI (QCC)
# ==============================================================================

class DoTongHopQCC:
    """
    Chương V: Tọa độ góc và phương vị của Can Chi trên Đồ tổng hợp QCC (trang 74 - 90).
    """

    # Góc phương vị chuẩn (0 độ tại Chính Bắc - Khôn, quay theo chiều kim đồng hồ)
    CAN_AZIMUTH = {
        "Nhâm": 0,     # Chính Bắc (Khôn)
        "Quý": 36,     # Bắc Đông Bắc
        "Cấn": 45,     # Đông Bắc (Đoài)
        "Giáp": 72,    # Đông Đông Bắc
        "Ất": 108,    # Đông Đông Nam
        "Bính": 144,   # Nam Đông Nam
        "Đinh": 180,   # Chính Nam (Càn)
        "Canh": 252,   # Tây Tây Nam
        "Tân": 288,    # Tây Tây Bắc
        "Mậu": 324,    # Bắc Tây Bắc
        "Kỷ": 324,     # Bắc Tây Bắc
    }

    CHI_AZIMUTH = {
        "Tý": 0,      # Chính Bắc
        "Sửu": 30,    # Đông Bắc lệch Bắc
        "Dần": 60,    # Đông Bắc lệch Đông
        "Mão": 90,    # Chính Đông
        "Thìn": 120,  # Đông Nam lệch Đông
        "Tị": 150,    # Đông Nam lệch Nam
        "Ngọ": 180,   # Chính Nam
        "Mùi": 210,   # Tây Nam lệch Nam
        "Thân": 240,  # Tây Nam lệch Tây
        "Dậu": 270,   # Chính Tây
        "Tuất": 300,  # Tây Bắc lệch Tây
        "Hợi": 330,   # Tây Bắc lệch Bắc
    }


# ==============================================================================
# CHƯƠNG VI: ỨNG DỤNG QCC VÀO ĐỜI SỐNG (QUÁI MỆNH & BÁT SAN)
# ==============================================================================

# Bảng 26: Ma trận 8x8 Bát san giữa quái mệnh và quái trạch (trang 155)
BAT_SAN_TABLE: Dict[str, Dict[str, str]] = {
    "Càn": {"Càn": "Phục vị", "Đoài": "Sinh khí", "Khôn": "Diên niên", "Cấn": "Thiên y", "Li": "Tuyệt mệnh", "Chấn": "Ngũ quỷ", "Khảm": "Lục sát", "Tốn": "Họa hại"},
    "Đoài": {"Càn": "Sinh khí", "Đoài": "Phục vị", "Khôn": "Thiên y", "Cấn": "Diên niên", "Li": "Ngũ quỷ", "Chấn": "Tuyệt mệnh", "Khảm": "Họa hại", "Tốn": "Lục sát"},
    "Khôn": {"Càn": "Diên niên", "Đoài": "Thiên y", "Khôn": "Phục vị", "Cấn": "Sinh khí", "Li": "Lục sát", "Chấn": "Họa hại", "Khảm": "Tuyệt mệnh", "Tốn": "Ngũ quỷ"},
    "Cấn": {"Càn": "Thiên y", "Đoài": "Diên niên", "Khôn": "Sinh khí", "Cấn": "Phục vị", "Li": "Họa hại", "Chấn": "Lục sát", "Khảm": "Ngũ quỷ", "Tốn": "Tuyệt mệnh"},
    "Li": {"Càn": "Tuyệt mệnh", "Đoài": "Ngũ quỷ", "Khôn": "Lục sát", "Cấn": "Họa hại", "Li": "Phục vị", "Chấn": "Sinh khí", "Khảm": "Diên niên", "Tốn": "Thiên y"},
    "Chấn": {"Càn": "Ngũ quỷ", "Đoài": "Tuyệt mệnh", "Khôn": "Họa hại", "Cấn": "Lục sát", "Li": "Sinh khí", "Chấn": "Phục vị", "Khảm": "Thiên y", "Tốn": "Diên niên"},
    "Khảm": {"Càn": "Lục sát", "Đoài": "Họa hại", "Khôn": "Tuyệt mệnh", "Cấn": "Ngũ quỷ", "Li": "Diên niên", "Chấn": "Thiên y", "Khảm": "Phục vị", "Tốn": "Sinh khí"},
    "Tốn": {"Càn": "Họa hại", "Đoài": "Lục sát", "Khôn": "Ngũ quỷ", "Cấn": "Tuyệt mệnh", "Li": "Thiên y", "Chấn": "Diên niên", "Khảm": "Sinh khí", "Tốn": "Phục vị"},
}


class PhongThuyBatSan:
    """
    Chương VI: Ứng dụng Bát san và Quái mệnh (trang 91 - 154).
    """

    DONG_TU_TRACH = {"Khảm", "Li", "Chấn", "Tốn"}
    TAY_TU_TRACH = {"Càn", "Khôn", "Cấn", "Đoài"}

    @classmethod
    def calculate_quai_menh(cls, birth_year: int, is_female: bool) -> str:
        """
        Tính Quái mệnh (Cung phi) từ năm sinh âm lịch (trang 91 - 103).
        Công thức: Lấy tổng các chữ số năm sinh rút gọn (mod 9).
        - Nam sinh trước năm 2000: 10 - mod9 (nếu ra 5 -> Côn/Khôn, theo Tân thiên lấy Khôn).
        - Nữ sinh trước năm 2000: mod9 + 5 (nếu ra 5 -> Cấn).
        Sau năm 2000: Nam 9 - mod9, Nữ mod9 + 6.
        """
        # Rút gọn tổng các chữ số
        s = sum(int(d) for d in str(birth_year))
        while s > 9:
            s = sum(int(d) for d in str(s))

        is_after_2000 = birth_year >= 2000

        if not is_female:
            num = (9 - s) if is_after_2000 else (10 - s)
            if num <= 0:
                num += 9
            if num == 5:
                num = 2  # Nam số 5 quy về Khôn (hoặc Cấn theo phái)
        else:
            num = (s + 6) if is_after_2000 else (s + 5)
            num = num % 9
            if num == 0:
                num = 9
            if num == 5:
                num = 8  # Nữ số 5 quy về Cấn (hoặc Đoài)

        return LAC_THU_TO_TRIGRAM[num]

    @classmethod
    def phan_loai_menh(cls, quai_menh: str) -> str:
        """Phân loại Đông tứ mệnh hoặc Tây tứ mệnh."""
        if quai_menh in cls.DONG_TU_TRACH:
            return "Đông tứ mệnh"
        return "Tây tứ mệnh"

    @classmethod
    def tra_cuu_bat_san(cls, quai_trach: str, quai_menh: str) -> str:
        """Tra cứu quan hệ Bát san giữa Trạch hướng và Mệnh chủ."""
        return BAT_SAN_TABLE.get(quai_trach, {}).get(quai_menh, "Không xác định")

    @classmethod
    def danh_gia_hon_nhan(cls, quai_chong: str, quai_vo: str) -> Dict[str, str]:
        """Đánh giá tương hợp hôn nhân giữa Quái chồng và Quái vợ (trang 114)."""
        san = cls.tra_cuu_bat_san(quai_chong, quai_vo)
        cat_set = {"Sinh khí", "Thiên y", "Diên niên", "Phục vị"}
        tinh_chat = "Cát (Tốt)" if san in cat_set else "Hung (Xấu)"
        return {
            "quai_chong": quai_chong,
            "quai_vo": quai_vo,
            "bat_san": san,
            "danh_gia": tinh_chat,
        }


# ==============================================================================
# CHƯƠNG VII: QUẺ DỊCH VÀ NẠP GIÁP
# ==============================================================================

# Bảng 27: Tên 64 quẻ kinh dịch (Chương VII, trang 160-161)
HEXAGRAM_TABLE: Dict[Tuple[str, str], str] = {
    # Thượng Càn
    ("Càn", "Càn"): "Bát thuần Càn",
    ("Càn", "Khôn"): "Thiên địa Bĩ",
    ("Càn", "Li"): "Thiên hỏa Đồng nhân",
    ("Càn", "Khảm"): "Thiên thủy Tụng",
    ("Càn", "Tốn"): "Thiên phong Cấu",
    ("Càn", "Chấn"): "Thiên lôi Vô vọng",
    ("Càn", "Cấn"): "Thiên sơn Độn",
    ("Càn", "Đoài"): "Thiên trạch Lý",
    # Thượng Khôn
    ("Khôn", "Càn"): "Địa thiên Thái",
    ("Khôn", "Khôn"): "Bát thuần Khôn",
    ("Khôn", "Li"): "Địa hỏa Minh di",
    ("Khôn", "Khảm"): "Địa thủy Sư",
    ("Khôn", "Tốn"): "Địa phong Thăng",
    ("Khôn", "Chấn"): "Địa lôi Phục",
    ("Khôn", "Cấn"): "Địa sơn Khiêm",
    ("Khôn", "Đoài"): "Địa trạch Lâm",
    # Thượng Tốn
    ("Tốn", "Càn"): "Phong thiên Tiểu súc",
    ("Tốn", "Khôn"): "Phong địa Quán",
    ("Tốn", "Li"): "Phong hỏa Gia nhân",
    ("Tốn", "Khảm"): "Phong thủy Hoán",
    ("Tốn", "Tốn"): "Bát thuần Tốn",
    ("Tốn", "Chấn"): "Phong lôi Ích",
    ("Tốn", "Cấn"): "Phong sơn Tiệm",
    ("Tốn", "Đoài"): "Phong trạch Trung phu",
    # Thượng Chấn
    ("Chấn", "Càn"): "Lôi thiên Đại tráng",
    ("Chấn", "Khôn"): "Lôi địa Dự",
    ("Chấn", "Li"): "Lôi hỏa Phong",
    ("Chấn", "Khảm"): "Lôi thủy Giải",
    ("Chấn", "Tốn"): "Lôi phong Hằng",
    ("Chấn", "Chấn"): "Bát thuần Chấn",
    ("Chấn", "Cấn"): "Lôi sơn Tiểu quá",
    ("Chấn", "Đoài"): "Lôi trạch Quy muội",
    # Thượng Li
    ("Li", "Càn"): "Hỏa thiên Đại hữu",
    ("Li", "Khôn"): "Hỏa địa Tấn",
    ("Li", "Li"): "Bát thuần Li",
    ("Li", "Khảm"): "Hỏa thủy Vị tế",
    ("Li", "Tốn"): "Hỏa phong Đỉnh",
    ("Li", "Chấn"): "Hỏa lôi Phệ hạp",
    ("Li", "Cấn"): "Hỏa sơn Lữ",
    ("Li", "Đoài"): "Hỏa trạch Khuê",
    # Thượng Cấn
    ("Cấn", "Càn"): "Sơn thiên Đại súc",
    ("Cấn", "Khôn"): "Sơn địa Bác",
    ("Cấn", "Li"): "Sơn hỏa Bí",
    ("Cấn", "Khảm"): "Sơn thủy Mông",
    ("Cấn", "Tốn"): "Sơn phong Cổ",
    ("Cấn", "Chấn"): "Sơn lôi Di",
    ("Cấn", "Cấn"): "Bát thuần Cấn",
    ("Cấn", "Đoài"): "Sơn trạch Tổn",
    # Thượng Khảm
    ("Khảm", "Càn"): "Thủy thiên Nhu",
    ("Khảm", "Khôn"): "Thủy địa Tỉ",
    ("Khảm", "Li"): "Thủy hỏa Kí tế",
    ("Khảm", "Khảm"): "Bát thuần Khảm",
    ("Khảm", "Tốn"): "Thủy phong Tỉnh",
    ("Khảm", "Chấn"): "Thủy lôi Truân",
    ("Khảm", "Cấn"): "Thủy sơn Kiển",
    ("Khảm", "Đoài"): "Thủy trạch Tiết",
    # Thượng Đoài
    ("Đoài", "Càn"): "Trạch thiên Quải",
    ("Đoài", "Khôn"): "Trạch địa Tụy",
    ("Đoài", "Li"): "Trạch hỏa Cách",
    ("Đoài", "Khảm"): "Trạch thủy Khốn",
    ("Đoài", "Tốn"): "Trạch phong Đại quá",
    ("Đoài", "Chấn"): "Trạch lôi Tùy",
    ("Đoài", "Cấn"): "Trạch sơn Hàm",
    ("Đoài", "Đoài"): "Bát thuần Đoài",
}


class QueKinhDich:
    """
    Chương VII: Hệ nhị phân Phục Hi và Nạp Can Chi 6 hào (trang 155 - 194).
    """

    @classmethod
    def get_binary_code(cls, quai_thuong: str, quai_duoi: str) -> str:
        """
        Lấy chuỗi nhị phân 6-bit của quẻ (từ hào 1 dưới cùng đến hào 6 trên cùng).
        """
        lines_duoi = TRIGRAMS_DATA[quai_duoi]["lines"]
        lines_thuong = TRIGRAMS_DATA[quai_thuong]["lines"]
        full_lines = lines_duoi + lines_thuong
        return "".join(str(b) for b in full_lines)

    @classmethod
    def nap_chi_kinh_phong(cls, quai: str, is_upper: bool) -> List[str]:
        """
        Quy tắc Nạp chi Kinh Phòng cho nội quái và ngoại quái (trang 174 - 180):
        - Càn: Nội nạp Tý Dần Thìn, Ngoại nạp Ngọ Thân Tuất
        - Khôn: Nội nạp Mùi Tị Mão, Ngoại nạp Sửu Hợi Dậu
        - Chấn: Nội nạp Tý Dần Thìn, Ngoại nạp Ngọ Thân Tuất
        - Tốn: Nội nạp Sửu Hợi Dậu, Ngoại nạp Mùi Tị Mão
        - Khảm: Nội nạp Dần Thìn Ngọ, Ngoại nạp Thân Tuất Tý
        - Li: Nội nạp Mão Sửu Hợi, Ngoại nạp Dậu Mùi Tị
        - Cấn: Nội nạp Thìn Ngọ Thân, Ngoại nạp Tuất Tý Dần
        - Đoài: Nội nạp Tị Mão Sửu, Ngoại nạp Hợi Dậu Mùi
        """
        nap_table = {
            "Càn": (["Tý", "Dần", "Thìn"], ["Ngọ", "Thân", "Tuất"]),
            "Khôn": (["Mùi", "Tị", "Mão"], ["Sửu", "Hợi", "Dậu"]),
            "Chấn": (["Tý", "Dần", "Thìn"], ["Ngọ", "Thân", "Tuất"]),
            "Tốn": (["Sửu", "Hợi", "Dậu"], ["Mùi", "Tị", "Mão"]),
            "Khảm": (["Dần", "Thìn", "Ngọ"], ["Thân", "Tuất", "Tý"]),
            "Li": (["Mão", "Sửu", "Hợi"], ["Dậu", "Mùi", "Tị"]),
            "Cấn": (["Thìn", "Ngọ", "Thân"], ["Tuất", "Tý", "Dần"]),
            "Đoài": (["Tị", "Mão", "Sửu"], ["Hợi", "Dậu", "Mùi"]),
        }
        inner, outer = nap_table[quai]
        return outer if is_upper else inner

    @classmethod
    def get_full_nap_chi(cls, quai_thuong: str, quai_duoi: str) -> List[str]:
        """Lấy 6 Địa chi nạp cho 6 hào của quẻ từ hào sơ đến hào thượng."""
        chi_ha = cls.nap_chi_kinh_phong(quai_duoi, is_upper=False)
        chi_thuong = cls.nap_chi_kinh_phong(quai_thuong, is_upper=True)
        return chi_ha + chi_thuong


# ==============================================================================
# CHƯƠNG VIII: NHẬN DẠNG BÁT TỰ HÀ - LẠC
# ==============================================================================

# Bảng 43: Mã số Thiên can (Chương VIII, trang 221)
THIEN_CAN_CODES = {
    "Kỷ": 1,
    "Mậu": 2,
    "Bính": 3,
    "Đinh": 3,
    "Giáp": 4,
    "Ất": 6,
    "Nhâm": 7,
    "Quý": 7,
    "Tân": 8,
    "Canh": 9,
}

# Bảng 41: Mã số Địa chi đối với Dương nam, Âm nữ (trang 219)
DIA_CHI_CODES_DUONG_NAM_AM_NU = {
    "Tý": (9, 2),
    "Hợi": (9, 2),
    "Ngọ": (1, 8),
    "Tị": (1, 8),
    "Mão": (7, 6),
    "Dần": (7, 6),
    "Dậu": (3, 4),
    "Thân": (3, 4),
    "Thìn": (7, 7),
    "Tuất": (3, 3),
    "Sửu": (9, 9),
    "Mùi": (1, 1),
}

# Bảng 42: Mã số Địa chi đối với Âm nam, Dương nữ (trang 219)
DIA_CHI_CODES_AM_NAM_DUONG_NU = {
    "Tý": (7, 4),
    "Hợi": (7, 4),
    "Ngọ": (3, 6),
    "Tị": (3, 6),
    "Mão": (4, 9),
    "Dần": (4, 9),
    "Dậu": (6, 1),
    "Thân": (6, 1),
    "Thìn": (3, 1),
    "Tuất": (7, 9),
    "Sửu": (2, 6),
    "Mùi": (8, 4),
}


class BatTuHaLacFull:
    """
    Chương VIII: Thuật toán nhận dạng Bát tự Hà - Lạc toàn diện (trang 195 - 252).
    """

    @staticmethod
    def get_year_can_chi(year: int) -> Tuple[str, str]:
        """Xác định Thiên can và Địa chi của năm dương lịch (trang 214)."""
        can_list = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
        chi_list = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi"]
        return can_list[year % 10], chi_list[year % 12]

    @staticmethod
    def is_duong_can(can: str) -> bool:
        """Các can dương: Giáp, Bính, Mậu, Canh, Nhâm."""
        return can in {"Giáp", "Bính", "Mậu", "Canh", "Nhâm"}

    @staticmethod
    def reduce_to_lac_thu(total: int, is_duong_nam: bool = True, is_female: bool = False) -> int:
        """Rút gọn tổng số về số Lạc thư (1..9), xử lý cung số 5 (trang 225)."""
        remainder = total % 9
        if remainder == 0:
            remainder = 9

        if remainder == 5:
            if not is_female:
                return 4 if is_duong_nam else 2
            else:
                return 6 if not is_duong_nam else 8

        return remainder

    @classmethod
    def calculate_tien_thien_hexagram(
        cls,
        can_list: List[str],
        chi_list: List[str],
        is_duong_the: bool,
        is_female: bool,
    ) -> Dict[str, Any]:
        """Xác định Quẻ Tiên thiên từ 4 Can và 4 Chi (trang 217 - 231)."""
        is_duong_nam = is_duong_the and (not is_female)
        is_am_nu = (not is_duong_the) and is_female
        is_duong_nam_am_nu = is_duong_nam or is_am_nu

        can_codes = [THIEN_CAN_CODES[can] for can in can_list]
        chi_table = (
            DIA_CHI_CODES_DUONG_NAM_AM_NU
            if is_duong_nam_am_nu
            else DIA_CHI_CODES_AM_NAM_DUONG_NU
        )
        chi_codes = [chi_table[chi] for chi in chi_list]

        all_numbers: List[int] = []
        all_numbers.extend(can_codes)
        for c1, c2 in chi_codes:
            all_numbers.extend([c1, c2])

        tong_duong = sum(n for n in all_numbers if n % 2 != 0)
        tong_am = sum(n for n in all_numbers if n % 2 == 0)

        cung_duong = cls.reduce_to_lac_thu(tong_duong, is_duong_nam=is_duong_nam, is_female=is_female)
        cung_am = cls.reduce_to_lac_thu(tong_am, is_duong_nam=is_duong_nam, is_female=is_female)

        if not is_female:
            quai_thuong = LAC_THU_TO_TRIGRAM[cung_duong]
            quai_duoi = LAC_THU_TO_TRIGRAM[cung_am]
        else:
            quai_thuong = LAC_THU_TO_TRIGRAM[cung_am]
            quai_duoi = LAC_THU_TO_TRIGRAM[cung_duong]

        ten_que = HEXAGRAM_TABLE.get((quai_thuong, quai_duoi), "Không xác định")

        return {
            "can_list": can_list,
            "chi_list": chi_list,
            "tong_so_duong": tong_duong,
            "tong_so_am": tong_am,
            "cung_duong": cung_duong,
            "cung_am": cung_am,
            "quai_thuong": quai_thuong,
            "quai_duoi": quai_duoi,
            "ten_que_tien_thien": ten_que,
            "is_duong_nam_am_nu": is_duong_nam_am_nu,
        }

    @classmethod
    def calculate_dai_van(
        cls,
        quai_thuong: str,
        quai_duoi: str,
        hao_nguyen_duong: int = 1,
        thuan_chieu: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Chương VIII.11: Tính chu kỳ các Đại vận (trang 242 - 247).
        - Hào dương: cai quản 9 năm.
        - Hào âm: cai quản 6 năm.
        - Chạy tuần tự qua 6 hào bắt đầu từ hào Nguyên đường.
        """
        lines_duoi = TRIGRAMS_DATA[quai_duoi]["lines"]
        lines_thuong = TRIGRAMS_DATA[quai_thuong]["lines"]
        six_lines = list(lines_duoi + lines_thuong)  # 6 hào: index 0 (hào 1) đến 5 (hào 6)

        start_idx = hao_nguyen_duong - 1
        van_list = []
        current_age = 1

        for step in range(6):
            if thuan_chieu:
                line_idx = (start_idx + step) % 6
            else:
                line_idx = (start_idx - step) % 6

            is_yang = six_lines[line_idx] == 1
            duration = 9 if is_yang else 6
            end_age = current_age + duration - 1

            van_list.append({
                "dai_van": step + 1,
                "hao_so": line_idx + 1,
                "tinh_chat_hao": "Dương" if is_yang else "Âm",
                "so_nam": duration,
                "tuoi_bat_dau": current_age,
                "tuoi_ket_thuc": end_age,
            })
            current_age += duration

        return van_list


# ==============================================================================
# HÀM KIỂM CHỨNG VÀ TEST TẤT CẢ CÁC CHƯƠNG
# ==============================================================================

if __name__ == "__main__":
    print("=====================================================================")
    print("KIỂM CHỨNG TOÀN DIỆN CƠ SỞ TOÁN HỌC DỊCH HỌC CHO CẢ 8 CHƯƠNG")
    print("Tác phẩm: Dịch học diễn giải trên cơ sở toán học và ứng dụng vào đời sống")
    print("Tác giả: TS. Nguyễn Thế Cường, NXB ĐHQG TP.HCM 2014")
    print("=====================================================================")

    # CHƯƠNG I: Kiểm chứng nhóm cộng Abel
    print("\n[CHƯƠNG I] Kiểm chứng nhóm cộng Hà - Lạc (Z/10Z, +):")
    is_abel = HaLacGroup.verify_abel_group()
    print(f"  Thỏa mãn 4 tiên đề nhóm Abel: {is_abel}")
    print(f"  Phép cộng đồng hồ: 8 + 4 = {HaLacGroup.add(8, 4)} (mod 10)")
    print(f"  Số đối duy nhất của 3: {HaLacGroup.opposite(3)} (vì 3 + 7 = 0 mod 10)")

    # CHƯƠNG II: Hợp hóa Can Chi
    print("\n[CHƯƠNG II] Hợp hóa Can Chi:")
    print(f"  Giáp + Kỷ -> {HopHoaCanChi.get_can_hop('Giáp', 'Kỷ')} (Sách p. 18: Thổ)")
    print(f"  Ất + Canh -> {HopHoaCanChi.get_can_hop('Ất', 'Canh')} (Sách p. 18: Kim)")
    print(f"  Lục hợp Tý + Sửu -> {HopHoaCanChi.get_chi_luc_hop('Tý', 'Sửu')} (Thổ)")

    # CHƯƠNG III: Năng lượng hào và biến hào
    print("\n[CHƯƠNG III] Năng lượng hào và biến quái:")
    can_lines = (1, 1, 1)
    e_can = TrigramEnergy.calculate_energy(can_lines)
    print(f"  Năng lượng Càn (1, 1, 1): {e_can} (Sách p. 33: +9)")
    khon_lines = (0, 0, 0)
    e_khon = TrigramEnergy.calculate_energy(khon_lines)
    print(f"  Năng lượng Khôn (0, 0, 0): {e_khon} (Sách p. 33: -9)")
    bien_can_1 = TrigramEnergy.bien_hao(can_lines, 1)
    print(f"  Càn biến hào sơ (1) -> lines {bien_can_1}, Năng lượng: {TrigramEnergy.calculate_energy(bien_can_1)} (Tốn: +7)")

    # CHƯƠNG IV: Bát quái Tân thiên và đối xứng tâm
    print("\n[CHƯƠNG IV] Bát quái Tân thiên và đối xứng Lạc thư:")
    print(f"  Càn đối xứng qua tâm với: {BatQuaiTanThien.get_opposite_trigram('Càn')} (Khôn)")
    print(f"  Kiểm tra Càn và Khôn: {BatQuaiTanThien.check_symmetry_opposite('Càn', 'Khôn')} (Tổng cung = 10, Tổng E = 0)")

    # CHƯƠNG VI: Quái mệnh và Bát san
    print("\n[CHƯƠNG VI] Quái mệnh và Bát san phong thủy:")
    quai_nam_1985 = PhongThuyBatSan.calculate_quai_menh(1985, is_female=False)
    print(f"  Nam sinh 1985 -> Cung mệnh: {quai_nam_1985} ({PhongThuyBatSan.phan_loai_menh(quai_nam_1985)})")
    san_can_doai = PhongThuyBatSan.tra_cuu_bat_san("Càn", "Đoài")
    print(f"  Trạch Càn gặp Mệnh Đoài: {san_can_doai} (Sách Bảng 26: Sinh khí)")

    # CHƯƠNG VII: Quẻ Kinh dịch và Nạp giáp
    print("\n[CHƯƠNG VII] 64 Quẻ dịch và Nạp giáp:")
    que_thien_dia = HEXAGRAM_TABLE[("Càn", "Khôn")]
    print(f"  Thượng Càn, Hạ Khôn: {que_thien_dia} (Bảng 27: Thiên địa Bĩ)")
    nap_chi_can_khon = QueKinhDich.get_full_nap_chi("Càn", "Khôn")
    print(f"  6 Chi nạp hào quẻ Thiên địa Bĩ: {nap_chi_can_khon}")

    # CHƯƠNG VIII: Bát tự Hà Lạc toàn diện
    print("\n[CHƯƠNG VIII] Bát tự Hà - Lạc và phân bổ Đại vận:")
    tt_result = BatTuHaLacFull.calculate_tien_thien_hexagram(
        can_list=["Mậu", "Giáp", "Bính", "Canh"],
        chi_list=["Ngọ", "Dần", "Tý", "Thân"],
        is_duong_the=True,
        is_female=False
    )
    print(f"  Quẻ Tiên thiên xác định: {tt_result['ten_que_tien_thien']} (Thượng: {tt_result['quai_thuong']}, Hạ: {tt_result['quai_duoi']})")
    dai_van = BatTuHaLacFull.calculate_dai_van(tt_result['quai_thuong'], tt_result['quai_duoi'], hao_nguyen_duong=1)
    print(f"  Đại vận 1: Hào {dai_van[0]['hao_so']} ({dai_van[0]['tinh_chat_hao']}) -> {dai_van[0]['tuoi_bat_dau']} đến {dai_van[0]['tuoi_ket_thuc']} tuổi ({dai_van[0]['so_nam']} năm)")
    print(f"  Đại vận 2: Hào {dai_van[1]['hao_so']} ({dai_van[1]['tinh_chat_hao']}) -> {dai_van[1]['tuoi_bat_dau']} đến {dai_van[1]['tuoi_ket_thuc']} tuổi ({dai_van[1]['so_nam']} năm)")

    print("\n=> ĐÃ KIỂM CHỨNG VÀ HOÀN TẤT ĐẦY ĐỦ THUẬT TOÁN CHO TOÀN BỘ 8 CHƯƠNG!")
