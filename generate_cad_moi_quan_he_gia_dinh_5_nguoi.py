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
    l_am.rgb = (217, 119, 6) # Màu vàng hổ phách chuẩn skill cad-color-blue-to-yellow
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
    print(f"  [Đã xuất Bản vẽ Gia đình 5 người] {os.path.basename(png_path)} ({os.path.getsize(png_path):,} bytes)")

def draw_family_5_relationship():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_moi_quan_he_gia_dinh_5_nguoi.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_moi_quan_he_gia_dinh_5_nguoi.png")
    doc = setup_dxf_document()
    msp = doc.modelspace()
    
    # =========================================================================
    # 1. TIÊU ĐỀ BẢN VẼ VÀ KHUNG BAO NGOÀI
    # =========================================================================
    msp.add_line((-148, 120), (148, 120), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((148, 120), (148, -120), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((148, -120), (-148, -120), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((-148, -120), (-148, 120), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    
    msp.add_text("BẢN VẼ KỸ THUẬT: ĐỒ HÌNH NĂNG LƯỢNG & TƯƠNG TÁC GIA ĐÌNH 5 THÀNH VIÊN", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.6}).set_placement((-144, 112))
    msp.add_text("Cơ sở toán học: Nhóm cộng Hà - Lạc, Bát quái Tân thiên & Véctơ gia mệnh (TS. Nguyễn Thế Cường, NXB ĐHQG TP.HCM)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-144, 105))
    
    msp.add_line((-148, 101), (148, 101), dxfattribs={"layer": "KHUNG", "lineweight": 20})

    # =========================================================================
    # 2. KHỐI I: SƠ ĐỒ MẠNG TƯƠNG TÁC 5 THÀNH VIÊN (TRÁI: x = -144 đến -10, y = 97 đến -26)
    # =========================================================================
    msp.add_line((-144, 97), (-10, 97), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-10, 97), (-10, -26), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-10, -26), (-144, -26), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-144, -26), (-144, 97), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("I. SƠ ĐỒ MẠNG LIÊN KẾT TƯƠNG TÁC 5 THÀNH VIÊN", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 3.0}).set_placement((-140, 91))
    msp.add_text("(Phân định 3 thế hệ: Bà ngoại - Bố Mẹ - Con cái, Can Chi ngũ hợp và Bát san tương phối)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.0}).set_placement((-140, 86))

    # --- HỘP 5 THÀNH VIÊN (Kích thước mỗi hộp: Width = 46, Height = 25) ---
    # Node 1: Bà ngoại (Nữ - 1965, Ất Tị) - Quái ĐOÀI
    # Box đỉnh giữa: x = -99 đến -53, y = 84 đến 59
    msp.add_line((-99, 84), (-53, 84), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-53, 84), (-53, 59), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-53, 59), (-99, 59), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-99, 59), (-99, 84), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_text("BÀ NGOẠI: NỮ (1965)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.2}).set_placement((-96, 78))
    msp.add_text("Năm sinh: Ất Tị (Âm nữ)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-96, 73))
    msp.add_text("Quái: ĐOÀI (Âm Kim, E = -1)", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 2.0}).set_placement((-96, 68))
    msp.add_text("TÂY TỨ MỆNH | Trạch (Đầm)", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 1.7}).set_placement((-96, 62))

    # Node 2: Bố (Nam - 1984, Giáp Tý) - Quái TỐN
    # Box tầng giữa trái: x = -140 đến -94, y = 53 đến 28
    msp.add_line((-140, 53), (-94, 53), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-94, 53), (-94, 28), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-94, 28), (-140, 28), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-140, 28), (-140, 53), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_text("BỐ: NAM (1984)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.2}).set_placement((-137, 47))
    msp.add_text("Năm sinh: Giáp Tý (Dương nam)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-137, 42))
    msp.add_text("Quái: TỐN (Âm Mộc, E = +7)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 2.0}).set_placement((-137, 37))
    msp.add_text("ĐÔNG TỨ MỆNH | Phong (Gió)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.7}).set_placement((-137, 31))

    # Node 3: Mẹ (Nữ - 1985, Ất Sửu) - Quái KHÔN
    # Box tầng giữa phải: x = -58 đến -12, y = 53 đến 28
    msp.add_line((-58, 53), (-12, 53), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-12, 53), (-12, 28), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-12, 28), (-58, 28), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-58, 28), (-58, 53), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_text("MẸ: NỮ (1985)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.2}).set_placement((-55, 47))
    msp.add_text("Năm sinh: Ất Sửu (Âm nữ)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-55, 42))
    msp.add_text("Quái: KHÔN (Âm Thổ, E = -9)", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 2.0}).set_placement((-55, 37))
    msp.add_text("TÂY TỨ MỆNH | Địa (Đất)", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 1.7}).set_placement((-55, 31))

    # Node 4: Con 2 (Nam - 2019, Kỷ Hợi) - Quái CHẤN
    # Box tầng dưới trái: x = -140 đến -94, y = 14 đến -11
    msp.add_line((-140, 14), (-94, 14), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-94, 14), (-94, -11), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-94, -11), (-140, -11), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-140, -11), (-140, 14), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_text("CON 2: NAM (2019)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.2}).set_placement((-137, 8))
    msp.add_text("Năm sinh: Kỷ Hợi (Âm nam)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-137, 3))
    msp.add_text("Quái: CHẤN (Âm Mộc, E = -7)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 2.0}).set_placement((-137, -2))
    msp.add_text("ĐÔNG TỨ MỆNH | Lôi (Sấm)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.7}).set_placement((-137, -8))

    # Node 5: Con 1 (Nam - 2014, Giáp Ngọ) - Quái CẤN
    # Box tầng dưới phải: x = -58 đến -12, y = 14 đến -11
    msp.add_line((-58, 14), (-12, 14), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-12, 14), (-12, -11), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-12, -11), (-58, -11), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_line((-58, -11), (-58, 14), dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_text("CON 1: NAM (2014)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.2}).set_placement((-55, 8))
    msp.add_text("Năm sinh: Giáp Ngọ (Dương nam)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.8}).set_placement((-55, 3))
    msp.add_text("Quái: CẤN (Dương Thổ, E = +1)", dxfattribs={"layer": "HAO_DUONG", "style": "VN_BOLD", "height": 2.0}).set_placement((-55, -2))
    msp.add_text("TÂY TỨ MỆNH | Sơn (Núi)", dxfattribs={"layer": "HAO_DUONG", "style": "VN_BOLD", "height": 1.7}).set_placement((-55, -8))

    # --- ĐƯỜNG LIÊN KẾT TƯƠNG TÁC ĐẶC BIỆT ---
    # 1. Bà ngoại <---> Mẹ (Nối từ (-63, 59) đến (-45, 53))
    msp.add_line((-63, 59), (-45, 53), dxfattribs={"layer": "SAN_CAT", "lineweight": 35})
    msp.add_text("BÀ - MẸ: THIÊN Y (Thổ sinh Kim)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.7}).set_placement((-38, 57), align=TextEntityAlignment.BOTTOM_CENTER)
    msp.add_text("Tị - Sửu Bán tam hợp", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.5}).set_placement((-38, 54), align=TextEntityAlignment.BOTTOM_CENTER)

    # 2. Bà ngoại <---> Bố (Nối từ (-89, 59) đến (-107, 53))
    msp.add_line((-89, 59), (-107, 53), dxfattribs={"layer": "SAN_HUNG", "lineweight": 20})
    msp.add_text("BÀ - RỂ: Lục sát", dxfattribs={"layer": "SAN_HUNG", "style": "VN_TEXT", "height": 1.6}).set_placement((-114, 55), align=TextEntityAlignment.BOTTOM_CENTER)

    # 3. Bố <---> Mẹ (Ngang giữa: y = 40.5, x từ -94 đến -58, rộng 36 units)
    msp.add_line((-94, 42.5), (-58, 42.5), dxfattribs={"layer": "SAN_CAT", "lineweight": 30})
    msp.add_line((-94, 38.5), (-58, 38.5), dxfattribs={"layer": "SAN_HUNG", "lineweight": 20})
    msp.add_text("Tý - Sửu: LỤC HỢP", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.7}).set_placement((-76, 45.5), align=TextEntityAlignment.MIDDLE_CENTER)
    msp.add_text("Tốn - Khôn: Ngũ quỷ", dxfattribs={"layer": "SAN_HUNG", "style": "VN_TEXT", "height": 1.5}).set_placement((-76, 35.5), align=TextEntityAlignment.MIDDLE_CENTER)

    # 4. Bố <---> Con 2 (Dọc trái: x = -117, từ y = 28 đến 14)
    msp.add_line((-117, 28), (-117, 14), dxfattribs={"layer": "SAN_CAT", "lineweight": 35})
    msp.add_text("Giáp - Kỷ: CAN HỢP", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.6}).set_placement((-119, 23), align=TextEntityAlignment.MIDDLE_RIGHT)
    msp.add_text("Diên niên cát", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.5}).set_placement((-119, 19), align=TextEntityAlignment.MIDDLE_RIGHT)

    # 5. Mẹ <---> Con 1 (Dọc phải: x = -35, từ y = 28 đến 14)
    msp.add_line((-35, 28), (-35, 14), dxfattribs={"layer": "SAN_CAT", "lineweight": 35})
    msp.add_text("Khôn - Cấn: SINH KHÍ", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.6}).set_placement((-33, 23), align=TextEntityAlignment.MIDDLE_LEFT)
    msp.add_text("(Phu thê Tân thiên)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.4}).set_placement((-33, 19), align=TextEntityAlignment.MIDDLE_LEFT)

    # 6. Con 2 <---> Con 1 (Ngang dưới: y = 1.5, x từ -94 đến -58)
    msp.add_line((-94, 3.5), (-58, 3.5), dxfattribs={"layer": "SAN_CAT", "lineweight": 30})
    msp.add_line((-94, -0.5), (-58, -0.5), dxfattribs={"layer": "SAN_HUNG", "lineweight": 20})
    msp.add_text("Giáp - Kỷ: CAN HỢP", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.6}).set_placement((-76, 6.5), align=TextEntityAlignment.MIDDLE_CENTER)
    msp.add_text("Chấn - Cấn: Lục sát", dxfattribs={"layer": "SAN_HUNG", "style": "VN_TEXT", "height": 1.5}).set_placement((-76, -3.5), align=TextEntityAlignment.MIDDLE_CENTER)

    # Huy hiệu trung tâm cân bằng đối xứng
    msp.add_circle((-76, 21.0), 6.5, dxfattribs={"layer": "KHUNG", "lineweight": 25})
    msp.add_text("CÂN BẰNG", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 1.6}).set_placement((-76, 23.2), align=TextEntityAlignment.MIDDLE_CENTER)
    msp.add_text("2 ĐÔNG : 3 TÂY", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.5}).set_placement((-76, 19.2), align=TextEntityAlignment.MIDDLE_CENTER)

    # =========================================================================
    # 3. KHỐI II: MA TRẬN BÁT SAN 5x5 & THỐNG KÊ TOÁN HỌC (PHẢI: x = -4 đến 144, y = 97 đến -26)
    # =========================================================================
    msp.add_line((-4, 97), (144, 97), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((144, 97), (144, -26), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((144, -26), (-4, -26), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-4, -26), (-4, 97), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("II. MA TRẬN BÁT SAN 5x5 & CÂN BẰNG NĂNG LƯỢNG GIA ĐÌNH", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.8}).set_placement((4, 91))
    msp.add_text("(Đánh giá tương tác định lượng toàn diện theo Nhóm cộng Hà - Lạc)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.0}).set_placement((4, 86))

    # Bảng Ma trận Bát san 5x5 (x từ 0 đến 140, y từ 82 đến 34)
    col_x = [0, 24, 47, 70, 93, 117, 140]
    row_y = [82, 74, 66, 58, 50, 42, 34]
    
    for x in col_x:
        msp.add_line((x, 82), (x, 34), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    for y in row_y:
        msp.add_line((0, y), (140, y), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
        
    headers_col = ["Đối tượng", "Bà (Đoài)", "Bố (Tốn)", "Mẹ (Khôn)", "Con 1 (Cấn)", "Con 2 (Chấn)"]
    for i, h in enumerate(headers_col):
        cx = (col_x[i] + col_x[i+1]) / 2.0
        msp.add_text(h, dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 1.7}).set_placement((cx, 77.5), align=TextEntityAlignment.MIDDLE_CENTER)
        
    matrix_data = [
        ("Bà (Đoài)", [("Phục vị", False, True), ("Lục sát", True, False), ("THIÊN Y", False, True), ("DIÊN NIÊN", False, True), ("Tuyệt mệnh", True, False)]),
        ("Bố (Tốn)", [("Lục sát", True, False), ("Phục vị", False, True), ("Ngũ quỷ", True, False), ("Tuyệt mệnh", True, False), ("DIÊN NIÊN", False, True)]),
        ("Mẹ (Khôn)", [("THIÊN Y", False, True), ("Ngũ quỷ", True, False), ("Phục vị", False, True), ("SINH KHÍ", False, True), ("Họa hại", True, False)]),
        ("Con 1 (Cấn)", [("DIÊN NIÊN", False, True), ("Tuyệt mệnh", True, False), ("SINH KHÍ", False, True), ("Phục vị", False, True), ("Lục sát", True, False)]),
        ("Con 2 (Chấn)", [("Tuyệt mệnh", True, False), ("DIÊN NIÊN", False, True), ("Họa hại", True, False), ("Lục sát", True, False), ("Phục vị", False, True)]),
    ]
    
    for r_idx, (r_name, row_cells) in enumerate(matrix_data):
        cy = (row_y[r_idx+1] + row_y[r_idx+2]) / 2.0
        cx0 = (col_x[0] + col_x[1]) / 2.0
        msp.add_text(r_name, dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 1.7}).set_placement((cx0, cy), align=TextEntityAlignment.MIDDLE_CENTER)
        
        for c_idx, (val, is_hung, is_cat) in enumerate(row_cells):
            cx = (col_x[c_idx+1] + col_x[c_idx+2]) / 2.0
            layer = "SAN_CAT" if is_cat else ("SAN_HUNG" if is_hung else "CHU_THICH")
            style = "VN_BOLD" if (is_cat or is_hung) else "VN_TEXT"
            msp.add_text(val, dxfattribs={"layer": layer, "style": style, "height": 1.6}).set_placement((cx, cy), align=TextEntityAlignment.MIDDLE_CENTER)

    # Thống kê toán học bên dưới bảng
    msp.add_text("1. Phân bổ Trạch mệnh: 2 Đông tứ (Bố, Con 2) : 3 Tây tứ (Mẹ, Con 1, Bà ngoại) -> Nghiêng 60% Tây tứ.", 
                 dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((2, 27))
    msp.add_text("2. Cơ cấu Ngũ hành: 2 Mộc (Tốn E=+7, Chấn E=-7) + 2 Thổ (Khôn E=-9, Cấn E=+1) + 1 Kim (Đoài E=-1).", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((2, 21))
    msp.add_text("3. Tổng năng lượng gia mệnh: E_tong = (+7) + (-9) + (+1) + (-7) + (-1) = -9 (Âm tính, tụ khí dưỡng thân).", 
                 dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 1.7}).set_placement((2, 15))
    msp.add_text("4. Tương sinh cốt lõi: Mẹ (Khôn Thổ) dưỡng Bà (Đoài Kim) đạt THIÊN Y THƯỢNG CÁT; Tị - Sửu bán tam hợp.", 
                 dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.7}).set_placement((2, 9))
    msp.add_text("5. Bà - Cháu tương hợp: Bà ngoại (Đoài Kim) phối Con 1 (Cấn Thổ) đạt DIÊN NIÊN CÁT (Thổ sinh Kim hiếu thuận).", 
                 dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.7}).set_placement((2, 3))
    msp.add_text("6. Điểm lưu ý cơ học: Bà ngoại (Đoài Kim) và Con 2 (Chấn Mộc) Tuyệt mệnh & Tị - Hợi xung -> Cách ly tiếng ồn.", 
                 dxfattribs={"layer": "SAN_HUNG", "style": "VN_BOLD", "height": 1.7}).set_placement((2, -3))
    msp.add_text("7. Cơ chế hóa giải: Sức hút Can hợp (Giáp-Kỷ) và Chi hợp (Tý-Sửu, Tị-Sửu) giữ vững khối gia đạo bền chặt.", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((2, -9))
    msp.add_text("8. Kết luận hình thế: Gia đình 5 người có đủ Kim - Mộc - Thổ; Kim của Bà kiềm tỏa bớt tính xung bộc của Mộc.", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((2, -15))
    msp.add_text("9. Trọng tâm phong thủy: An trí Bà ngoại tại cung Tây Nam (Thiên y dưỡng thọ) để đón nguồn khí phục hồi.", 
                 dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.7}).set_placement((2, -21))

    # =========================================================================
    # 4. KHỐI III: QUY HOẠCH KHÔNG GIAN DƯƠNG TRẠCH 5 NGƯỜI (DƯỚI: y = -30 đến -116)
    # =========================================================================
    msp.add_line((-144, -30), (144, -30), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((144, -30), (144, -116), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((144, -116), (-144, -116), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-144, -116), (-144, -30), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("III. QUY HOẠCH KHÔNG GIAN DƯƠNG TRẠCH & KHUYẾN NGHỊ BỐ TRÍ CÔNG NĂNG 5 THÀNH VIÊN", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 3.4}).set_placement((-140, -36))

    # Chia 3 cột công năng
    # Cột 1: x = -140 đến -48
    msp.add_line((-140, -40), (-48, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((-48, -40), (-48, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((-48, -112), (-140, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((-140, -112), (-140, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    
    msp.add_text("1. PHÂN KHU ĐÔNG TỨ TRẠCH (BỐ & CON 2)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.2}).set_placement((-137, -45))
    msp.add_text("- Đối tượng: Bố (Tốn Mộc) & Con 2 (Chấn Mộc)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((-137, -51))
    msp.add_text("- Hướng Cát ưu tiên:", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 1.8}).set_placement((-137, -57))
    msp.add_text("  + CHÍNH BẮC (Sinh khí Tốn / Thiên y Chấn)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-137, -63))
    msp.add_text("  + CHÍNH NAM (Thiên y Tốn / Sinh khí Chấn)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-137, -69))
    msp.add_text("  + CHÍNH ĐÔNG & ĐÔNG NAM (Diên niên / Phục vị)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-137, -75))
    msp.add_text("- Bố trí công năng: Phòng làm việc của Bố và phòng", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-137, -82))
    msp.add_text("  ngủ của Con 2 hướng Bắc hoặc Nam.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-137, -88))
    msp.add_text("- Lưu ý Con 2: Khu vui chơi vận động của Con 2 cần", dxfattribs={"layer": "SAN_HUNG", "style": "VN_BOLD", "height": 1.7}).set_placement((-137, -95))
    msp.add_text("  cách âm tốt, tránh đặt sát vách phòng Bà ngoại.", dxfattribs={"layer": "SAN_HUNG", "style": "VN_BOLD", "height": 1.7}).set_placement((-137, -101))

    # Cột 2: x = -44 đến 48
    msp.add_line((-44, -40), (48, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((48, -40), (48, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((48, -112), (-44, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((-44, -112), (-44, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    
    msp.add_text("2. PHÂN KHU TÂY TỨ TRẠCH (MẸ, CON 1 & BÀ)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.2}).set_placement((-41, -45))
    msp.add_text("- Đối tượng: Mẹ (Khôn), Con 1 (Cấn), Bà ngoại (Đoài)", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 1.8}).set_placement((-41, -51))
    msp.add_text("- Hướng Cát chung Tây tứ trạch:", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 1.8}).set_placement((-41, -57))
    msp.add_text("  + TÂY BẮC (Sinh khí Đoài / Diên niên Khôn)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-41, -63))
    msp.add_text("  + TÂY NAM (Thiên y Đoài / Phục vị Khôn)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-41, -69))
    msp.add_text("  + ĐÔNG BẮC (Diên niên Đoài / Sinh khí Khôn)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-41, -75))
    msp.add_text("- Bố trí công năng: Phòng ngủ của Mẹ, phòng học Con 1", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-41, -82))
    msp.add_text("  và phòng nghỉ Bà ngoại liền kề nhau để dễ hỗ trợ.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-41, -88))
    msp.add_text("- Màu sắc & vật liệu: Vàng đất, nâu ấm, trắng, xám nhạt;", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-41, -95))
    msp.add_text("  ánh sáng ấm áp, gốm sứ và kim loại trang nhã.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((-41, -101))

    # Cột 3: x = 52 đến 140
    msp.add_line((52, -40), (140, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((140, -40), (140, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((140, -112), (52, -112), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    msp.add_line((52, -112), (52, -40), dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
    
    msp.add_text("3. PHÒNG DƯỠNG THỌ BÀ NGOẠI & HÓA GIẢI", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 2.2}).set_placement((55, -45))
    msp.add_text("- Vị trí phòng Bà ngoại ưu tiên số 1: TÂY NAM", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((55, -51))
    msp.add_text("  (Cung Thiên y của Đoài Kim, dưỡng thân thọ mệnh).", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((55, -57))
    msp.add_text("- Thiết kế không gian người cao tuổi:", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 1.7}).set_placement((55, -63))
    msp.add_text("  + Tầng trệt (hoặc có thang máy), không bậc tam cấp.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((55, -69))
    msp.add_text("  + Thông gió tự nhiên, đón ánh sáng ban mai dịu nhẹ.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((55, -75))
    msp.add_text("- Bếp nấu dùng chung (Tọa hung hướng cát):", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.8}).set_placement((55, -82))
    msp.add_text("  + Tọa Đông/Đông Nam nhìn về Tây Bắc/Tây Nam.", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((55, -88))
    msp.add_text("- Trung cung & Phòng sinh hoạt chung: Giữ thanh tịnh,", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.7}).set_placement((55, -95))
    msp.add_text("  gắn kết ba thế hệ đầm ấm, hiếu thuận và an lạc.", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 1.7}).set_placement((55, -101))

    export_dxf_to_png(doc, dxf_path, png_path)

if __name__ == "__main__":
    print("Bắt đầu vẽ bản vẽ kỹ thuật CAD Mối quan hệ Gia đình 5 người (chuẩn hóa tỷ lệ)...")
    draw_family_5_relationship()
    print("Hoàn tất 100% xuất bản vẽ CAD và hình ảnh PNG.")
