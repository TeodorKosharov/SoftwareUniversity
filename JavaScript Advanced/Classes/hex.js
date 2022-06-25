class Hex {
    constructor(value) {
        this.value = value;
    }

    valueOf() {
        return this.value;
    }

    toString() {
        return '0x' + `${this.value.toString(16)}`.toUpperCase();
    }

    plus(number) {
        if (typeof number === 'object') {
            const result = this.value + number.value;
            return new Hex(result);
        } else {
            const result = this.value + number;
            return new Hex(result)
        }
    }

    minus(number) {
        if (typeof number === 'object') {
            const result = this.value - number.value;
            return new Hex(result);
        } else {
            const result = this.value - number;
            return new Hex(result)
        }
    }

    parse(number) {
        return parseInt(number, 16);
    }
}
