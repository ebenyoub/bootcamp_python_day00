import string


def text_analyzer(text=None, *args):
    """\n    This function counts the number of upper characters, \
        lower characters, punctuation and spaces in a given text."""
    if len(args) != 0:
        print("ERROR")
    else:
        char = upper = lower = p_mark = sp = 0
        if text is None:
            text = input("What is the text to analyse?\n>> ")
        for letter in text:
            if letter.isupper():
                upper += 1
            if letter.islower():
                lower += 1
            if letter in string.punctuation:
                p_mark += 1
            if letter in ' ':
                sp += 1
            char += 1
        print("The text contains " + str(char) + " characters:\n")
        print("- ", upper, " upper letter\n")
        print("- ", lower, " lower letter\n")
        print("- ", p_mark, " punctuation marks\n")
        print("- ", sp, " spaces\n")
