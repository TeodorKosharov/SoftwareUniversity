function solve(arr) {
    let bottles = new Map();
    let juices = {};

    for (const el of arr) {
        let [juice, quantity] = el.split(' => ');
        quantity = Number(quantity);

        if (juices[juice] === undefined) juices[juice] = quantity;
        else juices[juice] += quantity;

        if (juices[juice] >= 1000) {
            let producedBottles = Math.floor(juices[juice] / 1000);
            juices[juice] -= producedBottles * 1000;

            if (bottles[juice] === undefined) bottles[juice] = producedBottles;
            else bottles[juice] += producedBottles;
        }
    }

    Object.entries(bottles).filter(x => console.log(`${x[0]} => ${x[1]}`));

}
