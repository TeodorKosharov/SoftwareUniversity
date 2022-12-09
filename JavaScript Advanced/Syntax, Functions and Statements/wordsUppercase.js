function solve(string) {
    let regex = /([a-zA-Z]+)/g;
    let matches = string.match(regex);
    matches = matches.map(x => x.toUpperCase());
    console.log(matches.join(', '));
}
