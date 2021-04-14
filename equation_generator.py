import operator
import random
import discord
from discord.ext import commands

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
        op1: int = random.randint(1, 10)
        op2: int = random.randint(1, 10)
        print("{} {} {} = ".format(op1, operation, op2))
        self.answer = self.operations[operation](op1, op2)
        return "{} {} {} = ".format(op1, operation, op2)

    def check_answer(self, answer: str):
        if int(answer):
            return self.answer == int(answer)
        else:
            return False
        