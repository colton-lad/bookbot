def sortOn(dict):
    return dict["num"]

def countWords(text):
    wordList = text.split()

    return len(wordList)

def countChars(text):

    charCount = {}
    charList = []

    for ch in text.lower():
        if ch.isalpha() == False:
            continue

        if ch in charCount:
            charCount[ch] += 1
        else:
            charCount[ch] = 1

    for ch in charCount:
        charList.append({"char": ch, "num": charCount[ch]})

    return charList

def main():
    path = "./books/frankenstein.txt"
    fileContents = ""

    with open(path) as f:
        fileContents = f.read()

    # print(fileContents)
    wordCount = countWords(fileContents)
    charCount = countChars(fileContents)
    charCount.sort(reverse=True, key=sortOn)
    print(f"--- Begin report of {path} ---")
    print(f"{wordCount} words found in the document")
    # print(charCount)
    for dict in charCount:
        print(f"The {dict['char']} character was found {dict['num']} times")

main()