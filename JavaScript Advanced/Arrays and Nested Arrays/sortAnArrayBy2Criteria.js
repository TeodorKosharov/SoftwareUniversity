function solve(arr) {
    function sortByTwoCriteria(current, next) {
        if (current.length === next.length) return current.localeCompare(next);
        return current.length - next.length;
    }

    arr.sort(sortByTwoCriteria);
    return arr.join('\n');
}
