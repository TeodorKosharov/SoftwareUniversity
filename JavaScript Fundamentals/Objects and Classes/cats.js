function solve(arr) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    for (let el of arr) {
        let tokens = el.split(' ');
        let cat = new Cat(tokens[0], tokens[1]);
        cat.meow();
    }
}
