def get_books(filename):
    books = []
    with open(filename, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.strip().split("|")
            parts[3] = int(parts[3])
            parts[4] = float(parts[4])
            books.append(parts)
    print(books)
    return books

def choice_books(books, keyword):
    choices = []
    for book in books:
        if keyword.lower() in book[1].lower():
            choices.append(book)

    print(choices)
    return choices

def count_books(books):
    count = []
    for book in books:
        isbn = book[0]
        total_value = round(book[3] * book[4], 2)
        count.append((isbn, total_value))
    print(count)
    return count
if __name__ == "__main__":
    all_books = get_books("books.csv")
    count_Bool = choice_books(all_books, input("Язык программирование: "))
    total = count_books(all_books)
