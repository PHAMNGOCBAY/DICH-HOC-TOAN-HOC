import os
import sys
import io
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy, ColorPolicy
from ezdxf.enums import TextEntityAlignment

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

OUTPUT_DIR = r"C:\DICH HOC\drawings"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def setup_dxf_document():
    doc = ezdxf.new("R2010", setup=True)
    doc.styles.new("VN_TEXT", dxfattribs={"font": "arial.ttf"})
    doc.styles.new("VN_BOLD", dxfattribs={"font": "arialbd.ttf"})
    
    # Lớp nét vẽ chuẩn màu kỹ thuật
    l_khung = doc.layers.add("KHUNG", color=7)
    l_khung.rgb = (0, 0, 0)
    l_net = doc.layers.add("NET_CHINH", color=7)
    l_net.rgb = (0, 0, 0)
    l_tieu_de = doc.layers.add("TIEU_DE", color=7)
    l_tieu_de.rgb = (0, 0, 0)
    l_chu_thich = doc.layers.add("CHU_THICH", color=7)
    l_chu_thich.rgb = (0, 0, 0)
    
    l_cat = doc.layers.add("SAN_CAT", color=3)
    l_cat.rgb = (21, 128, 61) # Xanh lục đậm chuẩn kỹ thuật
    l_hung = doc.layers.add("SAN_HUNG", color=1)
    l_hung.rgb = (185, 28, 28) # Đỏ đậm
    l_duong = doc.layers.add("HAO_DUONG", color=1)
    l_duong.rgb = (185, 28, 28)
    l_am = doc.layers.add("HAO_AM", color=2)
    l_am.rgb = (217, 119, 6) # Màu vàng kỹ thuật sắc nét trên nền trắng (chuẩn skill cad-color-blue-to-yellow)
    return doc

def export_dxf_to_png(doc, dxf_path, png_path, dpi=300):
    doc.saveas(dxf_path)
    fig = plt.figure(figsize=(16, 12), dpi=dpi, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#FFFFFF')
    ctx = RenderContext(doc)
    cfg = Configuration(background_policy=BackgroundPolicy.WHITE, color_policy=ColorPolicy.COLOR)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out, config=cfg).draw_layout(doc.modelspace(), finalize=True)
    fig.savefig(png_path, dpi=dpi, facecolor='#FFFFFF', edgecolor='none')
    plt.close(fig)
    print(f"  [Đã xuất Bản vẽ Tương tác Gia đình] {os.path.basename(png_path)} ({os.path.getsize(png_path):,} bytes)")

def draw_family_relationship():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_moi_quan_he_gia_dinh.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_moi_quan_he_gia_dinh.png")
    doc = setup_dxf_document()
    msp = doc.modelspace()
    
    # =========================================================================
    # 1. TIÊU ĐỀ BẢN VẼ VÀ KHUNG BAO NGOÀI
    # =========================================================================
    # Khung biên ngoài
    msp.add_line((-148, 120), (148, 120), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((148, 120), (148, -120), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((148, -120), (-148, -120), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((-148, -120), (-148, 120), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    
    msp.add_text("BẢN VẼ KỸ THUẬT: ĐỒ HÌNH NĂNG LƯỢNG & TƯƠNG TÁC GIA ĐÌNH 4 THÀNH VIÊN", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.8}).set_placement((-144, 112))
    msp.add_text("Cơ sở toán học: Nhóm cộng Hà - Lạc, Bát quái Tân thiên & Véctơ gia mệnh (TS. Nguyễn Thế Cường, NXB ĐHQG TP.HCM)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.3}).set_placement((-144, 105))
    
    msp.add_line((-148, 101), (148, 101), dxfattribs={"layer": "KHUNG", "lineweight": 20})

    # =========================================================================
    # 2. KHỐI I: SƠ ĐỒ MẠNG TƯƠNG TÁC 4 THÀNH VIÊN (TRÁI: x = -144 đến -10, y = 97 đến -26)
    # =========================================================================
    msp.add_line((-144, 97), (-10, 97), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-10, 97), (-10, -26), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-10, -26), (-144, -26), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-144, -26), (-144, 97), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("I. SƠ ĐỒ MẠNG LIÊN KẾT TƯƠNG TÁC GIA ĐÌNH", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 3.0}).set_placement((-140, 91))
    msp.add_text("(Thiên can ngũ hợp, Địa chi lục hợp và Bát san tương phối)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.1}).set_placement((-140, 86))

    # --- HỘP 4 THÀNH VIÊN ---
    # Node 1: Người 1 (Bố - Tốn Mộc)
    # Box: x = -138 đến -88, y = 82 đến 48 (Width 50, Height 34)
    msp.add_line((-138, 82), (-88, 82), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-88, 82), (-88, 48), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-88, 48), (-138, 48), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-138, 48), (-138, 82), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_text("NGƯỜI 1: BỐ (Nam - 1984)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.5}).set_placement((-135, 75))
    msp.add_text("Năm sinh: Giáp Tý (Dương nam)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.0}).set_placement((-135, 69))
    msp.add_text("Quái: TỐN (Âm Mộc, E = +7)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 2.2}).set_placement((-135, 63))
    msp.add_text("Trạch mệnh: ĐÔNG TỨ MỆNH", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 2.0}).set_placement((-135, 57))
    msp.add_text("Tượng quái: Phong (Gió)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.9}).set_placement((-135, 51))

    # Node 2: Người 2 (Mẹ - Khôn Thổ)
    # Box: x = -62 đến -12, y = 82 đến 48 (Width 50, Height 34)
    msp.add_line((-62, 82), (-12, 82), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-12, 82), (-12, 48), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-12, 48), (-62, 48), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-62, 48), (-62, 82), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_text("NGƯỜI 2: MẸ (Nữ - 1985)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.5}).set_placement((-59, 75))
    msp.add_text("Năm sinh: Ất Sửu (Âm nữ)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.0}).set_placement((-59, 69))
    msp.add_text("Quái: KHÔN (Âm Thổ, E = -9)", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 2.2}).set_placement((-59, 63))
    msp.add_text("Trạch mệnh: TÂY TỨ MỆNH", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 2.0}).set_placement((-59, 57))
    msp.add_text("Tượng quái: Địa (Đất)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.9}).set_placement((-59, 51))

    # Node 4: Người 4 (Con 2 - Chấn Mộc)
    # Box: x = -138 đến -88, y = 20 đến -14 (Width 50, Height 34)
    msp.add_line((-138, 20), (-88, 20), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-88, 20), (-88, -14), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-88, -14), (-138, -14), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-138, -14), (-138, 20), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_text("NGƯỜI 4: CON 2 (Nam - 2019)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.5}).set_placement((-135, 13))
    msp.add_text("Năm sinh: Kỷ Hợi (Âm nam)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.0}).set_placement((-135, 7))
    msp.add_text("Quái: CHẤN (Âm Mộc, E = -7)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 2.2}).set_placement((-135, 1))
    msp.add_text("Trạch mệnh: ĐÔNG TỨ MỆNH", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 2.0}).set_placement((-135, -5))
    msp.add_text("Tượng quái: Lôi (Sấm sét)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.9}).set_placement((-135, -11))

    # Node 3: Người 3 (Con 1 - Cấn Thổ)
    # Box: x = -62 đến -12, y = 20 đến -14 (Width 50, Height 34)
    msp.add_line((-62, 20), (-12, 20), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-12, 20), (-12, -14), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-12, -14), (-62, -14), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-62, -14), (-62, 20), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_text("NGƯỜI 3: CON 1 (Nam - 2014)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.5}).set_placement((-59, 13))
    msp.add_text("Năm sinh: Giáp Ngọ (Dương nam)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.0}).set_placement((-59, 7))
    msp.add_text("Quái: CẤN (Dương Thổ, E = +1)", dxfattribs={"layer": "HAO_DUONG", "style": "VN_BOLD", "height": 2.2}).set_placement((-59, 1))
    msp.add_text("Trạch mệnh: TÂY TỨ MỆNH", dxfattribs={"layer": "HAO_DUONG", "style": "VN_BOLD", "height": 2.0}).set_placement((-59, -5))
    msp.add_text("Tượng quái: Sơn (Núi đá)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.9}).set_placement((-59, -11))

    # --- ĐƯỜNG LIÊN KẾT TƯƠNG TÁC ---
    # 1. Liên kết Bố <---> Mẹ (Ngang trên: y = 65, từ x = -88 đến -62)
    msp.add_line((-88, 67), (-62, 67), dxfattribs={"layer": "SAN_CAT", "lineweight": 30})
    msp.add_line((-88, 63), (-62, 63), dxfattribs={"layer": "SAN_HUNG", "lineweight": 20})
    msp.add_text("Tý - Sửu: LỤC HỢP", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((-75, 70), align=TextEntityAlignment.MIDDLE_CENTER)
    msp.add_text("Tốn - Khôn: Ngũ quỷ", dxfattribs={"layer": "SAN_HUNG", "style": "VN_BOLD", "height": 1.7}).set_placement((-75, 59), align=TextEntityAlignment.MIDDLE_CENTER)

    # 2. Liên kết Bố <---> Con 2 (Dọc trái: x = -113, từ y = 48 đến 20)
    msp.add_line((-113, 48), (-113, 20), dxfattribs={"layer": "SAN_CAT", "lineweight": 35})
    msp.add_text("Giáp - Kỷ: CAN HỢP", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((-116, 36), align=TextEntityAlignment.MIDDLE_RIGHT)
    msp.add_text("Tốn - Chấn: DIÊN NIÊN", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((-116, 31), align=TextEntityAlignment.MIDDLE_RIGHT)

    # 3. Liên kết Mẹ <---> Con 1 (Dọc phải: x = -37, từ y = 48 đến 20)
    msp.add_line((-37, 48), (-37, 20), dxfattribs={"layer": "SAN_CAT", "lineweight": 35})
    msp.add_text("Khôn - Cấn: SINH KHÍ", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((-34, 36), align=TextEntityAlignment.MIDDLE_LEFT)
    msp.add_text("(Phu thê Tân thiên)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.6}).set_placement((-34, 31), align=TextEntityAlignment.MIDDLE_LEFT)

    # 4. Liên kết Con 2 <---> Con 1 (Ngang dưới: y = 3, từ x = -88 đến -62)
    msp.add_line((-88, 5), (-62, 5), dxfattribs={"layer": "SAN_CAT", "lineweight": 30})
    msp.add_line((-88, 1), (-62, 1), dxfattribs={"layer": "SAN_HUNG", "lineweight": 20})
    msp.add_text("Giáp - Kỷ: CAN HỢP", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((-75, 8), align=TextEntityAlignment.MIDDLE_CENTER)
    msp.add_text("Chấn - Cấn: Lục sát", dxfattribs={"layer": "SAN_HUNG", "style": "VN_TEXT", "height": 1.7}).set_placement((-75, -3), align=TextEntityAlignment.MIDDLE_CENTER)

    # 5. Hai đường chéo tương tác
    msp.add_line((-88, 48), (-62, 20), dxfattribs={"layer": "SAN_HUNG", "lineweight": 15})
    msp.add_line((-62, 48), (-88, 20), dxfattribs={"layer": "SAN_HUNG", "lineweight": 15})
    
    # Huy hiệu trung tâm cân bằng đối xứng
    msp.add_circle((-75, 34), 8.5, dxfattribs={"layer": "KHUNG", "lineweight": 25})
    msp.add_text("CÂN BẰNG", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 1.8}).set_placement((-75, 36.5), align=TextEntityAlignment.MIDDLE_CENTER)
    msp.add_text("2 ĐÔNG : 2 TÂY", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.7}).set_placement((-75, 32.5), align=TextEntityAlignment.MIDDLE_CENTER)

    # =========================================================================
    # 3. KHỐI II: MA TRẬN BÁT SAN 4x4 & THỐNG KÊ TOÁN HỌC (PHẢI: x = -4 đến 144, y = 97 đến -26)
    # =========================================================================
    msp.add_line((-4, 97), (144, 97), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((144, 97), (144, -26), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((144, -26), (-4, -26), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-4, -26), (-4, 97), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("II. MA TRẬN BÁT SAN 4x4 & CÂN BẰNG NĂNG LƯỢNG GIA ĐÌNH", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.8}).set_placement((4, 91))
    msp.add_text("(Đánh giá tương tác định lượng theo Hà - Lạc & Bát quái Tân thiên)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.0}).set_placement((4, 86))

    # Bảng Ma trận Bát san 4x4 (x từ 2 đến 138, y từ 82 đến 42)
    col_x = [2, 28, 55, 82, 110, 138]
    row_y = [82, 74, 66, 58, 50, 42]
    
    for x in col_x:
        msp.add_line((x, 82), (x, 42), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    for y in row_y:
        msp.add_line((2, y), (138, y), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
        
    headers_col = ["Đối tượng", "Bố (Tốn)", "Mẹ (Khôn)", "Con 1 (Cấn)", "Con 2 (Chấn)"]
    for i, h in enumerate(headers_col):
        cx = (col_x[i] + col_x[i+1]) / 2.0
        msp.add_text(h, dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 1.9}).set_placement((cx, 77.5), align=TextEntityAlignment.MIDDLE_CENTER)
        
    matrix_data = [
        ("Bố (Tốn)", [("Phục vị", False, True), ("Ngũ quỷ", True, False), ("Tuyệt mệnh", True, False), ("DIÊN NIÊN", False, True)]),
        ("Mẹ (Khôn)", [("Ngũ quỷ", True, False), ("Phục vị", False, True), ("SINH KHÍ", False, True), ("Họa hại", True, False)]),
        ("Con 1 (Cấn)", [("Tuyệt mệnh", True, False), ("SINH KHÍ", False, True), ("Phục vị", False, True), ("Lục sát", True, False)]),
        ("Con 2 (Chấn)", [("DIÊN NIÊN", False, True), ("Họa hại", True, False), ("Lục sát", True, False), ("Phục vị", False, True)]),
    ]
    
    for r_idx, (r_name, row_cells) in enumerate(matrix_data):
        cy = (row_y[r_idx+1] + row_y[r_idx+2]) / 2.0
        cx0 = (col_x[0] + col_x[1]) / 2.0
        msp.add_text(r_name, dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 1.8}).set_placement((cx0, cy), align=TextEntityAlignment.MIDDLE_CENTER)
        
        for c_idx, (val, is_hung, is_cat) in enumerate(row_cells):
            cx = (col_x[c_idx+1] + col_x[c_idx+2]) / 2.0
            layer = "SAN_CAT" if is_cat else ("SAN_HUNG" if is_hung else "CHU_THICH")
            style = "VN_BOLD" if (is_cat or is_hung) else "VN_TEXT"
            msp.add_text(val, dxfattribs={"layer": layer, "style": style, "height": 1.8}).set_placement((cx, cy), align=TextEntityAlignment.MIDDLE_CENTER)

    # Thống kê toán học bên dưới bảng (ngắt dòng hợp lý, tuyệt đối không tràn lề)
    msp.add_text("1. Đối xứng Trạch mệnh: 2 Đông tứ (Bố, Con 2) : 2 Tây tứ (Mẹ, Con 1) -> Tỷ lệ 1:1 cân bằng hoàn hảo.", 
                 dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.9}).set_placement((2, 34))
    msp.add_text("2. Cân bằng Ngũ hành Quái: 2 Mộc (Tốn E=+7, Chấn E=-7) đối ứng với 2 Thổ (Khôn E=-9, Cấn E=+1).", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((2, 28))
    msp.add_text("3. Tổng năng lượng Quái: E_tong = (+7) + (-9) + (+1) + (-7) = -8 (Âm nhu, chủ về tích lũy nội lực).", 
                 dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 1.8}).set_placement((2, 22))
    msp.add_text("4. Lực liên kết cốt lõi: 2 cặp Can ngũ hợp (Giáp-Kỷ) và 1 cặp Chi lục hợp (Tý-Sửu hóa Thổ) giữ vững gia đạo.", 
                 dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((2, 16))
    msp.add_text("5. Hai cặp tương thích tuyệt hảo: Bố - Con 2 đạt Diên niên cát; Mẹ - Con 1 đạt Sinh khí đại cát.", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((2, 10))
    msp.add_text("6. Cơ chế hóa giải: Sức hút Lục hợp và Can ngũ hợp trung hòa các quan hệ hung sát Bát san.", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((2, 4))

    # =========================================================================
    # 4. KHỐI III: QUY HOẠCH KHÔNG GIAN DƯƠNG TRẠCH & KHUYẾN NGHỊ HÓA GIẢI (DƯỚI: y = -30 đến -116)
    # =========================================================================
    msp.add_line((-144, -30), (144, -30), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((144, -30), (144, -116), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((144, -116), (-144, -116), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-144, -116), (-144, -30), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("III. QUY HOẠCH KHÔNG GIAN DƯƠNG TRẠCH & GIẢI PHÁP HÓA GIẢI THEO PHÂN VÙNG CÔNG NĂNG", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 3.4}).set_placement((-140, -36))

    # Chia 3 cột công năng
    # Cột 1: x = -140 đến -48
    msp.add_line((-140, -40), (-48, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((-48, -40), (-48, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((-48, -112), (-140, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((-140, -112), (-140, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    
    msp.add_text("1. PHÂN KHU ĐÔNG TỨ TRẠCH (BỐ & CON 2)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.3}).set_placement((-137, -45))
    msp.add_text("- Đối tượng: Bố (Tốn Mộc) & Con 2 (Chấn Mộc)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.9}).set_placement((-137, -51))
    msp.add_text("- Hướng Cát ưu tiên:", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 1.9}).set_placement((-137, -57))
    msp.add_text("  + CHÍNH BẮC (Sinh khí Tốn / Thiên y Chấn)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-137, -63))
    msp.add_text("  + CHÍNH NAM (Thiên y Tốn / Sinh khí Chấn)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-137, -69))
    msp.add_text("  + CHÍNH ĐÔNG & ĐÔNG NAM (Diên niên / Phục vị)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-137, -75))
    msp.add_text("- Bố trí công năng: Phòng làm việc của Bố, phòng ngủ", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-137, -82))
    msp.add_text("  và bàn học của Con 2 hướng về Bắc hoặc Nam.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-137, -88))
    msp.add_text("- Màu sắc & vật liệu: Xanh lá cây, xanh nước biển, đen;", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-137, -95))
    msp.add_text("  bổ trợ đồ gỗ tự nhiên và cây cảnh lọc không khí.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-137, -101))

    # Cột 2: x = -44 đến 48
    msp.add_line((-44, -40), (48, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((48, -40), (48, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((48, -112), (-44, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((-44, -112), (-44, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    
    msp.add_text("2. PHÂN KHU TÂY TỨ TRẠCH (MẸ & CON 1)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.3}).set_placement((-41, -45))
    msp.add_text("- Đối tượng: Mẹ (Khôn Thổ) & Con 1 (Cấn Thổ)", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 1.9}).set_placement((-41, -51))
    msp.add_text("- Hướng Cát ưu tiên:", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 1.9}).set_placement((-41, -57))
    msp.add_text("  + TÂY BẮC (Diên niên Khôn / Thiên y Cấn)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-41, -63))
    msp.add_text("  + TÂY NAM (Phục vị Khôn / Sinh khí Cấn)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-41, -69))
    msp.add_text("  + ĐÔNG BẮC & CHÍNH TÂY (Sinh khí / Thiên y)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-41, -75))
    msp.add_text("- Bố trí công năng: Khu vực nghỉ ngơi của Mẹ, phòng", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-41, -82))
    msp.add_text("  ngủ và bàn học Con 1 nhìn về Tây Bắc / Tây Nam.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-41, -88))
    msp.add_text("- Màu sắc & vật liệu: Vàng đất, nâu ấm, cam pastel, đỏ;", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-41, -95))
    msp.add_text("  ưu tiên vật liệu gốm sứ, đá granite, ánh sáng vàng ấm.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-41, -101))

    # Cột 3: x = 52 đến 140
    msp.add_line((52, -40), (140, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((140, -40), (140, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((140, -112), (52, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((52, -112), (52, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    
    msp.add_text("3. NGUYÊN TẮC HÒA GIẢI & BẾP NẤU DÙNG CHUNG", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.3}).set_placement((55, -45))
    msp.add_text("- Cửa chính căn nhà: Đặt theo hướng Cát của chủ sự", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.9}).set_placement((55, -51))
    msp.add_text("  kinh tế chính (Bố: chọn Nam/Bắc; hoặc Mẹ: Tây Bắc).", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((55, -57))
    msp.add_text("- Bếp nấu (Tọa hung hướng cát):", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.9}).set_placement((55, -64))
    msp.add_text("  + Đặt tại cung xấu của gia chủ để thiêu đốt hung khí.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((55, -70))
    msp.add_text("  + Miệng bếp ngoảnh về hướng Cát để đón sinh khí.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((55, -76))
    msp.add_text("- Phòng khách & Trung cung: Giữ không gian thông thoáng,", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((55, -83))
    msp.add_text("  dùng làm vùng đệm điều hòa trường khí Mộc - Thổ.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((55, -89))
    msp.add_text("- Đánh giá tổng quan: Gia đình 2 Đông - 2 Tây có tính", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((55, -96))
    msp.add_text("  bổ trợ đa diện, vững bền và linh hoạt trong cuộc sống.", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((55, -102))

    export_dxf_to_png(doc, dxf_path, png_path)

if __name__ == "__main__":
    print("Bắt đầu vẽ bản vẽ kỹ thuật CAD Mối quan hệ Gia đình 4 người (tinh chỉnh)...")
    draw_family_relationship()
    print("Hoàn tất 100% xuất bản vẽ CAD và hình ảnh PNG.")
