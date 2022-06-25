window.addEventListener("load", solve);

function solve() {
    const [sendButton, clearButton] = Array.from(document.getElementsByTagName('button'));
    sendButton.addEventListener('click', sending);
    clearButton.addEventListener('click', clearing);

    const receivedOrdersSection = document.getElementById('received-orders');
    const completedOrdersSection = document.getElementById('completed-orders');

    const productsSelector = document.getElementById('type-product');
    const descriptionArea = document.getElementById('description');
    const clientNameArea = document.getElementById('client-name');
    const clientPhoneArea = document.getElementById('client-phone');

    function sending(event) {
        event.preventDefault();

        if (descriptionArea.value !== '' && clientNameArea.value !== '' && clientPhoneArea.value !== '') {
            const newDiv = document.createElement('div');
            newDiv.className = 'container';
            newDiv.innerHTML = `
            <h2>Product type for repair: ${productsSelector.value}</h2>
            <h3>Client information: ${clientNameArea.value}, ${clientPhoneArea.value}</h3>
            <h4>Description of the problem: ${descriptionArea.value}</h4>
            <button class="start-btn">Start repair</button>
            <button class="finish-btn" disabled>Finish repair</button>`;
            receivedOrdersSection.appendChild(newDiv);

            const [startButton, finishButton] = Array.from(newDiv.querySelectorAll('button'));
            startButton.addEventListener('click', start);
            finishButton.addEventListener('click', finish);

            function start(event) {
                event.target.disabled = true;
                finishButton.disabled = false;
            }

            function finish(event) {
                const newDiv = event.target.parentElement;
                newDiv.removeChild(event.target.parentElement.getElementsByTagName('button')[0]);
                event.target.parentElement.parentElement.removeChild(newDiv);
                newDiv.removeChild(event.target);
                completedOrdersSection.appendChild(newDiv);
            }
        }

        descriptionArea.value = '';
        clientNameArea.value = '';
        clientPhoneArea.value = '';
    }

    function clearing() {
        const divs = Array.from(completedOrdersSection.querySelectorAll('.container'));
        divs.forEach(x => x.remove());
    }
}
