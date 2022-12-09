function solve(arr, criteria) {
    let result = [];

    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination;
            this.price = price;
            this.status = status;
        }

        compareTo(other, criteria) {
            if (typeof this[criteria] === 'string') {
                return this[criteria].localeCompare(other[criteria]);
            } else {
                return this[criteria] - other[criteria];
            }
        }
    }

    for (const el of arr) {
        const [city, price, status] = el.split('|');
        result.push(new Ticket(city, Number(price), status));
    }

    result.sort((a, b) => a.compareTo(b, criteria));
    return result;
}
