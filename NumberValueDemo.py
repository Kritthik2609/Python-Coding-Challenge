limit = int(input("Enter the limit: "))
num = int(input("Enter the number: "))
small = num
big = num

while limit>1:
    num=int(input("Enter the number: "))
    if num>big:
        big = num
    if num<small:
        small = num

    limit = limit - 1

print("The biggest number is", big)
print("The smallest number is", small)






