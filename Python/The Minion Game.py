def minion_game(string):
    vowels = ["A", 'E', "I", "O", "U"]
    consonent = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    vowelCounter = 0
    consonentCounter = 0
    newstring = ""
    for i in range(0,len(string)):
        #print('string outside:' + newstring)
        for j in range(i, len(string) + 1):
            newstring = string[i:j]
            #for eachVowel in vowels:
            if newstring.startswith(tuple(vowels)):
                vowelCounter += 1
            elif newstring.startswith(tuple(consonent)):
                consonentCounter += 1
                
    if consonentCounter > vowelCounter:
        print('Stuart ' + str(consonentCounter))
    elif vowelCounter > consonentCounter:
        print('Kevin ' + str(vowelCounter))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
