# Đề cương và phạm vi dự án

## Chủ đề

**So sánh hiệu quả của SVM, K-Nearest Neighbors và Decision Tree trong phân loại khối u vú lành tính và ác tính.**

Tên tiếng Anh: *Comparative Analysis of SVM, K-Nearest Neighbors, and Decision Tree for Breast Cancer Diagnosis Classification.*

## Bài toán

Từ các đặc trưng số được trích xuất từ ảnh chọc hút kim nhỏ (FNA), dự đoán nhãn `diagnosis`:

- `B` - Benign, lành tính.
- `M` - Malignant, ác tính.

Đây là bài toán phân loại nhị phân có giám sát. Dự án chỉ phục vụ mục đích học tập và so sánh thuật toán, không cung cấp chẩn đoán y khoa.

## Dataset

- Tên dự kiến: Breast Cancer Wisconsin Diagnostic.
- Nguồn Kaggle: <https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data>.
- Nguồn tham chiếu UCI: <https://archive.ics.uci.edu/dataset/17/breast-cancer-wisconsin-diagnostic>.
- File nhóm đang giữ: `data/Craw_data/data.csv`.

Trước khi thực nghiệm, nhóm phải xác minh trực tiếp trên CSV số hàng, số cột, kiểu dữ liệu và tên cột để bảo đảm đúng bản Diagnostic, không dựa hoàn toàn vào mô tả trên Internet.

## Mục tiêu

1. Khám phá, kiểm tra chất lượng và tiền xử lý dữ liệu một cách tái lập được.
2. Xây dựng baseline và tuning cho SVM, KNN, Decision Tree.
3. So sánh hiệu năng, lỗi dự đoán, thời gian và khả năng diễn giải của ba mô hình.
4. Trả lời các câu hỏi nghiên cứu sau bằng số liệu thực nghiệm.

## Câu hỏi nghiên cứu

- RQ1: Thuật toán nào đạt kết quả tốt nhất trên dataset này?
- RQ2: Thay đổi siêu tham số ảnh hưởng thế nào đến từng thuật toán?
- RQ3: Mô hình nào cân bằng tốt giữa các chỉ số phân loại, khả năng nhận diện lớp ác tính và thời gian huấn luyện?
- RQ4: Hạn chế nào của dữ liệu hoặc phương pháp làm giảm khả năng tổng quát hóa?

## Ngoài phạm vi hiện tại

- Không xây dựng hệ thống dự đoán để sử dụng trong lâm sàng.
- Không thu thập thêm dữ liệu bệnh nhân hoặc dữ liệu nhạy cảm.
- Không dùng mô hình deep learning.
- Không kết luận mô hình thắng khi chưa hoàn tất quy trình đánh giá đã thống nhất.
