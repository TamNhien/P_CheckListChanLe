L = list(map(int, input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ").split(',')))
print(all((x + y) % 2 == 1 for x in L for y in L))

