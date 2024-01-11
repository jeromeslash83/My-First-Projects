from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from icalendar import Calendar, Event
from datetime import datetime
import pytz

# Function to validate event data
def validate_event_data(event):
    if not event['summary']:
        raise ValueError("Missing event summary")
    if not isinstance(event['dtstart'], datetime):
        raise TypeError("dtstart is not a datetime object")

# URL of the website to scrape
url = 'https://pace.uwinnipegcourses.ca/program-calendar?program=10095'

# Set up Chrome options for Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background without opening a browser window

# Set up the WebDriver
service = Service(executable_path= r"C:\Drivers\chromedriver-win64\chromedriver.exe")  
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the webpage
driver.get(url)

# Use WebDriverWait to wait for the element to be present
wait = WebDriverWait(driver, 10)
events = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.tui-full-calendar-weekday-schedule-block')))

for event in events:
    try:
        date_element = event.find_element(By.CSS_SELECTOR, '.tui-full-calendar-weekday-grid-date')
        title_element = event.find_element(By.CSS_SELECTOR, '.tui-full-calendar-weekday-schedule-title')
        
        date = date_element.text
        title = title_element.text

        print(f"Event: {title} on {date}")
    except NoSuchElementException:
        print("Element not found")

if not events:
    raise Exception("No calendar elements found. Check the CSS selector.")

events = []
for element in events:
    date_text = element.find_element(By.CLASS_NAME, 'DATE_CLASS').text
    event_name = element.find_element(By.CLASS_NAME, 'EVENT_CLASS').text

    if not date_text or not event_name:
        raise Exception("Date or Event name not found in an element.")

    try:
        # Convert date_text to datetime object (modify format as per actual data)
        event_date = datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Incorrect date format for {date_text}")

    event = {'summary': event_name, 'dtstart': event_date}
    validate_event_data(event)
    events.append(event)

# Create an ICS file
cal = Calendar()
for event in events:
    ical_event = Event()
    ical_event.add('summary', event['summary'])
    ical_event.add('dtstart', event['dtstart'])
    ical_event.add('dtstamp', datetime.now(pytz.utc))
    cal.add_component(ical_event)

# Write to an ical file
ics_file_path = 'my_calendar.ics'
with open(ics_file_path, 'wb') as ics_file:
    ics_file.write(cal.to_ical())

print("ICS file created at", ics_file_path)

# Close the browser
driver.quit()

# Debugging: Print events for verification
print("Scraped Events:", events)
