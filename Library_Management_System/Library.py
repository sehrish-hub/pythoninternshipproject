import csv
import datetime
# Constants
csv_file = 'library_data.csv'
checkout_time = 14  # days
# Functions
def my_library_data():
    """Load library data from CSV file or initialize with some books if file is missing."""
    library_data = {}
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                book_id = row['Book ID']  # Assuming 'Book ID' is a column in your CSV file
                library_data[book_id] = {
                    'Title': row['Title'],
                    'Author': row['Author'],
                    'Status': row['Status'],
                    'Due Date': row['Due Date'] if row['Due Date'] else None  # Handle empty due dates
                }
        # print("Library data loaded from CSV:")
        # print(library_data)
    except FileNotFoundError:
        print("Library data file not found. Creating a new one with default books.")
        library_data = {"""
            'book1': {'Title': "Alice's Adventures in Wonderland", 'Author': "Lewis Carroll", 'Status': 'Available', 'Due Date': '2024-10-20'},
            'book2': {'Title': "1984", 'Author': "George Orwell", 'Status': 'Available', 'Due Date': '2024-10-12'},
            'book3': {'Title': "The Great Gatsby", 'Author': "F. Scott Fitzgerald", 'Status': 'Available', 'Due Date': '2024-10-10'},
            'book4': {'Title': "To Kill a Mockingbird", 'Author': "Harper Lee", 'Status': 'Available', 'Due Date': '2024-10-10'},
            'book5': {'Title': "Pride and Prejudice", 'Author': "Jane Austen", 'Status': 'Available', 'Due Date': '2024-10-30'},
            'book6': {'Title': "Moby-Dick", 'Author': "Herman Melville", 'Status': 'Available', 'Due Date': '2024-10-15'},
            'book7': {'Title': "War and Peace", 'Author': "Leo Tolstoy", 'Status': 'Available', 'Due Date': '2024-10-01'},
            'book8': {'Title': "Leo Tolstoy", 'Author': "Unknown", 'Status': 'Available', 'Due Date': None},
            'book9': {'Title': "Yusra Swims", 'Author': "Julie Abery", 'Status': 'Available', 'Due Date': '2024-10-06'},
            'book10': {'Title': "Sisters: Venus and Serena Williams", 'Author': "Jeanette Winter", 'Status': 'Available', 'Due Date': None},
        """}
        save_my_library_data(library_data)  # Save this default data to the CSV file
    return library_data
def save_my_library_data(library_data):
    """Save the library data back to the CSV file."""
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ['Book ID', 'Title', 'Author', 'Status', 'Due Date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for book_id, book_data in library_data.items():
            writer.writerow({
                'Book ID': book_id,
                'Title': book_data['Title'],
                'Author': book_data['Author'],
                'Status': book_data['Status'],
                'Due Date': book_data['Due Date'] or ''
            })
def list_available_books(library_data):
    """List available books."""
    available_books = [book for book in library_data.values() if book['Status'] == 'Available']
    print("Available Books:")
    if available_books:
        for book in available_books:
            print(f"{book['Title']} by {book['Author']}")
    else:
        print("No books currently available.")
def checkout_book(library_data, book_id):
    """Checkout a book."""
    book = library_data.get(book_id)
    if book and book['Status'] == 'Available':
        book['Status'] = 'Checked Out'
        book['Due Date'] = (datetime.date.today() + datetime.timedelta(days=checkout_time)).strftime('%Y-%m-%d')
        save_my_library_data(library_data)
        print(f"You have checked out '{book['Title']}' by {book['Author']}. Due date: {book['Due Date']}")
    else:
        print("Book not available or does not exist.")
def return_book(library_data, book_id):
    """Return a book."""
    book = library_data.get(book_id)
    if book and book['Status'] == 'Checked Out':
        book['Status'] = 'Available'
        book['Due Date'] = None
        save_my_library_data(library_data)
        print(f"You have returned '{book['Title']}' by {book['Author']}.")
    else:
        print("Book is not checked out or does not exist.")
def add_book(library_data, title, author):
    """Add a new book to the library."""
    book_id = str(len(library_data) + 1)  # Generate a new book ID
    library_data[book_id] = {
        'Title': title,
        'Author': author,
        'Status': 'Available',
        'Due Date': None
    }
    save_my_library_data(library_data)
    print(f"Book '{title}' by {author} added with ID: {book_id}")
def main():
    library_data = my_library_data()
    print(library_data)
    while True:
        print("\nLibrary Management System")
        print("a. List Available Books")
        print("b. Checkout Book")
        print("c. Return Book")
        print("d. Add Book")
        print("e. Exit")
        choice = input("enter options: ")
        if choice == 'a':
            list_available_books(library_data)
        elif choice == 'b':
            book_id = input("enter book ID: ")
            checkout_book(library_data, book_id)
        elif choice == 'c':
            book_id = input("enter book ID: ")
            return_book(library_data, book_id)
        elif choice == 'd':
            title = input("enter book title: ")
            author = input("enter book author: ")
            add_book(library_data, title, author)
        elif choice == 'e':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()
