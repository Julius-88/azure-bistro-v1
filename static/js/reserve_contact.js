(function () {
  emailjs.init('reJOcVVShhJl7jLGK');
})();

window.onload = function () {
  // Get the reservation details from local storage
  const reservationDate = localStorage.getItem('reservation_date');
  const reservationTime = localStorage.getItem('reservation_time');
  const reservationGuests = localStorage.getItem('reservation_guests');

  // Set the reservation details as hidden inputs in the form
  document.getElementById('reservation_date').value = reservationDate;
  document.getElementById('reservation_time').value = reservationTime;
  document.getElementById('reservation_guests').value = reservationGuests;

  document.getElementById('form').addEventListener('submit', function (event) {
    event.preventDefault();

    // console.log('reservation_date:', this.reservation_date.value);
    // console.log('reservation_time:', this.reservation_time.value);
    // console.log('reservation_guests:', this.reservation_guests.value);
    emailjs.sendForm('service_azure', 'template_confirm', this).then(
      function () {
        alert('Your message has been sent!');
        window.location.href = '/reserve/';
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
