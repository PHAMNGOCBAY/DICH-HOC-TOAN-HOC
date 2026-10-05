import fitz
import easyocr
import io
import sys
import os
import time
import cv2
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

PDF_PATH = r"C:\DICH HOC\DICH HOC-TOANHOC-DOI SONG.pdf"
OUTPUT_DIR = r"C:\DICH HOC"

CHAPTERS = [
    {
        "id": 0,
        "filename": "Chuong_0_Mo_Dau.md",
        "title": "Lời mở đầu, Giới thiệu & Mục lục nguyên bản",
        "start_pdf": 1,
        "end_pdf": 13
    },
    {
        "id": 1,
        "filename": "Chuong_1_Co_So_Toan_Hoc.md",
        "title": "Chương I: Cơ sở toán học của Bát quái",
        "start_pdf": 14,
        "end_pdf": 19
    },
    {
        "id": 2,
        "filename": "Chuong_2_Am_Duong_Thai_Cuc.md",
        "title": "Chương II: Âm, dương và Thái cực",
        "start_pdf": 20,
        "end_pdf": 36
    },
    {
        "id": 3,
        "filename": "Chuong_3_Tao_Quai_Tu_Luong_Nghi.md",
        "title": "Chương III: Tạo quái từ lưỡng nghi âm, dương",
        "start_pdf": 37,
        "end_pdf": 60
    },
    {
        "id": 4,
        "filename": "Chuong_4_Bat_Quai_Tan_Thien.md",
        "title": "Chương IV: Bát quái Tân thiên",
        "start_pdf": 61,
        "end_pdf": 86
    },
    {
        "id": 5,
        "filename": "Chuong_5_Do_Tong_Hop_QCC.md",
        "title": "Chương V: Đồ tổng hợp Quái - Can - Chi",
        "start_pdf": 87,
        "end_pdf": 103
    },
    {
        "id": 6,
        "filename": "Chuong_6_Ung_Dung_QCC.md",
        "title": "Chương VI: Một số phát triển ứng dụng từ đồ tổng hợp QCC vào đời sống cá nhân và gia đình",
        "start_pdf": 104,
        "end_pdf": 167
    },
    {
        "id": 7,
        "filename": "Chuong_7_Que_Dich.md",
        "title": "Chương VII: Quẻ dịch",
        "start_pdf": 168,
        "end_pdf": 207
    },
    {
        "id": 8,
        "filename": "Chuong_8_Bat_Tu_Ha_Lac.md",
        "title": "Chương VIII: Nhận dạng theo phương pháp Bát tự Hà – Lạc",
        "start_pdf": 208,
        "end_pdf": 265
    },
    {
        "id": 9,
        "filename": "Chuong_9_Ket_Luan_Tham_Khao.md",
        "title": "Lời kết, Tài liệu tham khảo và Mục lục cuối sách",
        "start_pdf": 266,
        "end_pdf": 278
    }
]

def reconstruct_page_text(ocr_results):
    boxes = []
    for bbox, text, conf in ocr_results:
        text = text.strip()
        if not text:
            continue
        y_top = bbox[0][1]
        y_bottom = bbox[2][1]
        x_left = bbox[0][0]
        y_center = (y_top + y_bottom) / 2.0
        height = y_bottom - y_top
        boxes.append({
            'text': text,
            'x': x_left,
            'y': y_top,
            'y_center': y_center,
            'h': height,
            'conf': conf
        })
    
    if not boxes:
        return ""
    
    boxes.sort(key=lambda b: (b['y'], b['x']))
    
    lines = []
    current_line = [boxes[0]]
    line_y = boxes[0]['y_center']
    line_h = boxes[0]['h']
    
    for b in boxes[1:]:
        if abs(b['y_center'] - line_y) < max(line_h, b['h']) * 0.65:
            current_line.append(b)
            line_y = sum(x['y_center'] for x in current_line) / len(current_line)
            line_h = sum(x['h'] for x in current_line) / len(current_line)
        else:
            current_line.sort(key=lambda x: x['x'])
            lines.append(" ".join(x['text'] for x in current_line))
            current_line = [b]
            line_y = b['y_center']
            line_h = b['h']
            
    if current_line:
        current_line.sort(key=lambda x: x['x'])
        lines.append(" ".join(x['text'] for x in current_line))
        
    return "\n\n".join(lines)

def main():
    print(f"Bắt đầu quy trình OCR toàn văn tài liệu: {PDF_PATH}")
    reader = easyocr.Reader(['vi', 'en'], gpu=True)
    doc = fitz.open(PDF_PATH)
    total_pages = len(doc)
    print(f"Tổng số trang PDF: {total_pages}")
    
    for ch in CHAPTERS:
        out_path = os.path.join(OUTPUT_DIR, ch["filename"])
        print(f"\n--- Bắt đầu xử lý: {ch['title']} (PDF p.{ch['start_pdf']} -> p.{ch['end_pdf']}) ---")
        t_start = time.time()
        
        md_content = []
        md_content.append(f"# {ch['title'].upper()}\n")
        md_content.append(f"Tài liệu gốc: [DICH HOC-TOANHOC-DOI SONG.pdf](file:///{PDF_PATH.replace(os.sep, '/')})  ")
        md_content.append(f"Phạm vi trang PDF: Trang {ch['start_pdf']} đến Trang {ch['end_pdf']}  ")
        md_content.append(f"Phương pháp trích xuất: Nhận dạng quang học ký tự toàn văn (OCR Engine: EasyOCR GPU, Tiếng Việt + Tiếng Anh)  ")
        md_content.append("\n---\n")
        
        for p_idx in range(ch['start_pdf'] - 1, ch['end_pdf']):
            pdf_page_num = p_idx + 1
            book_page_num = pdf_page_num - 13 if pdf_page_num >= 14 else f"Phụ lục/La Mã (PDF {pdf_page_num})"
            
            p_t0 = time.time()
            page = doc.load_page(p_idx)
            # Render at 180 DPI for optimal speed & accuracy
            pix = page.get_pixmap(dpi=180)
            img_bytes = pix.tobytes("png")
            nparr = np.frombuffer(img_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            ocr_res = reader.readtext(img)
            text = reconstruct_page_text(ocr_res)
            p_t1 = time.time()
            
            print(f"  [PDF p.{pdf_page_num:03d} / Sách p.{str(book_page_num):>4}] OCR thành công ({p_t1 - p_t0:.2f}s, {len(ocr_res)} khối chữ)")
            
            md_content.append(f"\n## TRANG SÁCH {book_page_num} (TRANG PDF {pdf_page_num})\n")
            md_content.append(text)
            md_content.append("\n\n---\n")
            
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md_content))
            
        t_elapsed = time.time() - t_start
        print(f"Đã lưu thành công: {ch['filename']} ({os.path.getsize(out_path):,} bytes, hoàn thành trong {t_elapsed:.1f}s)")
        
    print("\nHoàn tất 100% công tác số hóa toàn văn 10 phần của cuốn sách.")

if __name__ == "__main__":
    main()
