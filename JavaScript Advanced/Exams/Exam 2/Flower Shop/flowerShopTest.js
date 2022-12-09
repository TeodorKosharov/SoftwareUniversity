const flowerShop = require('./flowerShop');
const {expect} = require('chai');

describe('flowerShop object functions testing', () => {
    describe('calcPriceOfFlowers function testing', () => {
        it('happy path', () => {
            expect(flowerShop.calcPriceOfFlowers('flower', 2, 2)).to.equal('You need $4.00 to buy flower!');
            expect(flowerShop.calcPriceOfFlowers('flower', 0, 2)).to.equal('You need $0.00 to buy flower!');
            expect(flowerShop.calcPriceOfFlowers('flower', 2, 0)).to.equal('You need $0.00 to buy flower!');
            expect(flowerShop.calcPriceOfFlowers('flower', 0, 0)).to.equal('You need $0.00 to buy flower!');
        });

        it('invalid input', () => {
            expect(() => flowerShop.calcPriceOfFlowers(1, 0, 0)).to.throw();
            expect(() => flowerShop.calcPriceOfFlowers('flower', 1.5, 0)).to.throw();
            expect(() => flowerShop.calcPriceOfFlowers('flower', 1, 1.5)).to.throw();
            expect(() => flowerShop.calcPriceOfFlowers(1, 1.5, 'asd')).to.throw();
        });
    });

    describe('checkFlowersAvailable function testing', () => {
        it('available flower', () => {
            expect(flowerShop.checkFlowersAvailable('flower', ['flower'])).to.equal('The flower are available!');
        });

        it('absent flower', () => {
            expect(flowerShop.checkFlowersAvailable('flower', [])).to.equal('The flower are sold! You need to purchase more!');
        });
    });

    describe('sellFlowers function testing', () => {
       it('happy path', () => {
            expect(flowerShop.sellFlowers(["Rose", "Lily", "Orchid"], 1)).to.equal('Rose / Orchid');
       });

       it('invalid input', () => {
           expect(() => flowerShop.sellFlowers(1, 1)).to.throw();
           expect(() => flowerShop.sellFlowers(1, 'ads')).to.throw();
           expect(() => flowerShop.sellFlowers(1, -1)).to.throw();
           expect(() => flowerShop.sellFlowers(['1', '2'], 2)).to.throw();
           expect(() => flowerShop.sellFlowers(['1', '2'], 3)).to.throw();

       });
    });
});

