import random2

answer = random2.randint(1,10)
#print(f'answer is {answer}')

while True:
    try:
        guess = int(input("Guess a number 1~10:..."))
        if 0 < guess < 11:
            if guess == answer:
                print("Hey you are a genies")
                break
        else:
            print("Hey : I said 1~10")
    except ValueError:
        print("Please enter number 1~10")
        continue


