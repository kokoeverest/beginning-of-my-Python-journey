searched_book = input()
searched_books_count = 0

while True:
    book = input()

    if book == searched_book:
        print(f"You checked {searched_books_count} books and found it.")
        break

    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {searched_books_count} books.")
        break

    searched_books_count += 1

# Ани отива до родния си град след много дълъг период извън страната. Прибирайки се вкъщи, тя вижда старата/
# библиотека на баба си и си спомня за любимата си книга. Помогнете на Ани, като напишете програма, в която тя /
# въвежда търсената от нея книга (текст). Докато Ани не намери любимата си книга или не провери всички книги в /
# библиотеката, програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст), която тя /
# проверява. Книгите в библиотеката са свършили щом получите текст "No More Books".
#     • Ако не открие търсената книгата да се отпечата на два реда:
#     • "The book you search is not here!"
#     • "You checked {брой} books."
#     • Ако открие книгата си се отпечатва един ред:
#         ◦ "You checked {брой} books and found it."