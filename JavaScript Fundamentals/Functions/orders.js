function solve(product, quantity) {
    let result = 0;
    if (product == 'coffee') result = quantity * 1.50;
    else if (product == 'water') result = quantity * 1;
    else if (product == 'coke') result = quantity * 1.40;
    else result = quantity * 2;
    console.log(result.toFixed(2));
}