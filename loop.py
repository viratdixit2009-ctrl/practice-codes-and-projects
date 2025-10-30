count = 0
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
for x in range(start, end):
    count += 1 if x % 23 == 0 else 0
# print("Here we have {} numbers that are divisible by 23 between 99 and 1199".format(count))
print(f"We have {count} multiples of 23 between {start} and {end}")




    

