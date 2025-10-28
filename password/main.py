import bcrypt

password ="test"
hashed = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode()
print(hashed)

print(bcrypt.checkpw(password.encode("utf-8"),hashed.encode()))

