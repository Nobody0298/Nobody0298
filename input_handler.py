from processor import Processor

processor = Processor()

def taking_nums():
    while True:
        numbers = processor.take_calculation_inputs()
        if numbers is None:
            continue
        return numbers


def inputs():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = processor.take_choice_input("Enter choice (1/2/3/4): ", ['1', '2', '3', '4'])
        processor.validate_choice(int(choice))
        return choice


def num_for_calc():
    while True:
        try:
            num_of_calc = int(input("how many numbers do you want to use for the calculation? "))
            return num_of_calc
        except ValueError:
            print('Please give a valid number')