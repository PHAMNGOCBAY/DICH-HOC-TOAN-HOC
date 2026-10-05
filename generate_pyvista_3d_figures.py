import pyvista as pv
import numpy as np
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

pv.OFF_SCREEN = True
OUTPUT_DIR = r"C:\DICH HOC\drawings"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. HÌNH 3D THỨ NHẤT: BÁT QUÁI TÂN THIÊN VÀ ĐỊA HÌNH NĂNG LƯỢNG 3D
def draw_bat_quai_3d_energy():
    out_png = os.path.join(OUTPUT_DIR, "pyvista_bat_quai_3d_energy.png")
    plotter = pv.Plotter(off_screen=True, window_size=[1600, 1200])
    plotter.set_background("white")

    # Dữ liệu 8 quái + Thái cực (x, y, z_energy, ten, mau)
    # Lạc thư 3x3: x theo cột (-4, 0, 4), y theo hàng (4, 0, -4)
    quai_data = [
        # Hàng 1 (trên - Nam)
        (-4.0, 4.0, 7.0, "TON (+7)", "#E11D48"),      # Tốn (4)
        (0.0, 4.0, 9.0, "CAN (+9)", "#BE123C"),       # Càn (9)
        (4.0, 4.0, 1.0, "CAN_THO (+1)", "#FB7185"),  # Cấn (2)
        # Hàng 2 (giữa)
        (-4.0, 0.0, 3.0, "LI (+3)", "#F43F5E"),       # Li (3)
        (0.0, 0.0, 0.0, "THAI CUC (0)", "#475569"),   # Thái cực (5)
        (4.0, 0.0, -3.0, "KHAM (-3)", "#0284C7"),     # Khảm (7)
        # Hàng 3 (dưới - Bắc)
        (-4.0, -4.0, -1.0, "DOAI (-1)", "#38BDF8"),   # Đoài (8)
        (0.0, -4.0, -9.0, "KHON (-9)", "#0369A1"),    # Khôn (1)
        (4.0, -4.0, -7.0, "CHAN (-7)", "#075985")     # Chấn (6)
    ]

    # Mặt đế lưới 3x3 (Grid Base)
    grid_plane = pv.Plane(center=(0, 0, -10), direction=(0, 0, 1), i_size=12, j_size=12, i_resolution=3, j_resolution=3)
    plotter.add_mesh(grid_plane, style='wireframe', color='#94A3B8', line_width=2.5)

    # Trục tọa độ cơ sở Z = 0
    zero_plane = pv.Plane(center=(0, 0, 0), direction=(0, 0, 1), i_size=12, j_size=12, i_resolution=1, j_resolution=1)
    plotter.add_mesh(zero_plane, color='#E2E8F0', opacity=0.35)

    for x, y, z, label, color in quai_data:
        # Cột năng lượng từ Z=0 đến Z=z
        h = abs(z)
        if h > 0.01:
            z_center = z / 2.0
            cylinder = pv.Cylinder(center=(x, y, z_center), direction=(0, 0, 1 if z > 0 else -1), radius=0.75, height=h, resolution=32)
            plotter.add_mesh(cylinder, color=color, opacity=0.85, smooth_shading=True)

        # Khối đỉnh cầu tại vị trí năng lượng E
        cap_sphere = pv.Sphere(center=(x, y, z), radius=0.9 if label.startswith("THAI") else 0.8)
        plotter.add_mesh(cap_sphere, color=color, smooth_shading=True)

        # Nhãn text 3D
        label_z = z + (1.2 if z >= 0 else -1.4)
        plotter.add_point_labels([(x, y, label_z)], [label], font_size=14, text_color='#0F172A', shape=None, show_points=False)

    # Đường đối xứng qua tâm nối các cặp quái đối nghịch
    pairs = [
        ((0, 4, 9), (0, -4, -9)),   # Càn (+9) đối Khôn (-9)
        ((-4, 0, 3), (4, 0, -3)),   # Li (+3) đối Khảm (-3)
        ((-4, 4, 7), (4, -4, -7)),  # Tốn (+7) đối Chấn (-7)
        ((4, 4, 1), (-4, -4, -1))   # Cấn (+1) đối Đoài (-1)
    ]
    for p1, p2 in pairs:
        line = pv.Line(p1, p2)
        plotter.add_mesh(line, color='#64748B', line_width=2.0)

    plotter.camera_position = [(18, -20, 16), (0, 0, 0), (0, 0, 1)]
    plotter.screenshot(out_png)
    plotter.close()
    print(f"  [PyVista 3D] Đã tạo thành công: {os.path.basename(out_png)}")


# 2. HÌNH 3D THỨ HAI: TƯƠNG TÁC 3 CHIỀU QUÁI CHỒNG TỐN (1984) VÀ QUÁI VỢ KHÔN (1985)
def draw_tuong_tac_ton_khon_3d():
    out_png = os.path.join(OUTPUT_DIR, "pyvista_tuong_tac_ton_khon_3d.png")
    plotter = pv.Plotter(off_screen=True, window_size=[1600, 1200])
    plotter.set_background("white")

    # Chồng: Tốn (0, 1, 1) tại x = -4
    # Vợ: Khôn (0, 0, 0) tại x = +4
    # Các hào ở z = 1, 3, 5 (tương ứng với trọng số hào 1, 2, 3)

    # Vẽ các hào của Tốn (Chồng)
    # Hào 1: Âm (2 đoạn đứt)
    bar1a = pv.Cube(center=(-4.8, 0, 1), x_length=1.2, y_length=0.4, z_length=0.3)
    bar1b = pv.Cube(center=(-3.2, 0, 1), x_length=1.2, y_length=0.4, z_length=0.3)
    # Hào 2: Dương (1 thanh liền)
    bar2 = pv.Cube(center=(-4.0, 0, 3), x_length=2.8, y_length=0.4, z_length=0.3)
    # Hào 3: Dương (1 thanh liền)
    bar3 = pv.Cube(center=(-4.0, 0, 5), x_length=2.8, y_length=0.4, z_length=0.3)

    for mesh in [bar1a, bar1b]:
        plotter.add_mesh(mesh, color="#0284C7") # Âm xanh
    for mesh in [bar2, bar3]:
        plotter.add_mesh(mesh, color="#E11D48") # Dương đỏ

    # Vẽ các hào của Khôn (Vợ) - cả 3 hào đều là âm (đoạn đứt)
    for z in [1, 3, 5]:
        b_left = pv.Cube(center=(3.2, 0, z), x_length=1.2, y_length=0.4, z_length=0.3)
        b_right = pv.Cube(center=(4.8, 0, z), x_length=1.2, y_length=0.4, z_length=0.3)
        plotter.add_mesh(b_left, color="#0284C7")
        plotter.add_mesh(b_right, color="#0284C7")

    # Thêm nhãn quái
    plotter.add_point_labels([(-4, 0, 6.2)], ["CHONG: TON (Moc, E=+7)"], font_size=15, text_color="#E11D48", show_points=False)
    plotter.add_point_labels([(4, 0, 6.2)], ["VO: KHON (Tho, E=-9)"], font_size=15, text_color="#0369A1", show_points=False)

    # Vẽ các đường tương tác giữa 3 cặp hào:
    # Cặp hào 1: Cùng âm -> Đẩy nhau (Repulsion)
    line1 = pv.Line((-2.5, 0, 1), (2.5, 0, 1))
    plotter.add_mesh(line1, color="#DC2626", line_width=4.0) # Đỏ cảnh báo lực đẩy
    plotter.add_point_labels([(0, 0, 1.4)], ["Hao 1: Cung Am (Day nhau)"], font_size=12, text_color="#DC2626", show_points=False)

    # Cặp hào 2: Dương (Tốn) - Âm (Khôn) -> Hút nhau (Attraction)
    line2 = pv.Line((-2.5, 0, 3), (2.5, 0, 3))
    plotter.add_mesh(line2, color="#16A34A", line_width=4.0) # Xanh lá hút
    plotter.add_point_labels([(0, 0, 3.4)], ["Hao 2: Khac tinh (Hut nhau)"], font_size=12, text_color="#16A34A", show_points=False)

    # Cặp hào 3: Dương (Tốn) - Âm (Khôn) -> Hút nhau (Attraction)
    line3 = pv.Line((-2.5, 0, 5), (2.5, 0, 5))
    plotter.add_mesh(line3, color="#16A34A", line_width=4.0)
    plotter.add_point_labels([(0, 0, 5.4)], ["Hao 3: Khac tinh (Hut nhau)"], font_size=12, text_color="#16A34A", show_points=False)

    # Nhãn kết luận Bát san ở trung tâm
    plotter.add_point_labels([(0, 0, -1.0)], ["KET HOP BAT SAN: NGU QUY (Moc khac Tho)"], font_size=16, text_color="#991B1B", show_points=False)

    plotter.camera_position = [(0, -18, 5), (0, 0, 3), (0, 0, 1)]
    plotter.screenshot(out_png)
    plotter.close()
    print(f"  [PyVista 3D] Đã tạo thành công: {os.path.basename(out_png)}")


# 3. HÌNH 3D THỨ BA: ĐỒNG HỒ 10 SỐ HÀ - LẠC DẠNG VÒNG XUYẾN 3D (3D TORUS CLOCK)
def draw_dong_ho_ha_lac_3d():
    out_png = os.path.join(OUTPUT_DIR, "pyvista_dong_ho_ha_lac_3d.png")
    plotter = pv.Plotter(off_screen=True, window_size=[1600, 1200])
    plotter.set_background("white")

    # Vòng tròn vành 3D
    ring = pv.ParametricTorus(ringradius=6.0, crosssectionradius=0.35)
    plotter.add_mesh(ring, color="#CBD5E1", smooth_shading=True)

    R = 6.0
    # 10 quả cầu số đại diện cho 10 số (0 đến 9)
    coords = {}
    for i in range(10):
        angle = np.pi/2 - i * (2*np.pi / 10)
        x = R * np.cos(angle)
        y = R * np.sin(angle)
        z = 0.0
        coords[i] = (x, y, z)

        # Quả cầu số
        col = "#F59E0B" if i == 0 or i == 5 else ("#EF4444" if i % 2 != 0 else "#3B82F6")
        sp = pv.Sphere(center=(x, y, z), radius=0.65)
        plotter.add_mesh(sp, color=col, smooth_shading=True)

        label_pos = (x * 1.25, y * 1.25, z)
        plotter.add_point_labels([label_pos], [f"{i}"], font_size=16, text_color="#0F172A", show_points=False)

    # Nối các cặp số đối qua tâm: 1-9, 2-8, 3-7, 4-6
    pairs = [(1, 9), (2, 8), (3, 7), (4, 6)]
    for a, b in pairs:
        c1 = coords[a]
        c2 = coords[b]
        cyl_line = pv.Cylinder(center=((c1[0]+c2[0])/2, (c1[1]+c2[1])/2, 0),
                               direction=(c2[0]-c1[0], c2[1]-c1[1], 0),
                               radius=0.12, height=np.linalg.norm(np.array(c2)-np.array(c1)))
        plotter.add_mesh(cyl_line, color="#64748B", opacity=0.8)

    # Cầu trung tâm Thái Cực (e = 0)
    center_sphere = pv.Sphere(center=(0, 0, 0), radius=1.0)
    plotter.add_mesh(center_sphere, color="#1E293B", smooth_shading=True)
    plotter.add_point_labels([(0, 0, 1.5)], ["THAI CUC (e=0)"], font_size=14, text_color="#1E293B", show_points=False)

    plotter.camera_position = [(0, -16, 14), (0, 0, 0), (0, 0, 1)]
    plotter.screenshot(out_png)
    plotter.close()
    print(f"  [PyVista 3D] Đã tạo thành công: {os.path.basename(out_png)}")


def main():
    print("Bắt đầu sinh các hình minh họa 3D bằng thư viện PyVista...")
    draw_bat_quai_3d_energy()
    draw_tuong_tac_ton_khon_3d()
    draw_dong_ho_ha_lac_3d()
    print("Hoàn tất 100% xuất các hình minh họa 3D PyVista chuẩn phân giải cao (*.png).")

if __name__ == "__main__":
    main()
