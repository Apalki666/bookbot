def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
#        print(file_contents)

def counting(text):
    countWords = len(text())
    print(countWords)

counting(file_contents)

if __name__ == "__main__":
    main()
