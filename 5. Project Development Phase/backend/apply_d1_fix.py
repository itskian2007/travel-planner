import json

with open('backend/destinations_extra.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Rio Arpoador
old_rio_block = '''                    {
                        "activity_name": "Arpoador Rock Sunset Ritual & Ipanema Beachside Samba",
                        "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",'''

new_rio_block = '''                    {
                        "activity_name": "Arpoador Rock Sunset Ritual & Ipanema Beachside Samba",
                        "image_url": "https://images.unsplash.com/photo-1694798059838-b276ae8d356a?auto=format&fit=crop&w=800&q=80",'''

# Replace Cape Town Camps Bay
old_ct_block = '''                    {
                        "activity_name": "Camps Bay Sunset Beach Promenade & Atlantic Breakers",
                        "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",'''

new_ct_block = '''                    {
                        "activity_name": "Camps Bay Sunset Beach Promenade & Atlantic Breakers",
                        "image_url": "https://images.unsplash.com/photo-1576485375217-d6a95e34d043?auto=format&fit=crop&w=800&q=80",'''

assert old_rio_block in text, 'old_rio_block not found!'
assert old_ct_block in text, 'old_ct_block not found!'

text = text.replace(old_rio_block, new_rio_block, 1)
text = text.replace(old_ct_block, new_ct_block, 1)

with open('backend/destinations_extra.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Successfully updated Rio and Cape Town Day 1!')
