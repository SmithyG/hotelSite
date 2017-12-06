function pastDate() {
    //The pastDate function is used in bookings.html to prevent a user from selecting a date in the past
    //The current date is assigned to the variable date
    var today = new Date().toISOString().split('T')[0];
    //The elements that need to be changed are selected here and set
    document.getElementsByName("arrivalDate")[0].setAttribute('min', today);
    document.getElementsByName("departureDate")[0].setAttribute('min', today);
}

function myMap() {
    //the myMap function is used to control the embedded google map found on home.html
    var mapCanvas = document.getElementById("map");
    var myCenter = new google.maps.LatLng(28.486230, -81.462494);
    var mapOptions = {center: myCenter, zoom: 11};
    var map = new google.maps.Map(mapCanvas, mapOptions);
    var marker = new google.maps.Marker({
        position: myCenter,
        animation: google.maps.Animation.BOUNCE
    });
    marker.setMap(map);
}
