from ebook import Ebook
def main():
    my_book = Ebook("Lord of the Rings: The Two Towers","J.R.R. Tolkien",413)
    my_book.open_book()
    my_book.display_status()

    i = 1
    while i < 35:
        my_book.go_to_next_page()
        i +=1
    my_book.display_status()

    my_book.close_book()
    my_book.go_to_next_page()
    my_book.go_to_next_page()
    my_book.go_to_next_page()
    my_book.go_to_next_page()
    my_book.display_status()

if __name__ == "__main__":
   main() 

    