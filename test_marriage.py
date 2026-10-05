import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from dich_hoc_core import PhongThuyBatSan, BAT_SAN_TABLE, TRIGRAMS_DATA, HopHoaCanChi

quai_chong = "Tốn"
quai_vo = "Khôn"

san_chong_vo = PhongThuyBatSan.tra_cuu_bat_san(quai_chong, quai_vo)
danh_gia = PhongThuyBatSan.danh_gia_hon_nhan(quai_chong, quai_vo)

print("=== PHÂN TÍCH HÔN NHÂN THEO DỊCH HỌC (TS. NGUYỄN THẾ CƯỜNG) ===")
print(f"Người 1 (Chồng, sinh 05-10-1984 - Giáp Tý):")
print(f"  - Quái mệnh: {quai_chong} (Hành {TRIGRAMS_DATA[quai_chong]['ngu_hanh']}, Cung Lạc thư {TRIGRAMS_DATA[quai_chong]['cung_lac_thu']})")
print(f"  - Phân loại: {PhongThuyBatSan.phan_loai_menh(quai_chong)}")
print(f"  - Cấu trúc hào: {TRIGRAMS_DATA[quai_chong]['lines']} (Hào 1: Âm, Hào 2: Dương, Hào 3: Dương), Năng lượng E = {TRIGRAMS_DATA[quai_chong]['tri_so']}")

print(f"\nNgười 2 (Vợ, sinh 05-10-1985 - Ất Sửu):")
print(f"  - Quái mệnh: {quai_vo} (Hành {TRIGRAMS_DATA[quai_vo]['ngu_hanh']}, Cung Lạc thư {TRIGRAMS_DATA[quai_vo]['cung_lac_thu']})")
print(f"  - Phân loại: {PhongThuyBatSan.phan_loai_menh(quai_vo)}")
print(f"  - Cấu trúc hào: {TRIGRAMS_DATA[quai_vo]['lines']} (Hào 1: Âm, Hào 2: Âm, Hào 3: Âm), Năng lượng E = {TRIGRAMS_DATA[quai_vo]['tri_so']}")

print(f"\nQuan hệ phối ngẫu:")
print(f"  - Bát san (Bảng 26, trang 144): {quai_chong} phối {quai_vo} -> {san_chong_vo}")
print(f"  - Tính chất Bát san: {danh_gia['danh_gia']}")
print(f"  - Ngũ hành quái mệnh: Mộc (Tốn) khắc Thổ (Khôn)")
print(f"  - Thiên can: Giáp (Mộc) gặp Ất (Mộc) -> Bình hòa")
print(f"  - Địa chi: Tý gặp Sửu -> Lục hợp (Hóa Thổ)")
