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

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

OUTPUT_DIR = r"C:\DICH HOC\drawings"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def setup_dxf_document():
    doc = ezdxf.new("R2010", setup=True)
    # Khởi tạo Text Style hỗ trợ 100% tiếng Việt Unicode UTF-8
    doc.styles.new("VN_TEXT", dxfattribs={"font": "arial.ttf"})
    doc.styles.new("VN_BOLD", dxfattribs={"font": "arialbd.ttf"})
    
    # Thiết lập các Layer kỹ thuật chuẩn
    doc.layers.add("KHUNG_BAN_VE", color=7)      # Màu đen/trắng tiêu chuẩn
    doc.layers.add("DUONG_NET_CHINH", color=7)
    doc.layers.add("HAO_DUONG", color=1)         # Màu đỏ kỹ thuật
    doc.layers.add("HAO_AM", color=5)            # Màu xanh dương
    doc.layers.add("SAN_CAT", color=3)           # Màu xanh lá cây (Cát)
    doc.layers.add("SAN_HUNG", color=1)          # Màu đỏ (Hung)
    doc.layers.add("CHU_THICH", color=7)
    doc.layers.add("TIEU_DE", color=7)
    return doc

def export_dxf_to_png(doc, dxf_path, png_path, dpi=300):
    doc.saveas(dxf_path)
    fig = plt.figure(figsize=(12, 10), dpi=dpi, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#FFFFFF')
    ctx = RenderContext(doc)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
    fig.savefig(png_path, dpi=dpi, facecolor='#FFFFFF', edgecolor='none')
    plt.close(fig)
    print(f"  [Đã xuất CAD 2D có dấu tiếng Việt] {os.path.basename(png_path)} ({os.path.getsize(png_path):,} bytes)")

# 1. BẢN VẼ 1: BÁT QUÁI TÂN THIÊN 2D TIẾNG VIỆT ĐẦY ĐỦ DẤU
def draw_bat_quai_tan_thien_vn():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_bat_quai_tan_thien_vn.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_bat_quai_tan_thien_vn.png")
    doc = setup_dxf_document()
    msp = doc.modelspace()
    
    cell_w, cell_h = 75.0, 75.0
    x_min, y_min = -112.5, -112.5
    
    # Khung ma trận 3x3
    for i in range(4):
        y = y_min + i * cell_h
        msp.add_line((x_min, y), (x_min + 3*cell_w, y), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 30})
        x = x_min + i * cell_w
        msp.add_line((x, y_min), (x, y_min + 3*cell_h), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 30})
        
    # Tiêu đề bản vẽ
    msp.add_text("BẢN VẼ KỸ THUẬT: BÁT QUÁI TÂN THIÊN TRÊN MA TRẬN LẠC THƯ 3x3", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 6.5}).set_placement((-110, 128))
    msp.add_text("Tác phẩm: Dịch học diễn giải trên cơ sở toán học - TS. Nguyễn Thế Cường (NXB ĐHQG TP.HCM)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.2}).set_placement((-110, 120))
    
    # 9 ô theo cấu trúc Bát quái Tân thiên (Chương IV)
    # Hàng 1 (trên - Chính Nam): Tốn (4), Càn (9), Cấn (2)
    # Hàng 2 (giữa): Li (3), Thái Cực (5), Khảm (7)
    # Hàng 3 (dưới - Chính Bắc): Đoài (8), Khôn (1), Chấn (6)
    cells = [
        # (r, c, ten, so_lac_thu, tri_so, lines_yang, phuong_vi, ngu_hanh)
        (0, 0, "TỐN", 4, "+7", [0, 1, 1], "Đông Nam", "Mộc"),
        (0, 1, "CÀN", 9, "+9", [1, 1, 1], "Chính Nam", "Kim"),
        (0, 2, "CẤN", 2, "+1", [0, 0, 1], "Tây Nam", "Thổ"),
        (1, 0, "LI", 3, "+3", [1, 0, 1], "Chính Đông", "Hỏa"),
        (1, 1, "THÁI CỰC", 5, "0", None, "Trung Cung", "Bản Thể"),
        (1, 2, "KHẢM", 7, "-3", [0, 1, 0], "Chính Tây", "Thủy"),
        (2, 0, "ĐOÀI", 8, "-1", [1, 1, 0], "Đông Bắc", "Kim"),
        (2, 1, "KHÔN", 1, "-9", [0, 0, 0], "Chính Bắc", "Thổ"),
        (2, 2, "CHẤN", 6, "-7", [1, 0, 0], "Tây Bắc", "Mộc")
    ]
    
    for r, c, name, num, val, lines, direction, hanh in cells:
        cx = x_min + c * cell_w + cell_w / 2.0
        cy = y_min + (2 - r) * cell_h + cell_h / 2.0
        
        # Số Lạc thư góc trên trái ô
        msp.add_text(f"Cung {num}", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 5}).set_placement((cx - 32, cy + 24))
        # Tên quái ở giữa trên
        msp.add_text(f"{name}", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 7}).set_placement((cx - 10, cy + 23))
        # Trị số năng lượng E và Ngũ hành
        msp.add_text(f"E = {val} ({hanh})", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.5}).set_placement((cx - 24, cy - 25))
        # Phương vị
        msp.add_text(f"Hướng: {direction}", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.0}).set_placement((cx - 26, cy - 32))
        
        # Vẽ các hào
        if lines:
            lw = 36.0
            gap = 6.5
            for l_idx, is_yang in enumerate(lines):
                ly = cy - 10 + l_idx * gap
                if is_yang == 1:
                    # Hào dương: thanh liền màu đỏ
                    msp.add_line((cx - lw/2, ly), (cx + lw/2, ly), dxfattribs={"layer": "HAO_DUONG", "lineweight": 40})
                else:
                    # Hào âm: hai thanh đứt màu xanh dương
                    half = (lw - 6.0) / 2.0
                    msp.add_line((cx - lw/2, ly), (cx - lw/2 + half, ly), dxfattribs={"layer": "HAO_AM", "lineweight": 40})
                    msp.add_line((cx + lw/2 - half, ly), (cx + lw/2, ly), dxfattribs={"layer": "HAO_AM", "lineweight": 40})
        else:
            # Trung cung Thái Cực: Vẽ 2 vòng tròn đồng tâm
            msp.add_circle((cx, cy), 14, dxfattribs={"layer": "DUONG_NET_CHINH", "lineweight": 30})
            msp.add_circle((cx, cy), 5, dxfattribs={"layer": "HAO_DUONG", "lineweight": 20})
            msp.add_text("Thái Cực (e = 0)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4}).set_placement((cx - 16, cy - 2))
            
    # Chú thích chân bản vẽ
    msp.add_text("Ghi chú: Hào dương vẽ nét liền (đỏ), hào âm vẽ nét đứt (xanh).", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((-110, -122))
    msp.add_text("Các cặp quái đối xứng qua tâm: Càn(9) - Khôn(1), Li(3) - Khảm(7), Tốn(4) - Chấn(6), Cấn(2) - Đoài(8).", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((-110, -128))
    
    export_dxf_to_png(doc, dxf_path, png_path)

# 2. BẢN VẼ 2: MA TRẬN 8x8 BÁT SAN 2D TIẾNG VIỆT ĐẦY ĐỦ DẤU
def draw_bat_san_vn():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_ma_tran_bat_san_vn.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_ma_tran_bat_san_vn.png")
    doc = setup_dxf_document()
    msp = doc.modelspace()
    
    quais = ["Càn", "Đoài", "Khôn", "Cấn", "Li", "Chấn", "Khảm", "Tốn"]
    matrix_data = [
        ["Phục vị", "Sinh khí", "Diên niên", "Thiên y", "Tuyệt mệnh", "Ngũ quỷ", "Lục sát", "Họa hại"],
        ["Sinh khí", "Phục vị", "Thiên y", "Diên niên", "Ngũ quỷ", "Tuyệt mệnh", "Họa hại", "Lục sát"],
        ["Diên niên", "Thiên y", "Phục vị", "Sinh khí", "Lục sát", "Họa hại", "Tuyệt mệnh", "Ngũ quỷ"],
        ["Thiên y", "Diên niên", "Sinh khí", "Phục vị", "Họa hại", "Lục sát", "Ngũ quỷ", "Tuyệt mệnh"],
        ["Tuyệt mệnh", "Ngũ quỷ", "Lục sát", "Họa hại", "Phục vị", "Sinh khí", "Diên niên", "Thiên y"],
        ["Ngũ quỷ", "Tuyệt mệnh", "Họa hại", "Lục sát", "Sinh khí", "Phục vị", "Thiên y", "Diên niên"],
        ["Lục sát", "Họa hại", "Tuyệt mệnh", "Ngũ quỷ", "Diên niên", "Thiên y", "Phục vị", "Sinh khí"],
        ["Họa hại", "Lục sát", "Ngũ quỷ", "Tuyệt mệnh", "Thiên y", "Diên niên", "Sinh khí", "Phục vị"]
    ]
    cat_set = {"Sinh khí", "Thiên y", "Diên niên", "Phục vị"}
    
    cw = 24.0
    ch = 13.0
    x0 = -105.0
    y0 = 65.0
    
    # Tiêu đề
    msp.add_text("BẢNG 26: MA TRẬN 8x8 BÁT SAN (QUÁI TRẠCH PHỐI QUÁI MỆNH)", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 6.0}).set_placement((x0 - 20, y0 + 22))
    msp.add_text("Định lượng Dịch học: 4 cung Cát (Sinh khí, Thiên y, Diên niên, Phục vị) - 4 cung Hung (Tuyệt mệnh, Ngũ quỷ, Lục sát, Họa hại)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((x0 - 20, y0 + 15))
    
    # Vẽ lưới
    for i in range(10):
        y = y0 - i * ch
        msp.add_line((x0 - 28, y), (x0 + 8 * cw, y), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    for j in range(10):
        x = x0 - 28 if j == 0 else x0 + (j - 1) * cw
        msp.add_line((x, y0), (x, y0 - 9 * ch), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
        
    # Tiêu đề góc
    msp.add_text("Trạch \\ Mệnh", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 3.8}).set_placement((x0 - 26, y0 - 9))
    
    # Header cột (Mệnh)
    for j, q in enumerate(quais):
        msp.add_text(f"M.{q}", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.2}).set_placement((x0 + j*cw + 4, y0 - 9))
        
    # Header hàng (Trạch) và nội dung ô
    for i, q in enumerate(quais):
        msp.add_text(f"Tr.{q}", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.2}).set_placement((x0 - 25, y0 - (i+1)*ch - 9))
        for j in range(8):
            san_val = matrix_data[i][j]
            is_cat = san_val in cat_set
            layer = "SAN_CAT" if is_cat else "SAN_HUNG"
            msp.add_text(san_val, dxfattribs={"layer": layer, "style": "VN_TEXT", "height": 3.6}).set_placement((x0 + j*cw + 2, y0 - (i+1)*ch - 9))
            
    # Ghi chú
    msp.add_text("Màu xanh lá: Cung Cát (Tốt) | Màu đỏ: Cung Hung (Xấu). Đối chiếu nguyên bản trang 144.", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((x0 - 20, y0 - 10*ch - 2))
    
    export_dxf_to_png(doc, dxf_path, png_path)

# 3. BẢN VẼ 3: PHÂN TÍCH TƯƠNG HỢP HÔN NHÂN 2D CÓ DẤU TIẾNG VIỆT (NAM 1984 - NỮ 1985)
def draw_hon_nhan_2d_vn():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_hon_nhan_ton_khon_vn.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_hon_nhan_ton_khon_vn.png")
    doc = setup_dxf_document()
    msp = doc.modelspace()
    
    # Tiêu đề
    msp.add_text("SƠ ĐỒ KỸ THUẬT PHÂN TÍCH HÔN NHÂN THEO DỊCH HỌC VÀ BÁT SAN", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 6.5}).set_placement((-120, 95))
    msp.add_text("Đối tượng: Người 1 (Nam sinh 05-10-1984, Giáp Tý) phối Người 2 (Nữ sinh 05-10-1985, Ất Sửu)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.5}).set_placement((-120, 87))
    
    # Khung bao Chồng (Tốn) bên trái: x = -90 đến -20
    msp.add_line((-95, 75), (-20, 75), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    msp.add_line((-20, 75), (-20, -50), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    msp.add_line((-20, -50), (-95, -50), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    msp.add_line((-95, -50), (-95, 75), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    
    msp.add_text("NGƯỜI 1: CHỒNG", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 5.5}).set_placement((-85, 66))
    msp.add_text("- Năm sinh: 05-10-1984 (Giáp Tý)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((-90, 58))
    msp.add_text("- Quái mệnh: TỐN (Cung Lạc thư 4)", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 4.2}).set_placement((-90, 51))
    msp.add_text("- Ngũ hành: Âm Mộc (Đông tứ mệnh)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((-90, 44))
    msp.add_text("- Mức năng lượng: E = +7", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((-90, 37))
    
    # Khung bao Vợ (Khôn) bên phải: x = 20 đến 95
    msp.add_line((20, 75), (95, 75), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    msp.add_line((95, 75), (95, -50), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    msp.add_line((95, -50), (20, -50), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    msp.add_line((20, -50), (20, 75), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    
    msp.add_text("NGƯỜI 2: VỢ", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 5.5}).set_placement((30, 66))
    msp.add_text("- Năm sinh: 05-10-1985 (Ất Sửu)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((25, 58))
    msp.add_text("- Quái mệnh: KHÔN (Cung Lạc thư 1)", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 4.2}).set_placement((25, 51))
    msp.add_text("- Ngũ hành: Âm Thổ (Tây tứ mệnh)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((25, 44))
    msp.add_text("- Mức năng lượng: E = -9", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((25, 37))
    
    # Vẽ các hào đối chiếu
    y_lines = [20.0, 0.0, -20.0]  # Hào 3 (thượng), Hào 2 (trung), Hào 1 (sơ)
    labels = ["HÀO 3 (Thượng hào)", "HÀO 2 (Trung hào)", "HÀO 1 (Sơ hào)"]
    interactions = [
        ("Dương (+) phối Âm (-)", "Khác tính: LỰC HÚT XÃ HỘI", "SAN_CAT"),
        ("Dương (+) phối Âm (-)", "Khác tính: LỰC HÚT TÂM LÝ", "SAN_CAT"),
        ("Âm (-) phối Âm (-)", "Cùng tính: LỰC ĐẨY NỀN TẢNG", "SAN_HUNG")
    ]
    
    # Hào của Tốn: (Hào 1: Âm, Hào 2: Dương, Hào 3: Dương) -> y_lines index 2, 1, 0
    ton_lines = [1, 1, 0] # hào 3, 2, 1
    khon_lines = [0, 0, 0]
    
    for idx in range(3):
        y = y_lines[idx]
        is_yang_ton = ton_lines[idx]
        is_yang_khon = khon_lines[idx]
        
        # Vẽ hào Tốn
        if is_yang_ton:
            msp.add_line((-80, y), (-35, y), dxfattribs={"layer": "HAO_DUONG", "lineweight": 45})
        else:
            msp.add_line((-80, y), (-60, y), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
            msp.add_line((-55, y), (-35, y), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
            
        # Vẽ hào Khôn
        if is_yang_khon:
            msp.add_line((35, y), (80, y), dxfattribs={"layer": "HAO_DUONG", "lineweight": 45})
        else:
            msp.add_line((35, y), (55, y), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
            msp.add_line((60, y), (80, y), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
            
        # Vẽ đường kết nối tương tác ở giữa
        desc1, desc2, layer_color = interactions[idx]
        msp.add_line((-20, y), (20, y), dxfattribs={"layer": layer_color, "lineweight": 25})
        msp.add_text(labels[idx], dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 3.4}).set_placement((-18, y + 4.5))
        msp.add_text(desc2, dxfattribs={"layer": layer_color, "style": "VN_BOLD", "height": 3.0}).set_placement((-18, y - 5.5))
        
    # Khung kết luận tổng hợp ở đáy
    msp.add_line((-120, -60), (120, -60), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    msp.add_line((120, -60), (120, -110), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    msp.add_line((120, -110), (-120, -110), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    msp.add_line((-120, -110), (-120, -60), dxfattribs={"layer": "KHUNG_BAN_VE", "lineweight": 20})
    
    msp.add_text("KẾT LUẬN ĐỐI CHIẾU DỊCH HỌC:", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.8}).set_placement((-115, -69))
    msp.add_text("1. Quan hệ Bát san: TỐN gặp KHÔN tạo thành NGŨ QUỶ (Mộc khắc Thổ, thuộc nhóm 4 cung Hung).", 
                 dxfattribs={"layer": "SAN_HUNG", "style": "VN_BOLD", "height": 4.0}).set_placement((-115, -77))
    msp.add_text("2. Điểm nâng đỡ: Địa chi TÝ (1984) và SỬU (1985) thuộc LỤC HỢP (Tý - Sửu nhị hợp hóa Thổ), tạo sự gắn kết thực tế.", 
                 dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 4.0}).set_placement((-115, -85))
    msp.add_text("3. Biện pháp điều hòa: Hướng nhà chính chọn hướng SINH KHÍ (Chính Bắc); bếp xoay hướng Li (Chính Nam, Hỏa) làm cầu nối Mộc sinh Hỏa -> Hỏa sinh Thổ.", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((-115, -95))
    msp.add_text("4. Hai quẻ kinh dịch hình thành: Quẻ số 20 'Phong địa Quán' và Quẻ số 46 'Địa phong Thăng'.", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.8}).set_placement((-115, -103))
    
    export_dxf_to_png(doc, dxf_path, png_path)

def main():
    print("Bắt đầu sinh 3 bản vẽ kỹ thuật CAD 2D có đầy đủ dấu tiếng Việt Unicode...")
    draw_bat_quai_tan_thien_vn()
    draw_bat_san_vn()
    draw_hon_nhan_2d_vn()
    print("Hoàn tất 100% xuất bản vẽ CAD 2D (*.dxf) và ảnh (*.png) tiếng Việt có dấu.")

if __name__ == "__main__":
    main()
