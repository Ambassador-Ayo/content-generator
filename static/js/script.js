function generateContent() {
    const inputText = document.getElementById('input-text').value;

    // Send an AJAX request to the server to generate content
    fetch('/generate', {
        method: 'POST',
        body: JSON.stringify({ input_text: inputText }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.text())
    .then(data => {
        // Update the generated content on the webpage
        document.getElementById('generated-text').textContent = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
