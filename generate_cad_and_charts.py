import os
import sys
import io
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Cấu hình Matplotlib hỗ trợ tiếng Việt Unicode
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = r"C:\DICH HOC\drawings"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def export_dxf_to_png(doc, dxf_path, png_path, dpi=300):
    doc.saveas(dxf_path)
    fig = plt.figure(figsize=(10, 10), dpi=dpi, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#FFFFFF')
    ctx = RenderContext(doc)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
    fig.savefig(png_path, dpi=dpi, facecolor='#FFFFFF', edgecolor='none')
    plt.close(fig)
    print(f"  [CAD Rendered] {os.path.basename(png_path)}")

# 1. BẢN VẼ 1: ĐỒNG HỒ 10 VẠCH CHIA & NHÓM CỘNG HÀ - LẠC (CHƯƠNG I)
def create_cad_dong_ho():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_dong_ho_ha_lac.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_dong_ho_ha_lac.png")
    doc = ezdxf.new("R2010", setup=True)
    msp = doc.modelspace()
    
    # Layer setup
    doc.layers.add("FRAME", color=7)
    doc.layers.add("TICKS", color=1)
    doc.layers.add("OPPOSITE_LINES", color=5)
    doc.layers.add("TEXT_NUMBERS", color=7)
    
    R = 100.0
    msp.add_circle((0, 0), R, dxfattribs={"layer": "FRAME", "lineweight": 35})
    msp.add_circle((0, 0), R - 15, dxfattribs={"layer": "FRAME", "lineweight": 18})
    msp.add_circle((0, 0), 5, dxfattribs={"layer": "FRAME", "lineweight": 25})
    
    # 10 vạch chia (0 đến 9)
    # Vị trí số 0 ở trên đỉnh (90 độ), quay theo chiều kim đồng hồ
    coords = {}
    for i in range(10):
        angle_deg = 90 - i * 36
        angle_rad = math.radians(angle_deg)
        x_out = R * math.cos(angle_rad)
        y_out = R * math.sin(angle_rad)
        x_in = (R - 15) * math.cos(angle_rad)
        y_in = (R - 15) * math.sin(angle_rad)
        x_text = (R + 14) * math.cos(angle_rad) - 4
        y_text = (R + 14) * math.sin(angle_rad) - 4
        
        coords[i] = (x_in, y_in)
        msp.add_line((x_in, y_in), (x_out, y_out), dxfattribs={"layer": "TICKS", "lineweight": 30})
        msp.add_text(str(i), dxfattribs={"layer": "TEXT_NUMBERS", "height": 10, "style": "Standard"}).set_placement((x_text, y_text))
        
    # Các đường nối cặp số đối: 1-9, 2-8, 3-7, 4-6 (tổng mod 10 = 0)
    pairs = [(1, 9), (2, 8), (3, 7), (4, 6)]
    for a, b in pairs:
        msp.add_line(coords[a], coords[b], dxfattribs={"layer": "OPPOSITE_LINES", "lineweight": 15})
        
    msp.add_text("DONG HO 10 VACH CHIA - NHOM CONG HA - LAC (Z/10Z)", dxfattribs={"layer": "TEXT_NUMBERS", "height": 7}).set_placement((-85, -135))
    msp.add_text("Phan tu trung hoa e = 0; Cap so doi: 1-9, 2-8, 3-7, 4-6, 5-5", dxfattribs={"layer": "TEXT_NUMBERS", "height": 5}).set_placement((-75, -145))
    
    export_dxf_to_png(doc, dxf_path, png_path)

# 2. BẢN VẼ 2: BÁT QUÁI TÂN THIÊN & MA TRẬN LẠC THƯ 3x3 (CHƯƠNG IV)
def create_cad_bat_quai():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_bat_quai_tan_thien.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_bat_quai_tan_thien.png")
    doc = ezdxf.new("R2010", setup=True)
    msp = doc.modelspace()
    
    doc.layers.add("GRID", color=7)
    doc.layers.add("TRIGRAM_LINES", color=1)
    doc.layers.add("TEXT", color=7)
    
    cell_w, cell_h = 70.0, 70.0
    # 3x3 grid centered
    for i in range(4):
        y = -105 + i * cell_h
        msp.add_line((-105, y), (105, y), dxfattribs={"layer": "GRID", "lineweight": 25})
        x = -105 + i * cell_w
        msp.add_line((x, -105), (x, 105), dxfattribs={"layer": "GRID", "lineweight": 25})
        
    # Lạc thư 3x3 matrix:
    # Hàng 1 (trên): Tốn (4, SE), Càn (9, S), Khôn/Đoài ? Sách: Càn ở Chính Nam (trên đỉnh Lạc thư cung 9)
    # Theo Bát quái Tân thiên (Chương IV):
    # Cung 4 (Đông Nam): Tốn (+7) | Cung 9 (Chính Nam): Càn (+9) | Cung 2 (Tây Nam): Cấn (+1)
    # Cung 3 (Chính Đông): Li (+3) | Cung 5 (Trung cung): Thái Cực | Cung 7 (Chính Tây): Khảm (-3)
    # Cung 8 (Đông Bắc): Đoài (-1) | Cung 1 (Chính Bắc): Khôn (-9) | Cung 6 (Tây Bắc): Chấn (-7)
    grid_data = [
        # (row, col, ten, so_lac_thu, tri_so, lines_yang) row 0: top (Nam)
        (0, 0, "TON", 4, "+7", [0, 1, 1], "Dong Nam"),
        (0, 1, "CAN", 9, "+9", [1, 1, 1], "Chinh Nam"),
        (0, 2, "CAN (Tho)", 2, "+1", [0, 0, 1], "Tay Nam"),
        (1, 0, "LI", 3, "+3", [1, 0, 1], "Chinh Dong"),
        (1, 1, "THAI CUC", 5, "0", None, "Trung Cung"),
        (1, 2, "KHAM", 7, "-3", [0, 1, 0], "Chinh Tay"),
        (2, 0, "DOAI", 8, "-1", [1, 1, 0], "Dong Bac"),
        (2, 1, "KHON", 1, "-9", [0, 0, 0], "Chinh Bac"),
        (2, 2, "CHAN", 6, "-7", [1, 0, 0], "Tay Bac")
    ]
    
    for r, c, name, num, val, lines, direction in grid_data:
        cx = -70 + c * cell_w
        cy = 70 - r * cell_h
        
        msp.add_text(f"{num}", dxfattribs={"layer": "TEXT", "height": 10}).set_placement((cx - 28, cy + 20))
        msp.add_text(f"{name}", dxfattribs={"layer": "TEXT", "height": 7}).set_placement((cx - 15, cy + 20))
        msp.add_text(f"E={val}", dxfattribs={"layer": "TEXT", "height": 6}).set_placement((cx - 15, cy - 28))
        msp.add_text(f"{direction}", dxfattribs={"layer": "TEXT", "height": 4}).set_placement((cx - 28, cy - 32))
        
        # Vẽ 3 hào
        if lines:
            line_w = 30.0
            gap = 6.0
            for l_idx, is_yang in enumerate(lines):
                ly = cy - 12 + l_idx * gap
                if is_yang:
                    msp.add_line((cx - line_w/2, ly), (cx + line_w/2, ly), dxfattribs={"layer": "TRIGRAM_LINES", "lineweight": 35})
                else:
                    half = (line_w - 6) / 2
                    msp.add_line((cx - line_w/2, ly), (cx - line_w/2 + half, ly), dxfattribs={"layer": "TRIGRAM_LINES", "lineweight": 35})
                    msp.add_line((cx + line_w/2 - half, ly), (cx + line_w/2, ly), dxfattribs={"layer": "TRIGRAM_LINES", "lineweight": 35})
        else:
            msp.add_circle((cx, cy), 12, dxfattribs={"layer": "TRIGRAM_LINES", "lineweight": 25})
            
    export_dxf_to_png(doc, dxf_path, png_path)

# 3. BẢN VẼ 3: BẢNG MA TRẬN 8x8 BÁT SAN (CHƯƠNG VI, BẢNG 26)
def create_cad_bat_san():
    dxf_path = os.path.join(OUTPUT_DIR, "cad_ma_tran_bat_san.dxf")
    png_path = os.path.join(OUTPUT_DIR, "cad_ma_tran_bat_san.png")
    doc = ezdxf.new("R2010", setup=True)
    msp = doc.modelspace()
    
    doc.layers.add("GRID", color=7)
    doc.layers.add("GOOD_SAN", color=3) # green
    doc.layers.add("BAD_SAN", color=1)  # red
    doc.layers.add("TEXT", color=7)
    
    quais = ["Can", "Doai", "Khon", "Can(2)", "Li", "Chan", "Kham", "Ton"]
    bat_san_data = [
        ["Phuc vi", "Sinh khi", "Dien nien", "Thien y", "Tuyet menh", "Ngu quy", "Luc sat", "Hoa hai"],
        ["Sinh khi", "Phuc vi", "Thien y", "Dien nien", "Ngu quy", "Tuyet menh", "Hoa hai", "Luc sat"],
        ["Dien nien", "Thien y", "Phuc vi", "Sinh khi", "Luc sat", "Hoa hai", "Tuyet menh", "Ngu quy"],
        ["Thien y", "Dien nien", "Sinh khi", "Phuc vi", "Hoa hai", "Luc sat", "Ngu quy", "Tuyet menh"],
        ["Tuyet menh", "Ngu quy", "Luc sat", "Hoa hai", "Phuc vi", "Sinh khi", "Dien nien", "Thien y"],
        ["Ngu quy", "Tuyet menh", "Hoa hai", "Luc sat", "Sinh khi", "Phuc vi", "Thien y", "Dien nien"],
        ["Luc sat", "Hoa hai", "Tuyet menh", "Ngu quy", "Dien nien", "Thien y", "Phuc vi", "Sinh khi"],
        ["Hoa hai", "Luc sat", "Ngu quy", "Tuyet menh", "Thien y", "Dien nien", "Sinh khi", "Phuc vi"]
    ]
    good_set = {"Sinh khi", "Thien y", "Dien nien", "Phuc vi"}
    
    cw = 22.0
    ch = 14.0
    x0 = -100.0
    y0 = 70.0
    
    # Header Trach / Menh
    msp.add_text("TRACH / MENH", dxfattribs={"layer": "TEXT", "height": 4}).set_placement((x0 - 20, y0 + 5))
    for j, q in enumerate(quais):
        msp.add_text(q, dxfattribs={"layer": "TEXT", "height": 4}).set_placement((x0 + j*cw + 2, y0 + 5))
        
    for i in range(9):
        msp.add_line((x0 - 25, y0 - i*ch), (x0 + 8*cw, y0 - i*ch), dxfattribs={"layer": "GRID", "lineweight": 20})
    for j in range(10):
        x = x0 - 25 if j == 0 else x0 + (j-1)*cw
        msp.add_line((x, y0 + 12), (x, y0 - 8*ch), dxfattribs={"layer": "GRID", "lineweight": 20})
        
    for i, q in enumerate(quais):
        msp.add_text(q, dxfattribs={"layer": "TEXT", "height": 4}).set_placement((x0 - 22, y0 - i*ch - 9))
        for j in range(8):
            val = bat_san_data[i][j]
            layer = "GOOD_SAN" if val in good_set else "BAD_SAN"
            msp.add_text(val, dxfattribs={"layer": layer, "height": 3.2}).set_placement((x0 + j*cw + 1.5, y0 - i*ch - 9))
            
    msp.add_text("BANG 26: MA TRAN 8x8 BAT SAN (QUAI TRACH GAP QUAI MENH)", dxfattribs={"layer": "TEXT", "height": 5}).set_placement((-80, y0 - 8*ch - 15))
    msp.add_text("Cat: Sinh khi, Thien y, Dien nien, Phuc vi | Hung: Tuyet menh, Ngu quy, Luc sat, Hoa hai", dxfattribs={"layer": "TEXT", "height": 4}).set_placement((-80, y0 - 8*ch - 22))
    
    export_dxf_to_png(doc, dxf_path, png_path)

# 4. BIỂU ĐỒ 1: MỨC NĂNG LƯỢNG 8 QUÁI (CHƯƠNG III)
def create_chart_nang_luong():
    png_path = os.path.join(OUTPUT_DIR, "chart_nang_luong_bat_quai.png")
    quais = ['Khôn\n(-9)', 'Chấn\n(-7)', 'Khảm\n(-3)', 'Đoài\n(-1)', 'Cấn\n(+1)', 'Li\n(+3)', 'Tốn\n(+7)', 'Càn\n(+9)']
    values = [-9, -7, -3, -1, 1, 3, 7, 9]
    colors = ['#1f77b4' if v < 0 else '#d62728' for v in values]
    
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300, facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    bars = ax.bar(quais, values, color=colors, width=0.55, edgecolor='#000000', linewidth=1.2)
    
    ax.axhline(0, color='#000000', linewidth=1.5)
    ax.set_ylim(-11, 11)
    ax.set_ylabel("Mức năng lượng quái E = h1(±1) + h2(±3) + h3(±5)", fontsize=11, fontweight='bold')
    ax.set_title("QUY PHẠM ĐỊNH LƯỢNG NĂNG LƯỢNG BÁT QUÁI TÂN THIÊN (CHƯƠNG III)", fontsize=13, fontweight='bold', pad=15)
    
    for bar, val in zip(bars, values):
        y = bar.get_height()
        offset = 0.6 if y > 0 else -1.2
        ax.text(bar.get_x() + bar.get_width()/2., y + offset, f"{val:+d}", ha='center', va='bottom', fontsize=11, fontweight='bold')
        
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    fig.tight_layout()
    fig.savefig(png_path, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"  [Chart Rendered] {os.path.basename(png_path)}")

# 5. BIỂU ĐỒ 2: SƠ ĐỒ QUY TRÌNH THUẬT TOÁN BÁT TỰ HÀ LẠC (CHƯƠNG VIII)
def create_chart_quy_trinh():
    png_path = os.path.join(OUTPUT_DIR, "chart_quy_trinh_bat_tu_ha_lac.png")
    fig, ax = plt.subplots(figsize=(12, 7), dpi=300, facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.axis('off')
    
    boxes = [
        ("BƯỚC 1: NHẬP BÁT TỰ", "4 Thiên can + 4 Địa chi\n(Năm, Tháng, Ngày, Giờ sinh)", 0.05, 0.7, 0.22, 0.2),
        ("BƯỚC 2: TRA MÃ SỐ HÀ - LẠC", "4 mã Can + 8 mã Chi (Bảng 41, 42)\nTổng cộng 12 số nguyên", 0.38, 0.7, 0.25, 0.2),
        ("BƯỚC 3: PHÂN TÍCH ÂM DƯƠNG", "Σ(+) = Tổng các số lẻ (1,3,7,9)\nΣ(-) = Tổng các số chẵn (2,4,6,8)", 0.72, 0.7, 0.24, 0.2),
        ("BƯỚC 4: RÚT GỌN LẠC THƯ", "Modulo 9 (kết quả 1..9)\nĐặc biệt: Số 5 quy về Tốn/Chấn/Cấn/Đoài", 0.72, 0.2, 0.24, 0.2),
        ("BƯỚC 5: LẬP QUẺ TIÊN THIÊN", "Xác định Quái Thượng và Quái Hạ\nTra Bảng 27 ra tên quẻ", 0.38, 0.2, 0.25, 0.2),
        ("BƯỚC 6: HÀO NGUYÊN ĐƯỜNG & ĐẠI VẬN", "Hào Nguyên đường -> Quẻ Hậu thiên\nPhân kỳ Đại vận: Dương 9 năm, Âm 6 năm", 0.05, 0.2, 0.25, 0.2)
    ]
    
    for title, text, x, y, w, h in boxes:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03", 
                                      facecolor="#F8FAFC", edgecolor="#1E293B", linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h - 0.04, title, ha='center', va='top', fontsize=9.5, fontweight='bold', color='#0F172A')
        ax.text(x + w/2, y + h/2 - 0.03, text, ha='center', va='center', fontsize=8, color='#334155')
        
    # Mũi tên kết nối
    ax.annotate('', xy=(0.37, 0.8), xytext=(0.28, 0.8), arrowprops=dict(arrowstyle="->", lw=2, color="#0284C7"))
    ax.annotate('', xy=(0.71, 0.8), xytext=(0.64, 0.8), arrowprops=dict(arrowstyle="->", lw=2, color="#0284C7"))
    ax.annotate('', xy=(0.84, 0.41), xytext=(0.84, 0.69), arrowprops=dict(arrowstyle="->", lw=2, color="#0284C7"))
    ax.annotate('', xy=(0.64, 0.3), xytext=(0.71, 0.3), arrowprops=dict(arrowstyle="->", lw=2, color="#0284C7"))
    ax.annotate('', xy=(0.31, 0.3), xytext=(0.37, 0.3), arrowprops=dict(arrowstyle="->", lw=2, color="#0284C7"))
    
    ax.text(0.5, 0.96, "LƯU TRÌNH THUẬT TOÁN NHẬN DẠNG BÁT TỰ HÀ - LẠC (CHƯƠNG VIII)", ha='center', fontsize=13, fontweight='bold', color='#0F172A')
    
    fig.tight_layout()
    fig.savefig(png_path, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"  [Chart Rendered] {os.path.basename(png_path)}")

# 6. BIỂU ĐỒ 3: TIMELINE ĐẠI VẬN ĐỜI NGƯỜI
def create_chart_dai_van():
    png_path = os.path.join(OUTPUT_DIR, "chart_dai_van_timeline.png")
    fig, ax = plt.subplots(figsize=(11, 4.5), dpi=300, facecolor='#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    
    # Ví dụ minh họa chu kỳ 6 đại vận: Sơ (Dương 9), Nhị (Âm 6), Tam (Dương 9), Tứ (Dương 9), Ngũ (Âm 6), Thượng (Dương 9)
    periods = [
        ("Vận 1: Hào 1 (Dương)", 9, "#EF4444"),
        ("Vận 2: Hào 2 (Âm)", 6, "#3B82F6"),
        ("Vận 3: Hào 3 (Dương)", 9, "#EF4444"),
        ("Vận 4: Hào 4 (Dương)", 9, "#EF4444"),
        ("Vận 5: Hào 5 (Âm)", 6, "#3B82F6"),
        ("Vận 6: Hào 6 (Dương)", 9, "#EF4444"),
    ]
    
    start_age = 1
    for name, dur, col in periods:
        end_age = start_age + dur - 1
        ax.barh(0, dur, left=start_age, height=0.6, color=col, edgecolor='#000000', linewidth=1.2)
        ax.text(start_age + dur/2, 0, f"{name}\n{start_age}-{end_age} tuổi\n({dur} năm)", ha='center', va='center', color='#FFFFFF', fontweight='bold', fontsize=8.5)
        start_age += dur
        
    ax.set_xlim(0, 52)
    ax.set_ylim(-0.8, 0.8)
    ax.set_xlabel("Tuổi đời theo chu kỳ Đại vận", fontsize=10, fontweight='bold')
    ax.set_yticks([])
    ax.set_title("PHÂN BỔ CHU KỲ ĐẠI VẬN BÁT TỰ HÀ - LẠC (HÀO DƯƠNG 9 NĂM, HÀO ÂM 6 NĂM)", fontsize=12, fontweight='bold', pad=15)
    
    fig.tight_layout()
    fig.savefig(png_path, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"  [Chart Rendered] {os.path.basename(png_path)}")

def main():
    print("Bắt đầu tạo bản vẽ kỹ thuật CAD (ezdxf) và biểu đồ phân tích (matplotlib)...")
    create_cad_dong_ho()
    create_cad_bat_quai()
    create_cad_bat_san()
    create_chart_nang_luong()
    create_chart_quy_trinh()
    create_chart_dai_van()
    print("Hoàn tất tạo 100% bản vẽ CAD và biểu đồ đồ họa kỹ thuật chuẩn in ấn.")

if __name__ == "__main__":
    main()
