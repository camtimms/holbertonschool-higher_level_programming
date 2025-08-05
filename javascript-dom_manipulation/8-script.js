document.addEventListener('DOMContentLoaded', function() {
    // Simulate API response
    const mockData = { hello: "Salut" };
    document.getElementById('hello').textContent = mockData.hello;

    // Or try the real API (might still fail due to CORS)
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json())
        .then(data => {
            document.getElementById('hello').textContent = data.hello;
        })
        .catch(error => {
            console.log('CORS error (expected), using mock data');
            document.getElementById('hello').textContent = "Salut";
        });
});