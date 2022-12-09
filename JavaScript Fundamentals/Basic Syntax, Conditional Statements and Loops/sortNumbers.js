function sorting(a, b, c) {
    let nums = [a, b, c];
    nums.sort().reverse();
    nums.forEach(element => {
        console.log(element)
    });
}

sorting(1, 2, 3);