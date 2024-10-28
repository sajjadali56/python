import requests, pickle, os

CONFIG_FILE = 'config.pkl'

def get_rates(currency):
    url = 'https://api.exchangerate-api.com/v4/latest/' + currency
    response = requests.get(url)
    data = response.json()

    print(data)

    rates = data['rates']
    return rates

def read_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'rb') as f:
            config = pickle.load(f)
    else:
        config = {'ref_currency': 'USD'}
        write_config(config)
    return config

def write_config(config):
    with open(CONFIG_FILE, 'wb') as f:
        pickle.dump(config, f)
    