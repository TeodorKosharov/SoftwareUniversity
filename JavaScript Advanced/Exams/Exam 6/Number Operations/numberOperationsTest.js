const numberOperations = require('./numberOperations');
const {expect} = require('chai');

describe('numberOperations object functions testing', function () {
    describe('powNumber function testing', function () {
        it('testing', () => {
            expect(numberOperations.powNumber(2)).to.equal(4);
            expect(numberOperations.powNumber(-2)).to.equal(4);
            expect(numberOperations.powNumber(0)).to.equal(0);
            expect(numberOperations.powNumber(1)).to.equal(1);
            expect(numberOperations.powNumber('3')).to.equal(9);
        });
    });

    describe('numberChecker function testing', function () {
        it('happy path', () => {
            expect(numberOperations.numberChecker(1)).to.equal('The number is lower than 100!');
            expect(numberOperations.numberChecker(-1)).to.equal('The number is lower than 100!');
            expect(numberOperations.numberChecker(100)).to.equal('The number is greater or equal to 100!');
            expect(numberOperations.numberChecker(101)).to.equal('The number is greater or equal to 100!');
            expect(numberOperations.numberChecker('101')).to.equal('The number is greater or equal to 100!');
        });

        it('invalid input', () => {
            expect(() => numberOperations.numberChecker([])).to.throw;
        });
    });

    describe('sumArrays function testing', function () {
        it('happy path', () => {
            expect(numberOperations.sumArrays([1, 2], [1, 2, 3])).to.deep.equal([2, 4, 3]);
            expect(numberOperations.sumArrays([1, 2], [1, 2])).to.deep.equal([2, 4]);
            expect(numberOperations.sumArrays([1], [1])).to.deep.equal([2]);
            expect(numberOperations.sumArrays([], [1])).to.deep.equal([1]);
            expect(numberOperations.sumArrays(['1', '2'], ['1', '3'])).to.deep.equal(['11', '23']);
        });
    });
});


