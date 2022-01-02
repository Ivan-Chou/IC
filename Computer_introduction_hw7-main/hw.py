class Judge:
    def __init__(self, answer: str) -> None:
        self.answer = int(answer)

        self.ansLength = len(answer) 
        """
        will be used in <function>:guess, 
        so set it here to reduce the time of counting again
        """

    def guess(self, num: str) -> bool:
        A, B = 0, 0

        ansStr = str(self.answer)
        
        for i in range(0, self.ansLength):
            if (num[i] in ansStr):
                if (num[i] == ansStr[i]): # same number at same place -> A
                    A += 1
                else: # at different place -> B 
                    B += 1

        print(f"Your guess is {num}; the result is {A}A{B}B")
        
        return (num == ansStr)


digits = {str(i) for i in range(0,10)}
"""
frequently used in <function>:read_input, 
so declare here to reduce the time of declaration
"""

def read_input(guess_len: int) -> str:
    print("Enter your guess:")
    
    while True:
        guess = input()

        if(len(guess) != guess_len):
            print("Invalid, please enter your guess again:")
            continue

        appeared = [False for i in range(0,10)]

        for c in guess:
            if (c not in digits)or(appeared[ int(c) ]): # has "not-numbers" or repeat
                print("Invalid, please enter your guess again:")
                break
            appeared[int(c)] = True
        else:
            return guess
        """
        should "continue" if it breaks out from the loop and "return" if doesn't, 
        but since it's the last condition in "while", I just skip the "continue"
        And there is a syntax called "for...else...", which statements in "else" 
        will be done only if the for loop doesn't "break" out.
        So I use it to simplfy my code of the "return" part.
        """


def enter_answer() -> str:
    return input()