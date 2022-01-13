print("Whats the center letter?")
center = input(">")
print("What are the other letters? List all in a row, no delimiters")
inLetters = input(">")
letters=set((center))
for char in inLetters:
    letters.add(char)

alphabet={"a","b","c","d","e","f","g","h",
          "i","j","k","l","m","n","o","p",
          "q","r","s","t","u","v","w","x",
          "y","z"}
bad_letters=alphabet.difference(letters)
special={"-",".","!","'","0","1","2","3","4","5","6","7","8","9"}

words=open("english_words.txt")

wordlist = set(())
for word in words:
    wordlist.add(str(word).lower()[:-1])
soln = {}
for word in wordlist:
    if center in word:
        if len(word) > 3:
            if any(letter in bad_letters for letter in word) == False:
                if center in word:
                    if any(letter in special for letter in word) == False:
                        if len(word) in soln:
                            soln[len(word)].append(word)
                        else:
                            soln[len(word)] = [word]

for num in range(4,20):
    if num in soln:
        print("\n-->",num,"<------")
        count = 0
        for word in soln[num]:
            print("  ",word, end="")
            count += 1
            if count == 5:
                print() 
                count = 0
