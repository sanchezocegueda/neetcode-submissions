def divide_numbers(a: str, b: str) -> None:
    try:
        a, b = int(a), int(b)
        res = a / b
        print(res)
    except ValueError as e:
        print("Error: Invalid value!")
    except ZeroDivisionError as e:
        print("Error: Division by zero!")
    except Exception as e:
        print("An error occurred:", e)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
