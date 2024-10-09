document.getElementById('generateBtn').addEventListener('click', function() {
    const length = document.getElementById('lengthSlider').value;
    const uppercase = document.getElementById('uppercase').checked;
    const lowercase = document.getElementById('lowercase').checked;
    const numbers = document.getElementById('numbers').checked;
    const symbols = document.getElementById('symbols').checked;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            length: parseInt(length),
            uppercase: uppercase,
            lowercase: lowercase,
            numbers: numbers,
            symbols: symbols
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('password').value = data.password;
    });
});

function updateSliderValue(value) {
    document.getElementById('sliderValue').textContent = value;
}
