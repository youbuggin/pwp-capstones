class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "This users email has been updated."


    def __repr__(self):
        return "User {name}, email: {email}, books read: {books_read}".format(name = self.name, email = self.email, books_read = str(len(self.books)))
    def __eq__(self, other):
        if self.name == other.name:
            return True
        if self.email == other.email:
            return True
        return False

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        average_rating = 0
        ratings_total = 0
        for bud in self.books.values():
            ratings_total += bud
        average_rating = ratings_total / len(self.books)
        return average_rating



#print(User("steven hawkings", "hawkings@universe,edu"))

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.rating = []

    def get_title(self):
            return self.title

    def get_isbn(self):
            return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This books's ISBN has been updated"

    def add_rating(self,rating):
        if 0 <= rating <= 4:
            self.rating.append(rating)
        else:
            return "Invalid Rating"

    def __eq__(self, other_isbn):
        if self.isbn == other_isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        average = 0
        ratings_total = 0
        for value in self.rating:
            ratings_total += value
        average = ratings_total /len(self.rating)
        return average

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{title}, ISBN: {isbn}".format(title=self.title, isbn=self.isbn)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater:
    class User(object):
        def __init__(self, name, email):
            self.name = name
            self.email = email
            self.books = {}

        def get_email(self):
            return self

        def change_email(self, address):
            self.email = address
            print("Email address has been updated.")

        def __repr__(self):
            return "User {name}, email: {email}, books read: {books_read}".format(name=self.name, email=self.email,
                                                                                  books_read=str(len(self.books)))

        def __eq__(self, other_user):
            if self.name == other_user:
                return True
            else:
                return False

        def read_book(self, book, rating=None):
            self.books[book] = rating

        def get_average_rating(self):
            average_rating = 0
            ratings_total = 0
            for rating in self.books.values():
                ratings_total += rating
            average_rating = ratings_total / len(self.books)
            return average_rating

class Book:
    def __init__(self, title, isbn):
            self.title = title
            self.isbn = isbn
            self.ratings = []

    def get_title(self):
            return self.title

    def get_isbn(self):
            return self.isbn

    def set_isbn(self, new_isbn):
            self.isbn = new_isbn
            print("This book's ISBN has been updated.")

    def add_rating(self, rating):
        if rating and 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        average_rating = 0
        ratings_total = 0
        for rating in self.ratings:
            ratings_total += rating
        average_rating = ratings_total / len(self.ratings)
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

        def __eq__(self, other_isbn):
            if self.isbn == other_isbn:
                return True
            else:
                return False

        def __repr__(self):
            return "{title}, ISBN: {isbn}".format(title=self.title, isbn=self.isbn)

class Fiction(Book):
        def __init__(self, title, author, isbn):
            super().__init__(title, isbn)
            self.author = author

        def get_author(self):
            return self.author

        def __repr__(self):
            return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level,
                                                                   subject=self.subject)

class TomeRater():
    def __init__(self):
            self.users = {}
            self.books = {}

    def create_book(self, title, isbn):
            return Book(title, isbn)

    def create_novel(self, title, author, isbn):
            return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
            return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            user = self.users.get(email, None)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for title in self.books.keys():
            print(title)

    def print_users(self):
        for user in self.users.keys():
            print(user)

    def get_most_read_book(self):
        most_read = None
        read_count = 0
        for book in self.books.keys():
            if self.books[book] > read_count:
                    read_count = self.books[book]
            if self.books[book] == read_count:
                    most_read = book
        return most_read

    def highest_rated_book(self):
        highest_book = None
        highest_rating = 0
        for book in self.books.keys():
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                highest_book = book
        return highest_book

    def most_positive_user(self):
        highest_rating = 0
        highest_user = None
        for user in self.users.values():
                average = User.get_average_rating(self)
                if User.get_average_rating(self) > highest_rating:
                    highest_rating = User.get_average_rating(self)
                    highest_user = user
        return highest_user






