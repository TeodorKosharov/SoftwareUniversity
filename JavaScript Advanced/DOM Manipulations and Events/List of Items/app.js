function addItem() {
    let fieldValue = document.getElementById('newItemText');
    const list = document.getElementById('items');
    const newLi = document.createElement('li');
    newLi.textContent = fieldValue.value;
    fieldValue.value = '';
    list.appendChild(newLi);

}
