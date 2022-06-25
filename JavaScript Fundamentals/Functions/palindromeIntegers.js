function solve(arr) {
    for (let index = 0; index < arr.length; index++) {
        let currentNum = String(arr[index]);
        let middleIndex = Math.floor(currentNum.length / 2);
        let lastIndex = currentNum.length - 1;
        let isPalindrome = true;

        for (let i = 0; i < middleIndex; i++) {
            currentNum[i] == currentNum[lastIndex] ? isPalindrome = true : isPalindrome = false;
            lastIndex--;
            if (isPalindrome == false) break;
        }

        console.log(isPalindrome);
    }
}
