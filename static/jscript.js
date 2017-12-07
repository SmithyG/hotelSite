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

function validateBookingForm() {
    //The validateBookingForm function is designed to prevent an incomplete form to be submitted
    //Each of the blocks below get each field from the form and check that they are not empty
    //If they are empty, an alert is displayed and the bookings file is left unchanged
    var complete = true;
    var x = document.forms["bookingForm"]["bookingName"].value;
    if (x == "") {
        alert("Name must be filled out");
        complete = false;
        return false;
    }
    var x = document.forms["bookingForm"]["email"].value;
    if (x == "") {
        alert("Email must be filled out");
        complete = false;
        return false;
    }
    var x = document.forms["bookingForm"]["arrivalDate"].value;
    if (x == "") {
        alert("Arrival Date must be filled out");
        complete = false;
        return false;
    }
    var x = document.forms["bookingForm"]["departureDate"].value;
    if (x == "") {
        alert("Departure Date must be filled out");
        complete = false;
        return false;
    }
    //Here the two date inputs are compared with each other
    var arrival = new Date(document.forms["bookingForm"]["arrivalDate"].value);
    var departure = new Date(document.forms["bookingForm"]["departureDate"].value);
    //If a user has entered an arrival date that is after the departure date, an alert is displayed
    //The form is prevented from being submitted as a result
    if (arrival > departure)
    {
        alert("Arrival cannot be after departure");
        complete = false;
        return false;
    }
    //If any of the above statements are executed, the value of complete is set to false
    //Therefore, if complete still equals its original value of true then we know that the form is valid
    //An appropriate message is given to the user for feedback
    if (complete === true)
    {
        alert("Thank you for your booking request! Your selected booking will appear once hotel staff confirm dates")
    }

}

function validateReviewForm() {
    var complete = true;
    var x = document.forms["reviewForm"]["name"].value;
    if (x == "") {
        alert("Name must be filled out");
        complete = false;
        return false;
    }
    var x = document.getElementById("commentField").value;
    if (x == "") {
        alert("Comment must be filled out");
        complete = false;
        return false;
    }
    //If any of the above statements are executed, the value of complete is set to false
    //Therefore, if complete still equals its original value of true then we know that the form is valid
    //An appropriate message is given to the user for feedback
    if (complete === true) {
        alert("Thank you for your feedback!");
    }
}
