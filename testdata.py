def is_safe_temperature(temp):
    return 0 <= temp <= 100

# TODO: Write test cases for boundary values
print(is_safe_temperature(-5))
print(is_safe_temperature(6))
print(is_safe_temperature(80))
print(is_safe_temperature(1243092394523948723948239487324983294872394872398472))

def ticket_price(age):
    if age < 5:
        return "Free"
    elif 5 <= age <= 17:
        return "$5"
    elif 18 <= age <= 64:
        return "$10"
    else:
        return "Senior Discount - $7"

# TODO: Write test cases for all paths
print(ticket_price(2))
print(ticket_price(10))
print(ticket_price(50))
print(ticket_price(109238019283091230182301923812093812093812034823495290437934613897461298346))


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input, numbers required"

# TODO: Write test cases for abnormal and faulty inputs
print(divide_numbers(5,0))
print(divide_numbers(324,'OHIO'))