function solve(arr) {
    let heroes = [];
    class Hero {
        constructor(name, level, items) {
            this.name = name;
            this.level = level;
            this.items = items;
        }
    }

    for (let element of arr) {
        let tokens = element.split(' / ');
        heroes.push(new Hero(tokens[0], tokens[1], tokens[2]));
    }
    
    heroes.sort((a, b) => a.level - b.level);
    for (let hero of heroes) {
        console.log(`Hero: ${hero.name}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items}`);
    }
}
