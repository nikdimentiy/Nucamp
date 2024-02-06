// Get current time and display it in different cities
// script.js

document.addEventListener("DOMContentLoaded", function () {
    // Function to fetch ISS location
    function getISSLocation() {
        fetch("https://api.wheretheiss.at/v1/satellites/25544")
            .then(response => response.json())
            .then(data => {
                updateLocation(data.latitude, data.longitude);
            })
            .catch(error => {
                console.error("Error fetching ISS location:", error);
            });
    }

    // Function to update latitude and longitude on the page
    function updateLocation(latitude, longitude) {
        document.getElementById("latitude").textContent = latitude.toFixed(2);
        document.getElementById("longitude").textContent = longitude.toFixed(2);
    }

    // Initial call to get ISS location
    getISSLocation();

    // Set interval to update ISS location every 5 seconds (adjust as needed)
    setInterval(getISSLocation, 5000);
});

function updateCurrentTime() {
    var now = new Date();

    // Tokyo time
    var tokyoTime = now.toLocaleString("en-US", { timeZone: "Asia/Tokyo" });
    document.getElementById('tokyoTime').innerHTML = tokyoTime;

    // New York time
    var newYorkTime = now.toLocaleString("en-US", { timeZone: "America/New_York" });
    document.getElementById('newYorkTime').innerHTML = newYorkTime;

    // London time
    var londonTime = now.toLocaleString("en-US", { timeZone: "Europe/London" });
    document.getElementById('londonTime').innerHTML = londonTime;

    // Brussels time
    var brusselsTime = now.toLocaleString("en-US", { timeZone: "Europe/Brussels" });
    document.getElementById('brusselsTime').innerHTML = brusselsTime;

    // San Francisco time
    var sanFranciscoTime = now.toLocaleString("en-US", { timeZone: "America/Los_Angeles" });
    document.getElementById('sanFranciscoTime').innerHTML = sanFranciscoTime;
}

// Update time every second
setInterval(updateCurrentTime, 1000);

// Get last notification time and display it
function updateLastNotificationTime() {
    var lastNotificationTime = new Date(); // Replace this with the actual last notification time
    var hours = lastNotificationTime.getUTCHours();
    var minutes = lastNotificationTime.getUTCMinutes();
    var seconds = lastNotificationTime.getUTCSeconds();
    document.getElementById('lastNotificationTime').innerHTML = 'Last Notification Time (UTC): ' + hours + ':' + minutes + ':' + seconds;
}

// Call the function to update last notification time
updateLastNotificationTime();



