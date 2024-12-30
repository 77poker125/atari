import feedparser
import re

# now do the weather
import requests

url = "https://USER:PASSWORD@api.meteomatics.com/now--now+6H:PT1H/t_2m:F,precip_1h:mm/postal_POSTCODEHERE/csv?model=mix"
output_file = "weather.txt"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Write the content to a text file
    with open(output_file, 'w') as file:
        file.write(response.text)
    print(f"Data has been successfully written to {output_file}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

