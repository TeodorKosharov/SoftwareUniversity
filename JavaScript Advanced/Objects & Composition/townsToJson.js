function solve(arr) {
    const result = [];

    for (const el of arr.slice(1)) {
        let [town, latitude, longitude] = el.split(' | ');
        town = town.replace('| ', '');
        latitude = Number(latitude).toFixed(2);
        longitude = Number(longitude.replace(' |', '')).toFixed(2);
        result.push(({
            "Town": town, "Latitude": Number(latitude), "Longitude": Number(longitude)
        }));
    }
    console.log(JSON.stringify(result));
}
