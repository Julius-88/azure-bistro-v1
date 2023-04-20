let map;

function initMap() {
  // Define the coordinates for the center of the map and the marker
  const location = { lat: 59.293667, lng: 18.082105 };

  // Initialize the map
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 59.293667, lng: 18.082105 },
    zoom: 16,
    disableDefaultUI: true,
    gestureHandling: 'cooperative',
  });

  // Add a marker to the map
  const marker = new google.maps.Marker({
    position: location,
    map: map,
  });
}
