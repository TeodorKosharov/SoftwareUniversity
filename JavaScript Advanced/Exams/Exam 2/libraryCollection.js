class LibraryCollection {
    constructor(capacity) {
        this.capacity = capacity;
        this.books = [];
    }

    addBook(bookName, bookAuthor) {
        if (this.capacity === 0) throw Error('Not enough space in the collection.');
        this.books.push({bookName, bookAuthor, payed: false});
        this.capacity--;
        return `The ${bookName}, with an author ${bookAuthor}, collect.`;
    }

    payBook(bookName) {
        if (!(this.books.map(x => x.bookName).includes(bookName))) throw Error(`${bookName} is not in the collection.`);
        const selectedBook = this.books.filter(x => x.bookName === bookName)[0];

        if (selectedBook.payed === true) throw Error(`${bookName} has already been paid.`);
        selectedBook.payed = true;
        return `${bookName} has been successfully paid.`;
    }

    removeBook(bookName) {
        if (this.books.filter(x => x.bookName === bookName).length === 0) throw Error('The book, you\'re looking for, is not found.');
        const selectedBook = this.books.filter(x => x.bookName === bookName)[0];

        if (selectedBook.payed === false) throw Error(`${bookName} need to be paid before removing from the collection.`);
        this.books.splice(this.books.indexOf(selectedBook), 1);
        this.capacity++;
        return `${bookName} remove from the collection.`;
    }

    getStatistics(...params) {
        if (params.length === 0) {
            let result = `The book collection has ${this.capacity} empty spots left.`;
            this.books.sort((a, b) => (a.bookName).localeCompare(b.bookName));
            for (const book of this.books) {
                let paidInfo;
                book.payed === false ? paidInfo = 'Not Paid' : paidInfo = 'Has Paid';
                result += `\n${book.bookName} == ${book.bookAuthor} - ${paidInfo}.`;
            }
            return result;
        }
        const bookAuthor = params[0];
        const selectedBook = this.books.filter(x => x.bookAuthor === bookAuthor)[0];
        if (selectedBook === undefined) throw Error(`${bookAuthor} is not in the collection.`);
        let paidInfo;
        selectedBook.payed === false ? paidInfo = 'Not Paid' : paidInfo = 'Has Paid';

        return `${selectedBook.bookName} == ${selectedBook.bookAuthor} - ${paidInfo}.`;
    }
}
