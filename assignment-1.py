# Section 1
name = "Mauricio"
age = 30
height = 5.8
is_student = True

print(f"{name} {type(name)}")
print(f"{age} {type(age)}")
print(f"{height} {type(height)}")
print(f"{is_student} {type(is_student)}\n")

# Section 2
name = input("What is your name? ").strip()
birth_year = int(input("What year were you born? ").strip())
age = __import__("datetime").date.today().year - birth_year

print(f"Hi, {name}! You are approximately {age} years old.\n")

# Section 3
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

print(f"{num1} × {num2} = {num1 * num2:.2f}\n")

# Section 4
item_name = "Nintendo Switch™ 2 - The Legend of Zelda™ – 40th Anniversary Edition"
item_price = 519.99
item_quantity = 3

print("===========================")
print("         RECEIPT           ")
print("===========================")
print(f"Item:     {item_name}")
print(f"Price:    ${item_price:,.2f}")
print(f"Quantity: {item_quantity}")
print("---------------------------")
print(f"Total:    ${item_price * item_quantity:,.2f}")
print("===========================\n")

# Section 5
name = input("What is your name? ").lstrip()
hometown = input("What is your hometown? ").lstrip()
hobby = input("What is your favorite hobby? ").lstrip()
fact = input("What is one fun fact about yourself? ").lstrip()
birth_year = int(input("What year were you born? "))

print()
print("╔══════════════════════════════╗")
print(f"      PROFILE: {name}          ")
print("╚══════════════════════════════╝")
print(f"Hometown:   {hometown}")
print(f"Hobby:      {hobby}")
print(f"Fun fact:   {fact}")
print(f"Age:        {__import__("datetime").date.today().year - birth_year}")
