import random
from equation_generator import EquationGenerator

# main function
def main(args=None):
    e_generator = EquationGenerator()
    op_list = ["+", "*", "/", "-"]

    while True:

        # use a random operator
        op = op_list[random.randint(0, len(op_list) - 1)]
        print(e_generator.generate(op))
        answer = input(">> ")
        if e_generator.check_answer(answer):
            print("Correct!")
        else:
            print("Wrong! {}".format(e_generator.answer))

if __name__ == '__main__':
    main()