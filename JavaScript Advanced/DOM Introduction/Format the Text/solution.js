function solve() {
    const input = document.getElementById('input').value;
    const output = document.getElementById('output');
    const sentences = input.split('.').filter(s => s.length != 0);

    if (sentences.length > 0) {
        for (const text of sentences) {
            const textParagraph = sentences.splice(0, 3).join('. ') + '.';
            const p = document.createElement('p');
            p.textContent = textParagraph;
            output.appendChild(p);
        }
    }
}
