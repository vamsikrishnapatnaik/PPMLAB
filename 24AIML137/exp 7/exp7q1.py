m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))

numbers = []
for i in range(m, n + 1):
    numbers.append(i)

print("List of numbers:", numbers)

total_sum = sum(numbers)
average = total_sum / len(numbers)
largest = max(numbers)
smallest = min(numbers)

print("Sum:", total_sum)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)

filtered_list = []
for num in numbers:
    if num % 3 != 0:
        filtered_list.append(num)

print("List excluding numbers divisible by 3:", filtered_list)