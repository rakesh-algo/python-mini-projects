'''
Python identifier must follow below rules:
1. Must begin with an alphabet or underscore.
2. Must be made of alphabets, digits, underscore.
3. Must not use builtin functions and constants.
4. Must not use keywords.
'''

import keyword

def check_first_character(ch):
    return (
        (ord(ch) >= 65 and ord(ch) <= 90) # check whether it's an uppercase
        or
        (ord(ch) >= 97 and ord(ch) <= 122) # check whether it's a lowercase
        or
        (ord(ch) == 95) #check whether it's an underscore
    )

def check_identifier(name):
    if name and check_first_character(name[0]):
        if name.isidentifier():
            try:
                dir(__builtins__).index(name)
            except ValueError:
                if keyword.iskeyword(name):
                    print('Invalid identifier...must not use keywords.')
                else:
                    print('Valid identifier.')
            else:
                print('Invalid identifier...must not use builtin functions and constants.')
        else:
            print('Invalid identifier...must be made of alphabets, digits and underscore.')
    else:
        print('Invalid identifier...must begin with an alphabet or underscore.')

def main():
    while True:
        name = input('Enter a string - \'quit\' to stop: ')
        if name.lower().strip() == 'quit':
            break
        check_identifier(name)

if __name__ == '__main__':
    main()