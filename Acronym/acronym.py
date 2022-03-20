user_input = str(input("Please enter a phrase: "))
text = user_input.split(" ")
result = ""
for i in text:
    result += i[0].upper()
print(result)
