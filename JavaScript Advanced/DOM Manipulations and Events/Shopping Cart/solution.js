function solve() {
    Array.from(document.getElementsByClassName('add-product')).forEach(x => x.addEventListener('click', addButtonClick));
    const area = document.querySelector('textarea');
    let totalSum = 0;
    const checkout = document.getElementsByClassName('checkout')[0];
    checkout.addEventListener('click', calculateTotal);
    let products = new Set();

    function addButtonClick(event) {
        const currentButton = event.target;
        const productBlock = currentButton.parentElement.parentElement;
        const productBlockElements = productBlock.children;
        const productInfo = Array.from(productBlockElements).filter(x => x.className === 'product-details')[0];
        const productName = productInfo.children[0].textContent;
        products.add(productName);
        const productPrice = productBlockElements[3].textContent;
        totalSum += Number(productPrice);
        area.value += `Added ${productName} for ${Number(productPrice).toFixed(2)} to the cart.\n`;
    }

    function calculateTotal() {
        area.value += `You bought ${Array.from(products).join(', ')} for ${totalSum.toFixed(2)}.`;
        Array.from(document.getElementsByClassName('add-product')).forEach(x => x.removeEventListener('click', addButtonClick));
        checkout.removeEventListener('click', calculateTotal);
    }
}
