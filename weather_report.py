import jinja2
from datetime import datetime
import logging
import clear_sky
import nws

def make_report():
    env = env = jinja2.Environment(
                    loader=jinja2.PackageLoader("weather_report"),
                    autoescape=jinja2.select_autoescape()
                )
    template = env.get_template('weather.html')

    report_data = dict()

    try:
        report_data['clear_sky'] = clear_sky.forecast('BothelWA')
    except Exception as e:
        logging.error(e)

    try:
        apartment_coordinates = (47.720, -122.300) # TODO parameterize
        report_data['nws'] = nws.forecast(*apartment_coordinates)
    except Exception as e:
        logging.error(e)

    report_data['date'] = datetime.now().strftime("%A, %B %d, %Y")
    return template.render(**report_data)
