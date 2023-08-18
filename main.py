from calculator import Calculator
from processor import Processor
from input_handler import taking_nums, inputs, num_for_calc

calculator = Calculator()
processor = Processor()

operations = {
    1: calculator.add,
    2: calculator.subtract,
    3: calculator.multiply,
    4: calculator.divide
}

num_for_calc()
inputs()
taking_nums()

while True:
    operation = operations.get(int(choice))
    if operation:
        result = numbers[0]
        for num in numbers[1:]:
            result = operation(result, num)
        print("Result:", result)
    else:
        print("Invalid input")

    choice = processor.take_choice_input("Do you want to perform another calculation? (yes/no): ", ['yes', 'no'])

    if choice.lower() == "no":
        break