# Import các thư viện cần thiết
from sklearn.linear_model import LinearRegression
import numpy as np

# --- 1. Chuẩn bị dữ liệu (Giả định) ---
# Hãy tưởng tượng chúng ta có dữ liệu về diện tích nhà (X) và giá nhà (y)
# X: Diện tích (mét vuông)
X_train = np.array([[50], [70], [100], [120], [150]])
# y: Giá nhà (triệu đồng)
y_train = np.array([1000, 1500, 2200, 2700, 3300])

# --- 2. Khởi tạo mô hình ---
# Chúng ta chọn mô hình Hồi quy tuyến tính (Linear Regression)
model = LinearRegression()
print(f"Trạng thái mô hình trước khi huấn luyện: {model}")

# --- 3. Huấn luyện mô hình (Training) ---
# Đây là bước "train model". Chúng ta cung cấp dữ liệu (X_train, y_train)
# để mô hình học được mối quan hệ giữa diện tích và giá nhà.
# Phương thức .fit() chính là quá trình huấn luyện.
print("\nBắt đầu quá trình huấn luyện...")
model.fit(X_train, y_train)
print("Quá trình huấn luyện đã hoàn tất!")

# --- 4. Kiểm tra mô hình đã học ---
# Sau khi huấn luyện, mô hình đã học được các tham số (coefficients)
print(f"\nTrạng thái mô hình sau khi huấn luyện:")
print(f"  - Hệ số góc (slope/coefficient): {model.coef_[0]:.2f}")
print(f"  - Hệ số chặn (intercept): {model.intercept_:.2f}")

# --- 5. Sử dụng mô hình đã huấn luyện để dự đoán ---
# Giờ đây, chúng ta có thể dùng mô hình để dự đoán giá cho một căn nhà mới
dien_tich_nha_moi = np.array([[150]]) # Nhà mới rộng 150 m2
gia_nha_du_doan = model.predict(dien_tich_nha_moi)
print(f"\nDự đoán giá cho căn nhà {dien_tich_nha_moi[0][0]} m2: {gia_nha_du_doan[0]:.2f} triệu đồng")

dien_tich_nha_moi_2 = np.array([[200]]) # Nhà mới rộng 200 m2
gia_nha_du_doan_2 = model.predict(dien_tich_nha_moi_2)
print(f"Dự đoán giá cho căn nhà {dien_tich_nha_moi_2[0][0]} m2: {gia_nha_du_doan_2[0]:.2f} triệu đồng")