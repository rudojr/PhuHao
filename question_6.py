def edit_distance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m - 1] == str2[n - 1]:
        return edit_distance(str1, str2, m - 1, n - 1)

    return 1 + min(edit_distance(str1, str2, m, n - 1),  # Chèn
                   edit_distance(str1, str2, m - 1, n),  # Xóa
                   edit_distance(str1, str2, m - 1, n - 1)  # Thay thế
                   )

def calculate_edit_distance(str1, str2):
    return edit_distance(str1, str2, len(str1), len(str2))

str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

print("Khoảng cách chỉnh sửa giữa hai chuỗi là:", calculate_edit_distance(str1, str2))