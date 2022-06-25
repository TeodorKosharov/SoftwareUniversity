function extractText() {
    // const selected = Array.from(document.querySelectorAll('li'));
    // const filtered = selected.map(x => x.textContent);
    // const field = document.getElementById('result');
    // field.value = filtered.join('\n');

    // Second variant:
    const selected = Array.from(document.getElementsByTagName('li'));
    const filtered = selected.map(x => x.textContent);
    const field = document.getElementById('result');
    field.value = filtered.join('\n');

}
