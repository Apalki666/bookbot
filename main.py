def main():    
    book_path = "books/frankenstein.txt"    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)  
    report(book_path,num_words,chars_dict)

    

def report(book_path,num_words,chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print(" ")

    mydict = {}
    mylist = []
    for name in chars_dict:
        if name.isalpha():
            number = chars_dict[name]    
            mydict["name"] = name
            mydict["times"] = number
            mylist.append(mydict.copy()) 
            mylist.sort(reverse=True, key = sort_on)             
    Lname = [d.get("name") for d in mylist]       
    Lnumber = [d.get("times") for d in mylist]   
    for i in range (0, len(Lname)):
        print(f"The {Lname[i]} characte was found {Lnumber[i]} times")

    print(" ")
    print("--- End report ---")

def sort_on(mydict):
    return mydict["times"]

def sort_on(new_dict):
    return new_dict["times"]

def get_num_words(text):
    words = text.split()    
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

if __name__ == "__main__":
    main()
