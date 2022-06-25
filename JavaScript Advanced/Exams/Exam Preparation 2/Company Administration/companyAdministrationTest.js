const companyAdministration = require('./companyAdministration');
const {expect} = require('chai');

describe('companyAdministration function testing', () => {
    describe('hiringEmployee function testing', () => {
        it('happy path', () => {
            expect(companyAdministration.hiringEmployee('Teodor', 'Programmer', 4)).to.equal('Teodor was successfully hired for the position Programmer.');
            expect(companyAdministration.hiringEmployee('Teodor', 'Programmer', 3)).to.equal('Teodor was successfully hired for the position Programmer.');
            expect(companyAdministration.hiringEmployee('Teodor', 'Programmer', 2)).to.equal('Teodor is not approved for this position.');
        });

        it('invalid position', () => {
            expect(() => companyAdministration.hiringEmployee('Teodor', 'Manager', 4)).to.throw();
        });

    });

    describe('calculateSalary function testing', () => {
        it('happy path', () => {
            expect(companyAdministration.calculateSalary(1)).to.equal(15);
            expect(companyAdministration.calculateSalary(200)).to.equal(4000);
        });

        it('invalid input', () => {
            expect(() => companyAdministration.calculateSalary('asd')).to.throw();
            expect(() => companyAdministration.calculateSalary(-10)).to.throw();
        });

    });

    describe('firedEmployee function testing', () => {
        it('happy path', () => {
            expect(companyAdministration.firedEmployee(['Teodor', 'Plamen', 'Fati'], 1)).to.equal('Teodor, Fati');
            expect(companyAdministration.firedEmployee(['Teodor'], 0)).to.equal('');
        });

        it('invalid cases', () => {
            expect(() => companyAdministration.firedEmployee(2, 1)).to.throw();
            expect(() => companyAdministration.firedEmployee(['Teodor'], 'asd')).to.throw();
            expect(() => companyAdministration.firedEmployee(['Teodor'], -1)).to.throw();
            expect(() => companyAdministration.firedEmployee(['Teodor'], 1)).to.throw();
        });
    });
});
