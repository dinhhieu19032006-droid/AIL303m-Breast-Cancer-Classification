# Train test split dùng chung

Thư mục này sẽ được tạo dữ liệu bởi notebook `notebooks/02_thiet_lap_du_lieu_thi_nghiem.ipynb`.

Khi notebook chạy lần đầu, nó tạo ba file:

- `train_indices.csv` - chỉ số dòng thuộc tập train.
- `test_indices.csv` - chỉ số dòng thuộc tập test.
- `split_metadata.json` - tham số split, phân bố nhãn và SHA-256 của file dữ liệu sạch.

Ba file này được `.gitignore` bỏ qua cho đến khi nhóm thống nhất kết quả split và chủ động quyết định theo dõi chúng bằng Git. Không tự ý sửa hoặc tạo lại một phần file trong ba file trên.
