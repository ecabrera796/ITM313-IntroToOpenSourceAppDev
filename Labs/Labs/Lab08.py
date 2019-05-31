import array as arr

arr = []
for i in range(6):
    num = int(input("Please enter a number: ").format(i))
    arr.append(num)

arr.sort()
print("Sorted list of numbers in ascending order:", arr)

arr.sort(reverse=True)
print("Sorted list of numbers in descending order:", arr)
