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
    l_am.rgb = (217, 119, 6) # Màu vàng kỹ thuật sắc nét trên nền trắng (theo chuẩn skill cad-color-blue-to-yellow)
    return doc

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
    print(f"  [Đã xuất Bản vẽ Vận mệnh Người 3] {os.path.basename(png_path)} ({os.path.getsize(png_path):,} bytes)")

def draw_van_menh_nguoi_3():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_van_menh_nguoi_3.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_van_menh_nguoi_3.png")
    doc = setup_dxf_document()
    msp = doc.modelspace()
    
    # 1. TIÊU ĐỀ BẢN VẼ VÀ KHUNG BAO TOÀN CẢNH
    msp.add_text("BẢN VẼ KỸ THUẬT: ĐỒ HÌNH VẬN MỆNH & PHONG THỦY BÁT TRẠCH - NGƯỜI 3 (NAM)", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 6.0}).set_placement((-140, 116))
    msp.add_text("Cơ sở toán học: Nhóm cộng Hà - Lạc & Bát quái Tân thiên (TS. Nguyễn Thế Cường, NXB ĐHQG TP.HCM)", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 4.0}).set_placement((-140, 109))
    
    # Khung biên bản vẽ
    msp.add_line((-145, 125), (145, 125), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((145, 125), (145, -125), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((145, -125), (-145, -125), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    msp.add_line((-145, -125), (-145, 125), dxfattribs={"layer": "KHUNG", "lineweight": 35})
    
    # 2. KHỐI THÔNG TIN BÁT TỰ & QUÁI MỆNH (GÓC TRÊN TRÁI: x = -140 đến 8, y = 103 đến 18)
    msp.add_line((-140, 103), (8, 103), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((8, 103), (8, 18), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((8, 18), (-140, 18), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-140, 18), (-140, 103), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("I. THÔNG TIN BÁT TỰ & BẢN MỆNH (NGƯỜI 3 - NAM)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.0}).set_placement((-136, 96))
    msp.add_text("- Ngày sinh DL: 25-11-2014 (Thứ Ba)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-136, 88))
    msp.add_text("- Ngày sinh ÂL: Ngày 04 tháng 10 năm Giáp Ngọ", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-136, 80))
    msp.add_text("- Trụ Năm: GIÁP NGỌ (Hạ nguyên vận 8, Dương nam)", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 3.2}).set_placement((-136, 72))
    msp.add_text("- Trụ Tháng: ẤT HỢI  |  Trụ Ngày: CANH TÝ", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-136, 64))
    msp.add_text("- QUÁI MỆNH: CẤN (Cung Lạc thư 2, Dương Thổ)", dxfattribs={"layer": "HAO_DUONG", "style": "VN_BOLD", "height": 3.6}).set_placement((-136, 56))
    msp.add_text("- Trị số năng lượng quái: E = +1 (Dương quái)", dxfattribs={"layer": "HAO_DUONG", "style": "VN_BOLD", "height": 3.2}).set_placement((-136, 49))
    msp.add_text("- Phân loại phong thủy: Tây tứ mệnh (Hợp Tây tứ trạch)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-136, 42))
    msp.add_text("- Cặp phu thê Tân thiên: KHÔN (Chính Bắc, E = -9, Âm Thổ)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-136, 35))
    msp.add_text("- CHU KỲ VẬN MỆNH: 12 Đại vận (Hào Dương 9 năm, Hào Âm 6 năm)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 3.0}).set_placement((-136, 28))
    msp.add_text("  (Tiền vận: 1-48 tuổi; Hậu vận: 49-90 tuổi theo Bát tự Hà Lạc)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.5}).set_placement((-136, 22))

    # 3. KHỐI CẤU TRÚC 3 HÀO QUÁI CẤN (GÓC DƯỚI TRÁI: x = -140 đến 8, y = 12 đến -50)
    msp.add_line((-140, 12), (8, 12), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((8, 12), (8, -50), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((8, -50), (-140, -50), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-140, -50), (-140, 12), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("II. CẤU TRÚC 3 HÀO QUÁI CẤN (DƯƠNG THỔ, E = +1)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.0}).set_placement((-136, 5))
    
    # Hào 3 (Thượng): Dương (+5) (nét liền màu đỏ)
    msp.add_line((-136, -4), (-106, -4), dxfattribs={"layer": "HAO_DUONG", "lineweight": 45})
    msp.add_text("Hào 3 (Thượng): Dương (+5) - Hậu vận vững vàng", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.0}).set_placement((-100, -5.5))
    
    # Hào 2 (Trung): Âm (-3) (hai đoạn đứt - MÀU VÀNG)
    msp.add_line((-136, -16), (-123, -16), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
    msp.add_line((-119, -16), (-106, -16), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
    msp.add_text("Hào 2 (Trung): Âm (-3) - Trung vận nhu thuận", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 3.0}).set_placement((-100, -17.5))
    
    # Hào 1 (Sơ): Âm (-1) (hai đoạn đứt - MÀU VÀNG)
    msp.add_line((-136, -28), (-123, -28), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
    msp.add_line((-119, -28), (-106, -28), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
    msp.add_text("Hào 1 (Sơ): Âm (-1) - Tiền vận tĩnh tâm rèn đức", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 3.0}).set_placement((-100, -29.5))
    
    msp.add_text("Công thức năng lượng: E = (-1)*1 + (-1)*3 + (+1)*5 = +1", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 3.2}).set_placement((-136, -39))
    msp.add_text("Bản chất cơ học: Núi đá (Cấn vi sơn) - Vững chắc, tĩnh tại, thâm trầm", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.8}).set_placement((-136, -46))

    # 4. KHỐI ĐỒ HÌNH BÁT TRẠCH LA BÀN 8 HƯỚNG CỦA QUÁI CẤN (BÊN PHẢI: tâm tại x = 76, y = 26)
    ox, oy = 76.0, 26.0
    R_in = 16.0
    R_mid = 33.0
    R_out = 53.0
    
    msp.add_circle((ox, oy), R_in, dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_circle((ox, oy), R_mid, dxfattribs={"layer": "NET_CHINH", "lineweight": 20})
    msp.add_circle((ox, oy), R_out, dxfattribs={"layer": "KHUNG", "lineweight": 30})
    
    # Nhãn trung tâm
    msp.add_text("MỆNH CẤN", dxfattribs={"layer": "HAO_DUONG", "style": "VN_BOLD", "height": 3.6}).set_placement((ox, oy + 2.5), align=TextEntityAlignment.MIDDLE_CENTER)
    msp.add_text("Dương Thổ (E=+1)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.3}).set_placement((ox, oy - 2.5), align=TextEntityAlignment.MIDDLE_CENTER)
    
    # 8 Hướng la bàn của Quái Cấn (Tây tứ mệnh):
    # 225 deg (Tây Nam): Sinh khí (Cát)
    # 135 deg (Tây Bắc): Thiên y (Cát)
    # 180 deg (Chính Tây): Diên niên (Cát)
    # 45 deg (Đông Bắc): Phục vị (Cát)
    # 315 deg (Đông Nam): Tuyệt mệnh (Hung)
    # 270 deg (Chính Nam): Họa hại (Hung)
    # 90 deg (Chính Bắc): Ngũ quỷ (Hung)
    # 0 deg (Chính Đông): Lục sát (Hung)
    directions_data = [
        (225, "TÂY NAM (Khôn)", "SINH KHÍ", True),
        (135, "TÂY BẮC (Càn)", "THIÊN Y", True),
        (180, "TÂY (Đoài)", "DIÊN NIÊN", True),
        (45, "ĐÔNG BẮC (Cấn)", "PHỤC VỊ", True),
        (315, "ĐÔNG NAM (Tốn)", "TUYỆT MỆNH", False),
        (270, "NAM (Li)", "HỌA HẠI", False),
        (90, "BẮC (Khảm)", "NGŨ QUỶ", False),
        (0, "ĐÔNG (Chấn)", "LỤC SÁT", False),
    ]
    
    # Vẽ các tia phân cung
    for deg in range(0, 360, 45):
        rad = math.radians(deg + 22.5)
        msp.add_line((ox + R_in * math.cos(rad), oy + R_in * math.sin(rad)),
                     (ox + R_out * math.cos(rad), oy + R_out * math.sin(rad)),
                     dxfattribs={"layer": "NET_CHINH", "lineweight": 15})
        
    for deg, h_name, san, is_cat in directions_data:
        rad = math.radians(deg)
        layer = "SAN_CAT" if is_cat else "SAN_HUNG"
        
        # Điểm đặt chữ tên san (vành trong)
        r_text1 = 24.5
        tx1 = ox + r_text1 * math.cos(rad)
        ty1 = oy + r_text1 * math.sin(rad)
        msp.add_text(san, dxfattribs={"layer": layer, "style": "VN_BOLD", "height": 2.5}).set_placement((tx1, ty1), align=TextEntityAlignment.MIDDLE_CENTER)
        
        # Điểm đặt hướng (vành ngoài)
        r_text2 = 43.0
        tx2 = ox + r_text2 * math.cos(rad)
        ty2 = oy + r_text2 * math.sin(rad)
        msp.add_text(h_name, dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.1}).set_placement((tx2, ty2), align=TextEntityAlignment.MIDDLE_CENTER)

    # 5. KHỐI TRỤC THỜI GIAN 12 ĐẠI VẬN BÁT TỰ HÀ LẠC (TIỀN VẬN: 1-48 TUỔI & HẬU VẬN: 49-90 TUỔI)
    msp.add_line((-140, -56), (140, -56), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((140, -56), (140, -120), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((140, -120), (-140, -120), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-140, -120), (-140, -56), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("III. CHU KỲ 12 ĐẠI VẬN BÁT TỰ HÀ LẠC: TIỀN VẬN (1 - 48 TUỔI) & HẬU VẬN (49 - 90 TUỔI)", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.2}).set_placement((-136, -61))
    
    # Dữ liệu phân kỳ 12 Đại vận cho Nam sinh năm 2014 (Giáp Ngọ):
    # Hào Dương quản 9 năm (màu đỏ), Hào Âm quản 6 năm (màu vàng hổ phách)
    tien_van_data = [
        ("Vận 1: Hào 1 (Dương)", 9, 1, 9, "2014 - 2022", True),
        ("Vận 2: Hào 2 (Âm)", 6, 10, 15, "2023 - 2028", False),
        ("Vận 3: Hào 3 (Âm)", 6, 16, 21, "2029 - 2034", False),
        ("Vận 4: Hào 4 (Dương)", 9, 22, 30, "2035 - 2043", True),
        ("Vận 5: Hào 5 (Dương)", 9, 31, 39, "2044 - 2052", True),
        ("Vận 6: Hào 6 (Dương)", 9, 40, 48, "2053 - 2061", True),
    ]
    
    hau_van_data = [
        ("Vận 7: Hào 1 (Âm)", 6, 49, 54, "2062 - 2067", False),
        ("Vận 8: Hào 2 (Dương)", 9, 55, 63, "2068 - 2076", True),
        ("Vận 9: Hào 3 (Dương)", 9, 64, 72, "2077 - 2085", True),
        ("Vận 10: Hào 4 (Âm)", 6, 73, 78, "2086 - 2091", False),
        ("Vận 11: Hào 5 (Âm)", 6, 79, 84, "2092 - 2097", False),
        ("Vận 12: Hào 6 (Âm)", 6, 85, 90, "2098 - 2103", False),
    ]
    
    # HÀNG 1: TIỀN VẬN (1 - 48 tuổi)
    msp.add_text("1. TIỀN VẬN (Quẻ Tiên thiên, 1 - 48 tuổi):", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 3.0}).set_placement((-136, -66.5))
    x_cursor = -130.0
    for title, dur, a1, a2, y_range, is_yang in tien_van_data:
        block_w = dur * 5.0
        box_y = -68.0
        box_h = 16.0
        box_layer = "HAO_DUONG" if is_yang else "HAO_AM"
        
        msp.add_line((x_cursor, box_y), (x_cursor + block_w, box_y), dxfattribs={"layer": box_layer, "lineweight": 20})
        msp.add_line((x_cursor + block_w, box_y), (x_cursor + block_w, box_y - box_h), dxfattribs={"layer": box_layer, "lineweight": 20})
        msp.add_line((x_cursor + block_w, box_y - box_h), (x_cursor, box_y - box_h), dxfattribs={"layer": box_layer, "lineweight": 20})
        msp.add_line((x_cursor, box_y - box_h), (x_cursor, box_y), dxfattribs={"layer": box_layer, "lineweight": 20})
        
        msp.add_text(f"{dur} năm", dxfattribs={"layer": box_layer, "style": "VN_BOLD", "height": 3.2}).set_placement((x_cursor + 2, box_y - 4.5))
        msp.add_text(f"{a1}-{a2} tuổi", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 2.5}).set_placement((x_cursor + 2, box_y - 8.5))
        msp.add_text(y_range, dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.1}).set_placement((x_cursor + 2, box_y - 12.0))
        msp.add_text("Dương (+)" if is_yang else "Âm (-)", dxfattribs={"layer": box_layer, "style": "VN_BOLD", "height": 2.1}).set_placement((x_cursor + 2, box_y - 15.0))
        x_cursor += block_w + 4.0

    # HÀNG 2: HẬU VẬN (49 - 90 tuổi)
    msp.add_text("2. HẬU VẬN (Quẻ Hậu thiên, 49 - 90 tuổi):", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 3.0}).set_placement((-136, -87.5))
    x_cursor = -130.0
    for title, dur, a1, a2, y_range, is_yang in hau_van_data:
        block_w = dur * 5.0
        box_y = -89.0
        box_h = 16.0
        box_layer = "HAO_DUONG" if is_yang else "HAO_AM"
        
        msp.add_line((x_cursor, box_y), (x_cursor + block_w, box_y), dxfattribs={"layer": box_layer, "lineweight": 20})
        msp.add_line((x_cursor + block_w, box_y), (x_cursor + block_w, box_y - box_h), dxfattribs={"layer": box_layer, "lineweight": 20})
        msp.add_line((x_cursor + block_w, box_y - box_h), (x_cursor, box_y - box_h), dxfattribs={"layer": box_layer, "lineweight": 20})
        msp.add_line((x_cursor, box_y - box_h), (x_cursor, box_y), dxfattribs={"layer": box_layer, "lineweight": 20})
        
        msp.add_text(f"{dur} năm", dxfattribs={"layer": box_layer, "style": "VN_BOLD", "height": 3.2}).set_placement((x_cursor + 2, box_y - 4.5))
        msp.add_text(f"{a1}-{a2} tuổi", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 2.5}).set_placement((x_cursor + 2, box_y - 8.5))
        msp.add_text(y_range, dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.1}).set_placement((x_cursor + 2, box_y - 12.0))
        msp.add_text("Dương (+)" if is_yang else "Âm (-)", dxfattribs={"layer": box_layer, "style": "VN_BOLD", "height": 2.1}).set_placement((x_cursor + 2, box_y - 15.0))
        x_cursor += block_w + 4.0
        
    msp.add_text("ỨNG DỤNG KHUYẾN NGHỊ: Người 3 hiện tại (năm 2026, 12 tuổi) đang ở ĐẠI VẬN 2 (10-15 tuổi) - Thời kỳ thiếu niên rèn luyện trí đức, phát triển học vấn.", 
                 dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 2.8}).set_placement((-136, -110.5))
    msp.add_text("Phong thủy bổ trợ: Mệnh Cấn hợp Tây tứ trạch, góc học tập ưu tiên TÂY NAM (Sinh khí) hoặc TÂY BẮC (Thiên y). Bổ trợ hành Hỏa (tương sinh) và Thổ.", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.5}).set_placement((-136, -116.0))

    export_dxf_to_png(doc, dxf_path, png_path)

if __name__ == "__main__":
    print("Bắt đầu vẽ bản vẽ kỹ thuật CAD Vận mệnh Người 3 (Nam 2014) bổ sung chu kỳ 12 đại vận...")
    draw_van_menh_nguoi_3()
    print("Hoàn tất 100% xuất bản vẽ CAD và hình ảnh PNG Người 3.")
