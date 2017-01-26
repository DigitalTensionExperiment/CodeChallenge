

omega_string = "Write a subroutine"

def reverser(input):
    '''
    Takes an array of characters and returns
    an array of the same characters
    in reversed order with every consonant lower cased
    and every vowel upper cased ;
    '''

    reversed_array = []

    if input is not None:

        for letter in input:
            # every vowel upper cased
            if letter.lower() in ("a", "e", "i", "o", "u"):
                letter = letter.upper()
            # every consonant lower cased: range(65,90) are ASCII values for upper case letters
            elif ord(letter) in range(65,90):
                letter = letter.lower()
            # generate an array of the same characters in reversed order
            reversed_array.insert(0,letter)

        return reversed_array

    else:
        # If input is None: return an empty string
        return ""


def tester(omega_string):
    '''
    Prove your implementation works:

    calls reverser() and reverses omega_string (result_1);
    calls reverser() on result_1 (result_2);
    compares result_2 [in lower case] to omega_string [in lower case];

    '''

    result_1 = reverser(omega_string)

    result_2 = reverser(result_1)

    result_2 = ''.join(result_2)

    if omega_string.lower() == result_2.lower():
        print "Double reversal returns a string equivalent to the original: test passes;"
    else:
        print "Equivalent string was not returned: test failed;"



if __name__ == "__main__":

    tester(omega_string)

    print "//////////////////////////////////////////////////////////////"




