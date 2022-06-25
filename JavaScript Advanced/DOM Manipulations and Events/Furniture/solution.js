function solve() {
    const buttons = Array.from(document.getElementsByTagName('button'));
    const generateButton = buttons[0];
    const buyButton = buttons[1];

    const areas = Array.from(document.getElementsByTagName('textarea'));
    const generateArea = areas[0];
    const buyArea = areas[1];

    generateButton.addEventListener('click', generate);
    buyButton.addEventListener('click', buying);

    function generate() {
        const table = document.getElementsByClassName('table')[0];
        const products = JSON.parse(generateArea.value);

        for (const productObj of products) {
            const name = productObj.name;
            const img = productObj.img;
            const price = productObj.price;
            const decfactor = productObj['decFactor'];

            const newRow1 = document.createElement('tr');
            const newData1 = document.createElement('td');
            const newImg = document.createElement('img');
            newImg.src = img;
            newData1.appendChild(newImg)
            newRow1.appendChild(newData1);
            table.children[1].appendChild(newRow1);

            const newData2 = document.createElement('td');
            const newPara = document.createElement('p');
            newPara.textContent = name;
            newData2.appendChild(newPara);
            newRow1.appendChild(newData2);

            const newData3 = document.createElement('td');
            const newPara2 = document.createElement('p');
            newPara2.textContent = price;
            newData3.appendChild(newPara2);
            newRow1.appendChild(newData3);

            const newData4 = document.createElement('td');
            const newPara3 = document.createElement('p');
            newPara3.textContent = decfactor;
            newData4.appendChild(newPara3);
            newRow1.appendChild(newData4);

            const newData5 = document.createElement('td');
            const inpField = document.createElement('input');
            inpField.type = 'checkbox';
            newData5.appendChild(inpField);
            newRow1.appendChild(newData5);


        }


    }

    function buying() {
        const tableDates = Array.from(document.querySelectorAll('tbody')[0].children);
        let boughtFurniture = [];
        let totalPrice = 0;
        let totalDecor = 0;
        let totalCheckedBoxes = 0;

        for (const td of tableDates) {
            const tdElements = td.children;
            const checkBox = tdElements[4].children[0];
            const isChecked = checkBox.checked;

            if (isChecked) {
                const furnitureName = tdElements[1].textContent;
                const furnitureSum = Number(tdElements[2].textContent);
                const furnitureDecor = Number(tdElements[3].textContent);
                boughtFurniture.push(furnitureName);
                totalPrice += furnitureSum;
                totalDecor += furnitureDecor;
                totalCheckedBoxes++;
            }
        }
        buyArea.value += `Bought furniture: ${boughtFurniture.join(', ')}\n`;
        buyArea.value += `Total price: ${totalPrice.toFixed(2)}\n`;
        buyArea.value += `Average decoration factor: ${totalDecor / totalCheckedBoxes}`;

    }
}
