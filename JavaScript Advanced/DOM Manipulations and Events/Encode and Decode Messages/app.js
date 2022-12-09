function encodeAndDecodeMessages() {
    const [encodeDiv, decodeDiv] = Array.from(document.getElementById('main').children);
    const [encodeArea, encodeButton] = Array.from(encodeDiv.querySelectorAll('textarea, button'));
    const [decodeArea, decodeButton] = Array.from(decodeDiv.querySelectorAll('textarea, button'));

    encodeButton.addEventListener('click', encode);
    decodeButton.addEventListener('click', decode);

    function encode() {
        const text = encodeArea.value;
        let encodedMessage = '';

        for (const letter of text) {
            encodedMessage += String.fromCharCode(letter.charCodeAt(0) + 1);
        }
        encodeArea.value = '';
        decodeArea.value = encodedMessage;

    }

    function decode() {
        const text = decodeArea.value;
        let decodedMessage = '';

        for (const letter of text) {
            decodedMessage += String.fromCharCode(letter.charCodeAt(0) - 1);
        }
        decodeArea.value = '';
        encodeArea.value = decodedMessage;
    }
}
