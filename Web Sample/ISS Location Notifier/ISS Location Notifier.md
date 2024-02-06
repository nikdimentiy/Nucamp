# 🚀 ISS Location Notifier 🌌

## Project Overview
This HTML document represents the frontend of a project named "ISS Location Notifier." The purpose of this project is to provide real-time updates about the current location of the International Space Station (ISS). Users receive notifications and can explore the ISS coordinates on a map. The project also displays the last notification time and the current time in various cities.

## Structure
- **HTML Structure:** The HTML document is structured with essential elements such as headings, paragraphs, lists, and tables.
  
- **CSS Styling:** The document includes internal styles for basic formatting, such as font, alignment, and table styles. External styling is applied through a linked "styles.css" file.

## Features
1. **ISS Location Display:**
   - The project fetches the ISS location from the [ISS Location Now API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/) and displays the latitude and longitude on the webpage.

2. **Notifications:**
   - The page presents information about the last notification time, keeping users informed about when the last update occurred.

3. **Current Time:**
   - A table showcases the current time in different cities, allowing users to track the ISS position across various time zones.

4. **Leaflet Map Integration:**
   - The Leaflet library is integrated into the project using a script tag to create an interactive map of the ISS location.

## City Time Display
- 🗼 Tokyo
- 🗽 New York
- 🎡 London
- 🍫 Brussels
- 🌉 San Francisco

## ISS Location Updates
- The webpage automatically updates the ISS location every 5 seconds, providing real-time information.

## Dependencies
- [Leaflet Library](https://unpkg.com/leaflet@1.7.1/dist/leaflet.js): Used for mapping functionality.

## How to Run
1. Open the HTML file in a web browser.
2. The page will automatically fetch and display the ISS location.
3. Explore the map and check the last notification time and current times in different cities.

**Note:** Adjust the API endpoint, update intervals, and other settings as needed for your specific requirements.

Feel free to explore the code in "script.js" for additional details on functionality.

🌍 Happy ISS tracking! 🛰️
