# Quy trình dự án

## Tổng quan pipeline

```text
Dữ liệu gốc
  -> Xác minh và khám phá dữ liệu
  -> Tiền xử lý có kiểm soát
  -> Baseline và tuning từng mô hình
  -> Đánh giá trên tập test độc lập
  -> Tổng hợp báo cáo và slide
```

## Giai đoạn 1 - Chốt đề tài và xác minh dataset

**Mục tiêu:** xác nhận chủ đề, nguồn dữ liệu và cấu trúc CSV thực tế.

**Công việc:**

- Đối chiếu file CSV với mô tả của Breast Cancer Wisconsin Diagnostic.
- Kiểm tra số hàng, số cột, tên cột, nhãn `B/M`, cột `id` và cột rỗng dư thừa nếu có.
- Lưu nguyên vẹn file gốc trong `data/Craw_data/`.

**Đầu ra:** brief đã chốt và ghi nhận nguồn dữ liệu.

## Giai đoạn 2 - Khám phá và tiền xử lý

**Mục tiêu:** hiểu dữ liệu và chuẩn bị đầu vào công bằng cho cả ba mô hình.

**Công việc dự kiến:**

- Kiểm tra dữ liệu thiếu, trùng lặp, kiểu dữ liệu, phân bố lớp và tương quan đặc trưng.
- Loại `id` và cột rỗng hoàn toàn nếu xác nhận là cột kỹ thuật.
- Xác định `X` là đặc trưng số, `y` là `diagnosis`.
- Mã hóa nhãn theo một quy ước duy nhất và ghi rõ quy ước đó.
- Chia train/test 80/20 theo `stratify`, dùng `random_state=42`.

**Đầu ra:** notebook EDA, mô tả các quyết định làm sạch và quy tắc chia dữ liệu.

## Giai đoạn 3 - Baseline và tuning

**Mục tiêu:** mỗi thành viên thử nghiệm một mô hình, nhưng dùng chung dữ liệu và tiêu chí.

**Công việc dự kiến:**

- Xây dựng baseline cho SVM, KNN và Decision Tree.
- Dùng StratifiedKFold 5 folds và GridSearchCV trên tập train.
- Chỉ fit scaler và lựa chọn đặc trưng bên trong pipeline/fold huấn luyện.

**Đầu ra:** notebook riêng cho từng mô hình, cấu hình tuning và log kết quả cross-validation.

## Giai đoạn 4 - Đánh giá và đối sánh

**Mục tiêu:** đánh giá một lần trên tập test chưa từng tham gia tuning.

**Công việc dự kiến:**

- Tạo bảng đối sánh metric của ba mô hình.
- Phân tích confusion matrix và ROC curve khi phù hợp.
- Đối chiếu điểm cross-validation với điểm test; giải thích khác biệt thay vì chỉ chọn số lớn nhất.

**Đầu ra:** bảng kết quả, biểu đồ và phần nhận xét dựa trên bằng chứng.

## Giai đoạn 5 - Hoàn thiện báo cáo

**Mục tiêu:** biến kết quả thành báo cáo và slide nhất quán.

**Công việc dự kiến:**

- Viết báo cáo mini capstone bằng tiếng Việt.
- Nêu hạn chế dữ liệu, nguy cơ overfitting và giới hạn tổng quát hóa.
- Chuẩn bị slide và luyện giải thích về tiền xử lý, tuning, metric và kết luận.

**Đầu ra:** báo cáo, slide và phần trả lời câu hỏi.
