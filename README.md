# Mini Capstone Machine Learning

## So sánh SVM KNN và Decision Tree trong phân loại khối u vú

Đây là workspace cho mini capstone môn Machine Learning. Nhóm nghiên cứu bài toán phân loại khối u vú lành tính (`B`) và ác tính (`M`) trên bộ dữ liệu Breast Cancer Wisconsin Diagnostic.

Ở thời điểm hiện tại, dự án đang ở giai đoạn **chốt đề tài, xác minh dữ liệu và chuẩn bị quy trình**. Chưa có mã nguồn huấn luyện, notebook thực nghiệm hoặc kết luận về mô hình tốt nhất.

## Cấu trúc dự án

| Thư mục | Vai trò | Trạng thái hiện tại |
| --- | --- | --- |
| `data/` | Dữ liệu gốc và dữ liệu đã xử lý | Đã có CSV gốc trong `data/Craw_data/` |
| `docs/` | Đề cương, quy trình, phân công và quy ước báo cáo | Đang sử dụng |
| `notebooks/` | Notebook khám phá dữ liệu và thực nghiệm sau này | Chưa tạo notebook |
| `src/` | Mã nguồn dùng chung sau này | Chưa tạo mã nguồn |
| `reports/` | Báo cáo và nội dung slide | Chưa tạo báo cáo |
| `outputs/` | Bảng kết quả và biểu đồ sinh ra từ thực nghiệm | Chưa có kết quả |

## Tài liệu cần đọc trước

1. `docs/01_de_cuong_va_pham_vi.md` - chủ đề, mục tiêu và ranh giới dự án.
2. `docs/02_quy_trinh_du_an.md` - pipeline 5 giai đoạn của nhóm.
3. `docs/03_quy_uoc_du_lieu_va_danh_gia.md` - các quy ước phải thống nhất trước thực nghiệm.
4. `docs/04_phan_cong_va_tien_do.md` - nhiệm vụ của ba thành viên và mốc tiến độ.
5. `docs/05_moi_truong_phat_trien.md` - môi trường Python 3.13 và thư viện dùng chung.

## Nguyên tắc làm việc

- Giữ nguyên dữ liệu gốc trong `data/Craw_data/`; không sửa trực tiếp file CSV gốc.
- Mọi thành viên phải dùng cùng quy tắc chia train/test và cùng tiêu chí đánh giá.
- Chỉ được dùng tập test để đánh giá cuối cùng, sau khi hoàn tất tuning trên tập train.
- Không tuyên bố mô hình tốt nhất trước khi có số liệu thực nghiệm.
- Đây là nghiên cứu học máy phục vụ học phần, không phải công cụ chẩn đoán lâm sàng.
