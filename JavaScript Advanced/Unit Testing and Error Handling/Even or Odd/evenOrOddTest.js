const {isOddOrEven} = require('./evenOrOdd');
const {expect} = require('chai');

describe('Even or odd testing', () => {
    it('even len', () => {
        expect(isOddOrEven('abcd')).to.equal('even');
    });

    it('odd len', () => {
        expect(isOddOrEven('abc')).to.equal('odd');
    });

    it('non string type', () => {
        expect(isOddOrEven(5)).to.be.undefined;
    });
});
