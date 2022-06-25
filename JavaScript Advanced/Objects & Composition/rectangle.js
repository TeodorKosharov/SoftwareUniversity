function rectangle(width, height, color) {
    const result = {
        width,
        height,
        color: color[0].toUpperCase() + color.slice(1),
        calcArea() {
            return result.width * result.height
        }
    };
    return result;
}
