const rentCar = require('./rentCar');
const {expect} = require('chai');

describe('rentCar object functions testing', () => {
    describe('searchCar function testing', () => {
        it('happy path', () => {
            expect(rentCar.searchCar(['Mercedes', 'Audi'], 'Mercedes')).to.equal('There is 1 car of model Mercedes in the catalog!');
            expect(() => rentCar.searchCar(['Mercedes', 'Audi'], 'BMW')).to.throw();
        });

        it('invalid input', () => {
            expect(() => rentCar.searchCar('asd', 'Audi')).to.throw();
            expect(() => rentCar.searchCar(['Audi'], 1)).to.throw();
            expect(() => rentCar.searchCar('asd', 1)).to.throw();
        });
    });

    describe('calculatePriceOfCar function testing', () => {
        it('happy path', () => {
            expect(rentCar.calculatePriceOfCar('Mercedes', 1)).to.equal('You choose Mercedes and it will cost $50!');
            expect(rentCar.calculatePriceOfCar('Mercedes', 0)).to.equal('You choose Mercedes and it will cost $0!');
            expect(() => rentCar.calculatePriceOfCar('Tesla', 1)).to.throw();
        });

        it('invalid input', () => {
            expect(() => rentCar.calculatePriceOfCar(1, 1)).to.throw();
            expect(() => rentCar.calculatePriceOfCar('Mercedes', '1')).to.throw();
            expect(() => rentCar.calculatePriceOfCar(1, '1')).to.throw();
            expect(() => rentCar.calculatePriceOfCar('Mercedes', 1.2)).to.throw();
            expect(rentCar.calculatePriceOfCar('Mercedes', -1)).to.equal('You choose Mercedes and it will cost $-50!');
        });
    });

    describe('checkBudget function testing', () => {
        it('happy path', () => {
            expect(rentCar.checkBudget(1, 1, 2)).to.equal('You rent a car!');
            expect(rentCar.checkBudget(1, 1, 1)).to.equal('You rent a car!');
            expect(rentCar.checkBudget(3, 2, 2)).to.equal('You need a bigger budget!');
        });

        it('invalid input', () => {
            expect(() => rentCar.checkBudget('asd', 1, 1)).to.throw();
            expect(() => rentCar.checkBudget(1, 'asd', 1)).to.throw();
            expect(() => rentCar.checkBudget(1, 1, 'asd')).to.throw();
            expect(() => rentCar.checkBudget('qwerty', 'dsa', 'asd')).to.throw();
        });
    });
});
