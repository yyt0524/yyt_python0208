import random


def sele_random():
    red_balls = [x for x in range(1, 34)]
    sele_balls = []
    sele_balls = random.sample(red_balls, 6)
    sele_balls.sort()
    sele_balls.append(random.randint(1,16))
    return sele_balls

print(sele_random())