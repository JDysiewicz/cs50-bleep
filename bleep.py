import cs50
import sys


def main():

    # error checking
    argc = len(sys.argv)
    if (argc != 2):
        print("Usage: python bleep.py dictionary")
        exit(1)
    try:
        banned = open(sys.argv[1])
    except FileNotFoundError:
        print("Usage: python bleep.py dictionary")
        exit(1)

    # get string then seperate into words with split, compare each word to those in dictionary, if lowercase version in dicitnoary then replace it in the string, continue
    inString = cs50.get_string("What message would you like to censor?\n")
    for x in inString.split():
        with open(sys.argv[1]) as file:
            if x.lower() in file.read():
                inString = inString.replace(x, ("*" * len(x)))
    print(inString)


if __name__ == "__main__":
    main()
