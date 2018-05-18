char=str(input())
if (char>='a' and char<='z')or(char>='A'and char<='Z'):
    if char in ['a','e','i','o','u']:
        print("vowel")
    else:
        print("consonant")
else:
    print("please enter a character")
