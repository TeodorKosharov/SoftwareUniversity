function solve(arr) {
    let result = {};

    for (const el of arr) {
        const tokens = el.split(' ');
        if (tokens[0] === 'create') create(tokens[1]);
        else if (tokens[2] === 'inherits') inherits(tokens[1], tokens[3]);
        else if (tokens[0] === 'set') setProps(tokens[1], tokens[2], tokens[3]);
        else print(tokens[1]);

    }

    function create(name) {
        result[name] = {};
    }

    function inherits(name, parentName) {
        result[name] = result[parentName];
    }

    function setProps(name, key, value) {
        result[name][key] = value;
    }

    function print(name) {
        for (const key in result[name]) console.log(`${key}:${result[name][key]}`);
    }
}
