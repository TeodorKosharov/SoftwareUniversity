function solve() {
    document.querySelector('#searchBtn').addEventListener('click', onClick);
    const searchWord = document.getElementById('searchField');
    const table = Array.from(document.querySelectorAll('tbody tr'));

    function onClick() {
        for (const row of table) {
            row.classList.remove('select');
            if (row.textContent.includes(searchWord.value)) {
                row.className = 'select';
            }
        }
        searchWord.value = '';
    }
}
