print("NHAP DOANH THU CAC NGAY TRONG TUAN")

total_revenue = 0
target_days = 0

for day in range(1, 8):
    revenue = int(input(f"Nhap doanh thu Ngay {day}: "))
    total_revenue = total_revenue + revenue
    if revenue >= 5000000:
        target_days = target_days + 1

average_revenue = total_revenue / 7

print("--- BAO CAO DOANH THU TUAN RIKKEI STORE ---")
print(f"Tong doanh thu ca tuan: {total_revenue} VND")
print(f"Doanh thu trung binh moi ngay: {int(average_revenue)} VND")
print(f"So ngay dat doanh thu muc tieu (≥ 5,000,000 VND): {target_days} ngay")