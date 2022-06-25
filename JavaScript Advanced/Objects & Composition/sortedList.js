function createSortedList() {
    const result = {
        numbers: [], add(element) {
            this.numbers.push(element);
            this.numbers.sort((a, b) => a - b);
            this.size++;
        }, remove(index) {
            if (index >= 0 && index < result.numbers.length) {
                this.numbers.splice(index, 1);
                this.size--;
            }
            this.numbers.sort((a, b) => a - b);

        }, get(index) {
            if (this.numbers[index] !== undefined) return this.numbers[index];
        }, size: 0
    }
    return result;
}
