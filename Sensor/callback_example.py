# example 1
class Calculator:
    def __init__(self):
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def add(self, a, b):
        result = a + b
        if self.callback:
            self.callback(result)

    def subtract(self, a, b):
        result = a - b
        if self.callback:
            self.callback(result)

    def multiply(self, a, b):
        result = a * b
        if self.callback:
            self.callback(result)

    def divide(self, a, b):
        if b == 0:
            print("Error: Division by zero")
            return
        result = a / b
        if self.callback:
            self.callback(result)

# the callback has been introduced. we can not set it as any function and the class will run with such function as callback

# Callback function example
def handle_result(result):  # this is the callback function that will be used in Calculator
    print("Result:", result)
def giveBack(result):
    print("This is the result of the operation:", result)

# Example usage
calc = Calculator()
calc.set_callback(giveBack)

calc.add(5, 3)  # Output: Result: 8
calc.subtract(10, 4)  # Output: Result: 6
calc.multiply(6, 2)  # Output: Result: 12
calc.divide(10, 2)  # Output: Result: 5.0

# --------------------------------

# example 2

class DataProcessor:
    def __init__(self, dataset):
        self.dataset = dataset
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def process_data(self):
        for data in self.dataset:
            # Perform some data processing
            processed_data = data * 2
            # Notify the user via callback function
            if self.callback:
                self.callback(processed_data)

# Callback function example
def handle_processed_data(data):
    print("Processed data:", data)

# Example usage
dataset = [1, 2, 3, 4, 5]
processor = DataProcessor(dataset)
processor.set_callback(handle_processed_data) # set the callback function as handle_processed_data
processor.process_data()

# --------------------------

# example 3

class Example:
    def __init__(self, stringa):
        self.stringa = stringa
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def Return(self):
        if len(self.stringa) > 2:
            if self.callback:
                self.callback(self.stringa)
        else:
            return "String length is less than 2"



def Lenght_string(data):
    print(f"the length of the word {data} is higher than 2")

stringa = "Inter"
ex = Example(stringa)
ex.set_callback(Lenght_string)
ex.Return()

# -------------------

# Example 4

class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def process_numbers(self):
        if self.callback:
            self.numbers = [self.callback(num) for num in self.numbers]

# Callback function example: Doubling the number
def double_number(num):
    return num * 2

# Callback function example: Squaring the number
def square_number(num):
    return num ** 2

# Example usage
numbers = [1, 2, 3, 4, 5]
processor = NumberProcessor(numbers)

# Set callback to double the numbers
processor.set_callback(double_number)
processor.process_numbers()
print("Doubled numbers:", processor.numbers)

# Set callback to square the numbers
processor.set_callback(square_number)
processor.process_numbers()
print("Squared numbers:", processor.numbers)





