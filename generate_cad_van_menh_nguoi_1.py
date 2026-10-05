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
    doc.styles.new("VN_TEXT", dxfattribs={"font": "arial.ttf"})
    doc.styles.new("VN_BOLD", dxfattribs={"font": "arialbd.ttf"})
    
    l_khung = doc.layers.add("KHUNG", color=7)
    l_khung.rgb = (0, 0, 0)
    l_net = doc.layers.add("NET_CHINH", color=7)
    l_net.rgb = (0, 0, 0)
    l_tieu_de = doc.layers.add("TIEU_DE", color=7)
    l_tieu_de.rgb = (0, 0, 0)
    l_chu_thich = doc.layers.add("CHU_THICH", color=7)
    l_chu_thich.rgb = (0, 0, 0)
    
    l_cat = doc.layers.add("SAN_CAT", color=3)
    l_cat.rgb = (21, 128, 61)
    l_hung = doc.layers.add("SAN_HUNG", color=1)
    l_hung.rgb = (185, 28, 28)
    l_duong = doc.layers.add("HAO_DUONG", color=1)
    l_duong.rgb = (185, 28, 28)
    l_am = doc.layers.add("HAO_AM", color=2)
    l_am.rgb = (217, 119, 6)
    return doc

from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy, ColorPolicy

def export_dxf_to_png(doc, dxf_path, png_path, dpi=300):
    doc.saveas(dxf_path)
    fig = plt.figure(figsize=(14, 11), dpi=dpi, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#FFFFFF')
    ctx = RenderContext(doc)
    cfg = Configuration(background_policy=BackgroundPolicy.WHITE, color_policy=ColorPolicy.COLOR)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out, config=cfg).draw_layout(doc.modelspace(), finalize=True)
    fig.savefig(png_path, dpi=dpi, facecolor='#FFFFFF', edgecolor='none')
    plt.close(fig)
    print(f"  [Đã xuất Bản vẽ Vận mệnh Người 1] {os.path.basename(png_path)} ({os.path.getsize(png_path):,} bytes)")

from ezdxf.enums import TextEntityAlignment

def draw_van_menh_nguoi_1():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_van_menh_nguoi_1.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_van_menh_nguoi_1.png")
    doc = setup_dxf_document()
    msp = doc.modelspace()
    
    # 1. TIÊU ĐỀ BẢN VẼ VÀ KHUNG BAO TOÀN CẢNH
    msp.add_text("BẢN VẼ KỸ THUẬT: ĐỒ HÌNH VẬN MỆNH & PHONG THỦY BÁT TRẠCH - NGƯỜI 1", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 7.0}).set_placement((-140, 115))
    msp.add_text("Cơ sở toán học: Nhóm cộng Hà - Lạc & Bát quái Tân thiên (TS. Nguyễn Thế Cường, NXB ĐHQG TP.HCM)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.5}).set_placement((-140, 107))
    
    # Khung biên bản vẽ
    msp.add_line((-145, 125), (145, 125), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((145, 125), (145, -125), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((145, -125), (-145, -125), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((-145, -125), (-145, 125), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    
    # 2. KHỐI THÔNG TIN BÁT TỰ & QUÁI MỆNH (GÓC TRÊN TRÁI: x = -140 đến 12, y = 98 đến 20)
    msp.add_line((-140, 98), (12, 98), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((12, 98), (12, 20), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((12, 20), (-140, 20), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-140, 20), (-140, 98), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("I. THÔNG TIN BÁT TỰ & BẢN MỆNH", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 5.0}).set_placement((-135, 90))
    msp.add_text("- Ngày sinh DL: 05-10-1984 (Thứ Sáu)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.0}).set_placement((-135, 82))
    msp.add_text("- Ngày sinh ÂL: Ngày 11 tháng 9 năm Giáp Tý", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.0}).set_placement((-135, 74))
    msp.add_text("- Trụ Năm: GIÁP TÝ (Hạ nguyên, Dương nam)", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 4.0}).set_placement((-135, 66))
    msp.add_text("- Trụ Tháng: GIÁP TUẤT | Trụ Ngày: NHÂM THÂN", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.0}).set_placement((-135, 58))
    msp.add_text("- QUÁI MỆNH: TỐN (Cung Lạc thư 4)", dxfattribs={"layer": "HAO_DUONG", "style": "VN_BOLD", "height": 4.5}).set_placement((-135, 50))
    msp.add_text("- Ngũ hành: Âm Mộc | Mệnh quái: Đông tứ mệnh", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.0}).set_placement((-135, 42))
    msp.add_text("- Trị số năng lượng: E = +7 (Dương thịnh)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.0}).set_placement((-135, 34))
    msp.add_text("- Cặp phu thê Tân thiên: KHẢM (Chính Tây)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.0}).set_placement((-135, 26))

    # 3. KHỐI CẤU TRÚC HÀO QUÁI TỐN (GÓC DƯỚI TRÁI: x = -140 đến 12, y = 10 đến -50)
    msp.add_line((-140, 10), (12, 10), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((12, 10), (12, -50), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((12, -50), (-140, -50), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-140, -50), (-140, 10), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("II. CẤU TRÚC 3 HÀO QUÁI TỐN", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 5.0}).set_placement((-135, 2))
    
    # Hào 3 (Thượng): Dương (+5)
    msp.add_line((-135, -8), (-105, -8), dxfattribs={"layer": "HAO_DUONG", "lineweight": 45})
    msp.add_text("Hào 3 (Thượng): Dương (+5) - Hậu vận vững vàng", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.4}).set_placement((-100, -9.5))
    
    # Hào 2 (Trung): Dương (+3)
    msp.add_line((-135, -20), (-105, -20), dxfattribs={"layer": "HAO_DUONG", "lineweight": 45})
    msp.add_text("Hào 2 (Trung): Dương (+3) - Trung vận thịnh vượng", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.4}).set_placement((-100, -21.5))
    
    # Hào 1 (Sơ): Âm (-1) (hai đoạn đứt - MÀU VÀNG)
    msp.add_line((-135, -32), (-122, -32), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
    msp.add_line((-118, -32), (-105, -32), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
    msp.add_text("Hào 1 (Sơ): Âm (-1) - Tiền vận cần tích lũy", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 3.4}).set_placement((-100, -33.5))
    
    msp.add_text("Công thức năng lượng: E = (-1) + (+3) + (+5) = +7", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 3.8}).set_placement((-135, -44))

    # 4. KHỐI ĐỒ HÌNH BÁT TRẠCH LA BÀN 8 HƯỚNG CỦA QUÁI TỐN (BÊN PHẢI: tâm tại x = 76, y = 24)
    ox, oy = 76.0, 24.0
    R_in = 18.0
    R_mid = 36.0
    R_out = 54.0
    
    msp.add_circle((ox, oy), R_in, dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_circle((ox, oy), R_mid, dxfattribs={"layer": "NET_CHINH", "lineweight": 20})
    msp.add_circle((ox, oy), R_out, dxfattribs={"layer": "KHUNG", "lineweight": 30})
    
    # Nhãn trung tâm
    msp.add_text("MỆNH TỐN", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.5}).set_placement((ox, oy + 3.2), align=TextEntityAlignment.MIDDLE_CENTER)
    msp.add_text("Âm Mộc (E=+7)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.0}).set_placement((ox, oy - 3.2), align=TextEntityAlignment.MIDDLE_CENTER)
    
    directions_data = [
        # (angle_deg, phuong_huong, ten_san, is_cat, y_nghia)
        (90, "BẮC (Khảm)", "SINH KHÍ", True, "Tài lộc, thăng tiến sự nghiệp"),
        (0, "ĐÔNG (Chấn)", "DIÊN NIÊN", True, "Hòa thuận gia đạo, tình duyên"),
        (270, "NAM (Li)", "THIÊN Y", True, "Sức khỏe dồi dào, quý nhân"),
        (315, "ĐÔNG NAM (Tốn)", "PHỤC VỊ", True, "Bình an, củng cố nội lực"),
        (45, "ĐÔNG BẮC (Cấn)", "TUYỆT MỆNH", False, "Tổn hại nguyên khí, tai ách"),
        (135, "TÂY BẮC (Đoài)", "LỤC SÁT", False, "Trục trặc tình cảm, thị phi"),
        (180, "TÂY (Càn)", "HỌA HẠI", False, "Thất bại, tranh chấp nhỏ"),
        (225, "TÂY NAM (Khôn)", "NGŨ QUỶ", False, "Mất mát, hao tài, hỏa hoạn")
    ]
    
    # Vẽ các tia phân cung
    for deg in range(0, 360, 45):
        rad = math.radians(deg + 22.5)
        msp.add_line((ox + R_in * math.cos(rad), oy + R_in * math.sin(rad)),
                     (ox + R_out * math.cos(rad), oy + R_out * math.sin(rad)),
                     dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
        
    for deg, h_name, san, is_cat, note in directions_data:
        rad = math.radians(deg)
        layer = "SAN_CAT" if is_cat else "SAN_HUNG"
        
        # Điểm đặt chữ tên san (vành trong)
        r_text1 = 27.0
        tx1 = ox + r_text1 * math.cos(rad)
        ty1 = oy + r_text1 * math.sin(rad)
        msp.add_text(san, dxfattribs={"layer": layer, "style": "VN_BOLD", "height": 3.0}).set_placement((tx1, ty1), align=TextEntityAlignment.MIDDLE_CENTER)
        
        # Điểm đặt hướng (vành ngoài)
        r_text2 = 46.0
        tx2 = ox + r_text2 * math.cos(rad)
        ty2 = oy + r_text2 * math.sin(rad)
        msp.add_text(h_name, dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.3}).set_placement((tx2, ty2), align=TextEntityAlignment.MIDDLE_CENTER)

    # 5. KHỐI TRỤC THỜI GIAN ĐẠI VẬN ĐỜI NGƯỜI (GÓC DƯỚI: x = -140 đến 140, y = -60 đến -118)
    msp.add_line((-140, -56), (140, -56), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((140, -56), (140, -118), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((140, -118), (-140, -118), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-140, -118), (-140, -56), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("III. CHU KỲ PHÂN KỲ ĐẠI VẬN THEO DÒNG ĐỜI (HÀO DƯƠNG 9 NĂM, HÀO ÂM 6 NĂM)", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.8}).set_placement((-135, -63))
    
    # 7 chu kỳ Đại vận vẽ thành các block ngang
    van_data = [
        ("Vận 1: Hào 1 (Âm)", 6, 1, 6, "1984 - 1989", False),
        ("Vận 2: Hào 2 (Dương)", 9, 7, 15, "1990 - 1998", True),
        ("Vận 3: Hào 3 (Dương)", 9, 16, 24, "1999 - 2007", True),
        ("Vận 4: Hào 4 (Dương)", 9, 25, 33, "2008 - 2016", True),
        ("Vận 5: Hào 5 (Âm)", 6, 34, 39, "2017 - 2022", False),
        ("Vận 6: Hào 6 (Dương)", 9, 40, 48, "2023 - 2031", True),
        ("Vận 7: Hào 1 (Âm)", 6, 49, 54, "2032 - 2037", False),
    ]
    
    x_cursor = -135.0
    for title, dur, a1, a2, y_range, is_yang in van_data:
        block_w = dur * 4.1
        box_y = -72.0
        box_h = 24.0
        
        # Khung đại vận
        box_layer = "HAO_DUONG" if is_yang else "HAO_AM"
        msp.add_line((x_cursor, box_y), (x_cursor + block_w, box_y), dxfattribs={"layer": box_layer, "lineweight": 22})
        msp.add_line((x_cursor + block_w, box_y), (x_cursor + block_w, box_y - box_h), dxfattribs={"layer": box_layer, "lineweight": 22})
        msp.add_line((x_cursor + block_w, box_y - box_h), (x_cursor, box_y - box_h), dxfattribs={"layer": box_layer, "lineweight": 22})
        msp.add_line((x_cursor, box_y - box_h), (x_cursor, box_y), dxfattribs={"layer": box_layer, "lineweight": 22})
        
        # Nhãn đại vận
        msp.add_text(f"{dur} năm", dxfattribs={"layer": box_layer, "style": "VN_BOLD", "height": 3.8}).set_placement((x_cursor + 2, box_y - 6))
        msp.add_text(f"{a1}-{a2} tuổi", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 3.0}).set_placement((x_cursor + 2, box_y - 12))
        msp.add_text(y_range, dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.6}).set_placement((x_cursor + 2, box_y - 17))
        msp.add_text("Dương (+)" if is_yang else "Âm (-)", dxfattribs={"layer": box_layer, "style": "VN_BOLD", "height": 2.6}).set_placement((x_cursor + 2, box_y - 21))
        
        x_cursor += block_w + 3.0
        
    msp.add_text("ỨNG DỤNG KHUYẾN NGHỊ: Người 1 hiện tại (năm 2026, 42 tuổi) đang ở ĐẠI VẬN 6 (Hào Dương, 40-48 tuổi) - Giai đoạn hành động mạnh mẽ, vượng khí.", 
                 dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 3.6}).set_placement((-135, -104))
    msp.add_text("Phong thủy bổ trợ: Bàn làm việc, hướng giường ưu tiên CHÍNH BẮC (Sinh khí) hoặc CHÍNH NAM (Thiên y). Bổ trợ hành Thủy và Mộc.", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.4}).set_placement((-135, -112))

    export_dxf_to_png(doc, dxf_path, png_path)

if __name__ == "__main__":
    print("Bắt đầu vẽ bản vẽ kỹ thuật CAD Vận mệnh Người 1 (Nam 1984)...")
    draw_van_menh_nguoi_1()
    print("Hoàn tất 100% xuất bản vẽ CAD và hình ảnh PNG.")
