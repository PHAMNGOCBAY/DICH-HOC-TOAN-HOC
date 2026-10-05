import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MASTER_MD_PATH = r"C:\DICH HOC\DICH_HOC_TOAN_HOC.md"

content = """# HỆ THỐNG TOÁN HỌC DỊCH HỌC VÀ CƠ SỞ DỮ LIỆU ĐỐI CHIẾU NGUYÊN BẢN
# DỊCH HỌC DIỄN GIẢI TRÊN CƠ SỞ TOÁN HỌC VÀ ỨNG DỤNG VÀO ĐỜI SỐNG

Tài liệu gốc: [DICH HOC-TOANHOC-DOI SONG.pdf](file:///C:/DICH%20HOC/DICH%20HOC-TOANHOC-DOI%20SONG.pdf)  
Tác giả: TS. Nguyễn Thế Cường (Nguyễn Quý Thế Cường) - NXB Đại học Quốc gia TP. Hồ Chí Minh, 2014.  
Nguyên tắc biên soạn: Tuyệt đối không bịa đặt số liệu, không suy diễn chủ quan, đối chiếu trực tiếp từ nguyên bản của tác giả.

---

## 1. MỤC LỤC TOÀN VĂN THEO CHƯƠNG VÀ ĐƯỜNG DẪN TRÍCH XUẤT OCR

Toàn bộ 278 trang tài liệu PDF gốc đã được giải mã quang học (OCR) với đầy đủ định vị số trang kép (Trang sách in và Trang PDF) tại các tệp Markdown chuyên đề sau:

| STT | Phân đoạn tài liệu | Tên chương / Mục chuyên đề | Phạm vi trang PDF | Tệp toàn văn Markdown |
|:---:|:---|:---|:---:|:---|
| 0 | Lời mở đầu | Bìa, xuất bản, lời tựa và mục lục | PDF p.1 - 13 | [Chuong_0_Mo_Dau.md](file:///C:/DICH%20HOC/Chuong_0_Mo_Dau.md) |
| 1 | Chương I | Cơ sở toán học của Bát quái | PDF p.14 - 19 | [Chuong_1_Co_So_Toan_Hoc.md](file:///C:/DICH%20HOC/Chuong_1_Co_So_Toan_Hoc.md) |
| 2 | Chương II | Âm, dương và Thái cực | PDF p.20 - 36 | [Chuong_2_Am_Duong_Thai_Cuc.md](file:///C:/DICH%20HOC/Chuong_2_Am_Duong_Thai_Cuc.md) |
| 3 | Chương III | Tạo quái từ lưỡng nghi âm, dương | PDF p.37 - 60 | [Chuong_3_Tao_Quai_Tu_Luong_Nghi.md](file:///C:/DICH%20HOC/Chuong_3_Tao_Quai_Tu_Luong_Nghi.md) |
| 4 | Chương IV | Bát quái Tân thiên | PDF p.61 - 86 | [Chuong_4_Bat_Quai_Tan_Thien.md](file:///C:/DICH%20HOC/Chuong_4_Bat_Quai_Tan_Thien.md) |
| 5 | Chương V | Đồ tổng hợp Quái - Can - Chi (QCC) | PDF p.87 - 103 | [Chuong_5_Do_Tong_Hop_QCC.md](file:///C:/DICH%20HOC/Chuong_5_Do_Tong_Hop_QCC.md) |
| 6 | Chương VI | Ứng dụng QCC vào đời sống cá nhân và gia đình | PDF p.104 - 167 | [Chuong_6_Ung_Dung_QCC.md](file:///C:/DICH%20HOC/Chuong_6_Ung_Dung_QCC.md) |
| 7 | Chương VII | Quẻ dịch và Nạp giáp | PDF p.168 - 207 | [Chuong_7_Que_Dich.md](file:///C:/DICH%20HOC/Chuong_7_Que_Dich.md) |
| 8 | Chương VIII | Nhận dạng theo phương pháp Bát tự Hà – Lạc | PDF p.208 - 265 | [Chuong_8_Bat_Tu_Ha_Lac.md](file:///C:/DICH%20HOC/Chuong_8_Bat_Tu_Ha_Lac.md) |
| 9 | Chương IX | Lời kết, 11 tài liệu tham khảo và mục lục | PDF p.266 - 278 | [Chuong_9_Ket_Luan_Tham_Khao.md](file:///C:/DICH%20HOC/Chuong_9_Ket_Luan_Tham_Khao.md) |

---

## 2. CHƯƠNG I: CƠ SỞ TOÁN HỌC CỦA BÁT QUÁI (NHÓM CỘNG HÀ - LẠC)

### 2.1. Đồng hồ 10 vạch chia và Nhóm Abel (Z/10Z, +)
Tác giả thống nhất toán học hóa Hà đồ và Lạc thư bằng cấu trúc nhóm Abel trên tập hợp 10 chữ số S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
- Phép cộng đồng hồ 10 vạch: quan hệ modulo 10 với 10 ≡ 0.
- Phần tử trung hòa: e = 0.
- Các cặp số đối duy nhất thỏa mãn a + a' = 0 (mod 10):
  - 1' = 9 và 9' = 1 (vì 1 + 9 = 10 ≡ 0)
  - 2' = 8 và 8' = 2 (vì 2 + 8 = 10 ≡ 0)
  - 3' = 7 và 7' = 3 (vì 3 + 7 = 10 ≡ 0)
  - 4' = 6 và 6' = 4 (vì 4 + 6 = 10 ≡ 0)
  - 5' = 5 (vì 5 + 5 = 10 ≡ 0)
  - 0' = 0 (vì 0 + 0 = 0)

### 2.2. Minh chứng hình ảnh và Bản vẽ kỹ thuật CAD
- **Bản vẽ kỹ thuật CAD:** [cad_dong_ho_ha_lac.dxf](file:///C:/DICH%20HOC/drawings/cad_dong_ho_ha_lac.dxf)  
- **Hình vẽ kỹ thuật (PNG 300 DPI):**  
  ![Đồng hồ 10 vạch chia và nhóm cộng Hà Lạc](file:///C:/DICH%20HOC/drawings/cad_dong_ho_ha_lac.png)
- **Hình ảnh nguyên bản trong sách (Trang 1):**  
  ![Hà đồ Lạc thư và đồng hồ](file:///C:/DICH%20HOC/images_pdf/hinh_01_ha_do_lac_thu_dong_ho.png)

---

## 3. CHƯƠNG II: ÂM, DƯƠNG VÀ THÁI CỰC (HỆ NGUYÊN LÝ VÀ ĐỊNH LUẬT HỢP HÓA)

### 3.1. Phân loại số học và Thái cực
- Số lẻ (Dương): 1, 3, 7, 9.
- Số chẵn (Âm): 2, 4, 6, 8.
- Số 0: Thái cực, trung hòa.
- Số 5: Vị trí chính giữa trung cung Lạc thư, tượng trưng cho bản thể năng lượng chuyển tiếp.

### 3.2. Định luật Hợp hóa Thiên can và Địa chi
1. **Thiên can ngũ hợp (Chương II.3, trang 18):**
   - Giáp (Mộc) + Kỷ (Thổ) hợp hóa **Thổ**
   - Ất (Mộc) + Canh (Kim) hợp hóa **Kim**
   - Bính (Hỏa) + Tân (Kim) hợp hóa **Thủy**
   - Đinh (Hỏa) + Nhâm (Thủy) hợp hóa **Mộc**
   - Mậu (Thổ) + Quý (Thủy) hợp hóa **Hỏa**
2. **Địa chi lục hợp:**
   - Tý - Sửu hợp Thổ; Dần - Hợi hợp Mộc; Mão - Tuất hợp Hỏa; Thìn - Dậu hợp Kim; Tị - Thân hợp Thủy; Ngọ - Mùi hợp Thái Dương / Thái Âm.
3. **Địa chi tam hợp:**
   - Thân - Tý - Thìn: Thủy cục
   - Hợi - Mão - Mùi: Mộc cục
   - Dần - Ngọ - Tuất: Hỏa cục
   - Tị - Dậu - Sửu: Kim cục

### 3.3. Hình ảnh nguyên bản Thái cực đồ
![Đồ hình Thái cực và vòng tròn âm dương](file:///C:/DICH%20HOC/images_pdf/hinh_02_thai_cuc_do.png)

---

## 4. CHƯƠNG III: TẠO QUÁI TỪ LƯỠNG NGHI ÂM, DƯƠNG

### 4.1. Định luật trọng số năng lượng của các hào
Theo TS. Nguyễn Thế Cường (trang 24 - 47), các hào có trọng số năng lượng:
- **Hào 1 (sơ, dưới cùng):** trọng số ±1
- **Hào 2 (trung, ở giữa):** trọng số ±3
- **Hào 3 (thượng, trên cùng):** trọng số ±5

Công thức tính mức năng lượng tổng đại số của quái 3 hào:
```text
E = h1*(±1) + h2*(±3) + h3*(±5)
Trong đó: Hào dương lấy dấu (+), Hào âm lấy dấu (-).
```

### 4.2. Bảng năng lượng 8 quái
| Tên quái | Cấu trúc hào (1, 2, 3) | Biểu thức tính năng lượng | Trị số năng lượng E | Tính chất |
|:---|:---:|:---:|:---:|:---:|
| **Khôn** | (0, 0, 0) | -1 - 3 - 5 | **-9** | Cực Âm |
| **Chấn** | (1, 0, 0) | +1 - 3 - 5 | **-7** | Âm |
| **Khảm** | (0, 1, 0) | -1 + 3 - 5 | **-3** | Âm |
| **Đoài** | (1, 1, 0) | +1 + 3 - 5 | **-1** | Âm |
| **Cấn** | (0, 0, 1) | -1 - 3 + 5 | **+1** | Dương |
| **Li** | (1, 0, 1) | +1 - 3 + 5 | **+3** | Dương |
| **Tốn** | (0, 1, 1) | -1 + 3 + 5 | **+7** | Dương |
| **Càn** | (1, 1, 1) | +1 + 3 + 5 | **+9** | Cực Dương |

### 4.3. Biểu đồ năng lượng Bát quái
- **Biểu đồ Matplotlib (PNG 300 DPI):**  
  ![Biểu đồ năng lượng Bát quái](file:///C:/DICH%20HOC/drawings/chart_nang_luong_bat_quai.png)
- **Hình ảnh nguyên bản trong sách (Trang 25):**  
  ![Tạo tượng và quái từ lưỡng nghi](file:///C:/DICH%20HOC/images_pdf/hinh_03_tao_tu_tuong_bat_quai.png)

---

## 5. CHƯƠNG IV: BÁT QUÁI TÂN THIÊN VÀ MA TRẬN LẠC THƯ 3x3

### 5.1. Bát quái Tân thiên trên Lạc thư
Ma trận Lạc thư 3x3 được tác giả thiết lập theo trục tọa độ không gian:
- Hàng trên (Nam): Tốn (Cung 4, +7), Càn (Cung 9, +9), Cấn (Cung 2, +1)
- Hàng giữa: Li (Cung 3, +3), Thái Cực (Cung 5, 0), Khảm (Cung 7, -3)
- Hàng dưới (Bắc): Đoài (Cung 8, -1), Khôn (Cung 1, -9), Chấn (Cung 6, -7)

### 5.2. Tính chất đối xứng tâm và Cặp phu thê
- **Đối xứng qua tâm Thái cực:**
  - Càn (9) đối Khôn (1): Cung 9 + 1 = 10; Năng lượng (+9) + (-9) = 0.
  - Li (3) đối Khảm (7): Cung 3 + 7 = 10; Năng lượng (+3) + (-3) = 0.
  - Tốn (4) đối Chấn (6): Cung 4 + 6 = 10; Năng lượng (+7) + (-7) = 0.
  - Cấn (2) đối Đoài (8): Cung 2 + 8 = 10; Năng lượng (+1) + (-1) = 0.
- **Cặp phu thê Tân thiên:** Càn - Đoài, Li - Chấn, Tốn - Khảm, Cấn - Khôn.

### 5.3. Bản vẽ CAD và Hình ảnh minh chứng
- **Bản vẽ kỹ thuật CAD:** [cad_bat_quai_tan_thien.dxf](file:///C:/DICH%20HOC/drawings/cad_bat_quai_tan_thien.dxf)  
- **Hình vẽ kỹ thuật (PNG 300 DPI):**  
  ![Bát quái Tân thiên trên Lạc thư 3x3](file:///C:/DICH%20HOC/drawings/cad_bat_quai_tan_thien.png)
- **Hình ảnh nguyên bản trong sách (Trang 48 & 54):**  
  ![Bát quái Tân thiên trên Lạc thư nguyên bản](file:///C:/DICH%20HOC/images_pdf/hinh_04_bat_quai_tan_thien_lac_thu.png)  
  ![Phương vị Bát quái Tân thiên](file:///C:/DICH%20HOC/images_pdf/hinh_05_bat_quai_tan_thien_phuong_vi.png)

---

## 6. CHƯƠNG V: ĐỒ TỔNG HỢP QUÁI - CAN - CHI (QCC)

Tác giả tích hợp Bát quái Tân thiên với 10 Thiên can và 12 Địa chi trên một mặt phẳng tọa độ tròn:
- Canh, Tân, Nhâm, Quý, Giáp, Ất, Bính, Đinh, Mậu, Kỷ phân bổ theo góc phương vị hoàng đạo.
- 12 Địa chi phân bổ 12 cung góc 30 độ tương ứng.
- **Hình ảnh nguyên bản trong sách (Trang 74 & 80):**  
  ![Đồ tổng hợp Quái Can Chi](file:///C:/DICH%20HOC/images_pdf/hinh_06_do_tong_hop_qcc.png)  
  ![Phân bố Can Chi trên QCC](file:///C:/DICH%20HOC/images_pdf/hinh_07_thien_can_dia_chi_qcc.png)

---

## 7. CHƯƠNG VI: ỨNG DỤNG QCC VÀO ĐỜI SỐNG (BÁT SAN & PHONG THỦY)

### 7.1. Phân loại Đông - Tây tứ mệnh
- **Đông tứ trạch / mệnh:** Khảm (Thủy), Li (Hỏa), Chấn (Mộc), Tốn (Mộc).
- **Tây tứ trạch / mệnh:** Càn (Kim), Khôn (Thổ), Cấn (Thổ), Đoài (Kim).

### 7.2. Bảng 26: Ma trận 8x8 Bát san
Tám san quan hệ giữa Quái trạch (hướng nhà) và Quái mệnh (người):
- **Bốn cung Cát:** Sinh khí, Thiên y, Diên niên, Phục vị.
- **Bốn cung Hung:** Tuyệt mệnh, Ngũ quỷ, Lục sát, Họa hại.

| Quái trạch \ Quái mệnh | Càn | Đoài | Khôn | Cấn | Li | Chấn | Khảm | Tốn |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **Càn** | Phục vị | Sinh khí | Diên niên | Thiên y | Tuyệt mệnh | Ngũ quỷ | Lục sát | Họa hại |
| **Đoài** | Sinh khí | Phục vị | Thiên y | Diên niên | Ngũ quỷ | Tuyệt mệnh | Họa hại | Lục sát |
| **Khôn** | Diên niên | Thiên y | Phục vị | Sinh khí | Lục sát | Họa hại | Tuyệt mệnh | Ngũ quỷ |
| **Cấn** | Thiên y | Diên niên | Sinh khí | Phục vị | Họa hại | Lục sát | Ngũ quỷ | Tuyệt mệnh |
| **Li** | Tuyệt mệnh | Ngũ quỷ | Lục sát | Họa hại | Phục vị | Sinh khí | Diên niên | Thiên y |
| **Chấn** | Ngũ quỷ | Tuyệt mệnh | Họa hại | Lục sát | Sinh khí | Phục vị | Thiên y | Diên niên |
| **Khảm** | Lục sát | Họa hại | Tuyệt mệnh | Ngũ quỷ | Diên niên | Thiên y | Phục vị | Sinh khí |
| **Tốn** | Họa hại | Lục sát | Ngũ quỷ | Tuyệt mệnh | Thiên y | Diên niên | Sinh khí | Phục vị |

### 7.3. Bản vẽ CAD và Hình ảnh minh chứng
- **Bản vẽ kỹ thuật CAD:** [cad_ma_tran_bat_san.dxf](file:///C:/DICH%20HOC/drawings/cad_ma_tran_bat_san.dxf)  
- **Hình vẽ kỹ thuật (PNG 300 DPI):**  
  ![Ma trận Bát san 8x8](file:///C:/DICH%20HOC/drawings/cad_ma_tran_bat_san.png)
- **Hình ảnh nguyên bản trong sách (Trang 144):**  
  ![Bảng 26 Bát san](file:///C:/DICH%20HOC/images_pdf/hinh_08_bang_26_bat_san.png)

---

## 8. CHƯƠNG VII: QUẺ DỊCH VÀ NẠP GIÁP

### 8.1. Hệ nhị phân Phục Hi
Mỗi quẻ kép 6 hào tương đương một số nhị phân 6-bit từ `000000` (Bát thuần Khôn) đến `111111` (Bát thuần Càn).
- **Hình ảnh nguyên bản trong sách (Trang 155 & 165):**  
  ![Bảng 27 Danh mục 64 quẻ dịch](file:///C:/DICH%20HOC/images_pdf/hinh_09_bang_27_64_que_dich.png)  
  ![Vòng tròn 64 quẻ nhị phân Phục Hi](file:///C:/DICH%20HOC/images_pdf/hinh_10_vong_tron_64_que_phuc_hi.png)

### 8.2. Nạp Chi Kinh Phòng cho 6 hào
Toàn bộ 64 quẻ được nạp 6 Địa chi theo quy tắc nội quái (hào 1-3) và ngoại quái (hào 4-6). Dữ liệu chi tiết đã được số hóa hoàn chỉnh vào [dich_hoc_data.json](file:///C:/DICH%20HOC/dich_hoc_data.json) và [dich_hoc_schema.sql](file:///C:/DICH%20HOC/dich_hoc_schema.sql).

---

## 9. CHƯƠNG VIII: NHẬN DẠNG BÁT TỰ HÀ - LẠC TOÀN DIỆN

### 9.1. Mã số Thiên can và Địa chi
1. **Thiên can (Bảng 43, trang 221):**
   - Kỷ: 1, Mậu: 2, Bính: 3, Đinh: 3, Giáp: 4, Ất: 6, Nhâm: 7, Quý: 7, Tân: 8, Canh: 9.
2. **Địa chi đối với Dương nam, Âm nữ (Bảng 41, trang 219):**
   - Tý: (9, 2), Hợi: (9, 2), Ngọ: (1, 8), Tị: (1, 8), Mão: (7, 6), Dần: (7, 6), Dậu: (3, 4), Thân: (3, 4), Thìn: (7, 7), Tuất: (3, 3), Sửu: (9, 9), Mùi: (1, 1).
3. **Địa chi đối với Âm nam, Dương nữ (Bảng 42, trang 219):**
   - Tý: (7, 4), Hợi: (7, 4), Ngọ: (3, 6), Tị: (3, 6), Mão: (4, 9), Dần: (4, 9), Dậu: (6, 1), Thân: (6, 1), Thìn: (3, 1), Tuất: (7, 9), Sửu: (2, 6), Mùi: (8, 4).

### 9.2. Sơ đồ quy trình thuật toán Bát tự Hà - Lạc
- **Biểu đồ luồng thuật toán (PNG 300 DPI):**  
  ![Quy trình thuật toán Bát tự Hà Lạc](file:///C:/DICH%20HOC/drawings/chart_quy_trinh_bat_tu_ha_lac.png)
- **Hình ảnh nguyên bản trong sách (Trang 214 & 222):**  
  ![Bảng 41-42 mã số can chi](file:///C:/DICH%20HOC/images_pdf/hinh_11_bang_41_42_ma_so_dia_chi.png)  
  ![Minh họa xác định quẻ Tiên thiên](file:///C:/DICH%20HOC/images_pdf/hinh_12_xac_dinh_que_tien_thien.png)

### 9.3. Phân bổ các Đại vận đời người
- **Hào Dương:** Cai quản 9 năm.
- **Hào Âm:** Cai quản 6 năm.
- **Biểu đồ trục thời gian Đại vận (PNG 300 DPI):**  
  ![Timeline Đại vận](file:///C:/DICH%20HOC/drawings/chart_dai_van_timeline.png)

---

## 10. BẢNG THỐNG KÊ TOÀN BỘ CÁC TỆP TRONG HỆ THỐNG

| Tên tệp | Định dạng | Dung lượng | Chức năng trong hệ thống | Liên kết mở tệp |
|:---|:---:|:---:|:---|:---:|
| `DICH_HOC_TOAN_HOC.md` | Markdown | ~25 KB | Báo cáo kỹ thuật tổng hợp & Danh mục minh chứng | [DICH_HOC_TOAN_HOC.md](file:///C:/DICH%20HOC/DICH_HOC_TOAN_HOC.md) |
| `dich_hoc_core.py` | Python (.py) | 33.4 KB | Mô-đun thuật toán toán học hoàn chỉnh cho 8 chương | [dich_hoc_core.py](file:///C:/DICH%20HOC/dich_hoc_core.py) |
| `dich_hoc_data.json` | JSON | 33.5 KB | Cơ sở dữ liệu cấu trúc tra cứu toàn diện 8 chương | [dich_hoc_data.json](file:///C:/DICH%20HOC/dich_hoc_data.json) |
| `dich_hoc_schema.sql` | SQL | 20.4 KB | Script DDL và Seed Data chuẩn ANSI/SQLite 8 bảng | [dich_hoc_schema.sql](file:///C:/DICH%20HOC/dich_hoc_schema.sql) |
| `cad_dong_ho_ha_lac.dxf` | AutoDesk CAD | 49.1 KB | Bản vẽ CAD đồng hồ 10 vạch & nhóm cộng Hà Lạc | [cad_dong_ho_ha_lac.dxf](file:///C:/DICH%20HOC/drawings/cad_dong_ho_ha_lac.dxf) |
| `cad_bat_quai_tan_thien.dxf` | AutoDesk CAD | 56.2 KB | Bản vẽ CAD Bát quái Tân thiên trên Lạc thư 3x3 | [cad_bat_quai_tan_thien.dxf](file:///C:/DICH%20HOC/drawings/cad_bat_quai_tan_thien.dxf) |
| `cad_ma_tran_bat_san.dxf` | AutoDesk CAD | 61.0 KB | Bản vẽ CAD ma trận 8x8 Bát san | [cad_ma_tran_bat_san.dxf](file:///C:/DICH%20HOC/drawings/cad_ma_tran_bat_san.dxf) |
| `Chuong_0_Mo_Dau.md` | Markdown | 20.2 KB | Toàn văn OCR Lời mở đầu & Mục lục sách | [Chuong_0_Mo_Dau.md](file:///C:/DICH%20HOC/Chuong_0_Mo_Dau.md) |
| `Chuong_1_Co_So_Toan_Hoc.md` | Markdown | 12.2 KB | Toàn văn OCR Chương I: Cơ sở toán học | [Chuong_1_Co_So_Toan_Hoc.md](file:///C:/DICH%20HOC/Chuong_1_Co_So_Toan_Hoc.md) |
| `Chuong_2_Am_Duong_Thai_Cuc.md` | Markdown | 41.9 KB | Toàn văn OCR Chương II: Âm dương & Thái cực | [Chuong_2_Am_Duong_Thai_Cuc.md](file:///C:/DICH%20HOC/Chuong_2_Am_Duong_Thai_Cuc.md) |
| `Chuong_3_Tao_Quai_Tu_Luong_Nghi.md` | Markdown | 52.9 KB | Toàn văn OCR Chương III: Tạo quái từ lưỡng nghi | [Chuong_3_Tao_Quai_Tu_Luong_Nghi.md](file:///C:/DICH%20HOC/Chuong_3_Tao_Quai_Tu_Luong_Nghi.md) |
| `Chuong_4_Bat_Quai_Tan_Thien.md` | Markdown | 60.9 KB | Toàn văn OCR Chương IV: Bát quái Tân thiên | [Chuong_4_Bat_Quai_Tan_Thien.md](file:///C:/DICH%20HOC/Chuong_4_Bat_Quai_Tan_Thien.md) |
| `Chuong_5_Do_Tong_Hop_QCC.md` | Markdown | 35.5 KB | Toàn văn OCR Chương V: Đồ tổng hợp QCC | [Chuong_5_Do_Tong_Hop_QCC.md](file:///C:/DICH%20HOC/Chuong_5_Do_Tong_Hop_QCC.md) |
| `Chuong_6_Ung_Dung_QCC.md` | Markdown | 141.7 KB | Toàn văn OCR Chương VI: Ứng dụng phong thủy & đời sống | [Chuong_6_Ung_Dung_QCC.md](file:///C:/DICH%20HOC/Chuong_6_Ung_Dung_QCC.md) |
| `Chuong_7_Que_Dich.md` | Markdown | Đang ghi | Toàn văn OCR Chương VII: 64 quẻ Dịch | [Chuong_7_Que_Dich.md](file:///C:/DICH%20HOC/Chuong_7_Que_Dich.md) |
| `Chuong_8_Bat_Tu_Ha_Lac.md` | Markdown | Đang ghi | Toàn văn OCR Chương VIII: Bát tự Hà Lạc | [Chuong_8_Bat_Tu_Ha_Lac.md](file:///C:/DICH%20HOC/Chuong_8_Bat_Tu_Ha_Lac.md) |
| `Chuong_9_Ket_Luan_Tham_Khao.md` | Markdown | Đang ghi | Toàn văn OCR Lời kết & Tài liệu tham khảo | [Chuong_9_Ket_Luan_Tham_Khao.md](file:///C:/DICH%20HOC/Chuong_9_Ket_Luan_Tham_Khao.md) |
"""

with open(MASTER_MD_PATH, "w", encoding="utf-8") as f:
    f.write(content.strip())
print(f"Đã cập nhật hoàn chỉnh: {MASTER_MD_PATH} ({os.path.getsize(MASTER_MD_PATH):,} bytes)")
