function addItem() {
    let fieldValue = document.getElementById('newItemText');
    const list = document.getElementById('items');
    const newLi = document.createElement('li');
    newLi.textContent = fieldValue.value;
    fieldValue.value = '';
    list.appendChild(newLi);
    const deleteBtn = document.createElement('a');
    deleteBtn.textContent = '[Delete]';
    deleteBtn.href = '#';
    newLi.appendChild(deleteBtn);
    deleteBtn.addEventListener('click', onDelete);

    function onDelete(event) {
        event.target.parentElement.remove();
    }
}
