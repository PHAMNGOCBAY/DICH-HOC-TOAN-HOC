# DỊCH HỌC DIỄN GIẢI TRÊN CƠ SỞ TOÁN HỌC VÀ ỨNG DỤNG VÀO ĐỜI SỐNG
### Tác giả: TS. Nguyễn Thế Cường (Nguyễn Quý Thế Cường)
**Nhà xuất bản Đại học Quốc gia Thành phố Hồ Chí Minh, 2014**  
**Mã số ISBN:** `978-604-73-2149-0` | **Tổng số trang:** 278 trang

---

## 1. Giới thiệu công trình
Dự án số hóa toàn văn, mô hình hóa toán học đại số và xây dựng cơ sở dữ liệu quan hệ cho công trình nghiên cứu khoa học của **TS. Nguyễn Thế Cường** (Cử nhân Vật lý ĐH Tổng hợp Minsk 1967, Tiến sĩ Toán - Lý ĐH Tổng hợp Leningrad 1973).

Hệ thống được chuyển đổi đa định dạng theo nguyên tắc học thuật:
- **Tuyệt đối không bịa đặt số liệu, không suy diễn chủ quan.**
- Đối chiếu số liệu đa nguồn từ nguyên bản tài liệu quét quang học.

---

## 2. Cấu trúc thư mục và Danh mục tệp tin

### 2.1. Báo cáo kỹ thuật tổng hợp
- [DICH_HOC_TOAN_HOC.md](DICH_HOC_TOAN_HOC.md): Báo cáo kỹ thuật đối chiếu 8 chương, nhúng toàn bộ minh chứng hình ảnh 300 DPI, bản vẽ CAD và bảng tra cứu toán học.

### 2.2. Số hóa toàn văn 10 phần (Full-Text OCR 278 trang)
1. [Chuong_0_Mo_Dau.md](Chuong_0_Mo_Dau.md): Lời mở đầu, thông tin xuất bản và mục lục nguyên bản (PDF p.1 - 13).
2. [Chuong_1_Co_So_Toan_Hoc.md](Chuong_1_Co_So_Toan_Hoc.md): Chương I - Cơ sở toán học của Bát quái, nhóm cộng Abel (Z/10Z, +), đồng hồ 10 vạch (PDF p.14 - 19).
3. [Chuong_2_Am_Duong_Thai_Cuc.md](Chuong_2_Am_Duong_Thai_Cuc.md): Chương II - Âm, dương và Thái cực; định luật Hợp hóa Can Chi (PDF p.20 - 36).
4. [Chuong_3_Tao_Quai_Tu_Luong_Nghi.md](Chuong_3_Tao_Quai_Tu_Luong_Nghi.md): Chương III - Trọng số năng lượng hào E = h1(±1) + h2(±3) + h3(±5), biến hào, đảo tượng (PDF p.37 - 60).
5. [Chuong_4_Bat_Quai_Tan_Thien.md](Chuong_4_Bat_Quai_Tan_Thien.md): Chương IV - Bát quái Tân thiên trên Lạc thư 3x3, đối xứng tâm, cặp phu thê (PDF p.61 - 86).
6. [Chuong_5_Do_Tong_Hop_QCC.md](Chuong_5_Do_Tong_Hop_QCC.md): Chương V - Đồ tổng hợp Quái - Can - Chi, phân bố tọa độ góc hoàng đạo (PDF p.87 - 103).
7. [Chuong_6_Ung_Dung_QCC.md](Chuong_6_Ung_Dung_QCC.md): Chương VI - Quái mệnh Nam/Nữ, Đông/Tây tứ trạch, ma trận 8x8 Bát san, tương hợp hôn nhân (PDF p.104 - 167).
8. [Chuong_7_Que_Dich.md](Chuong_7_Que_Dich.md): Chương VII - Hệ nhị phân Phục Hi, 64 quẻ kinh dịch, nạp chi Kinh Phòng 6 hào (PDF p.168 - 207).
9. [Chuong_8_Bat_Tu_Ha_Lac.md](Chuong_8_Bat_Tu_Ha_Lac.md): Chương VIII - Nhận dạng Bát tự Hà - Lạc toàn diện, quẻ Tiên thiên, Hậu thiên, Đại vận 6/9 năm (PDF p.208 - 265).
10. [Chuong_9_Ket_Luan_Tham_Khao.md](Chuong_9_Ket_Luan_Tham_Khao.md): Lời kết, 11 tài liệu tham khảo và mục lục cuối sách (PDF p.266 - 278).

### 2.3. Mã nguồn thuật toán & Cơ sở dữ liệu
- [dich_hoc_core.py](dich_hoc_core.py): Mô-đun thuật toán Python mô hình hóa đầy đủ 8 chương (nhóm Abel, hợp hóa, năng lượng hào, Bát san, nạp giáp, Bát tự Hà Lạc).
- [dich_hoc_data.json](dich_hoc_data.json): Cơ sở dữ liệu JSON cấu trúc chuẩn hóa cho toàn bộ tham số của cuốn sách.
- [dich_hoc_schema.sql](dich_hoc_schema.sql): Script DDL & DML 8 bảng quan hệ chuẩn ANSI SQL/SQLite.

### 2.4. Bản vẽ kỹ thuật CAD (AutoDesk .DXF) & Biểu đồ kỹ thuật
- [drawings/](drawings/):
  - `cad_dong_ho_ha_lac.dxf` & `.png`: Đồng hồ 10 vạch chia và nhóm cộng Hà - Lạc.
  - `cad_bat_quai_tan_thien.dxf` & `.png`: Bát quái Tân thiên trên ma trận Lạc thư 3x3.
  - `cad_ma_tran_bat_san.dxf` & `.png`: Bản vẽ ma trận 8x8 Bát san phân lớp Cát / Hung.
  - `chart_nang_luong_bat_quai.png`: Biểu đồ phổ năng lượng 8 quái theo trọng số hào.
  - `chart_quy_trinh_bat_tu_ha_lac.png`: Lưu trình thuật toán nhận dạng Bát tự Hà - Lạc.
  - `chart_dai_van_timeline.png`: Trục thời gian phân bổ Đại vận đời người (9 năm hào dương, 6 năm hào âm).
- [images_pdf/](images_pdf/): 12 hình ảnh minh chứng trích xuất trực tiếp từ các trang sách in ở độ phân giải cao 300 DPI.

---

## 3. Hướng dẫn chạy kiểm chứng
```bash
# 1. Chạy kiểm chứng toàn diện mô hình thuật toán Python
python dich_hoc_core.py

# 2. Sinh lại bản vẽ kỹ thuật CAD và biểu đồ
python generate_cad_and_charts.py
```
