import numpy as np

# Aggregate functions = summarize data and typically
#                       return a single value

array = np.array([[ 1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array)) # trung bình
# độ lệch chuẩn CT: σ=sqrt(N∑i=1 (Xi−μ)2/N)
# μ: giá trị trung bình

# Độ lệch chuẩn là một thước đo thống kê để mô tả mức độ phân tán của dữ liệu. Nó cho bạn biết trung bình các điểm dữ liệu cách xa giá trị trung bình (mean) bao nhiêu.
# Nếu độ lệch chuẩn nhỏ, các điểm dữ liệu tập trung gần giá trị trung bình.
# Nếu độ lệch chuẩn lớn, các điểm dữ liệu phân tán rộng.

print(np.std(array))

# σ^2 (Phương sai)
# Phương sai là giá trị trung bình của bình phương khoảng cách từ mỗi điểm dữ liệu đến giá trị trung bình (mean) của toàn bộ dữ liệu.
# Nó cung cấp một con số để đánh giá mức độ các điểm dữ liệu phân tán rộng như thế nào.

print(np.var(array))

# print(np.min(array))
# print(np.max(array))
print(np.argmin(array))
print(np.argmax(array))

print(np.sum(array, axis=0)) # sum chiều dọc
print(np.sum(array, axis=1)) # sum chiều ngang