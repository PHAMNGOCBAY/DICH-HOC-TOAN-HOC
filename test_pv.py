import pyvista as pv
import os

pv.OFF_SCREEN = True
plotter = pv.Plotter(off_screen=True, window_size=[1024, 768])
plotter.set_background("white")

sphere = pv.Sphere(radius=1.0)
plotter.add_mesh(sphere, color="lightblue", show_edges=True)

test_png = r"C:\DICH HOC\drawings\test_pyvista.png"
plotter.screenshot(test_png)
plotter.close()

print(f"PyVista screenshot created: {os.path.exists(test_png)}, size: {os.path.getsize(test_png)} bytes")
