function solve(string, char, string2) {
    let result = string.replace('_', char);
    result == string2 ? console.log('Matched') : console.log('Not Matched');
}