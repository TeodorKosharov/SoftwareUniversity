function solve(n, k){
    let result = [1];


    for (let i = 1; i < n; i++) {
        let len = result.length;
        let lastIndex = len - 1;
        let sum = 0;

        for (let j = 1; j <= k; j++) {
            sum += result[lastIndex];
            lastIndex--;
            if (lastIndex == -1) break;
        }
        result.push(sum);
    }
    
    return result;
}

solve(8, 2);
