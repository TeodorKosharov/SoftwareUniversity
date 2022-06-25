function solution() {
    let result = '';

    function append(str) {
        result += str;
    }

    function removeStart(x) {
        result = result.slice(x);
    }

    function removeEnd(x) {
        result = result.slice(0, -x);
    }

    function print() {
        console.log(result);
    }

    return {
        append,
        removeStart,
        removeEnd,
        print
    }
}
