document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    
    const message = `Thank you, ${name}! We will contact you at ${email}.`;
    document.getElementById('formMessage').textContent = message;
});
