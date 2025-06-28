import os
import json
import re
import requests
from urllib.parse import quote
import time

CITY_DATA_FILE = 'city_data.json'
CITY_DIR = os.path.join('locations', 'cities')
USER_AGENT = 'skerritteconomics-bot/1.0 (+https://skerritteconomics.com)'


def geocode(city, state):
    query = f"{city}, {state}"
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={quote(query)}"
    try:
        resp = requests.get(url, headers={'User-Agent': USER_AGENT}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data:
            return data[0]['lat'], data[0]['lon']
    except Exception as e:
        print(f"Failed to geocode {query}: {e}")
    return None, None


def update_file(filepath, lat, lon):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'<meta name="geo.position" content="[^"]*">',
                     f'<meta name="geo.position" content="{lat};{lon}">', content)
    content = re.sub(r'<meta name="ICBM" content="[^"]*">',
                     f'<meta name="ICBM" content="{lat}, {lon}">', content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    with open(CITY_DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for info in data.values():
        filename = info['filename']
        city = info['city_display']
        state = info['state_abbrev']
        filepath = os.path.join(CITY_DIR, filename)
        if not os.path.exists(filepath):
            continue
        lat, lon = geocode(city, state)
        if lat and lon:
            update_file(filepath, lat, lon)
            print(f"Updated {filepath} -> {lat}, {lon}")
            time.sleep(1)
        else:
            print(f"Skipping {filepath} (coordinates not found)")


if __name__ == '__main__':
    main()
