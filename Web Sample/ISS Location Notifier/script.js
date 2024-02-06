// Get current time and display it in different cities
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

