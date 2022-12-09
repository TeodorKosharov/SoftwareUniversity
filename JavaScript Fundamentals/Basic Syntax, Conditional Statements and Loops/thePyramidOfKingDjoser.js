function pyramid(base, increment) {
    let stone = 0;
    let marble = 0;
    let lapis = 0;
    let gold = 0;
    let stepCounter = 1;
    let height = 0;

    for (let i = base; i > 0; i -= 2) {
        if (i == 2) {
            gold += 4 * increment;
        } else if (i == 1) {
            gold += 1 * increment;
        } else {
            stone += Math.pow((i - 2), 2) * increment;
            if (stepCounter % 5 == 0) {
                lapis += (Math.pow(i, 2) - Math.pow((i - 2), 2)) * increment;
            } else {
                marble += (Math.pow(i, 2) - Math.pow((i - 2), 2)) * increment;
                } 
        }
        stepCounter++;
        height += increment;
    }   
    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapis)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${Math.floor(height)}`);
}
