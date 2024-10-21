import random

objectCount = {i: 0 for i in range(1, 46)}


def statistic(drew):
    for num in drew:
        objectCount[num] += 1


def draw():
    objectOptions = {i: i for i in range(1, 46)}
    drew = []
    for i in range(6):
        rand = random.randint(1, 45 - i)
        var1 = objectOptions[rand]
        var2 = objectOptions[45 - i]
        objectOptions[rand] = var2
        objectOptions[45 - i] = var1
        drew.append(var1)
    print(drew)
    statistic(drew)


def main():
    for _ in range(1000): # _ weil wir die variable nicht verwenden
        draw()

    print(objectCount)


if __name__ == "__main__":
    main()