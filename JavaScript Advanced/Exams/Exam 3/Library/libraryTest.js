const library = require('./library');
const {expect} = require('chai');

describe('library object functions testing', () => {
    describe('calcPriceOfBook function testing', () => {
        it('happy path', () => {
            expect(library.calcPriceOfBook('test', 2000)).to.equal('Price of test is 20.00');
            expect(library.calcPriceOfBook('test', 1904)).to.equal('Price of test is 10.00');
            expect(library.calcPriceOfBook('test', 1980)).to.equal('Price of test is 10.00');
        });

        it('invalid input', () => {
            expect(() => library.calcPriceOfBook(1, 2000)).to.throw();
            expect(() => library.calcPriceOfBook('test', 'asd')).to.throw();
            expect(() => library.calcPriceOfBook(1, 'asd')).to.throw();

        });
    });

    describe('findBook function testing', () => {
        it('happy path', () => {
            expect(library.findBook(['1', '2'], '1')).to.equal('We found the book you want.');
            expect(library.findBook(['1', '2'], '3')).to.equal('The book you are looking for is not here!');
        });

        it('invalid input', () => {
            expect(() => library.findBook([], '1')).to.throw();
        });
    });

    describe('arrangeTheBooks function testing', () => {
        it('happy path', () => {
            expect(library.arrangeTheBooks(30)).to.equal('Great job, the books are arranged.');
            expect(library.arrangeTheBooks(40)).to.equal('Great job, the books are arranged.');
            expect(library.arrangeTheBooks(50)).to.equal('Insufficient space, more shelves need to be purchased.');
        });

        it('invalid input', () => {
            expect(() => library.arrangeTheBooks('asd')).to.throw();
            expect(() => library.arrangeTheBooks(-1)).to.throw();
        });
    });

});
