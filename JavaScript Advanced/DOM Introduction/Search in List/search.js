function search() {
    const searchText = document.getElementById('searchText').value;
    const listTowns = Array.from(document.getElementById('towns').children);
    let matches = 0;

    for (const town of listTowns) {
        const currentTown = town.textContent;
        if (currentTown.includes(searchText)) {
            town.style.textDecoration = 'underline';
            town.style.fontWeight = 'bold';
            matches++;
        }
    }

    document.getElementById('result').textContent = `${matches} matches found`;
}
