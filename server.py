from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

data_file_path = os.path.join(os.path.dirname(__file__), 'data', 'books.json')


def load_books():
    try:
        with open(data_file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_books(books):
    with open(data_file_path, "w") as file:
        json.dumps(books, file, indent=4)


books = load_books()
auto_increment_id = 1


@app.route("/api/books", methods=["POST"])
def create_book():
    global auto_increment_id
    data = request.json
    if not data or not all(key in data for key in ('title', 'author', 'price')):
        return jsonify({'error': 'Invalid or incomplete data'}), 400
    book_id = auto_increment_id
    auto_increment_id += 1
    data['id'] = book_id
    books.append(data)
    return jsonify({'message': 'Book created successfully', 'id': book_id}), 201


@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404

    return jsonify(book)


@app.route('/api/books', methods=['GET'])
def get_all_books():
    return jsonify(books)


# Update operation (U)
@app.route('/api/books/<int:id>', methods=['PATCH'])
def update_book(id):
    data = request.json
    if not data:
        return jsonify({'error': 'Invalid or incomplete data'}), 400

    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404

    for key, value in data.items():
        if key in ('title', 'author', 'price'):
            book[key] = value

    return jsonify({'message': 'Book updated successfully'})


@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404

    books.remove(book)
    return '', 204


if __name__ == "__main__":
    app.run(debug=True, port=8000)
