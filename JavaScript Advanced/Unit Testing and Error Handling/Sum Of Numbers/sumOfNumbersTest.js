const {expect} = require('chai');
const {sum} = require('./sumOfNumbers');

describe('Tests', () => {
    it('numeric arr test', () => {
        expect(sum([1, 2, 3])).to.equal(6);
    });
})

