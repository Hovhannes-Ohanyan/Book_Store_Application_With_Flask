import requests

BASE_URL = "http://localhost:8000/api/books"  # Replace with your Flask server's URL


def create_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    price = float(input("Enter the price: "))

    data = {
        'title': title,
        'author': author,
        'price': price
    }

    response = requests.post(BASE_URL, json=data)

    if response.status_code == 201:
        print("Book created successfully.")
        print("Book ID:", response.json().get('id'))
    else:
        print("Failed to create the book.")
        print("Error:", response.json().get('error'))


def get_book():
    book_id = input("Enter the book ID: ")
    response = requests.get(f"{BASE_URL}/{book_id}")

    if response.status_code == 200:
        book = response.json()
        print("Book found:")
        print("Title:", book.get('title'))
        print("Author:", book.get('author'))
        print("Price:", book.get('price'))
    elif response.status_code == 404:
        print("Book not found.")
    else:
        print("Failed to retrieve the book.")
        print("Error:", response.json().get('error'))


def get_all_books():
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        books = response.json()
        print("All Books:")
        for book in books:
            print(f"Book ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Price: {book['price']}")
    else:
        print("Failed to retrieve books.")
        print("Error:", response.json().get('error'))


def update_book():
    book_id = input("Enter the book ID: ")
    title = input("Enter the updated book title (or press Enter to skip): ")
    author = input("Enter the updated author (or press Enter to skip): ")
    price = input("Enter the updated price (or press Enter to skip): ")

    data = {}
    if title:
        data['title'] = title
    if author:
        data['author'] = author
    if price:
        data['price'] = float(price)

    response = requests.patch(f"{BASE_URL}/{book_id}", json=data)

    if response.status_code == 200:
        print("Book updated successfully.")
    elif response.status_code == 404:
        print("Book not found.")
    else:
        print("Failed to update the book.")
        print("Error:", response.json().get('error'))


def delete_book():
    book_id = input("Enter the book ID: ")
    response = requests.delete(f"{BASE_URL}/{book_id}")

    if response.status_code == 204:
        print("Book deleted successfully.")
    elif response.status_code == 404:
        print("Book not found.")
    else:
        print("Failed to delete the book.")
        print("Error:", response.json().get('error'))


def main():
    while True:
        print("\nMenu:")
        print("1. Create a Book")
        print("2. Get a Book by ID")
        print("3. Get All Books")
        print("4. Update a Book by ID")
        print("5. Delete a Book by ID")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_book()
        elif choice == '2':
            get_book()
        elif choice == '3':
            get_all_books()
        elif choice == '4':
            update_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
