import requests
from bs4 import BeautifulSoup


def text_forecast(lat, lon):
    url_template = 'https://forecast.weather.gov/MapClick.php?'\
        'lat={:.3f}&lon={:.3f}&unit=0&lg=english&FcstType=text&TextType=1'
    url = url_template.format(lat, lon)
    # TODO make the parameters a dict in the get request
    page = requests.get(url)

    parsed = BeautifulSoup(page.text, 'html.parser')
    # print(parsed.prettify())
    forecast_block = ''.join([str(l) for l in parsed.find_all('table')[1].find('td').contents])
    forecasts = forecast_block.split('<br/>\n<br/>\n')
    return forecasts[:3]


def synoptic_map():
    return 'http://www.wpc.ncep.noaa.gov//noaa/noaa.gif'


def graphs(lat, lon):
    url_template = 'https://forecast.weather.gov/meteograms/Plotter.php?'\
        'lat={:.3f}&lon={:.3f}&wfo=SEW&zcode=WAZ556&gset=20&gdiff=3&unit=0&tinfo=PY8'\
        '&ahour={}&pcmd=10011111000000000000000000000000000000000000000000000000000'\
        '&lg=en&indu=1!1!1!&dd=&bw=&hrspan=48&pqpfhr=6&psnwhr=6'

    return [url_template.format(lat, lon, hour) for hour in range(0, 144, 48)]


def forecast(lat, lon):
    # TODO add try statements and make everything async
    data = dict()

    data['text'] = text_forecast(lat, lon)
    data['map'] = synoptic_map()
    data['graph'] = graphs(lat, lon)

    return data
