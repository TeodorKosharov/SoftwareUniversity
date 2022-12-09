function pass(arr) {
    let username = arr[0];
    let password = username.split("").reverse().join("");;
    let tries = 1;

    for (let index = 1; index < arr.length; index++) {
        if (arr[index] != password && tries < 4) {
            console.log('Incorrect password. Try again.');
            tries ++;
            continue;
        } else if (arr[index] == password) {
            console.log(`User ${username} logged in.`)
            break;
        }
        console.log(`User ${username} blocked!`)
    }
}
