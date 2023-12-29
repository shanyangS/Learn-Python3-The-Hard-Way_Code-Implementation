from sys import exit
# 当你遇到不理解的代码时，不要着急，只要在每行代码下面写下注释
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

"""
if 语句的规则：
每一个“if 语句”必须包含一个 else。

如果这个 else 永远都不应该被执行到，因为它本身没有任何意义，那你必须在 else 语句后面使用一个叫做 die 的函数，让它打印出错误信息并且死给你看，就像我们上节课做的那样，按照这个思路你可以找到很多错误。

“if 语句”的嵌套不要超过 2 层，最好尽量保持只有 1 层。

把“if 语句”当做段落来对待，其中的每一个 if, elif, else 就跟段落中的句子一样。在每句前后留一个空行以作区分。

你的布尔测试应该很简单，如果它们很复杂的话，你需要将它们的运算事先放到一个变量里，并且为变量取一个好名字。

如果你遵循上面的规则，你就会写出比大多数程序员都好的代码来。回到上一个练习中，看看我给出的代码有没有遵循这些规则，如果没有的话，就将其改正过来。
"""