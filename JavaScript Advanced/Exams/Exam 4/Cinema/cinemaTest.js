const cinema = require('./cinema');
const {expect} = require('chai');

describe('cinema object functions testing', () => {
    describe('showMovies function testing', function () {
        it('happy path', () => {
            expect(cinema.showMovies([])).to.equal('There are currently no movies to show.');
            expect(cinema.showMovies(['1', '2'])).to.equal('1, 2');
        });
    });

    describe('ticketPrice function testing', function () {
        it('happy path', () => {
            expect(cinema.ticketPrice('Premiere')).to.equal(12.00);
            expect(cinema.ticketPrice('Normal')).to.equal(7.50);
            expect(cinema.ticketPrice('Discount')).to.equal(5.50);
        });

        it('invalid input', () => {
            expect(() => cinema.ticketPrice('invalid')).to.throw();
        });

    });

    describe('swapSeatsInHall function testing', function () {
        it('happy path', () => {
            expect(cinema.swapSeatsInHall(1, 2)).to.equal('Successful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(20, 19)).to.equal('Successful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(19, 20)).to.equal('Successful change of seats in the hall.');
        });

        it('invalid input', () => {
            expect(cinema.swapSeatsInHall('1', 2)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(-1, 2)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(0, 2)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(21, 2)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, '1')).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, -1)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, 0)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, 21)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall(1, 1)).to.equal('Unsuccessful change of seats in the hall.');
            expect(cinema.swapSeatsInHall('1', '1')).to.equal('Unsuccessful change of seats in the hall.');
        });
    });
});
