from rich import print

def divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError as e:
        error_message = f"[red]Error[/red]: You have encountered [blue][link=https://docs.python.org/3/library/exceptions.html#ZeroDivisionError]ZeroDivisionError[/blue]"
        print(error_message)
        raise e

if __name__ == "__main__":
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    try:
        result = divide(numerator, denominator)
        print(f"Result: {result}")
    except ZeroDivisionError:
        pass  # Handle the error as needed
