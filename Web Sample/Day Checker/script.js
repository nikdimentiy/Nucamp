function checkDay() {
    var dayInput = document.getElementById("dayInput").value;
    var resultElement = document.getElementById("result");
    var inputElement = document.getElementById("dayInput");

    // Reset input color
    inputElement.classList.remove("red", "blue", "green");
    // Reset result text color
    resultElement.classList.remove("red-text", "blue-text", "green-text");

    switch (dayInput) {
        case "1":
        case "2":
        case "3":
            inputElement.classList.add("red");
            resultElement.classList.add("red-text");
            break;
        case "4":
        case "5":
            inputElement.classList.add("blue");
            resultElement.classList.add("blue-text");
            break;
        case "6":
        case "7":
            inputElement.classList.add("green");
            resultElement.classList.add("green-text");
            break;
        default:
            break;
    }

    var dayName;

    switch (dayInput) {
        case "1":
            dayName = "Monday 📅";
            resultElement.textContent = "This day of the week is " + dayName + ". It's the start of the week, time to set your goals!";
            break;
        case "2":
            dayName = "Tuesday 📅";
            resultElement.textContent = "This day of the week is " + dayName + ". Stay focused and keep pushing forward!";
            break;
        case "3":
            dayName = "Wednesday 📅";
            resultElement.textContent = "This day of the week is " + dayName + ". You're halfway there, keep up the good work!";
            break;
        case "4":
            dayName = "Thursday 📅";
            resultElement.textContent = "This day of the week is " + dayName + ". Finish strong, the weekend is almost here!";
            break;
        case "5":
            dayName = "Friday 📅";
            resultElement.textContent = "This day of the week is " + dayName + ". It's time to celebrate, you made it through the week!";
            break;
        case "6":
            dayName = "Saturday 📅";
            resultElement.textContent = "This day of the week is " + dayName + ". Relax and enjoy your day off!";
            break;
        case "7":
            dayName = "Sunday 📅";
            resultElement.textContent = "This day of the week is " + dayName + ". Make the most of your day off and recharge!";
            break;
        default:
            resultElement.textContent = "You entered a non-existent day of the week.";
            break;
    }

    resultElement.classList.add("result");
}

