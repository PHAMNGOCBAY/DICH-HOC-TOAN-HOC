import os
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DIR = r"C:\DICH HOC"

INSERTS = {
    "Chuong_1_Co_So_Toan_Hoc.md": [
        (
            r"## TRANG SÁCH 1 \(TRANG PDF 14\)",
            """## TRANG SÁCH 1 (TRANG PDF 14)

> [!NOTE]
> **HÌNH ẢNH MINH CHỨNG & BẢN VẼ KỸ THUẬT:**
> - Hình ảnh nguyên bản trong sách (Trang 1):  
>   ![Hà đồ Lạc thư và đồng hồ](file:///C:/DICH%20HOC/images_pdf/hinh_01_ha_do_lac_thu_dong_ho.png)
> - Bản vẽ kỹ thuật CAD (AutoDesk .DXF): [cad_dong_ho_ha_lac.dxf](file:///C:/DICH%20HOC/drawings/cad_dong_ho_ha_lac.dxf)  
>   ![Đồng hồ 10 vạch chia và nhóm cộng Hà Lạc](file:///C:/DICH%20HOC/drawings/cad_dong_ho_ha_lac.png)
"""
        )
    ],
    "Chuong_2_Am_Duong_Thai_Cuc.md": [
        (
            r"## TRANG SÁCH 16 \(TRANG PDF 29\)",
            """## TRANG SÁCH 16 (TRANG PDF 29)

> [!NOTE]
> **HÌNH ẢNH MINH CHỨNG NGUYÊN BẢN (TRANG 16):**  
> ![Đồ hình Thái cực và vòng tròn âm dương](file:///C:/DICH%20HOC/images_pdf/hinh_02_thai_cuc_do.png)
"""
        )
    ],
    "Chuong_3_Tao_Quai_Tu_Luong_Nghi.md": [
        (
            r"## TRANG SÁCH 25 \(TRANG PDF 38\)",
            """## TRANG SÁCH 25 (TRANG PDF 38)

> [!NOTE]
> **HÌNH ẢNH MINH CHỨNG & BIỂU ĐỒ NĂNG LƯỢNG:**
> - Hình ảnh nguyên bản trong sách (Trang 25):  
>   ![Tạo tượng và quái từ lưỡng nghi](file:///C:/DICH%20HOC/images_pdf/hinh_03_tao_tu_tuong_bat_quai.png)
> - Biểu đồ năng lượng 8 quái theo trọng số hào:  
>   ![Biểu đồ năng lượng Bát quái](file:///C:/DICH%20HOC/drawings/chart_nang_luong_bat_quai.png)
"""
        )
    ],
    "Chuong_4_Bat_Quai_Tan_Thien.md": [
        (
            r"## TRANG SÁCH 48 \(TRANG PDF 61\)",
            """## TRANG SÁCH 48 (TRANG PDF 61)

> [!NOTE]
> **HÌNH ẢNH MINH CHỨNG & BẢN VẼ KỸ THUẬT:**
> - Hình ảnh nguyên bản trong sách (Trang 48):  
>   ![Bát quái Tân thiên trên Lạc thư nguyên bản](file:///C:/DICH%20HOC/images_pdf/hinh_04_bat_quai_tan_thien_lac_thu.png)
> - Bản vẽ kỹ thuật CAD Lạc thư 3x3: [cad_bat_quai_tan_thien.dxf](file:///C:/DICH%20HOC/drawings/cad_bat_quai_tan_thien.dxf)  
>   ![Bát quái Tân thiên trên Lạc thư 3x3](file:///C:/DICH%20HOC/drawings/cad_bat_quai_tan_thien.png)
"""
        ),
        (
            r"## TRANG SÁCH 54 \(TRANG PDF 67\)",
            """## TRANG SÁCH 54 (TRANG PDF 67)

> [!NOTE]
> **HÌNH ẢNH NGUYÊN BẢN (TRANG 54):**  
> ![Phương vị Bát quái Tân thiên](file:///C:/DICH%20HOC/images_pdf/hinh_05_bat_quai_tan_thien_phuong_vi.png)
"""
        )
    ],
    "Chuong_5_Do_Tong_Hop_QCC.md": [
        (
            r"## TRANG SÁCH 74 \(TRANG PDF 87\)",
            """## TRANG SÁCH 74 (TRANG PDF 87)

> [!NOTE]
> **HÌNH ẢNH NGUYÊN BẢN (TRANG 74):**  
> ![Đồ tổng hợp Quái Can Chi](file:///C:/DICH%20HOC/images_pdf/hinh_06_do_tong_hop_qcc.png)
"""
        ),
        (
            r"## TRANG SÁCH 80 \(TRANG PDF 93\)",
            """## TRANG SÁCH 80 (TRANG PDF 93)

> [!NOTE]
> **HÌNH ẢNH NGUYÊN BẢN (TRANG 80):**  
> ![Phân bố Can Chi trên QCC](file:///C:/DICH%20HOC/images_pdf/hinh_07_thien_can_dia_chi_qcc.png)
"""
        )
    ],
    "Chuong_6_Ung_Dung_QCC.md": [
        (
            r"## TRANG SÁCH 144 \(TRANG PDF 157\)",
            """## TRANG SÁCH 144 (TRANG PDF 157)

> [!NOTE]
> **HÌNH ẢNH MINH CHỨNG & BẢN VẼ KỸ THUẬT:**
> - Bảng 26 nguyên bản trong sách (Trang 144):  
>   ![Bảng 26 Bát san](file:///C:/DICH%20HOC/images_pdf/hinh_08_bang_26_bat_san.png)
> - Bản vẽ kỹ thuật CAD Ma trận 8x8 Bát san: [cad_ma_tran_bat_san.dxf](file:///C:/DICH%20HOC/drawings/cad_ma_tran_bat_san.dxf)  
>   ![Ma trận Bát san 8x8](file:///C:/DICH%20HOC/drawings/cad_ma_tran_bat_san.png)
"""
        )
    ],
    "Chuong_7_Que_Dich.md": [
        (
            r"## TRANG SÁCH 155 \(TRANG PDF 168\)",
            """## TRANG SÁCH 155 (TRANG PDF 168)

> [!NOTE]
> **HÌNH ẢNH NGUYÊN BẢN (TRANG 155):**  
> ![Bảng 27 Danh mục 64 quẻ dịch](file:///C:/DICH%20HOC/images_pdf/hinh_09_bang_27_64_que_dich.png)
"""
        ),
        (
            r"## TRANG SÁCH 165 \(TRANG PDF 178\)",
            """## TRANG SÁCH 165 (TRANG PDF 178)

> [!NOTE]
> **HÌNH ẢNH NGUYÊN BẢN (TRANG 165):**  
> ![Vòng tròn 64 quẻ nhị phân Phục Hi](file:///C:/DICH%20HOC/images_pdf/hinh_10_vong_tron_64_que_phuc_hi.png)
"""
        )
    ],
    "Chuong_8_Bat_Tu_Ha_Lac.md": [
        (
            r"## TRANG SÁCH 214 \(TRANG PDF 227\)",
            """## TRANG SÁCH 214 (TRANG PDF 227)

> [!NOTE]
> **HÌNH ẢNH NGUYÊN BẢN (TRANG 214):**  
> ![Bảng 41-42 mã số can chi](file:///C:/DICH%20HOC/images_pdf/hinh_11_bang_41_42_ma_so_dia_chi.png)
"""
        ),
        (
            r"## TRANG SÁCH 222 \(TRANG PDF 235\)",
            """## TRANG SÁCH 222 (TRANG PDF 235)

> [!NOTE]
> **HÌNH ẢNH NGUYÊN BẢN & SƠ ĐỒ THUẬT TOÁN:**
> - Minh họa xác định quẻ Tiên thiên (Trang 222):  
>   ![Minh họa xác định quẻ Tiên thiên](file:///C:/DICH%20HOC/images_pdf/hinh_12_xac_dinh_que_tien_thien.png)
> - Sơ đồ quy trình thuật toán Bát tự Hà Lạc:  
>   ![Quy trình thuật toán Bát tự Hà Lạc](file:///C:/DICH%20HOC/drawings/chart_quy_trinh_bat_tu_ha_lac.png)
> - Biểu đồ trục thời gian phân bổ Đại vận:  
>   ![Timeline Đại vận](file:///C:/DICH%20HOC/drawings/chart_dai_van_timeline.png)
"""
        )
    ]
}

def main():
    print("Bắt đầu nhúng hình ảnh, bản vẽ CAD và biểu đồ vào từng file chương tương ứng...")
    for filename, patterns in INSERTS.items():
        file_path = os.path.join(DIR, filename)
        if not os.path.exists(file_path):
            print(f"  [Bỏ qua] Không tìm thấy file {filename}")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        modified = False
        for pattern, replacement in patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content, count=1)
                modified = True
            else:
                print(f"  [Cảnh báo] Không tìm thấy pattern '{pattern}' trong {filename}")
                
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  [Đã nhúng thành công] {filename} ({os.path.getsize(file_path):,} bytes)")

if __name__ == "__main__":
    main()
