-- =============================================================================
-- HỆ CƠ SỞ DỮ LIỆU QUAN HỆ TOÀN DIỆN CHO CẢ 8 CHƯƠNG
-- TÁC PHẨM: DỊCH HỌC DIỄN GIẢI TRÊN CƠ SỞ TOÁN HỌC VÀ ỨNG DỤNG VÀO ĐỜI SỐNG
-- TÁC GIẢ: TS. NGUYỄN THẾ CƯỜNG (NXB ĐHQG TP.HCM 2014)
-- =============================================================================


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

INSERT INTO bat_quai VALUES ('Càn', 1, 1, 1, 9, 9, 9, 'Chính Nam', 'Dương', 'Kim', 'Đoài');
INSERT INTO bat_quai VALUES ('Đoài', 1, 1, 0, -1, 8, 8, 'Đông Bắc', 'Âm', 'Kim', 'Càn');
INSERT INTO bat_quai VALUES ('Li', 1, 0, 1, 3, 3, 3, 'Chính Đông', 'Dương', 'Hỏa', 'Chấn');
INSERT INTO bat_quai VALUES ('Chấn', 1, 0, 0, -7, 6, 6, 'Tây Bắc', 'Âm', 'Mộc', 'Li');
INSERT INTO bat_quai VALUES ('Tốn', 0, 1, 1, 7, 4, 4, 'Đông Nam', 'Dương', 'Mộc', 'Khảm');
INSERT INTO bat_quai VALUES ('Khảm', 0, 1, 0, -3, 7, 7, 'Chính Tây', 'Âm', 'Thủy', 'Tốn');
INSERT INTO bat_quai VALUES ('Cấn', 0, 0, 1, 1, 2, 2, 'Tây Nam', 'Dương', 'Thổ', 'Khôn');
INSERT INTO bat_quai VALUES ('Khôn', 0, 0, 0, -9, 1, 1, 'Chính Bắc', 'Âm', 'Thổ', 'Cấn');

-- 5. BẢNG MA TRẬN 8x8 BÁT SAN (CHƯƠNG VI)
CREATE TABLE bat_san (
    quai_trach TEXT NOT NULL,
    quai_menh TEXT NOT NULL,
    ten_san TEXT NOT NULL,
    tinh_chat TEXT NOT NULL,
    PRIMARY KEY (quai_trach, quai_menh)
);

INSERT INTO bat_san VALUES ('Càn', 'Càn', 'Phục vị', 'Cát');
INSERT INTO bat_san VALUES ('Càn', 'Đoài', 'Sinh khí', 'Cát');
INSERT INTO bat_san VALUES ('Càn', 'Khôn', 'Diên niên', 'Cát');
INSERT INTO bat_san VALUES ('Càn', 'Cấn', 'Thiên y', 'Cát');
INSERT INTO bat_san VALUES ('Càn', 'Li', 'Tuyệt mệnh', 'Hung');
INSERT INTO bat_san VALUES ('Càn', 'Chấn', 'Ngũ quỷ', 'Hung');
INSERT INTO bat_san VALUES ('Càn', 'Khảm', 'Lục sát', 'Hung');
INSERT INTO bat_san VALUES ('Càn', 'Tốn', 'Họa hại', 'Hung');
INSERT INTO bat_san VALUES ('Đoài', 'Càn', 'Sinh khí', 'Cát');
INSERT INTO bat_san VALUES ('Đoài', 'Đoài', 'Phục vị', 'Cát');
INSERT INTO bat_san VALUES ('Đoài', 'Khôn', 'Thiên y', 'Cát');
INSERT INTO bat_san VALUES ('Đoài', 'Cấn', 'Diên niên', 'Cát');
INSERT INTO bat_san VALUES ('Đoài', 'Li', 'Ngũ quỷ', 'Hung');
INSERT INTO bat_san VALUES ('Đoài', 'Chấn', 'Tuyệt mệnh', 'Hung');
INSERT INTO bat_san VALUES ('Đoài', 'Khảm', 'Họa hại', 'Hung');
INSERT INTO bat_san VALUES ('Đoài', 'Tốn', 'Lục sát', 'Hung');
INSERT INTO bat_san VALUES ('Khôn', 'Càn', 'Diên niên', 'Cát');
INSERT INTO bat_san VALUES ('Khôn', 'Đoài', 'Thiên y', 'Cát');
INSERT INTO bat_san VALUES ('Khôn', 'Khôn', 'Phục vị', 'Cát');
INSERT INTO bat_san VALUES ('Khôn', 'Cấn', 'Sinh khí', 'Cát');
INSERT INTO bat_san VALUES ('Khôn', 'Li', 'Lục sát', 'Hung');
INSERT INTO bat_san VALUES ('Khôn', 'Chấn', 'Họa hại', 'Hung');
INSERT INTO bat_san VALUES ('Khôn', 'Khảm', 'Tuyệt mệnh', 'Hung');
INSERT INTO bat_san VALUES ('Khôn', 'Tốn', 'Ngũ quỷ', 'Hung');
INSERT INTO bat_san VALUES ('Cấn', 'Càn', 'Thiên y', 'Cát');
INSERT INTO bat_san VALUES ('Cấn', 'Đoài', 'Diên niên', 'Cát');
INSERT INTO bat_san VALUES ('Cấn', 'Khôn', 'Sinh khí', 'Cát');
INSERT INTO bat_san VALUES ('Cấn', 'Cấn', 'Phục vị', 'Cát');
INSERT INTO bat_san VALUES ('Cấn', 'Li', 'Họa hại', 'Hung');
INSERT INTO bat_san VALUES ('Cấn', 'Chấn', 'Lục sát', 'Hung');
INSERT INTO bat_san VALUES ('Cấn', 'Khảm', 'Ngũ quỷ', 'Hung');
INSERT INTO bat_san VALUES ('Cấn', 'Tốn', 'Tuyệt mệnh', 'Hung');
INSERT INTO bat_san VALUES ('Li', 'Càn', 'Tuyệt mệnh', 'Hung');
INSERT INTO bat_san VALUES ('Li', 'Đoài', 'Ngũ quỷ', 'Hung');
INSERT INTO bat_san VALUES ('Li', 'Khôn', 'Lục sát', 'Hung');
INSERT INTO bat_san VALUES ('Li', 'Cấn', 'Họa hại', 'Hung');
INSERT INTO bat_san VALUES ('Li', 'Li', 'Phục vị', 'Cát');
INSERT INTO bat_san VALUES ('Li', 'Chấn', 'Sinh khí', 'Cát');
INSERT INTO bat_san VALUES ('Li', 'Khảm', 'Diên niên', 'Cát');
INSERT INTO bat_san VALUES ('Li', 'Tốn', 'Thiên y', 'Cát');
INSERT INTO bat_san VALUES ('Chấn', 'Càn', 'Ngũ quỷ', 'Hung');
INSERT INTO bat_san VALUES ('Chấn', 'Đoài', 'Tuyệt mệnh', 'Hung');
INSERT INTO bat_san VALUES ('Chấn', 'Khôn', 'Họa hại', 'Hung');
INSERT INTO bat_san VALUES ('Chấn', 'Cấn', 'Lục sát', 'Hung');
INSERT INTO bat_san VALUES ('Chấn', 'Li', 'Sinh khí', 'Cát');
INSERT INTO bat_san VALUES ('Chấn', 'Chấn', 'Phục vị', 'Cát');
INSERT INTO bat_san VALUES ('Chấn', 'Khảm', 'Thiên y', 'Cát');
INSERT INTO bat_san VALUES ('Chấn', 'Tốn', 'Diên niên', 'Cát');
INSERT INTO bat_san VALUES ('Khảm', 'Càn', 'Lục sát', 'Hung');
INSERT INTO bat_san VALUES ('Khảm', 'Đoài', 'Họa hại', 'Hung');
INSERT INTO bat_san VALUES ('Khảm', 'Khôn', 'Tuyệt mệnh', 'Hung');
INSERT INTO bat_san VALUES ('Khảm', 'Cấn', 'Ngũ quỷ', 'Hung');
INSERT INTO bat_san VALUES ('Khảm', 'Li', 'Diên niên', 'Cát');
INSERT INTO bat_san VALUES ('Khảm', 'Chấn', 'Thiên y', 'Cát');
INSERT INTO bat_san VALUES ('Khảm', 'Khảm', 'Phục vị', 'Cát');
INSERT INTO bat_san VALUES ('Khảm', 'Tốn', 'Sinh khí', 'Cát');
INSERT INTO bat_san VALUES ('Tốn', 'Càn', 'Họa hại', 'Hung');
INSERT INTO bat_san VALUES ('Tốn', 'Đoài', 'Lục sát', 'Hung');
INSERT INTO bat_san VALUES ('Tốn', 'Khôn', 'Ngũ quỷ', 'Hung');
INSERT INTO bat_san VALUES ('Tốn', 'Cấn', 'Tuyệt mệnh', 'Hung');
INSERT INTO bat_san VALUES ('Tốn', 'Li', 'Thiên y', 'Cát');
INSERT INTO bat_san VALUES ('Tốn', 'Chấn', 'Diên niên', 'Cát');
INSERT INTO bat_san VALUES ('Tốn', 'Khảm', 'Sinh khí', 'Cát');
INSERT INTO bat_san VALUES ('Tốn', 'Tốn', 'Phục vị', 'Cát');

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

INSERT INTO que_kinh_dich VALUES (1, 'Bát thuần Càn', 'Càn', 'Càn', '111111', 'Tý,Dần,Thìn,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (2, 'Thiên địa Bĩ', 'Càn', 'Khôn', '000111', 'Mùi,Tị,Mão,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (3, 'Thiên hỏa Đồng nhân', 'Càn', 'Li', '101111', 'Mão,Sửu,Hợi,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (4, 'Thiên thủy Tụng', 'Càn', 'Khảm', '010111', 'Dần,Thìn,Ngọ,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (5, 'Thiên phong Cấu', 'Càn', 'Tốn', '011111', 'Sửu,Hợi,Dậu,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (6, 'Thiên lôi Vô vọng', 'Càn', 'Chấn', '100111', 'Tý,Dần,Thìn,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (7, 'Thiên sơn Độn', 'Càn', 'Cấn', '001111', 'Thìn,Ngọ,Thân,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (8, 'Thiên trạch Lý', 'Càn', 'Đoài', '110111', 'Tị,Mão,Sửu,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (9, 'Địa thiên Thái', 'Khôn', 'Càn', '111000', 'Tý,Dần,Thìn,Sửu,Hợi,Dậu');
INSERT INTO que_kinh_dich VALUES (10, 'Bát thuần Khôn', 'Khôn', 'Khôn', '000000', 'Mùi,Tị,Mão,Sửu,Hợi,Dậu');
INSERT INTO que_kinh_dich VALUES (11, 'Địa hỏa Minh di', 'Khôn', 'Li', '101000', 'Mão,Sửu,Hợi,Sửu,Hợi,Dậu');
INSERT INTO que_kinh_dich VALUES (12, 'Địa thủy Sư', 'Khôn', 'Khảm', '010000', 'Dần,Thìn,Ngọ,Sửu,Hợi,Dậu');
INSERT INTO que_kinh_dich VALUES (13, 'Địa phong Thăng', 'Khôn', 'Tốn', '011000', 'Sửu,Hợi,Dậu,Sửu,Hợi,Dậu');
INSERT INTO que_kinh_dich VALUES (14, 'Địa lôi Phục', 'Khôn', 'Chấn', '100000', 'Tý,Dần,Thìn,Sửu,Hợi,Dậu');
INSERT INTO que_kinh_dich VALUES (15, 'Địa sơn Khiêm', 'Khôn', 'Cấn', '001000', 'Thìn,Ngọ,Thân,Sửu,Hợi,Dậu');
INSERT INTO que_kinh_dich VALUES (16, 'Địa trạch Lâm', 'Khôn', 'Đoài', '110000', 'Tị,Mão,Sửu,Sửu,Hợi,Dậu');
INSERT INTO que_kinh_dich VALUES (17, 'Phong thiên Tiểu súc', 'Tốn', 'Càn', '111011', 'Tý,Dần,Thìn,Mùi,Tị,Mão');
INSERT INTO que_kinh_dich VALUES (18, 'Phong địa Quán', 'Tốn', 'Khôn', '000011', 'Mùi,Tị,Mão,Mùi,Tị,Mão');
INSERT INTO que_kinh_dich VALUES (19, 'Phong hỏa Gia nhân', 'Tốn', 'Li', '101011', 'Mão,Sửu,Hợi,Mùi,Tị,Mão');
INSERT INTO que_kinh_dich VALUES (20, 'Phong thủy Hoán', 'Tốn', 'Khảm', '010011', 'Dần,Thìn,Ngọ,Mùi,Tị,Mão');
INSERT INTO que_kinh_dich VALUES (21, 'Bát thuần Tốn', 'Tốn', 'Tốn', '011011', 'Sửu,Hợi,Dậu,Mùi,Tị,Mão');
INSERT INTO que_kinh_dich VALUES (22, 'Phong lôi Ích', 'Tốn', 'Chấn', '100011', 'Tý,Dần,Thìn,Mùi,Tị,Mão');
INSERT INTO que_kinh_dich VALUES (23, 'Phong sơn Tiệm', 'Tốn', 'Cấn', '001011', 'Thìn,Ngọ,Thân,Mùi,Tị,Mão');
INSERT INTO que_kinh_dich VALUES (24, 'Phong trạch Trung phu', 'Tốn', 'Đoài', '110011', 'Tị,Mão,Sửu,Mùi,Tị,Mão');
INSERT INTO que_kinh_dich VALUES (25, 'Lôi thiên Đại tráng', 'Chấn', 'Càn', '111100', 'Tý,Dần,Thìn,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (26, 'Lôi địa Dự', 'Chấn', 'Khôn', '000100', 'Mùi,Tị,Mão,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (27, 'Lôi hỏa Phong', 'Chấn', 'Li', '101100', 'Mão,Sửu,Hợi,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (28, 'Lôi thủy Giải', 'Chấn', 'Khảm', '010100', 'Dần,Thìn,Ngọ,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (29, 'Lôi phong Hằng', 'Chấn', 'Tốn', '011100', 'Sửu,Hợi,Dậu,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (30, 'Bát thuần Chấn', 'Chấn', 'Chấn', '100100', 'Tý,Dần,Thìn,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (31, 'Lôi sơn Tiểu quá', 'Chấn', 'Cấn', '001100', 'Thìn,Ngọ,Thân,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (32, 'Lôi trạch Quy muội', 'Chấn', 'Đoài', '110100', 'Tị,Mão,Sửu,Ngọ,Thân,Tuất');
INSERT INTO que_kinh_dich VALUES (33, 'Hỏa thiên Đại hữu', 'Li', 'Càn', '111101', 'Tý,Dần,Thìn,Dậu,Mùi,Tị');
INSERT INTO que_kinh_dich VALUES (34, 'Hỏa địa Tấn', 'Li', 'Khôn', '000101', 'Mùi,Tị,Mão,Dậu,Mùi,Tị');
INSERT INTO que_kinh_dich VALUES (35, 'Bát thuần Li', 'Li', 'Li', '101101', 'Mão,Sửu,Hợi,Dậu,Mùi,Tị');
INSERT INTO que_kinh_dich VALUES (36, 'Hỏa thủy Vị tế', 'Li', 'Khảm', '010101', 'Dần,Thìn,Ngọ,Dậu,Mùi,Tị');
INSERT INTO que_kinh_dich VALUES (37, 'Hỏa phong Đỉnh', 'Li', 'Tốn', '011101', 'Sửu,Hợi,Dậu,Dậu,Mùi,Tị');
INSERT INTO que_kinh_dich VALUES (38, 'Hỏa lôi Phệ hạp', 'Li', 'Chấn', '100101', 'Tý,Dần,Thìn,Dậu,Mùi,Tị');
INSERT INTO que_kinh_dich VALUES (39, 'Hỏa sơn Lữ', 'Li', 'Cấn', '001101', 'Thìn,Ngọ,Thân,Dậu,Mùi,Tị');
INSERT INTO que_kinh_dich VALUES (40, 'Hỏa trạch Khuê', 'Li', 'Đoài', '110101', 'Tị,Mão,Sửu,Dậu,Mùi,Tị');
INSERT INTO que_kinh_dich VALUES (41, 'Sơn thiên Đại súc', 'Cấn', 'Càn', '111001', 'Tý,Dần,Thìn,Tuất,Tý,Dần');
INSERT INTO que_kinh_dich VALUES (42, 'Sơn địa Bác', 'Cấn', 'Khôn', '000001', 'Mùi,Tị,Mão,Tuất,Tý,Dần');
INSERT INTO que_kinh_dich VALUES (43, 'Sơn hỏa Bí', 'Cấn', 'Li', '101001', 'Mão,Sửu,Hợi,Tuất,Tý,Dần');
INSERT INTO que_kinh_dich VALUES (44, 'Sơn thủy Mông', 'Cấn', 'Khảm', '010001', 'Dần,Thìn,Ngọ,Tuất,Tý,Dần');
INSERT INTO que_kinh_dich VALUES (45, 'Sơn phong Cổ', 'Cấn', 'Tốn', '011001', 'Sửu,Hợi,Dậu,Tuất,Tý,Dần');
INSERT INTO que_kinh_dich VALUES (46, 'Sơn lôi Di', 'Cấn', 'Chấn', '100001', 'Tý,Dần,Thìn,Tuất,Tý,Dần');
INSERT INTO que_kinh_dich VALUES (47, 'Bát thuần Cấn', 'Cấn', 'Cấn', '001001', 'Thìn,Ngọ,Thân,Tuất,Tý,Dần');
INSERT INTO que_kinh_dich VALUES (48, 'Sơn trạch Tổn', 'Cấn', 'Đoài', '110001', 'Tị,Mão,Sửu,Tuất,Tý,Dần');
INSERT INTO que_kinh_dich VALUES (49, 'Thủy thiên Nhu', 'Khảm', 'Càn', '111010', 'Tý,Dần,Thìn,Thân,Tuất,Tý');
INSERT INTO que_kinh_dich VALUES (50, 'Thủy địa Tỉ', 'Khảm', 'Khôn', '000010', 'Mùi,Tị,Mão,Thân,Tuất,Tý');
INSERT INTO que_kinh_dich VALUES (51, 'Thủy hỏa Kí tế', 'Khảm', 'Li', '101010', 'Mão,Sửu,Hợi,Thân,Tuất,Tý');
INSERT INTO que_kinh_dich VALUES (52, 'Bát thuần Khảm', 'Khảm', 'Khảm', '010010', 'Dần,Thìn,Ngọ,Thân,Tuất,Tý');
INSERT INTO que_kinh_dich VALUES (53, 'Thủy phong Tỉnh', 'Khảm', 'Tốn', '011010', 'Sửu,Hợi,Dậu,Thân,Tuất,Tý');
INSERT INTO que_kinh_dich VALUES (54, 'Thủy lôi Truân', 'Khảm', 'Chấn', '100010', 'Tý,Dần,Thìn,Thân,Tuất,Tý');
INSERT INTO que_kinh_dich VALUES (55, 'Thủy sơn Kiển', 'Khảm', 'Cấn', '001010', 'Thìn,Ngọ,Thân,Thân,Tuất,Tý');
INSERT INTO que_kinh_dich VALUES (56, 'Thủy trạch Tiết', 'Khảm', 'Đoài', '110010', 'Tị,Mão,Sửu,Thân,Tuất,Tý');
INSERT INTO que_kinh_dich VALUES (57, 'Trạch thiên Quải', 'Đoài', 'Càn', '111110', 'Tý,Dần,Thìn,Hợi,Dậu,Mùi');
INSERT INTO que_kinh_dich VALUES (58, 'Trạch địa Tụy', 'Đoài', 'Khôn', '000110', 'Mùi,Tị,Mão,Hợi,Dậu,Mùi');
INSERT INTO que_kinh_dich VALUES (59, 'Trạch hỏa Cách', 'Đoài', 'Li', '101110', 'Mão,Sửu,Hợi,Hợi,Dậu,Mùi');
INSERT INTO que_kinh_dich VALUES (60, 'Trạch thủy Khốn', 'Đoài', 'Khảm', '010110', 'Dần,Thìn,Ngọ,Hợi,Dậu,Mùi');
INSERT INTO que_kinh_dich VALUES (61, 'Trạch phong Đại quá', 'Đoài', 'Tốn', '011110', 'Sửu,Hợi,Dậu,Hợi,Dậu,Mùi');
INSERT INTO que_kinh_dich VALUES (62, 'Trạch lôi Tùy', 'Đoài', 'Chấn', '100110', 'Tý,Dần,Thìn,Hợi,Dậu,Mùi');
INSERT INTO que_kinh_dich VALUES (63, 'Trạch sơn Hàm', 'Đoài', 'Cấn', '001110', 'Thìn,Ngọ,Thân,Hợi,Dậu,Mùi');
INSERT INTO que_kinh_dich VALUES (64, 'Bát thuần Đoài', 'Đoài', 'Đoài', '110110', 'Tị,Mão,Sửu,Hợi,Dậu,Mùi');

-- 7. BẢNG MÃ SỐ BÁT TỰ HÀ - LẠC (CHƯƠNG VIII)
CREATE TABLE thien_can_ma_so (
    can TEXT PRIMARY KEY,
    ma_so INTEGER NOT NULL
);

INSERT INTO thien_can_ma_so VALUES ('Kỷ', 1);
INSERT INTO thien_can_ma_so VALUES ('Mậu', 2);
INSERT INTO thien_can_ma_so VALUES ('Bính', 3);
INSERT INTO thien_can_ma_so VALUES ('Đinh', 3);
INSERT INTO thien_can_ma_so VALUES ('Giáp', 4);
INSERT INTO thien_can_ma_so VALUES ('Ất', 6);
INSERT INTO thien_can_ma_so VALUES ('Nhâm', 7);
INSERT INTO thien_can_ma_so VALUES ('Quý', 7);
INSERT INTO thien_can_ma_so VALUES ('Tân', 8);
INSERT INTO thien_can_ma_so VALUES ('Canh', 9);

CREATE TABLE dia_chi_ma_so (
    chi TEXT NOT NULL,
    nhom_doi_tuong TEXT NOT NULL,
    ma_so_1 INTEGER NOT NULL,
    ma_so_2 INTEGER NOT NULL,
    PRIMARY KEY (chi, nhom_doi_tuong)
);

INSERT INTO dia_chi_ma_so VALUES ('Tý', 'Dương nam, Âm nữ', 9, 2);
INSERT INTO dia_chi_ma_so VALUES ('Hợi', 'Dương nam, Âm nữ', 9, 2);
INSERT INTO dia_chi_ma_so VALUES ('Ngọ', 'Dương nam, Âm nữ', 1, 8);
INSERT INTO dia_chi_ma_so VALUES ('Tị', 'Dương nam, Âm nữ', 1, 8);
INSERT INTO dia_chi_ma_so VALUES ('Mão', 'Dương nam, Âm nữ', 7, 6);
INSERT INTO dia_chi_ma_so VALUES ('Dần', 'Dương nam, Âm nữ', 7, 6);
INSERT INTO dia_chi_ma_so VALUES ('Dậu', 'Dương nam, Âm nữ', 3, 4);
INSERT INTO dia_chi_ma_so VALUES ('Thân', 'Dương nam, Âm nữ', 3, 4);
INSERT INTO dia_chi_ma_so VALUES ('Thìn', 'Dương nam, Âm nữ', 7, 7);
INSERT INTO dia_chi_ma_so VALUES ('Tuất', 'Dương nam, Âm nữ', 3, 3);
INSERT INTO dia_chi_ma_so VALUES ('Sửu', 'Dương nam, Âm nữ', 9, 9);
INSERT INTO dia_chi_ma_so VALUES ('Mùi', 'Dương nam, Âm nữ', 1, 1);
INSERT INTO dia_chi_ma_so VALUES ('Tý', 'Âm nam, Dương nữ', 7, 4);
INSERT INTO dia_chi_ma_so VALUES ('Hợi', 'Âm nam, Dương nữ', 7, 4);
INSERT INTO dia_chi_ma_so VALUES ('Ngọ', 'Âm nam, Dương nữ', 3, 6);
INSERT INTO dia_chi_ma_so VALUES ('Tị', 'Âm nam, Dương nữ', 3, 6);
INSERT INTO dia_chi_ma_so VALUES ('Mão', 'Âm nam, Dương nữ', 4, 9);
INSERT INTO dia_chi_ma_so VALUES ('Dần', 'Âm nam, Dương nữ', 4, 9);
INSERT INTO dia_chi_ma_so VALUES ('Dậu', 'Âm nam, Dương nữ', 6, 1);
INSERT INTO dia_chi_ma_so VALUES ('Thân', 'Âm nam, Dương nữ', 6, 1);
INSERT INTO dia_chi_ma_so VALUES ('Thìn', 'Âm nam, Dương nữ', 3, 1);
INSERT INTO dia_chi_ma_so VALUES ('Tuất', 'Âm nam, Dương nữ', 7, 9);
INSERT INTO dia_chi_ma_so VALUES ('Sửu', 'Âm nam, Dương nữ', 2, 6);
INSERT INTO dia_chi_ma_so VALUES ('Mùi', 'Âm nam, Dương nữ', 8, 4);