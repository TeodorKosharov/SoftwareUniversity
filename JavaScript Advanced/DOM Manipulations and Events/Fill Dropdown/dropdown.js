function addItem() {
    const [textInput, valueInput] = document.querySelectorAll('input[type="text"]');
    const selectEl = document.getElementById('menu');
    const optionEl = document.createElement('option');
    optionEl.textContent = textInput.value;
    optionEl.value = valueInput.value;
    selectEl.appendChild(optionEl);
    textInput.value = '';
    valueInput.value = '';
}
