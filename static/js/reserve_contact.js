(function () {
  emailjs.init('reJOcVVShhJl7jLGK');
})();

window.onload = function () {
  document
    .getElementById('contact-form')
    .addEventListener('submit', function (event) {
      event.preventDefault();
      // generate a five digit number for the contact_number variable
      this.contact_number.value = (Math.random() * 100000) | 0;
      emailjs.sendForm('service_azure', 'template_confirm', this).then(
        function () {
          alert('Your message has been sent!');
          window.location.href = '/reserve/reserve/';
        },
        function (error) {
          alert('Your message could not be sent.');
          console.log(error);
        }
      );
    });
};

const form = document.getElementById('contact-form');
const submitButton = document.getElementById('submit-button');

form.addEventListener('keydown', function (e) {
  if (e.key === 'Enter') {
    e.preventDefault(); // Prevent the default behavior of the 'Enter' key
    submitButton.click(); // Trigger the submit button's click event
  }
});
