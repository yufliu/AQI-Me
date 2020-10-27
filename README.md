# AQI-Me

## Next step notes:  
Figure out how to host it on a server so that a message (location) from a phone can be used to fetch the actual AQI

### Inspiration. 
I live in San Jose, California and it has been ravaged by wildfires within the last couple of weeks. The air quality here has reached dangerously unhealthy levels and I wanted an easier way for everyone to easily access air quality data on their phone without the need for WiFi. All you need is a cellular connection.

### What it does. 
The program analyzes air quality data from airnow.gov and texts it to your phone. It sends the AQI, any warnings, and an image of the current AQI status. This will provide someone good knowledge to start off their day knowing whether they should take it easy today and stay indoors or if it is okay for a jog around the neighborhood or etc. There are links that are attached for those with an internet connection as a bonus but the AQI and warning are all no-WiFi accessible.

### How I built it.  
I created this using Python and Selenium library to web scrape and gather the data from airnow.gov. The website provides accurate and current air quality data in any city. My program gathers the data and sends it using a Twillio API to successfully message an individual the current AQI in their location as well as links to pull up the website and look more in-depth

### Challenges I ran into.  
I had some issues grabbing the AQI data and the images initially but after stack overflowing around, I was able to figure it out

### Accomplishments that I'm proud of.  
I was proud to be able to scrape and attach two separate but useful links to the text message.

### What I learned.  
I learned how to send MMS with Twilio and scrape a weather website

### What's next for Air Quality Analyzer   
I would love to add tips and recommendations to keep the air quality in your home safe and clean as well as nearby cities that have better air quality without the use of WIFI. I want to also expand this ability to include COVID-19 data and include trends for it so people can have this information automatically sent to their phones as a one stop shop
