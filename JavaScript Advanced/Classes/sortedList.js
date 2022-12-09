class List {
    constructor() {
        this.numbers = [];
        this.size = 0;
    }

    add(element) {
        this.numbers.push(element);
        this.sorting();
        this.size++;
    }

    remove(index) {
        if (index >= 0 && index < this.numbers.length) {
            this.numbers.splice(index, 1);
            this.size--;
        }
        this.sorting();

    }

    get(index) {
        if (index >= 0 && index < this.numbers.length) {
            return this.numbers[index];
        }
        this.sorting();
    }

    sorting() {
        this.numbers.sort((a, b) => a - b);
    }
}
