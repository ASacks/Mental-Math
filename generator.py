from random import randint
import time

class Addition:
    def __init__(self,number):
        self.number = number

    def generate(self):
        x = randint(-self.number,self.number)
        y = randint(-self.number,self.number)
        return x,y

    def display(self,x,y):
        if y < 0:
            print(f"{x} + ({y})")
        else:
            print(f"{x} + {y}")

    def answer(self,x,y):
        correct = x + y
        response = int(input())
        if response == correct:
            return True
        else:
            return False

class Game:
    def __init__(self,numadd,nummultiply):
        self.add = Addition(numadd)

    def start(self,num):
        correct = 0
        while num > correct:
            x,y = self.add.generate()
            self.add.display(x,y)
            if self.add.answer(x,y):
                correct += 1
            else:
                correct -= 1

    def play(self,num):
        self.start(num)

# s = Game(10,10)
# s.start(5)
total = 0
for j in range(1000000):

    result = 0
    for i in range(30):
        x = randint(100,1001)
        result = max(result,x)

    total += result

print(total/1000000)

