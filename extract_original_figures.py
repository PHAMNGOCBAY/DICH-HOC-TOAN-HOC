import fitz
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

PDF_PATH = r"C:\DICH HOC\DICH HOC-TOANHOC-DOI SONG.pdf"
OUT_DIR = r"C:\DICH HOC\images_pdf"
os.makedirs(OUT_DIR, exist_ok=True)

# Danh sách các trang có hình minh họa/bảng quan trọng (PDF index 1-based)
KEY_PAGES = [
    (14, "hinh_01_ha_do_lac_thu_dong_ho", "Hà đồ, Lạc thư và đồng hồ 10 số (Trang sách 1)"),
    (29, "hinh_02_thai_cuc_do", "Đồ hình Thái cực và vòng tròn âm dương (Trang sách 16)"),
    (38, "hinh_03_tao_tu_tuong_bat_quai", "Tạo tượng và quái từ lưỡng nghi (Trang sách 25)"),
    (61, "hinh_04_bat_quai_tan_thien_lac_thu", "Bát quái Tân thiên trên Lạc thư (Trang sách 48)"),
    (67, "hinh_05_bat_quai_tan_thien_phuong_vi", "Phương vị Bát quái Tân thiên (Trang sách 54)"),
    (87, "hinh_06_do_tong_hop_qcc", "Đồ tổng hợp Quái - Can - Chi (Trang sách 74)"),
    (93, "hinh_07_thien_can_dia_chi_qcc", "Phân bố Thiên can Địa chi trên QCC (Trang sách 80)"),
    (157, "hinh_08_bang_26_bat_san", "Bảng 26: Tám san quái mệnh và quái trạch (Trang sách 144)"),
    (168, "hinh_09_bang_27_64_que_dich", "Bảng 27: 64 quẻ kinh dịch (Trang sách 155)"),
    (178, "hinh_10_vong_tron_64_que_phuc_hi", "Đồ hình 64 quẻ theo hệ nhị phân Phục Hi (Trang sách 165)"),
    (227, "hinh_11_bang_41_42_ma_so_dia_chi", "Bảng 41-42: Mã số Thiên can Địa chi Hà Lạc (Trang sách 214)"),
    (235, "hinh_12_xac_dinh_que_tien_thien", "Minh họa xác định quẻ Tiên thiên (Trang sách 222)")
]

doc = fitz.open(PDF_PATH)
print(f"Bắt đầu trích xuất ảnh minh chứng từ {PDF_PATH}...")

for page_num, filename, desc in KEY_PAGES:
    p_idx = page_num - 1
    page = doc.load_page(p_idx)
    # Render at 300 DPI for ultra clear archival quality
    pix = page.get_pixmap(dpi=300)
    out_file = os.path.join(OUT_DIR, f"{filename}.png")
    pix.save(out_file)
    print(f"  [Đã xuất] {filename}.png ({pix.width}x{pix.height}px) - {desc}")

print(f"\nHoàn thành trích xuất {len(KEY_PAGES)} hình ảnh minh chứng gốc độ phân giải cao 300 DPI.")
