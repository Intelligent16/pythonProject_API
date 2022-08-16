users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(f"Phone: {key}  User: {users[key]} ")

# Phone: +11111111  User: Tom
# Phone: +33333333  User: Bob
# Phone: +55555555  User: Alice

for key, value in users.items():
    print(f"Phone: {key}  User: {value} ")

# Phone: +11111111  User: Tom
# Phone: +33333333  User: Bob
# Phone: +55555555  User: Alice

print(f"{2*2}")
print(2*2)
