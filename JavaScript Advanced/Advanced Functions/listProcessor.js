function solve(arr) {
    let result = [];

    for (const el of arr) {
        const tokens = el.split(' ');
        if (tokens[0] === 'add') add(tokens[1]); else if (tokens[0] === 'remove') remove(tokens[1]); else print();
    }

    function add(str) {
        result.push(str);
    }

    function remove(str) {
        result = result.filter(x => x !== str);
    }

    function print() {
        console.log(result.join(','));
    }
}
