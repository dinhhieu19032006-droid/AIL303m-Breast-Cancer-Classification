# Môi trường phát triển

## Môi trường mục tiêu

Nhóm thống nhất chạy dự án trên **Conda base với Python 3.13.9**. Cả nhóm nên dùng cùng file `requirements.txt` để tránh khác biệt thư viện giữa các máy.

## Thư viện sử dụng

| Nhóm | Thư viện | Mục đích |
| --- | --- | --- |
| Dữ liệu | NumPy, pandas | Đọc, làm sạch và thao tác dữ liệu CSV |
| Machine Learning | scikit-learn | Chia dữ liệu, pipeline, chuẩn hóa, mô hình, tuning và metric |
| Trực quan hóa | matplotlib, seaborn | EDA, biểu đồ và confusion matrix |
| Notebook | JupyterLab, ipykernel, nbformat | Tạo, chạy và lưu notebook |
| Kiểm thử | pytest | Kiểm tra các thành phần dùng chung khi dự án có mã nguồn |

## Cài đặt trên Conda base

Mở **Anaconda Prompt**, bảo đảm đang ở môi trường `base`, rồi chạy:

```powershell
conda activate base
python --version
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Lệnh `python --version` phải hiển thị `Python 3.13.9` trước khi cài đặt.

## Đăng ký kernel Jupyter

Sau khi cài thư viện, chạy một lần từ thư mục dự án:

```powershell
python -m ipykernel install --user --name ail303m-base-py313 --display-name "AIL303m Python 3.13"
```

Sau đó mở JupyterLab:

```powershell
jupyter lab
```

Khi mở notebook của dự án, chọn kernel **AIL303m Python 3.13**.

## Kiểm tra nhanh trước khi làm notebook

```powershell
python -c "import numpy, pandas, sklearn, matplotlib, seaborn; print('Môi trường sẵn sàng')"
```

Nếu lệnh này chạy thành công, nhóm có thể bắt đầu giai đoạn EDA. Không cài thư viện riêng lẻ ngoài `requirements.txt` mà không cập nhật lại file này.
