number_list = []
while True:
    num = input("enter number here:")

    if num == "":
        break
    number_list.append(int(num))

print(number_list)

result = 0
for num in number_list:
    result = result + num
print(result)