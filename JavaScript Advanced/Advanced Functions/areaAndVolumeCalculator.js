function area() {
    return Math.abs(this.x * this.y);
}

function vol() {
    return Math.abs(this.x * this.y * this.z);
}

function solve(area, vol, input) {
    const arr = JSON.parse(input);
    let result = [];
    for (const el of arr) {
        result.push({
            area: area.call(el),
            volume: vol.call(el)
        });
    }
    return result;
}
