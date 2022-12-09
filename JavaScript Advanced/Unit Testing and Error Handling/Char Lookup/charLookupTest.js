const {lookupChar} = require('./charLookup');
const {expect} = require('chai');

describe('Char lookup testing', () => {
    it('non string param', () => {
        expect(lookupChar(4, 4)).to.be.undefined;
    });

    it('invalid type index', () => {
        expect(lookupChar('abcd', 'a')).to.be.undefined;
    });

    it('index out of bounds', () => {
        expect(lookupChar('abcd', 4)).to.equal('Incorrect index');
    });

    it('float index', () => {
        expect(lookupChar('abcd', 2.4)).to.be.undefined;
    });

    it('negative index', () => {
        expect(lookupChar('abcd', -2)).to.equal('Incorrect index');
    });

    it('both params invalid', () => {
        expect(lookupChar(2, 'abc')).to.be.undefined;
    });

    it('valid case', () => {
        expect(lookupChar('abcd', 1)).to.equal('b');
    });

    it('one letter string', () => {
        expect(lookupChar('X', 0)).to.equal('X');
    });
});

