const bookSelection = require('./bookSelection');
const {expect} = require('chai');


describe('Book selection testing', () => {
    describe('isGenreSuitable function testing', () => {
        it('age <= 12 and genre - Thriller', () => {
            expect(bookSelection.isGenreSuitable('Thriller', 10)).to.equal('Books with Thriller genre are not suitable for kids at 10 age');
        });

        it('age <= 12 and genre = Horror', () => {
            expect(bookSelection.isGenreSuitable('Horror', 10)).to.equal('Books with Horror genre are not suitable for kids at 10 age');
        });

        it('else case', () => {
            expect(bookSelection.isGenreSuitable('unknown', -14)).to.equal('Those books are suitable');
        });

        it('edge case', () => {
            expect(bookSelection.isGenreSuitable('Thriller', 12)).to.equal('Books with Thriller genre are not suitable for kids at 12 age');
            expect(bookSelection.isGenreSuitable('Horror', 12)).to.equal('Books with Horror genre are not suitable for kids at 12 age');
        });
    });

    describe('isItAffordable function testing', () => {
        it('happy path', () => {
            expect(bookSelection.isItAffordable(1, 2)).to.equal('Book bought. You have 1$ left');
            expect(bookSelection.isItAffordable(2, 1)).to.equal("You don't have enough money");
        });

        it('edge case', () => {
            expect(bookSelection.isItAffordable(1, 1)).to.equal('Book bought. You have 0$ left');
        });

        it('invalid input', () => {
            expect(() => bookSelection.isItAffordable('1', 1)).to.throw();
            expect(() => bookSelection.isItAffordable(1, '1')).to.throw();
            expect(() => bookSelection.isItAffordable('1', '1')).to.throw();
        });
    });

    describe('suitableTitles function testing', () => {
        it('happy path', () => {
            expect(bookSelection.suitableTitles([{
                title: 'The Curse', genre: 'Horror'
            }], 'Horror')).to.deep.equal(['The Curse']);
        });

        it('passed non array type', () => {
            expect(() => bookSelection.suitableTitles('str', 'Horror')).to.throw();
        });

        it('passed invalid genre type', () => {
            expect(() => bookSelection.suitableTitles([], 12)).to.throw();
        });
    });
});
