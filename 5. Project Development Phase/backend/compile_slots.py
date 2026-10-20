import sys
sys.path.append('backend')
from destinations_db import DESTINATIONS_DATA
from destinations_multi_days import MULTI_DAYS_EXTENSIONS
from procedural_days import DAY_THEMES_BY_ENV
import json

slots = []

# Curated
for city, data in DESTINATIONS_DATA.items():
    for idx, act in enumerate(data.get('days', [{}])[0].get('activities', [])):
        slots.append({
            'source': 'destinations_db' if city not in ['amsterdam', 'singapore', 'sydney', 'cairo', 'istanbul', 'rio', 'capetown'] else 'destinations_extra',
            'city': city,
            'day': 1,
            'slot_idx': idx,
            'activity_name': act['activity_name'],
            'location_name': act['location_name'],
            'search_query': act['location_name'] + ' ' + city,
            'current_url': act['image_url']
        })

for city, days in MULTI_DAYS_EXTENSIONS.items():
    for d_idx, day in enumerate(days, 2):
        for idx, act in enumerate(day.get('activities', [])):
            slots.append({
                'source': 'destinations_multi_days' if city not in ['amsterdam', 'singapore', 'sydney', 'cairo', 'istanbul', 'rio', 'capetown'] else 'destinations_multi_days_extra',
                'city': city,
                'day': d_idx,
                'slot_idx': idx,
                'activity_name': act['activity_name'],
                'location_name': act['location_name'],
                'search_query': act['location_name'] + ' ' + city,
                'current_url': act['image_url']
            })

# Procedural
for env, days in DAY_THEMES_BY_ENV.items():
    for d_idx, day in enumerate(days, 1):
        for slot_name in ['morning', 'midday', 'evening']:
            t = day[slot_name]
            slots.append({
                'source': 'procedural_days',
                'city': env,
                'day': d_idx,
                'slot_name': slot_name,
                'activity_name': t[0],
                'location_name': day['neighborhood'],
                'search_query': t[0] + ' ' + day['neighborhood'],
                'current_url': t[6]
            })

print('Total slots compiled:', len(slots))
with open('backend/slots_to_map.json', 'w', encoding='utf-8') as f:
    json.dump(slots, f, indent=2)
print('Successfully saved backend/slots_to_map.json')
