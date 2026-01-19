class Ebook():
    def __init__(self,title,author,page_amount):
        self.title = title
        self.author = author
        self.page_amount = page_amount
        self.current_page = 1
        self.is_open = False
    
    def open_book(self):
        self.is_open = True
    
    def close_book(self):
        self.is_open = False
    
    def set_page_number(self,new_page_number):
        self.current_page = new_page_number
    
    def go_to_next_page(self):
        if self.is_open:
            if self.current_page < self.page_amount:
                self.current_page += 1
        else:
            print("Can't perform action - book is closed.")
    
    def go_to_prev_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.page_amount -= 1
        else:
            print("Can't perform action - book is closed.")
    
    def display_status(self):
        if self.is_open:
            print(f"Book status:\n{"-" * 20}")
            print(f"Currently reading: '{self.title}', written by '{self.author}'.\nNumber of pages: {self.page_amount} pages.\nCurrent page number: {self.current_page}\n{"-" * 20}\n")
        elif not self.is_open:
            print("Book is closed.")
        
    
    
    
