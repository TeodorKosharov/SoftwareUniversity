(function solve() {
    Array.prototype.last = function () {
        return this[this.length - 1];
    };

    Array.prototype.skip = function (n) {
        return this.slice(n);
    };

    Array.prototype.take = function (n) {
        return this.slice(0, n);
    };

    Array.prototype.sum = function () {
        let total = 0;
        for (const el of this) total += el;
        return total;
    };


    Array.prototype.average = function () {
        const sum = this.sum();
        return sum / this.length;
    };
})()
