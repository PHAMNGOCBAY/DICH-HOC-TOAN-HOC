import json
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from dich_hoc_core import (
    TRIGRAMS_DATA,
    LAC_THU_TO_TRIGRAM,
    BAT_SAN_TABLE,
    HEXAGRAM_TABLE,
    THIEN_CAN_CODES,
    DIA_CHI_CODES_DUONG_NAM_AM_NU,
    DIA_CHI_CODES_AM_NAM_DUONG_NU,
    HopHoaCanChi,
    QueKinhDich
)

JSON_PATH = r"C:\DICH HOC\dich_hoc_data.json"
SQL_PATH = r"C:\DICH HOC\dich_hoc_schema.sql"

# 1. TỔNG HỢP DỮ LIỆU JSON ĐẦY ĐỦ CHO CẢ 8 CHƯƠNG
data = {
    "metadata": {
        "tac_pham": "Dịch học diễn giải trên cơ sở toán học và ứng dụng vào đời sống",
        "tac_gia": "TS. Nguyễn Thế Cường (Nguyễn Quý Thế Cường)",
        "sinh_nam": 1942,
        "hoc_vi": "Tiến sĩ Toán - Lý ĐH Tổng hợp Leningrad (1973)",
        "nha_xuat_ban": "Đại học Quốc gia Thành phố Hồ Chí Minh",
        "nam_xuat_ban": 2014,
        "isbn": "978-604-73-2149-0",
        "tong_so_trang_pdf": 278,
        "so_trang_sach_in": 261,
        "nguyen_tac_bien_soan": "Không bịa đặt, không suy diễn, đối chiếu trực tiếp từ nguyên bản của tác giả"
    },
    "chuong_I_co_so_toan_hoc": {
        "ten_chuong": "Cơ sở toán học của Bát quái",
        "tap_hop_so": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "quan_he_modulo": "10 ≡ 0 (Đồng hồ 10 vạch chia)",
        "phan_tu_trung_hoa": 0,
        "cau_truc_dai_so": "Nhóm giao hoán Abel (Z/10Z, +)",
        "cac_cap_so_doi": [
            {"a": 1, "doi": 9},
            {"a": 2, "doi": 8},
            {"a": 3, "doi": 7},
            {"a": 4, "doi": 6},
            {"a": 5, "doi": 5},
            {"a": 0, "doi": 0}
        ]
    },
    "chuong_II_am_duong_hop_hoa": {
        "ten_chuong": "Âm, dương và Thái cực",
        "phan_loai_so": {
            "duong": [1, 3, 7, 9],
            "am": [2, 4, 6, 8],
            "trung_hoa_thai_cuc": 0,
            "so_dac_biet_5": "Chính giữa (Trung cung Lạc thư)"
        },
        "thien_can_ngu_hop": [
            {"can1": "Giáp", "can2": "Kỷ", "hoa_hanh": "Thổ"},
            {"can1": "Ất", "can2": "Canh", "hoa_hanh": "Kim"},
            {"can1": "Bính", "can2": "Tân", "hoa_hanh": "Thủy"},
            {"can1": "Đinh", "can2": "Nhâm", "hoa_hanh": "Mộc"},
            {"can1": "Mậu", "can2": "Quý", "hoa_hanh": "Hỏa"}
        ],
        "dia_chi_luc_hop": [
            {"chi1": "Tý", "chi2": "Sửu", "hoa_hanh": "Thổ"},
            {"chi1": "Dần", "chi2": "Hợi", "hoa_hanh": "Mộc"},
            {"chi1": "Mão", "chi2": "Tuất", "hoa_hanh": "Hỏa"},
            {"chi1": "Thìn", "chi2": "Dậu", "hoa_hanh": "Kim"},
            {"chi1": "Tị", "chi2": "Thân", "hoa_hanh": "Thủy"},
            {"chi1": "Ngọ", "chi2": "Mùi", "hoa_hanh": "Thái Dương / Thái Âm"}
        ],
        "dia_chi_tam_hop": [
            {"tam_hop": ["Thân", "Tý", "Thìn"], "cuc": "Thủy cục"},
            {"tam_hop": ["Hợi", "Mão", "Mùi"], "cuc": "Mộc cục"},
            {"tam_hop": ["Dần", "Ngọ", "Tuất"], "cuc": "Hỏa cục"},
            {"tam_hop": ["Tị", "Dậu", "Sửu"], "cuc": "Kim cục"}
        ]
    },
    "chuong_III_nang_luong_quai": {
        "ten_chuong": "Tạo quái từ lưỡng nghi âm, dương",
        "cong_thuc_nang_luong": "E = h1*(±1) + h2*(±3) + h3*(±5)",
        "trong_so_hao": {
            "hao_1_so": 1,
            "hao_2_trung": 3,
            "hao_3_thuong": 5
        },
        "tu_tuong": {
            "Thai_Duong": {"lines": [1, 1], "tri_so": 4},
            "Thieu_Am": {"lines": [1, 0], "tri_so": -2},
            "Thieu_Duong": {"lines": [0, 1], "tri_so": 2},
            "Thai_Am": {"lines": [0, 0], "tri_so": -4}
        }
    },
    "chuong_IV_bat_quai_tan_thien": {
        "ten_chuong": "Bát quái Tân thiên",
        "danh_sach_quai": TRIGRAMS_DATA,
        "lac_thu_to_trigram": LAC_THU_TO_TRIGRAM
    },
    "chuong_VI_ung_dung_bat_san": {
        "ten_chuong": "Ứng dụng đồ tổng hợp QCC vào đời sống cá nhân và gia đình",
        "dong_tu_trach": ["Khảm", "Li", "Chấn", "Tốn"],
        "tay_tu_trach": ["Càn", "Khôn", "Cấn", "Đoài"],
        "phan_loai_san": {
            "cat": ["Sinh khí", "Thiên y", "Diên niên", "Phục vị"],
            "hung": ["Tuyệt mệnh", "Ngũ quỷ", "Lục sát", "Họa hại"]
        },
        "ma_tran_bat_san": BAT_SAN_TABLE
    },
    "chuong_VII_que_dich_64": {
        "ten_chuong": "Quẻ dịch và Nạp giáp",
        "danh_sach_64_que": []
    },
    "chuong_VIII_bat_tu_ha_lac": {
        "ten_chuong": "Nhận dạng theo phương pháp Bát tự Hà – Lạc",
        "ma_so_thien_can": THIEN_CAN_CODES,
        "ma_so_dia_chi_duong_nam_am_nu": {k: list(v) for k, v in DIA_CHI_CODES_DUONG_NAM_AM_NU.items()},
        "ma_so_dia_chi_am_nam_duong_nu": {k: list(v) for k, v in DIA_CHI_CODES_AM_NAM_DUONG_NU.items()},
        "quy_tac_chia_dai_van": {
            "hao_duong": 9,
            "hao_am": 6,
            "tong_so_dai_van": 6
        }
    }
}

# Sinh chi tiết 64 quẻ
idx = 1
for (q_thuong, q_duoi), ten in HEXAGRAM_TABLE.items():
    binary_str = QueKinhDich.get_binary_code(q_thuong, q_duoi)
    nap_chi = QueKinhDich.get_full_nap_chi(q_thuong, q_duoi)
    data["chuong_VII_que_dich_64"]["danh_sach_64_que"].append({
        "stt": idx,
        "ten_que": ten,
        "quai_thuong": q_thuong,
        "quai_duoi": q_duoi,
        "ma_nhi_phan": binary_str,
        "nap_chi_6_hao": nap_chi
    })
    idx += 1

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"Đã cập nhật thành công: {JSON_PATH} ({os.path.getsize(JSON_PATH):,} bytes)")


# 2. XÂY DỰNG FILE SCHEMA VÀ SEED DATA SQL ĐẦY ĐỦ
sql_lines = []
sql_lines.append("-- =============================================================================")
sql_lines.append("-- HỆ CƠ SỞ DỮ LIỆU QUAN HỆ TOÀN DIỆN CHO CẢ 8 CHƯƠNG")
sql_lines.append("-- TÁC PHẨM: DỊCH HỌC DIỄN GIẢI TRÊN CƠ SỞ TOÁN HỌC VÀ ỨNG DỤNG VÀO ĐỜI SỐNG")
sql_lines.append("-- TÁC GIẢ: TS. NGUYỄN THẾ CƯỜNG (NXB ĐHQG TP.HCM 2014)")
sql_lines.append("-- =============================================================================\n")

sql_lines.append("""
DROP TABLE IF EXISTS que_kinh_dich;
DROP TABLE IF EXISTS bat_san;
DROP TABLE IF EXISTS dia_chi_ma_so;
DROP TABLE IF EXISTS thien_can_ma_so;
DROP TABLE IF EXISTS thien_can_hop;
DROP TABLE IF EXISTS dia_chi_luc_hop;
DROP TABLE IF EXISTS bat_quai;
DROP TABLE IF EXISTS so_ha_lac;
DROP TABLE IF EXISTS sach_metadata;

-- 1. BẢNG SIÊU DỮ LIỆU
CREATE TABLE sach_metadata (
    id INTEGER PRIMARY KEY,
    ten_sach TEXT NOT NULL,
    tac_gia TEXT NOT NULL,
    nam_xuat_ban INTEGER NOT NULL,
    nha_xuat_ban TEXT NOT NULL,
    isbn TEXT NOT NULL,
    so_trang INTEGER NOT NULL
);

INSERT INTO sach_metadata VALUES (
    1,
    'Dịch học diễn giải trên cơ sở toán học và ứng dụng vào đời sống',
    'TS. Nguyễn Thế Cường',
    2014,
    'Nhà xuất bản Đại học Quốc gia Thành phố Hồ Chí Minh',
    '978-604-73-2149-0',
    278
);

-- 2. BẢNG NHÓM CỘNG HÀ - LẠC (CHƯƠNG I)
CREATE TABLE so_ha_lac (
    so INTEGER PRIMARY KEY,
    tinh_chat TEXT NOT NULL,
    so_doi INTEGER NOT NULL,
    FOREIGN KEY (so_doi) REFERENCES so_ha_lac(so)
);

INSERT INTO so_ha_lac VALUES (0, 'Thái cực / Trung hòa', 0);
INSERT INTO so_ha_lac VALUES (1, 'Dương (Lạc thư)', 9);
INSERT INTO so_ha_lac VALUES (2, 'Âm (Lạc thư)', 8);
INSERT INTO so_ha_lac VALUES (3, 'Dương (Lạc thư)', 7);
INSERT INTO so_ha_lac VALUES (4, 'Âm (Lạc thư)', 6);
INSERT INTO so_ha_lac VALUES (5, 'Thái cực (Trung cung)', 5);
INSERT INTO so_ha_lac VALUES (6, 'Âm (Lạc thư)', 4);
INSERT INTO so_ha_lac VALUES (7, 'Dương (Lạc thư)', 3);
INSERT INTO so_ha_lac VALUES (8, 'Âm (Lạc thư)', 2);
INSERT INTO so_ha_lac VALUES (9, 'Dương (Lạc thư)', 1);

-- 3. BẢNG HỢP HÓA THIÊN CAN & ĐỊA CHI (CHƯƠNG II)
CREATE TABLE thien_can_hop (
    can_1 TEXT NOT NULL,
    can_2 TEXT NOT NULL,
    hoa_hanh TEXT NOT NULL,
    PRIMARY KEY (can_1, can_2)
);

INSERT INTO thien_can_hop VALUES ('Giáp', 'Kỷ', 'Thổ');
INSERT INTO thien_can_hop VALUES ('Ất', 'Canh', 'Kim');
INSERT INTO thien_can_hop VALUES ('Bính', 'Tân', 'Thủy');
INSERT INTO thien_can_hop VALUES ('Đinh', 'Nhâm', 'Mộc');
INSERT INTO thien_can_hop VALUES ('Mậu', 'Quý', 'Hỏa');

CREATE TABLE dia_chi_luc_hop (
    chi_1 TEXT NOT NULL,
    chi_2 TEXT NOT NULL,
    hoa_hanh TEXT NOT NULL,
    PRIMARY KEY (chi_1, chi_2)
);

INSERT INTO dia_chi_luc_hop VALUES ('Tý', 'Sửu', 'Thổ');
INSERT INTO dia_chi_luc_hop VALUES ('Dần', 'Hợi', 'Mộc');
INSERT INTO dia_chi_luc_hop VALUES ('Mão', 'Tuất', 'Hỏa');
INSERT INTO dia_chi_luc_hop VALUES ('Thìn', 'Dậu', 'Kim');
INSERT INTO dia_chi_luc_hop VALUES ('Tị', 'Thân', 'Thủy');
INSERT INTO dia_chi_luc_hop VALUES ('Ngọ', 'Mùi', 'Thái Dương / Thái Âm');

-- 4. BẢNG BÁT QUÁI TÂN THIÊN (CHƯƠNG IV)
CREATE TABLE bat_quai (
    ten_quai TEXT PRIMARY KEY,
    hao_1 INTEGER NOT NULL,
    hao_2 INTEGER NOT NULL,
    hao_3 INTEGER NOT NULL,
    tri_so_nang_luong INTEGER NOT NULL,
    cung_lac_thu INTEGER NOT NULL,
    so_gan INTEGER NOT NULL,
    phuong_vi TEXT NOT NULL,
    tinh_chat TEXT NOT NULL,
    ngu_hanh TEXT NOT NULL,
    cap_phu_the TEXT NOT NULL
);
""")

for name, d in TRIGRAMS_DATA.items():
    h1, h2, h3 = d["lines"]
    sql_lines.append(f"INSERT INTO bat_quai VALUES ('{name}', {h1}, {h2}, {h3}, {d['tri_so']}, {d['cung_lac_thu']}, {d['so_gan']}, '{d['phuong_vi']}', '{d['tinh_chat']}', '{d['ngu_hanh']}', '{d['cap_phu_the']}');")

sql_lines.append("""
-- 5. BẢNG MA TRẬN 8x8 BÁT SAN (CHƯƠNG VI)
CREATE TABLE bat_san (
    quai_trach TEXT NOT NULL,
    quai_menh TEXT NOT NULL,
    ten_san TEXT NOT NULL,
    tinh_chat TEXT NOT NULL,
    PRIMARY KEY (quai_trach, quai_menh)
);
""")

cat_set = {"Sinh khí", "Thiên y", "Diên niên", "Phục vị"}
for q_trach, row in BAT_SAN_TABLE.items():
    for q_menh, san in row.items():
        tinh_chat = 'Cát' if san in cat_set else 'Hung'
        sql_lines.append(f"INSERT INTO bat_san VALUES ('{q_trach}', '{q_menh}', '{san}', '{tinh_chat}');")

sql_lines.append("""
-- 6. BẢNG 64 QUẺ KINH DỊCH & NẠP GIÁP (CHƯƠNG VII)
CREATE TABLE que_kinh_dich (
    stt INTEGER PRIMARY KEY,
    ten_que TEXT NOT NULL,
    quai_thuong TEXT NOT NULL,
    quai_duoi TEXT NOT NULL,
    ma_nhi_phan TEXT NOT NULL,
    nap_chi_6_hao TEXT NOT NULL,
    FOREIGN KEY (quai_thuong) REFERENCES bat_quai(ten_quai),
    FOREIGN KEY (quai_duoi) REFERENCES bat_quai(ten_quai)
);
""")

idx = 1
for (q_thuong, q_duoi), ten in HEXAGRAM_TABLE.items():
    b = QueKinhDich.get_binary_code(q_thuong, q_duoi)
    nc = ",".join(QueKinhDich.get_full_nap_chi(q_thuong, q_duoi))
    sql_lines.append(f"INSERT INTO que_kinh_dich VALUES ({idx}, '{ten}', '{q_thuong}', '{q_duoi}', '{b}', '{nc}');")
    idx += 1

sql_lines.append("""
-- 7. BẢNG MÃ SỐ BÁT TỰ HÀ - LẠC (CHƯƠNG VIII)
CREATE TABLE thien_can_ma_so (
    can TEXT PRIMARY KEY,
    ma_so INTEGER NOT NULL
);
""")
for c, code in THIEN_CAN_CODES.items():
    sql_lines.append(f"INSERT INTO thien_can_ma_so VALUES ('{c}', {code});")

sql_lines.append("""
CREATE TABLE dia_chi_ma_so (
    chi TEXT NOT NULL,
    nhom_doi_tuong TEXT NOT NULL,
    ma_so_1 INTEGER NOT NULL,
    ma_so_2 INTEGER NOT NULL,
    PRIMARY KEY (chi, nhom_doi_tuong)
);
""")
for c, (m1, m2) in DIA_CHI_CODES_DUONG_NAM_AM_NU.items():
    sql_lines.append(f"INSERT INTO dia_chi_ma_so VALUES ('{c}', 'Dương nam, Âm nữ', {m1}, {m2});")
for c, (m1, m2) in DIA_CHI_CODES_AM_NAM_DUONG_NU.items():
    sql_lines.append(f"INSERT INTO dia_chi_ma_so VALUES ('{c}', 'Âm nam, Dương nữ', {m1}, {m2});")

with open(SQL_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(sql_lines))
print(f"Đã cập nhật thành công: {SQL_PATH} ({os.path.getsize(SQL_PATH):,} bytes)")
