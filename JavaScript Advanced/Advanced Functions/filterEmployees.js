function solve(data, criteria) {
    const [prop, propName] = criteria.split('-');
    let counter = 0;

    for (const el of JSON.parse(data)) {
        if (el[prop] === propName) {
            console.log(`${counter}. ${el['first_name']} ${el['last_name']} - ${el['email']}`);
            counter++;
        }
    }
}
