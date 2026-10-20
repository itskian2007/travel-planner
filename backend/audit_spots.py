import sys
sys.path.append('backend')
from destinations_db import DESTINATIONS_DATA
from destinations_extra import EXTRA_DESTINATIONS
from destinations_multi_days import MULTI_DAYS_EXTENSIONS, EXTRA_MULTI_DAYS
from procedural_days import DAY_THEMES_BY_ENV

all_dests = {}
all_dests.update(DESTINATIONS_DATA)
all_dests.update(EXTRA_DESTINATIONS)

all_multi = {}
all_multi.update(MULTI_DAYS_EXTENSIONS)
all_multi.update(EXTRA_MULTI_DAYS)

print("=" * 70)
print("AUDIT: ALL 20 CURATED DESTINATIONS, SPOTS, & IMAGES")
print("=" * 70)

image_library = set()
duplicates = []

for idx, (name, data) in enumerate(all_dests.items(), 1):
    disp = data.get('destination_display', name)
    env = data.get('environment_type', 'N/A')
    hero = data.get('hero_image', 'N/A')
    landmarks = data.get('nature_landmarks', [])
    
    print(f"\n[{idx}/20] {disp}")
    print(f"  Biomic Context : {env}")
    print(f"  Nature / Fauna : {', '.join(landmarks)}")
    print(f"  Hero Landscape : {hero}")
    
    # Check Day 1
    for day in data.get('days', []):
        print(f"  --- {day.get('title', 'Day 1')} ({day.get('neighborhood', '')}) ---")
        for act in day.get('activities', []):
            loc = act.get('location_name', '')
            act_name = act.get('activity_name', '')
            img = act.get('image_url', '')
            if img in image_library:
                duplicates.append((disp, loc, img))
            else:
                image_library.add(img)
            print(f"    • {act_name}")
            print(f"      Location: {loc}")
            print(f"      Image   : {img}")

    # Check Day 2 & 3
    for day in all_multi.get(name, []):
        print(f"  --- Day {day.get('day_number', '+')}: {day.get('title', '')} ({day.get('neighborhood', '')}) ---")
        for act in day.get('activities', []):
            loc = act.get('location_name', '')
            act_name = act.get('activity_name', '')
            img = act.get('image_url', '')
            if img in image_library:
                duplicates.append((disp, loc, img))
            else:
                image_library.add(img)
            print(f"    • {act_name}")
            print(f"      Location: {loc}")
            print(f"      Image   : {img}")

print("\n" + "=" * 70)
print(f"TOTAL AUDITED IMAGES IN CURATED DB: {len(image_library)}")
print(f"DUPLICATE IMAGES: {len(duplicates)}")
for dup in duplicates:
    print(f"  WARNING DUPLICATE: {dup[0]} -> {dup[1]} -> {dup[2]}")

print("\n" + "=" * 70)
print("AUDIT: PROCEDURAL BIOME ARCHETYPES")
print("=" * 70)
for env_name, days in DAY_THEMES_BY_ENV.items():
    print(f"\nArchetype: {env_name} ({len(days)} procedural days)")
    for d in days:
        print(f"  Day Theme: {d.get('title')} ({d.get('neighborhood')})")
        for act in d.get('activities', []):
            loc = act.get('location_name')
            img = act.get('image_url')
            if img in image_library:
                duplicates.append((env_name, loc, img))
            else:
                image_library.add(img)
            print(f"    - {act.get('activity_name')} [{loc}]")
            print(f"      Image: {img}")

print("\n" + "=" * 70)
print(f"TOTAL COMBINED UNIQUE IMAGES: {len(image_library)}")
print(f"TOTAL PROCEDURAL DUPLICATES DETECTED: {len(duplicates)}")
