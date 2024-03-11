<<<<<<< HEAD
=======
def add(x, y):
    return x + y


>>>>>>> 173655e7d32d70f9efd603ad619a85cde07a0443
def operation(num1, operator, num2):

    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)


num1 = int(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
num2 = int(input("두 번째 숫자를 입력하세요: "))

result = operation(num1, operator, num2)
print(f"계산 결과: {result}")
