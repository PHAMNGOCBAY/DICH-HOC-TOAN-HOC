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
    print(f"  [Đã xuất Bản vẽ Vận mệnh Người 4] {os.path.basename(png_path)} ({os.path.getsize(png_path):,} bytes)")

def draw_van_menh_nguoi_4():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_van_menh_nguoi_4.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_van_menh_nguoi_4.png")
    doc = setup_dxf_document()
    msp = doc.modelspace()
    
    # 1. TIÊU ĐỀ BẢN VẼ VÀ KHUNG BAO TOÀN CẢNH
    msp.add_text("BẢN VẼ KỸ THUẬT: ĐỒ HÌNH VẬN MỆNH & PHONG THỦY BÁT TRẠCH - NGƯỜI 4 (NAM)", 
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
    
    msp.add_text("I. THÔNG TIN BÁT TỰ & BẢN MỆNH (NGƯỜI 4 - NAM)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.0}).set_placement((-136, 96))
    msp.add_text("- Ngày sinh DL: 19-06-2019 (Thứ Tư)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-136, 88))
    msp.add_text("- Ngày sinh ÂL: Ngày 17 tháng 5 năm Kỷ Hợi", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-136, 80))
    msp.add_text("- Trụ Năm: KỶ HỢI (Hạ nguyên vận 8, Âm nam)", dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 3.2}).set_placement((-136, 72))
    msp.add_text("- Trụ Tháng: CANH NGỌ  |  Trụ Ngày: ĐINH HỢI", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-136, 64))
    msp.add_text("- QUÁI MỆNH: CHẤN (Cung Lạc thư 6, Âm Mộc)", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 3.6}).set_placement((-136, 56))
    msp.add_text("- Trị số năng lượng quái: E = -7 (Âm quái)", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 3.2}).set_placement((-136, 49))
    msp.add_text("- Phân loại phong thủy: Đông tứ mệnh (Hợp Đông tứ trạch)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-136, 42))
    msp.add_text("- Cặp phu thê Tân thiên: LI (Đông Bắc, E = +3, Âm Hỏa)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.2}).set_placement((-136, 35))
    msp.add_text("- CHU KỲ VẬN MỆNH: 12 Đại vận (Hào Dương 9 năm, Hào Âm 6 năm)", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 3.0}).set_placement((-136, 28))
    msp.add_text("  (Tiền vận: 1-45 tuổi; Hậu vận: 46-90 tuổi theo Bát tự Hà Lạc)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.5}).set_placement((-136, 22))

    # 3. KHỐI CẤU TRÚC 3 HÀO QUÁI CHẤN (GÓC DƯỚI TRÁI: x = -140 đến 8, y = 12 đến -50)
    msp.add_line((-140, 12), (8, 12), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((8, 12), (8, -50), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((8, -50), (-140, -50), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-140, -50), (-140, 12), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("II. CẤU TRÚC 3 HÀO QUÁI CHẤN (ÂM MỘC, E = -7)", dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.0}).set_placement((-136, 5))
    
    # Hào 3 (Thượng): Âm (-5) (hai đoạn đứt - MÀU VÀNG)
    msp.add_line((-136, -4), (-123, -4), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
    msp.add_line((-119, -4), (-106, -4), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
    msp.add_text("Hào 3 (Thượng): Âm (-5) - Hậu vận nhu hòa tĩnh tại", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 3.0}).set_placement((-100, -5.5))
    
    # Hào 2 (Trung): Âm (-3) (hai đoạn đứt - MÀU VÀNG)
    msp.add_line((-136, -16), (-123, -16), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
    msp.add_line((-119, -16), (-106, -16), dxfattribs={"layer": "HAO_AM", "lineweight": 45})
    msp.add_text("Hào 2 (Trung): Âm (-3) - Trung vận ứng biến linh hoạt", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 3.0}).set_placement((-100, -17.5))
    
    # Hào 1 (Sơ): Dương (+1) (nét liền màu đỏ)
    msp.add_line((-136, -28), (-106, -28), dxfattribs={"layer": "HAO_DUONG", "lineweight": 45})
    msp.add_text("Hào 1 (Sơ): Dương (+1) - Tiền vận khởi phát mạnh mẽ", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 3.0}).set_placement((-100, -29.5))
    
    msp.add_text("Công thức năng lượng: E = (+1)*1 + (-1)*3 + (-1)*5 = -7", dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 3.2}).set_placement((-136, -39))
    msp.add_text("Bản chất cơ học: Sấm sét (Chấn vi lôi) - Động lực phát khởi, thức tỉnh, quyết đoán", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.8}).set_placement((-136, -46))

    # 4. KHỐI ĐỒ HÌNH BÁT TRẠCH LA BÀN 8 HƯỚNG CỦA QUÁI CHẤN (BÊN PHẢI: tâm tại x = 76, y = 26)
    ox, oy = 76.0, 26.0
    R_in = 16.0
    R_mid = 33.0
    R_out = 53.0
    
    msp.add_circle((ox, oy), R_in, dxfattribs={"layer": "NET_CHINH", "lineweight": 25})
    msp.add_circle((ox, oy), R_mid, dxfattribs={"layer": "NET_CHINH", "lineweight": 20})
    msp.add_circle((ox, oy), R_out, dxfattribs={"layer": "KHUNG", "lineweight": 30})
    
    # Nhãn trung tâm
    msp.add_text("MỆNH CHẤN", dxfattribs={"layer": "HAO_AM", "style": "VN_BOLD", "height": 3.6}).set_placement((ox, oy + 2.5), align=TextEntityAlignment.MIDDLE_CENTER)
    msp.add_text("Âm Mộc (E=-7)", dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.3}).set_placement((ox, oy - 2.5), align=TextEntityAlignment.MIDDLE_CENTER)
    
    # 8 Hướng la bàn của Quái Chấn (Đông tứ mệnh):
    # 270 deg (Chính Nam): Sinh khí (Cát)
    # 90 deg (Chính Bắc): Thiên y (Cát)
    # 315 deg (Đông Nam): Diên niên (Cát)
    # 0 deg (Chính Đông): Phục vị (Cát)
    # 180 deg (Chính Tây): Tuyệt mệnh (Hung)
    # 135 deg (Tây Bắc): Ngũ quỷ (Hung)
    # 225 deg (Tây Nam): Họa hại (Hung)
    # 45 deg (Đông Bắc): Lục sát (Hung)
    directions_data = [
        (270, "NAM (Li)", "SINH KHÍ", True),
        (90, "BẮC (Khảm)", "THIÊN Y", True),
        (315, "ĐÔNG NAM (Tốn)", "DIÊN NIÊN", True),
        (0, "ĐÔNG (Chấn)", "PHỤC VỊ", True),
        (180, "TÂY (Đoài)", "TUYỆT MỆNH", False),
        (135, "TÂY BẮC (Càn)", "NGŨ QUỶ", False),
        (225, "TÂY NAM (Khôn)", "HỌA HẠI", False),
        (45, "ĐÔNG BẮC (Cấn)", "LỤC SÁT", False),
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
        r_text1 = 23.5
        tx1 = ox + r_text1 * math.cos(rad)
        ty1 = oy + r_text1 * math.sin(rad)
        msp.add_text(san, dxfattribs={"layer": layer, "style": "VN_BOLD", "height": 2.2}).set_placement((tx1, ty1), align=TextEntityAlignment.MIDDLE_CENTER)
        
        # Điểm đặt hướng (vành ngoài)
        r_text2 = 44.0
        tx2 = ox + r_text2 * math.cos(rad)
        ty2 = oy + r_text2 * math.sin(rad)
        msp.add_text(h_name, dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 1.9}).set_placement((tx2, ty2), align=TextEntityAlignment.MIDDLE_CENTER)

    # 5. KHỐI TRỤC THỜI GIAN 12 ĐẠI VẬN BÁT TỰ HÀ LẠC (TIỀN VẬN: 1-45 TUỔI & HẬU VẬN: 46-90 TUỔI)
    msp.add_line((-140, -56), (140, -56), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((140, -56), (140, -120), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((140, -120), (-140, -120), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    msp.add_line((-140, -120), (-140, -56), dxfattribs={"layer": "KHUNG", "lineweight": 20})
    
    msp.add_text("III. CHU KỲ 12 ĐẠI VẬN BÁT TỰ HÀ LẠC: TIỀN VẬN (1 - 45 TUỔI) & HẬU VẬN (46 - 90 TUỔI)", 
                 dxfattribs={"layer": "TIEU_DE", "style": "VN_BOLD", "height": 4.2}).set_placement((-136, -61))
    
    # Dữ liệu phân kỳ 12 Đại vận cho Nam sinh năm 2019 (Kỷ Hợi):
    # Hào Dương quản 9 năm (màu đỏ), Hào Âm quản 6 năm (màu vàng hổ phách)
    tien_van_data = [
        ("Vận 1: Hào 1 (Dương)", 9, 1, 9, "2019 - 2027", True),
        ("Vận 2: Hào 2 (Dương)", 9, 10, 18, "2028 - 2036", True),
        ("Vận 3: Hào 3 (Dương)", 9, 19, 27, "2037 - 2045", True),
        ("Vận 4: Hào 4 (Âm)", 6, 28, 33, "2046 - 2051", False),
        ("Vận 5: Hào 5 (Âm)", 6, 34, 39, "2052 - 2057", False),
        ("Vận 6: Hào 6 (Âm)", 6, 40, 45, "2058 - 2063", False),
    ]
    
    hau_van_data = [
        ("Vận 7: Hào 1 (Dương)", 9, 46, 54, "2064 - 2072", True),
        ("Vận 8: Hào 2 (Âm)", 6, 55, 60, "2073 - 2078", False),
        ("Vận 9: Hào 3 (Âm)", 6, 61, 66, "2079 - 2084", False),
        ("Vận 10: Hào 4 (Dương)", 9, 67, 75, "2085 - 2093", True),
        ("Vận 11: Hào 5 (Dương)", 9, 76, 84, "2094 - 2102", True),
        ("Vận 12: Hào 6 (Âm)", 6, 85, 90, "2103 - 2108", False),
    ]
    
    # HÀNG 1: TIỀN VẬN (1 - 45 tuổi)
    msp.add_text("1. TIỀN VẬN (Quẻ Tiên thiên, 1 - 45 tuổi):", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 3.0}).set_placement((-136, -66.5))
    x_cursor = -130.0
    for title, dur, a1, a2, y_range, is_yang in tien_van_data:
        block_w = dur * 5.2
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

    # HÀNG 2: HẬU VẬN (46 - 90 tuổi)
    msp.add_text("2. HẬU VẬN (Quẻ Hậu thiên, 46 - 90 tuổi):", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_BOLD", "height": 3.0}).set_placement((-136, -87.5))
    x_cursor = -130.0
    for title, dur, a1, a2, y_range, is_yang in hau_van_data:
        block_w = dur * 5.2
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
        
    msp.add_text("ỨNG DỤNG KHUYẾN NGHỊ: Người 4 hiện tại (năm 2026, 7 tuổi) đang ở ĐẠI VẬN 1 (1-9 tuổi, Hào Dương) - Thời kỳ ấu thơ định hình thể chất & trí tuệ.", 
                 dxfattribs={"layer": "SAN_CAT", "style": "VN_BOLD", "height": 2.7}).set_placement((-136, -110.5))
    msp.add_text("Phong thủy bổ trợ: Mệnh Chấn hợp Đông tứ trạch, góc học tập ưu tiên CHÍNH NAM (Sinh khí) hoặc CHÍNH BẮC (Thiên y). Bổ trợ hành Thủy và Mộc.", 
                 dxfattribs={"layer": "CHU_THICH", "style": "VN_TEXT", "height": 2.5}).set_placement((-136, -116.0))

    export_dxf_to_png(doc, dxf_path, png_path)

if __name__ == "__main__":
    print("Bắt đầu vẽ bản vẽ kỹ thuật CAD Vận mệnh Người 4 (Nam 2019)...")
    draw_van_menh_nguoi_4()
    print("Hoàn tất 100% xuất bản vẽ CAD và hình ảnh PNG Người 4.")
