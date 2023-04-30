(function () {
  emailjs.init('reJOcVVShhJl7jLGK');
})();

window.onload = function () {
  document.getElementById('form').addEventListener('submit', function (event) {
    event.preventDefault();

    emailjs.sendForm('service_azure', 'template_azure', this).then(
      function () {
        alert('Your message has been sent!');
        setTimeout(() => {
          event.target.reset();
        }, 10);
      },
      function (error) {
        alert('Your message could not be sent.');
        console.log(error);
      }
    );
  });
};

const form = document.getElementById('form');
const submitButton = document.getElementById('submit-button');

form.addEventListener('keydown', function (e) {
  if (e.key === 'Enter') {
    e.preventDefault(); // Prevent the default behavior of the 'Enter' key
    submitButton.click(); // Trigger the submit button's click event
  }
});
