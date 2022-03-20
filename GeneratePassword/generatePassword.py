import random

length_of_password = int(input("Please enter length of password : "))

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

generated_password = "".join(random.sample(s, length_of_password))
print(generated_password)
