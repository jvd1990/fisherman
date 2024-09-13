# fisherman
import random
fish = int(input("How many kilos of fish did you catch: "))
lb = fish * 2.2046
dollar = lb*5

if lb > 50 :
    gift = random.randint(1,4)
if gift == 1:
    print("Congratulation you have won a fishing hat!!!")
    print(f"You will recive {dollar} $ for these {fish} of fish")
elif gift == 2:
    print("Congratulation you have won a fishing hook!!!")
    print(f"You will recive {dollar} $ for these {fish} of fish")
elif gift == 3:
    print("Congratulation you have won a fishing bucket!!!")
    print(f"You will recive {dollar} $ for these {fish} of fish")
elif gift == 4:
    print("Congratulation you have won a fishing boat!!!")
    print(f"You will recive {dollar} $ for these {fish} of fish")