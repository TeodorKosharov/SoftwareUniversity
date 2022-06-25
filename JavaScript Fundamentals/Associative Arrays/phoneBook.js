function solve(arr) {
    let register = {};
    
    for (let el of arr) {
        let tokens = el.split(' ');
        register[tokens[0]] = tokens[1];
    }

    for (let data in register) {
        console.log(`${data} -> ${register[data]}`);
    }
}
