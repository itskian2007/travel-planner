import json
import re

with open('backend/resolved_61_slots.json') as f:
    resolved = json.load(f)

# File 1: backend/destinations_multi_days.py
with open('backend/destinations_multi_days.py', 'r', encoding='utf-8') as f:
    text_std = f.read()

# File 2: backend/destinations_multi_days_extra.py
with open('backend/destinations_multi_days_extra.py', 'r', encoding='utf-8') as f:
    text_extra = f.read()

def update_file_text(file_text, target_city, target_loc, new_url):
    # Find block containing target_loc
    loc_pos = file_text.find(f'"{target_loc}"')
    if loc_pos == -1:
        loc_pos = file_text.find(f"'{target_loc}'")
    if loc_pos == -1:
        raise ValueError(f'Could not find location "{target_loc}" in file!')
    
    # Within the preceding ~500 characters, find "image_url": "..." or 'image_url': '...'
    preceding_start = max(0, loc_pos - 600)
    preceding = file_text[preceding_start:loc_pos]
    
    # Pattern to match image_url
    match = list(re.finditer(r'("image_url":\s*")[^"]+(")', preceding))
    if not match:
        match = list(re.finditer(r"('image_url':\s*')[^']+(')", preceding))
    if not match:
        raise ValueError(f'Could not find image_url before location "{target_loc}"!')
    
    last_match = match[-1]
    rel_start = preceding_start + last_match.start()
    rel_end = preceding_start + last_match.end()
    
    old_full = file_text[rel_start:rel_end]
    new_full = f'{last_match.group(1)}{new_url}{last_match.group(2)}'
    
    return file_text[:rel_start] + new_full + file_text[rel_end:]

STANDARD_CITIES = ['tokyo', 'bali', 'rome', 'paris', 'iceland', 'swiss alps', 'kyoto', 'barcelona', 'bangkok', 'dubai', 'seoul', 'new york', 'london']
EXTRA_CITIES = ['amsterdam', 'singapore', 'sydney', 'cairo', 'istanbul', 'rio', 'capetown']

import sys
sys.path.append('backend')
from destinations_multi_days import MULTI_DAYS_EXTENSIONS

applied_count = 0
for k, v in resolved.items():
    city, d_num, a_num = k.split('|')
    d_idx = int(d_num) - 2
    a_idx = int(a_num)
    target_loc = MULTI_DAYS_EXTENSIONS[city][d_idx]['activities'][a_idx]['location_name']
    new_url = v[1]
    
    if city in STANDARD_CITIES:
        text_std = update_file_text(text_std, city, target_loc, new_url)
        applied_count += 1
    elif city in EXTRA_CITIES:
        text_extra = update_file_text(text_extra, city, target_loc, new_url)
        applied_count += 1

print(f'Total updates processed: {applied_count}')

with open('backend/destinations_multi_days.py', 'w', encoding='utf-8') as f:
    f.write(text_std)

with open('backend/destinations_multi_days_extra.py', 'w', encoding='utf-8') as f:
    f.write(text_extra)

print('Successfully updated destinations_multi_days.py and destinations_multi_days_extra.py!')
