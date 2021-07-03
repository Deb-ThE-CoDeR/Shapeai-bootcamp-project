import hashlib

# initializing string
print("Enter a string please:-")
str2hash = input()

result = hashlib.md5(str2hash.encode())
result1=hashlib.sha1(str2hash.encode())
result2=hashlib.sha512(str2hash.encode())

# printing the equivalent hexadecimal value.

print("The hexadecimal equivalent of  MD5 hash is : ", end="")
print(result.hexdigest())
print("\n")
print("The hexadecimal equivalent of  sha1 hash is : ", end="")
print(result1.hexdigest())
print("\n")
print("The hexadecimal equivalent of  sha512 hash is : ", end="")
print(result2.hexdigest())