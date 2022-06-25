class Stringer {
    constructor(string, len) {
        this.innerString = string;
        this.innerLength = len;
    }

    increase(length) {
        this.innerLength += length;
    }

    decrease(length) {
        this.innerLength - length < 0 ? this.innerLength = 0 : this.innerLength -= length;
    }

    toString() {
        if (this.innerString.length > this.innerLength) {
            return this.innerString.slice(0, this.innerLength) + '...';
        }
        return this.innerString;
    }

}
