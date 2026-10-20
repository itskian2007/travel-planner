import json

with open('backend/biome_images_150.json') as f:
    biomes = json.load(f)

with open('backend/procedural_days.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where DAY_THEMES_BY_ENV starts and ends
start_marker = "DAY_THEMES_BY_ENV = {"
end_marker = "\ndef build_procedural_day("

start_pos = text.find(start_marker)
end_pos = text.find(end_marker)

assert start_pos != -1, "Could not find start_marker"
assert end_pos != -1, "Could not find end_marker"

import sys
sys.path.append('backend')
from procedural_days import DAY_THEMES_BY_ENV

# Modify DAY_THEMES_BY_ENV in python data structure
for env, days in DAY_THEMES_BY_ENV.items():
    urls = biomes[env]
    for d_idx, day in enumerate(days):
        m = list(day['morning'])
        m[6] = urls[d_idx * 3 + 0]
        day['morning'] = tuple(m)
        
        mid = list(day['midday'])
        mid[6] = urls[d_idx * 3 + 1]
        day['midday'] = tuple(mid)
        
        e = list(day['evening'])
        e[6] = urls[d_idx * 3 + 2]
        day['evening'] = tuple(e)

# Pretty format DAY_THEMES_BY_ENV
import pprint
formatted = pprint.pformat(DAY_THEMES_BY_ENV, indent=4, width=120, sort_dicts=False)
new_themes_code = f"DAY_THEMES_BY_ENV = {formatted}\n"

new_full_text = text[:start_pos] + new_themes_code + text[end_pos:]

with open('backend/procedural_days.py', 'w', encoding='utf-8') as f:
    f.write(new_full_text)

print("Successfully updated DAY_THEMES_BY_ENV in backend/procedural_days.py!")
