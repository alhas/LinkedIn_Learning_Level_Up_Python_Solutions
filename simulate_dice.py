import random
import pandas as pd


def roll_dice_legacy(one: int, two: int, three: int, play_count: int):
    dice_one = [_+1 for _ in range(one)]
    dice_two = [_+1 for _ in range(two)]
    dice_three = [_+1 for _ in range(three)]

    played = []
    for _ in range(play_count):
        played.append(random.choice(dice_one) +
                      random.choice(dice_two) +
                      random.choice(dice_three))

    count_of_occurence = {}
    for x in range(3, 17):
        count_of_occurence.update({x: played.count(x)})

    data = {
        'Number': [key for key in count_of_occurence],
        'Persentage': [f"{(value/play_count)*100:.2f}%" for value in count_of_occurence.values()]
    }
    print(pd.DataFrame(data))

# roll_dice(4, 6, 6, 1_000_000)


def roll_dice(*dices, play_count):
    played = []
    for _ in range(play_count):
        played.append(sum((random.randint(1, x) for x in dices)))
    count_of_occurence = {}
    for x in range(len(dices), sum(dices)+1):
        count_of_occurence.update({x: played.count(x)})

    data = {
        'Number': [key for key in count_of_occurence],
        'Persentage': [f"{(value/play_count)*100:.2f}%" for value in count_of_occurence.values()]
    }
    print(pd.DataFrame(data))


roll_dice(4, 6, 6, 21, play_count=1_000_000)
