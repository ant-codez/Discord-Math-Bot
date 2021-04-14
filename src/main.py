import operator
import random

class EquationGenerator:
    def __init__(self):
        self.answer: int
        self.operations = {
            "+": operator.add,
            "*": operator.mul,
            "-": operator.sub,
            "/": operator.truediv,
        }

    # Generates an equation with one of the operations as a parameter: +, /, *, -
    def generate(self, operation: str): 
        op1: int = random.randint(0, 10)
        op2: int = random.randint(0, 10)
        print("{} {} {} = ".format(op1, operation, op2))
        self.answer = self.operations[operation](op1, op2)

    def check_answer(self, answer: str):
        return self.answer == int(answer)

# main function
def main(args=None):
    e_generator = EquationGenerator()
    op_list = ["+", "*", "/", "-"]

    while True:

        e_generator.generate(op_list[random.randint(0, len(op_list) - 1)])
        answer = input(">> ")
        if e_generator.check_answer(answer):
            print("Correct!")
        else:
            print("Wrong! {}".format(e_generator.answer))

if __name__ == '__main__':
    main()