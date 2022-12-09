const {expect} = require('chai');
const {isSymmetric} = require('./checkForSymmetry');

describe('Symmetry tests', () => {
    it('Symmetric array test',  () => {
       expect(isSymmetric([1, 2, 2, 1])).to.be.true;
    });

    it('Non-Symmetric array test', () => {
       expect(isSymmetric([1, 2, 3])).to.be.false;
    });

    it('Incorrect argument', () => {
       expect(isSymmetric(5)).to.be.false;
    });

    it('Symmetric odd length', () => {
        expect(isSymmetric([1, 2, 1])).to.be.true;
    });

    it('Symmetric string array', () => {
        expect(isSymmetric(['a', 'b', 'b', 'a'])).to.be.true;
    });

    it('Non-num element in array', () => {
        expect(isSymmetric([1, 2, '1'])).to.be.false;
    });

    it('String argument', () => {
        expect(isSymmetric('abba')).to.be.false;
    });

    it('Missmatch element', () => {
        expect(isSymmetric([1, 2, 3, '4'])).to.be.false;
    })
});


