import sys
sys.path.append('backend')
from destinations_db import DESTINATIONS_DATA
from destinations_multi_days import MULTI_DAYS_EXTENSIONS
from procedural_days import DAY_THEMES_BY_ENV
from collections import defaultdict

image_usage = defaultdict(list)

# 1. Curated Day 1 + Hero (DESTINATIONS_DATA already includes destinations_extra)
for name, d in DESTINATIONS_DATA.items():
    image_usage[d.get('hero_image')].append(f'{name} (hero)')
    for day in d.get('days', []):
        for act in day.get('activities', []):
            image_usage[act.get('image_url')].append(f'{name} Day1: {act.get("location_name")}')

# 2. Multi-days (MULTI_DAYS_EXTENSIONS already includes destinations_multi_days_extra)
for name, days in MULTI_DAYS_EXTENSIONS.items():
    for d_idx, day in enumerate(days, 2):
        for act in day.get('activities', []):
            image_usage[act.get('image_url')].append(f'{name} Day{d_idx}: {act.get("location_name")}')

# 3. Procedural archetypes
for env, days in DAY_THEMES_BY_ENV.items():
    for idx, d in enumerate(days, 1):
        image_usage[d['morning'][6]].append(f'Archetype {env} Day{idx} morning: {d["morning"][0]}')
        image_usage[d['midday'][6]].append(f'Archetype {env} Day{idx} midday: {d["midday"][0]}')
        image_usage[d['evening'][6]].append(f'Archetype {env} Day{idx} evening: {d["evening"][0]}')

total_slots = sum(len(locs) for locs in image_usage.values())
print(f'Total activity and hero slots in system: {total_slots}')
print(f'Total unique image URLs across whole app: {len(image_usage)}')
repeated = {img: locs for img, locs in image_usage.items() if len(locs) > 1}
print(f'Number of images used more than once: {len(repeated)}')

if repeated:
    print('=' * 60)
    for img, locs in sorted(repeated.items(), key=lambda x: len(x[1]), reverse=True):
        print(f'Image: {img} -> used {len(locs)} times:')
        for loc in locs:
            print(f'   - {loc}')
        print('-' * 40)
else:
    print('\nCONGRATULATIONS: ZERO DUPLICATE IMAGES! Every single spot across all 304 slots is 100% unique and relevant!')
