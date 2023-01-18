
valid = ['Seattle', 'BothelWA']

def url(city):
    if city not in valid:
        raise ValueError('City not found')

    return f'https://www.cleardarksky.com/c/{city}csk.gif'


def forecast(city):
    return {'url': url(city)}
