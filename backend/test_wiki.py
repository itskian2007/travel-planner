import urllib.request, urllib.parse, json

def get_wiki_summary_image(query):
    endpoint = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(query)}"
    req = urllib.request.Request(endpoint, headers={'User-Agent': 'TravelPlannerBot/1.0 (contact: test@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=5) as res:
            data = json.loads(res.read())
            img = data.get('originalimage', {}).get('source') or data.get('thumbnail', {}).get('source')
            return img
    except Exception as e:
        return None

queries = [
    'Meiji_Shrine', 'Shimokitazawa', 'Shibuya_Crossing', 'Omoide_Yokocho', 'Akihabara',
    'Tegallalang_Rice_Terrace', 'Uluwatu_Temple', 'Canggu',
    'Colosseum', 'Aventine_Keyhole', 'Trastevere', 'Roman_Forum',
    'Pont_de_Bir-Hakeim', 'Passage_des_Panoramas', 'Montmartre', 'Sacre-Coeur,_Paris',
    'Seljalandsfoss', 'Solheimajokull', 'Reynisfjara', 'Thingvellir', 'Strokkur',
    'Lauterbrunnen', 'Murren', 'Gornergrat', 'Matterhorn',
    'Arashiyama', 'Fushimi_Inari-taisha', 'Gion',
    'Sagrada_Familia', 'Park_Guell', 'Bunkers_del_Carmel',
    'Wat_Arun', 'Chatuchak_Weekend_Market',
    'Museum_of_the_Future', 'Burj_Khalifa', 'Dubai_Marina',
    'Gyeongbokgung', 'Bukchon_Hanok_Village', 'N_Seoul_Tower', 'Seongsu-dong',
    'Central_Park', 'High_Line', 'Times_Square', 'Museum_of_Modern_Art',
    'Tower_Bridge', 'Borough_Market', 'Camden_Market', 'Soho,_London',
    'Rijksmuseum', 'Vondelpark', 'Zaanse_Schans',
    'Gardens_by_the_Bay', 'Marina_Bay_Sands',
    'Sydney_Opera_House', 'Bondi_Beach', 'Manly_Beach', 'The_Rocks,_Sydney',
    'Giza_pyramid_complex', 'Grand_Egyptian_Museum', 'Khan_el-Khalili', 'Hanging_Church', 'Saqqara',
    'Hagia_Sophia', 'Galata_Tower', 'Topkapi_Palace', 'Bosphorus', 'Ortakoy_Mosque',
    'Christ_the_Redeemer_(statue)', 'Sugarloaf_Mountain', 'Escadaria_Selaron', 'Ipanema', 'Tijuca_National_Park',
    'Table_Mountain', 'Bo-Kaap', 'Camps_Bay', 'Boulders_Beach', 'Kirstenbosch_National_Botanical_Garden', 'Cape_Point'
]

found = 0
for q in queries:
    img = get_wiki_summary_image(q)
    status = "FOUND" if img else "MISSING"
    if img:
        found += 1
    print(f"{q}: {status} -> {img[:60] if img else ''}")

print(f"\nTotal queries: {len(queries)}, Total Found: {found}")
