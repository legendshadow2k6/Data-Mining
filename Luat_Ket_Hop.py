list = ["Facebook", "Messenger"],["Facebook", "YouTube"],["Facebook", "Messenger", "YouTube"],["YouTube", "TikTok"],["Facebook", "Messenger"]

ve_trai = input("Nhap ve trai(A): ")
ve_phai = input("Nhap ve phai(B): ")

#Tong danh sach
total = len(list)

cout_A = 0
cout_B = 0
cout_AB = 0

#Dem so lan
for i in list:
    if ve_trai in i:
        cout_A+=1
    if ve_phai in i:
        cout_B+=1
    if ve_trai in i and ve_phai in i:
        cout_AB+=1

#Tinh Support
support_AB = cout_AB/total
support_A = cout_A/total
support_B = cout_B/total

#Tinh Confidence
confidence_AB = support_AB/support_A

#Tinh Lift
lift_AB = confidence_AB/support_B

print(f"Số lần mở {ve_trai}: {cout_A}")
print(f"Số lần mở {ve_phai}: {cout_B}")
print(f"Số lần mở cả 2: {cout_AB}")

print(f"Có khoảng {support_AB*100}% sử dụng cả {ve_trai} và {ve_phai}")
print(f"Trong các người dùng {ve_trai}, {confidence_AB*100}% sẽ sử dụng thêm {ve_phai}")

if lift_AB > 1:
    print(f"Ứng dụng {ve_trai} và {ve_phai} có liên quan đến nhau")
elif lift_AB == 1:
    print(f"Ứng dụng {ve_trai} và {ve_phai} chỉ có yếu tố ngẫu nhiên")
else:
    print(f"Ứng dụng {ve_trai} và {ve_phai} ít liên quan đến nhau")