const testNumbers = require('./testNumbers');
const {expect} = require('chai');

describe('testNumbers object functions testing', function () {
    describe('sumNumbers function testing', function () {
        it('happy path', () => {
            expect(testNumbers.sumNumbers(1, 1)).to.equal('2.00');
            expect(testNumbers.sumNumbers(0, 0)).to.equal('0.00');
            expect(testNumbers.sumNumbers(-1, -1)).to.equal('-2.00');
            expect(testNumbers.sumNumbers(-1.5, -1.5)).to.equal('-3.00');
            expect(testNumbers.sumNumbers(-1.5, 1.5)).to.equal('0.00');
        });

        it('invalid input', () => {
            expect(testNumbers.sumNumbers('1', 1)).to.be.undefined;
            expect(testNumbers.sumNumbers(1, '1')).to.be.undefined;
            expect(testNumbers.sumNumbers('1', '1')).to.be.undefined;
        });
    });

    describe('numberChecker function testing', function () {
        it('happy path', () => {
            expect(testNumbers.numberChecker(10)).to.equal('The number is even!');
            expect(testNumbers.numberChecker(9)).to.equal('The number is odd!');
            expect(testNumbers.numberChecker(0)).to.equal('The number is even!');
            expect(testNumbers.numberChecker(-2)).to.equal('The number is even!');
            expect(testNumbers.numberChecker(-1)).to.equal('The number is odd!');
            expect(testNumbers.numberChecker(1.5)).to.equal('The number is odd!');
        });

        it('invalid input', () => {
            expect(() => testNumbers.numberChecker([])).to.throw;
        });
    });

    describe('averageSumArray function testing', function () {
        it('happy path', () => {
            expect(testNumbers.averageSumArray([5, 5])).to.equal(5);
            expect(testNumbers.averageSumArray([5])).to.equal(5);
            expect(testNumbers.averageSumArray([-5, -5])).to.equal(-5);
        });
    });
});

