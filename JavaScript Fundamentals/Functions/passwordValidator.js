function solve(pass) {
    let digits = 0;
    if (!(pass.length >= 6 && pass.length <= 10)) console.log('Password must be between 6 and 10 characters');
    for (let index = 0; index < pass.length; index++) {
        let symbol = pass[index];
        let symbolAscii = symbol.charCodeAt(0);
        if (!((symbolAscii >= 48 && symbolAscii <= 57) || (symbolAscii >= 65 && symbolAscii <= 90) || (symbolAscii >= 97 && symbolAscii <= 122))) {
            console.log('Password must consist only of letters and digits');
            break;
        }
        if (symbolAscii >= 48 && symbolAscii <= 57) digits++;
    }

    if (digits < 2) console.log('Password must have at least 2 digits');
    else console.log('Password is valid');
}
