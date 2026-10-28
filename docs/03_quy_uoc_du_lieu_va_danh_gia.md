# Quy ước dữ liệu và đánh giá

Tài liệu này phải được cả nhóm thống nhất trước khi bất kỳ thành viên nào viết notebook thực nghiệm.

## Quy ước dữ liệu

| Hạng mục | Quy ước |
| --- | --- |
| File gốc | `data/Craw_data/data.csv`, chỉ đọc, không chỉnh sửa trực tiếp |
| Nhãn | `diagnosis` với `B` là lành tính và `M` là ác tính |
| Mã hóa đề xuất | `B = 0`, `M = 1`; phải ghi rõ trong mọi notebook và báo cáo |
| Cột không dùng để dự đoán | `id` và các cột rỗng hoàn toàn nếu có, ví dụ `Unnamed: 32` |
| Dữ liệu thiếu | Kiểm tra trước khi xử lý; mọi quyết định loại/điền giá trị phải được ghi lại |
| Dòng trùng | Kiểm tra và ghi quyết định trước khi loại bỏ |

## Chia dữ liệu và tránh data leakage

- Chỉ dùng **một** train/test split: 80/20, `stratify=y`, `random_state=42`.
- Ba mô hình phải dùng đúng split này.
- Tập test chỉ được mở để đánh giá cuối cùng; không dùng để chọn siêu tham số.
- StandardScaler cần dùng cho SVM và KNN, và chỉ được fit trên dữ liệu train của từng fold.
- Decision Tree không bắt buộc chuẩn hóa, nhưng vẫn phải dùng cùng train/test split.
- Nếu dùng lựa chọn đặc trưng hoặc PCA cho mô hình, phép biến đổi cũng phải fit trong pipeline của fold huấn luyện.

## Tuning dự kiến

| Mô hình | Siêu tham số khởi đầu |
| --- | --- |
| SVM | `kernel`, `C`, `gamma`; `degree` chỉ khi dùng kernel poly |
| KNN | `n_neighbors`, `weights`, metric/khoảng cách |
| Decision Tree | `max_depth`, `min_samples_split`, `min_samples_leaf`, `criterion` |

Tiêu chí tuning chính dự kiến là **F1-macro trung bình qua cross-validation**. Đây là quyết định khởi đầu; mọi thay đổi sau này phải được ghi lại cùng lý do.

## Đánh giá cuối cùng

Nhóm sẽ báo cáo Accuracy, Precision, Recall, F1-score, ROC-AUC khi phù hợp, confusion matrix, thời gian tuning/huấn luyện nếu đo nhất quán, cùng mean và standard deviation qua cross-validation.

Recall của lớp ác tính `M` là chỉ số cần được ưu tiên khi thảo luận rủi ro bỏ sót ca ác tính. Tuy nhiên, không được chỉ dùng một metric để quyết định mô hình tốt nhất.
