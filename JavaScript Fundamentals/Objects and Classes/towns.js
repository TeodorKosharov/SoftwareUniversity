function solve(arr) {
    for (let el of arr) {
        let data = {};
        let tokens = el.split(' | ');
        data['town'] = tokens[0];
        data['latitude'] = Number(tokens[1]).toFixed(2);
        data['longitude'] = Number(tokens[2]).toFixed(2);
        console.log(data);
    }
}
