print("Welcome to Dashboard")
print("1. View Products")
print("2. View Profile")
print("3. Logout")

choice = input("Enter your choice: ")

if choice == "1":
    print("Displaying Products...")
elif choice == "2":
    print("Displaying Profile...")
elif choice == "3":
    print("Logged out successfully!")
else:
    print("Invalid choice")