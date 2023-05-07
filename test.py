import requests

requests_result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en')

print(requests_result)

print(requests_result.content)