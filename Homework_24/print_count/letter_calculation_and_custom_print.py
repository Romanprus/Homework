import collections
import string
import os


def my_custom_print(*args, end='\n', sep=''):
    cust_print = sep.join(map(str, args)) + end
    os.write(1, cust_print.encode())


def letter_count(fileName):
    with open(fileName, 'r') as file:
        file_text = file.read()
        alphabet = string.ascii_lowercase
        text = file_text.lower()
        alphabet_set = set(alphabet)
        counts = collections.Counter(chars for chars in text if chars in alphabet_set)

    for letter in alphabet:
        print(f"{letter} {counts[letter]}")

    return counts


if __name__ == '__main__':
    letter_count('text-3.txt')

    my_custom_print("Hello Bohdan!")
