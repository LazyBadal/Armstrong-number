#This shit took way to long abt 2 hours....

Number = int(input("Enter a 3 digit number: "))

num_str = str(Number)


First_digit = num_str[0]
Second_digit = num_str[1]
Third_digit = num_str[2]


first = int(First_digit)
second = int(Second_digit)
third = int(Third_digit)

Sum_number = ((first ** 3) + (second ** 3) + (third ** 3))

if Sum_number == Number:
    print("Armstrong Number")

else:
    print("Not Armstrong Number")

