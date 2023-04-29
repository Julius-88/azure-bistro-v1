// Set the min date to today
const dateField = document.getElementById('date');
const today = new Date().toISOString().slice(0, 10);
dateField.min = today;

// Update the time field based on the selected date
dateField.addEventListener('change', updateAvailableTimes);

function updateAvailableTimes() {
  const selectedDate = new Date(dateField.value);
  const dayOfWeek = selectedDate.getDay();
  const timeField = document.getElementById('time');

  // Clear the current options
  timeField.innerHTML = '';

  let timeOptions = [];
  if (dayOfWeek === 0 || dayOfWeek === 6) {
    // Saturday and Sunday
    timeOptions = ['18:00', '20:00', '22:00', '00:00'];
  } else {
    // Monday to Friday
    timeOptions = ['16:00', '18:00', '20:00', '22:00'];
  }

  // Add new options
  for (const timeOption of timeOptions) {
    const option = document.createElement('option');
    option.value = timeOption;
    option.textContent = timeOption;
    timeField.appendChild(option);
  }
}

// Call updateAvailableTimes() to set initial values
updateAvailableTimes();
