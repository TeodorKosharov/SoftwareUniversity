const mathEnforcer = require('./mathEnforcer');
const {expect} = require('chai');

describe('Math enforcer object testing', () => {
    describe('addFive function testing', () => {
        it('non numeric parameter', () => {
            expect(mathEnforcer.addFive('2')).to.be.undefined;
        });
        it('valid case', () => {
            expect(mathEnforcer.addFive(4)).to.equal(9);
        });
        it('float parameter', () => {
            expect(mathEnforcer.addFive(4.5)).to.equal(9.5);
        });
        it('negative parameter', () => {
            expect(mathEnforcer.addFive(-5)).to.equal(0);
        });
    });

    describe('subtractTen function testing', () => {
        it('non numeric parameter', () => {
            expect(mathEnforcer.subtractTen('2')).to.be.undefined;
        });
        it('valid case', () => {
            expect(mathEnforcer.subtractTen(4)).to.equal(-6);
        });
        it('float parameter', () => {
            expect(mathEnforcer.subtractTen(10.1)).to.equal(0.09999999999999964);
        });
        it('negative parameter', () => {
            expect(mathEnforcer.subtractTen(-10)).to.equal(-20);
        });
    });

    describe('sum function testing', () => {
        it('first parameter invalid', () => {
            expect(mathEnforcer.sum('2', 2)).to.be.undefined;
        });
        it('second parameter invalid', () => {
            expect(mathEnforcer.sum(2, '2')).to.be.undefined;
        });
        it('both parameters invalid', () => {
            expect(mathEnforcer.sum('2', '2')).to.be.undefined;
        });
        it('valid case', () => {
            expect(mathEnforcer.sum(2, 2)).to.equal(4);
        });
        it('floating parameters', () => {
            expect(mathEnforcer.sum(2.6, 3.5)).to.equal(6.1);
        });
        it('negative parameters', () => {
            expect(mathEnforcer.sum(-3.5, -1.6)).to.equal(-5.1);
        });
    });
});
