const carService = require('./carService');
const {expect} = require('chai');

describe('carService object functions testing', function () {
    describe('isItExpensive function testing', function () {
        it('valid cases', () => {
            expect(carService.isItExpensive('Engine')).to.equal('The issue with the car is more severe and it will cost more money');
            expect(carService.isItExpensive('Transmission')).to.equal('The issue with the car is more severe and it will cost more money');
            expect(carService.isItExpensive('other case')).to.equal('The overall price will be a bit cheaper');
        });
    });

    describe('discount function testing', function () {
        it('valid cases', () => {
            expect(carService.discount(3, 100)).to.equal('Discount applied! You saved 15$');
            expect(carService.discount(8, 100)).to.equal('Discount applied! You saved 30$');
            expect(carService.discount(7, 100)).to.equal('Discount applied! You saved 15$');
            expect(carService.discount(2, 100)).to.equal('You cannot apply a discount');
            expect(carService.discount(1, 100)).to.equal('You cannot apply a discount');
        });

        it('invalid cases', () => {
            expect(() => carService.discount('2', 100)).to.throw;
            expect(() => carService.discount(2, '2')).to.throw;
            expect(() => carService.discount('2', '2')).to.throw;

        });
    });

    describe('partsToBuy function testing', function () {
        it('valid cases', () => {
            expect(carService.partsToBuy([{part: '1', price: 1}, {part: '2', price: 2}], ['1', '2'])).to.equal(3);
            expect(carService.partsToBuy([{part: '1', price: 1}, {part: '2', price: 2}], ['1'])).to.equal(1);
            expect(carService.partsToBuy([{part: '1', price: 1.5}, {part: '2', price: 2.5}], ['1', '2'])).to.equal(4);
        });

        it('invalid cases', () => {
            expect(() => carService.partsToBuy(1, [])).to.throw;
            expect(() => carService.partsToBuy([], 1)).to.throw;
            expect(() => carService.partsToBuy(1, 1)).to.throw;
        });
    });

});
