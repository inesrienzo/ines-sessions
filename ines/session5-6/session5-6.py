name = input("What is your name?")
age = input("How old are you?")
# print("Hello,", name, "!", sep="")

age = int(age)  # convert string to integer
birth_year = 2023 - age
print(name, ", You were born in", birth_year, ".", sep="")
print("hello,", name, "!", sep="")
