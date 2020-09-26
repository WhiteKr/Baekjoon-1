from sys import stdin
from collections import Counter

input = stdin.readline

def main():
    money = []

    for _ in range(int(input())):
        dice = Counter(map(int, input().split()))
        pair = list(dice.values()).count(2)
        key, val = dice.most_common(1)[0]

        if val == 4: temp = key * 5000 + 50000
        elif val == 3: temp = key * 1000 + 10000
        elif val == 2:
            if pair == 2: temp = sum(dice.keys()) * 500 + 2000
            elif pair == 1: temp = key * 100 + 1000
        else: temp = max(dice.keys()) * 100

        money.append(temp)

    print(max(money))

if __name__ == '__main__':
    main()