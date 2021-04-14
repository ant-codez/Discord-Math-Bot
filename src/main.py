import random
from database import Database
from equation_generator import EquationGenerator

# main function
def main(args=None):
    db = Database()
    e_generator = EquationGenerator()
    op_list = ["+", "*", "/", "-"]

    while True:
        # use a random operator
        op = op_list[random.randint(0, len(op_list) - 1)]
        print(e_generator.generate(op))
        answer = input(">> ")
        if e_generator.check_answer(answer):
            #db.increment_correct()
            print("Correct!")
        else:
            #db.increment_incorrect()
            print("Wrong! {}".format(e_generator.answer))

if __name__ == '__main__':
    main()
