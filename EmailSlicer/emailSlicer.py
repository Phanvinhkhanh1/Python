email = input("Please enter a email address: ").strip()

user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]

result = f"Your username is '{user_name}', and domain name is '{domain_name}'"

print(result)
