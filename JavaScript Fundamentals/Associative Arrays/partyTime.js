function solve(arr) {
    let guests = [];
    let absentGuests = 0;
    let regularGuests = [];
    let vipGuests = [];
    

    while (true) {
        let element = arr[0];
        if (element == 'PARTY') {
            arr.shift();
            break;
        }
        guests.push(arr.shift());
    }
    
    for (let el of guests) {
        if (!(arr.includes(el))) {
            absentGuests++;
            let firstElementValue = el.charCodeAt(0);
            if (firstElementValue >= 48 && firstElementValue <= 57) vipGuests.push(el);
            else regularGuests.push(el);
        } 
    }
    console.log(absentGuests);
    console.log(vipGuests.join('\n'));
    console.log(regularGuests.join('\n'));
}

solve(['7IK9Yo0h',
'9NoBUajQ',
'Ce8vwPmE','SVQXQCbc',
'tSzE5t0p',
'PARTY',
'9NoBUajQ',
'Ce8vwPmE',
'SVQXQCbc'
]);