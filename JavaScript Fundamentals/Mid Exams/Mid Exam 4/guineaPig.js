function solve(arr) {
    let food = Number(arr[0]) * 1000;
    let hay = Number(arr[1]) * 1000;
    let cover = Number(arr[2]) * 1000;
    let pigWeight = Number(arr[3]) * 1000;
    let runOutOfFood = false;

    for (let day = 1; day <= 30; day++) {
        food -= 300;
        if (day % 2 == 0) {
            hay -= 0.05 * food;
        }
        if (day % 3 == 0) {
            cover -= 1/3 * pigWeight;
        }
        if (food <= 0 || hay <= 0 || cover <= 0) {
            runOutOfFood = true;
            break;
        }
    }
    if (runOutOfFood) console.log("Merry must go to the pet store!");
    else console.log(`Everything is fine! Puppy is happy! Food: ${(food / 1000).toFixed(2)}, Hay: ${(hay / 1000).toFixed(2)}, Cover: ${(cover / 1000).toFixed(2)}.`);
}
