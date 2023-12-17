num1 = input("Enter a number: ")
operator = input("Enter an operator(+,-,*,/): ")
num2 = input("Enter a second number: ")
answer = 0

if operator == "+":
    answer = int(num1) + int(num2)
elif operator == "-":
    answer =  int(num1) - int(num2)
elif operator == "*":
    answer = int(num1) * int(num2)
elif operator == "/":
    answer = int(num1) / int(num2)
else:
    answer = "Use Suggested Opterators"
print("Your answer is:", answer)
