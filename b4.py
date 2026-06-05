branch_quantity = int(input("\nNhập số lượng chi nhánh: "))
for branch in range(branch_quantity):
    for class_room in range(2):
        print(f"Chi nhánh {branch + 1}: ")
        student_quantity = int(input(f"Nhập số học viên đi học của lớp {class_room + 1}:"))
        while student_quantity < 0:
            print("Số học viên không hợp lệ. Vui lòng nhập lại")
            student_quantity = int(input(f"Nhập số học viên đi học của lớp {class_room + 1}:"))
        if student_quantity > 20:
            print("Lớp học ổn định")
        elif student_quantity == 0:
            print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
            continue
        else:
            print("Lớp cần được nhắc nhở theo dõi")
    