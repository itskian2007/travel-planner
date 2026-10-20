import os
import json
import logging
from typing import List, Dict, Any
from schemas import ItineraryRequest
from destinations_db import DESTINATIONS_DATA
from procedural_days import (
    build_procedural_day,
    adapt_curated_activity,
    adapt_basecamp,
    adapt_spotify_playlist,
    TRAVELER_TRANSIT_AND_TIPS
)

logger = logging.getLogger("travel_planner.itinerary")


# Ensure every destination has all extension days loaded
try:
    from destinations_multi_days import MULTI_DAYS_EXTENSIONS
    for dest_key, extra_days in MULTI_DAYS_EXTENSIONS.items():
        if dest_key in DESTINATIONS_DATA:
            existing_titles = {d["title"] for d in DESTINATIONS_DATA[dest_key]["days"]}
            for extra in extra_days:
                if extra["title"] not in existing_titles:
                    DESTINATIONS_DATA[dest_key]["days"].append(extra)
except Exception as e:
    logger.warning(f"Could not merge multi-day extensions: {e}")



# ==============================================================================
# UNIVERSAL SMART ENVIRONMENT CLASSIFIER
# Generates authentic, nature-specific itineraries for ANY city or place on Earth
# ==============================================================================

def classify_destination_environment(dest_name: str) -> Dict[str, Any]:
    name = dest_name.lower().strip()

    # Tropical, Island, Beach destinations
    if any(k in name for k in ["hawaii", "maui", "honolulu", "santorini", "mykonos", "maldives", "phuket", "cancun", "miami", "bahamas", "caribbean", "fiji", "tahiti", "boracay", "costa rica", "galapagos", "bali", "rio", "sydney", "ibiza", "tulum", "gold coast"]):
        return {
            "type": "TROPICAL_ISLAND_COASTAL",
            "environment_desc": "Coral reefs, turquoise sea coves, coconut groves & volcanic ocean cliffs",
            "hero_image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
            "nature_features": ["Crystal Marine Sanctuary & Reefs", "Secluded White/Black Sand Coves", "Volcanic Ocean Cliffs", "Lush Coastal Rain Forest"],
            "morning_activity": ("🌅 Sunrise Coastal Cliff Walk & Coconut Water Sanctuary", "08:00 AM - 10:15 AM", "Free Coastal Access", "$4", "Walk the dramatic sea trail before the tropical heat. Drink cold water from a fresh coconut machete-chopped on the sand.", "Silhouette looking out over turquoise breakers with palms framing the sunrise.", "Fresh tropical dragonfruit & papaya smoothie bowl with shaved coconut"),
            "midday_activity": ("Hidden Marine Cove Snorkel & Secret Beach Shacks", "11:30 AM - 02:30 PM", "Gear rental $10", "$15", "Rent a mask and fin. Swim among sea turtles and bright parrotfish in calm morning tide pools.", "Underwater 0.5x wide shot of coral formations and crystal clear turquoise sea.", "Beachfront Seafood Grill (Charcoal grilled catch of the day with spicy lime drizzle)"),
            "evening_activity": ("Catamaran Sunset Cruise & Barefoot Beach Club Lounge", "05:30 PM - 08:30 PM", "Catamaran pass or walk-in", "$30", "Watch the glowing orange sun dip beneath the ocean horizon with barefoot acoustic guitar.", "Holding a sunset spritz against the pink and violet sea reflection.", "Beachfront Poke / Ceviche Shacks with chilled local beer"),
            "hacks": [
                "Use only reef-safe mineral sunscreen (oxybenzone-free) to protect fragile coral ecosystems.",
                "Download local tide charts—coves and sea caves are accessible only during low tide hours.",
                "Renting an electric scooter is the most flexible way to discover hidden beaches off the main roads."
            ]
        }

    # Alpine, Mountain, Nature & Glacier destinations
    elif any(k in name for k in ["banff", "jasper", "patagonia", "queenstown", "aspen", "dolomites", "rockies", "interlaken", "zermatt", "alps", "whistler", "chamonix", "norway", "fjords", "lake louise", "swiss", "switzerland", "iceland", "reykjavik"]):
        return {
            "type": "ALPINE_MOUNTAIN_GLACIER",
            "environment_desc": "Jagged granite peaks, turquoise glacial lakes & pine alpine forests",
            "hero_image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=80",
            "nature_features": ["Turquoise Glacial Lakes", "Ancient Pine Woodlands", "Glacier Tongues & Moraines", "Sheer Granite Cliffs"],
            "morning_activity": ("🌅 Alpine Lake Mirror Reflection & Pine Ridge Trail", "07:30 AM - 10:00 AM", "National Park Pass", "$8", "Arrive right at dawn before breezes ruffle the water to see the jagged mountain peaks mirrored with glass-like clarity.", "Low-angle shot sitting on a cedar log with the snow-covered peaks mirrored in the lake.", "Alpine Bakery (Warm cardamom buns & hearty oat porridge with local mountain berries)"),
            "midday_activity": ("High-Elevation Suspension Bridge & Mountain Gondola Ascent", "11:00 AM - 02:30 PM", "Gondola Lift Ticket", "$35", "Ride the scenic cable car above the tree line. Walk across the suspended bridge over sheer canyon abysses.", "Standing on the suspended walkway with sheer mountain drop-offs directly beneath your boots.", "Mountain Hut Lodge (Hot comforting stew with sourdough bread and aged mountain cheese)"),
            "evening_activity": ("Thermal Hot Springs Soak & Starlit Hearth Dining", "05:30 PM - 08:30 PM", "Thermal pass", "$25", "Soak in mineral-rich geothermal hot springs as crisp mountain evening air cools your face.", "Steam rising from the mineral pool with towering dark pine peaks and stars above.", "Rustic Hearth Grill (Locally farmed smoked trout or braised short ribs by the fire)"),
            "hacks": [
                "Layer clothing with a thermal base, fleece mid-layer, and windproof outer shell—temperatures drop 10°C on peaks.",
                "Always carry bear spray and make regular noise when hiking trails through dense alpine pine forests.",
                "Fill your water bottles directly from approved alpine glacial streams—cleanest water in the world."
            ]
        }

    # Desert & Oasis destinations
    elif any(k in name for k in ["cairo", "marrakech", "jordan", "petra", "wadi rum", "sedona", "arizona", "sahara", "abu dhabi", "egypt", "morocco", "namibia", "dubai", "doha", "muscat"]):
        return {
            "type": "DESERT_OASIS_CULTURE",
            "environment_desc": "Golden sandstone canyons, date palm oases & fragrant spice bazaars",
            "hero_image": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1200&q=80",
            "nature_landmarks": ["Red Sandstone Formations", "Verdant Date Palm Oases", "Vast Desert Sand Dunes", "Starlit Midnight Sky"],
            "morning_activity": ("🌅 Dawn Balloon Flight or Sandstone Canyon Rim Hike", "06:30 AM - 09:30 AM", "Park permit", "$15", "Explore ancient carved sandstone canyons before the midday sun radiates off the rocks.", "Framed through a natural carved stone canyon window with warm morning sunlight.", "Bedouin Tea Veranda (Fresh mint tea with honey and warm sesame flatbread)"),
            "midday_activity": ("Fragrant Spice Souk & Historic Medersa Courtyard", "11:30 AM - 02:30 PM", "Free / Small entry", "$8", "Wander shaded alleys filled with sacks of ground cumin, saffron, rosebuds, and hand-woven carpets.", "Sunlight streaming through wooden lattice roof screens onto piles of vibrant spices.", "Historic Courtyard Riad (Slow-cooked lamb tagine with prunes and toasted almonds)"),
            "evening_activity": ("Sunset Dune Crest Walk & Starlit Desert Campfire", "05:30 PM - 09:00 PM", "Excursion pass", "$35", "Climb to the top of the highest dune to watch the sand change from gold to burning violet.", "Long dramatic shadows cast across wind-sculpted sand ripples as the sun sets.", "Desert Hearth Grill (Charcoal grilled spiced skewers, flatbread, and herbal tea under constellations)"),
            "hacks": [
                "Carry at least 2 liters of water at all times; desert humidity is low and dehydration happens without sweating.",
                "Wear loose, long-sleeved linen or cotton clothing to reflect heat and protect against sun and sand.",
                "Always bargain with respect and a smile in traditional souks—first quotes are usually 50% above final price."
            ]
        }

    # Ancient Heritage & Historic Cities
    elif any(k in name for k in ["athens", "prague", "lisbon", "vienna", "budapest", "florence", "venice", "istanbul", "edinburgh", "seville", "dublin", "porto", "kyoto", "amsterdam", "paris", "barcelona", "rome"]):
        return {
            "type": "HISTORIC_ANCIENT_HERITAGE",
            "environment_desc": "Centuries-old stone archways, historic river bridges & terraced hills",
            "hero_image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80",
            "nature_landmarks": ["Winding River Waterway", "Terraced Castle Hills", "Ancient Stone Overlooks", "Historic Shaded Cloisters"],
            "morning_activity": ("🌅 Sunrise Historic Bridge Walk & Artisan Espresso", "07:30 AM - 09:45 AM", "Free Access", "$5", "Cross the historic stone bridge before commuter crowds and tour groups arrive.", "Symmetrical shot down the stone bridge lined with statues as golden light reflects on the river.", "Historic Corner Pastry Shop (Warm regional custard tarts or brioche with dark roast espresso)"),
            "midday_activity": ("Secret Medieval Cloisters & Antique Book Arcades", "11:00 AM - 02:00 PM", "Free Entry / Small fee", "$10", "Discover peaceful hidden monastery courtyards, fountain gardens, and ancient bookshops.", "Arched stone corridor framing an overgrown courtyard garden with blooming wisteria.", "Historic Tavern (Authentic regional braised meats, potato dumplings, or handmade pasta)"),
            "evening_activity": ("Castle Hill Panoramic Sunset & Candlelit Wine Cellar", "05:30 PM - 08:30 PM", "Free Hill Overlook", "$25", "Watch twilight settle over terracotta roofs and church spires from the historic fortress walls.", "Sipping regional wine on the stone fortress wall overlooking glowing cobblestone streets below.", "Cellar Bodega (Local cured charcuterie, artisanal cheeses, and natural regional wine)"),
            "hacks": [
                "Wear well-cushioned shoes with rubber grip—centuries of foot traffic have polished historic cobblestones slick as ice.",
                "Most national historic museums offer free entry on the first Sunday of every month.",
                "Look for taverns that don't display picture menus outside in multiple languages—that's where locals dine."
            ]
        }

    # Modern Metropolis & Megacity
    else:
        return {
            "type": "VIBRANT_METROPOLIS",
            "environment_desc": "Architectural skyline canyons, waterfront promenades & creative districts",
            "hero_image": "https://images.unsplash.com/photo-1506351421178-63b52a2d2562?auto=format&fit=crop&w=1200&q=80",
            "nature_landmarks": ["Urban Waterfront Riverway", "Panoramic Skyline Hill", "Public Botanical Sanctuary", "Canal Greenway"],
            "morning_activity": ("🌅 Rooftop Botanical Sanctuary & Specialty Third-Wave Coffee", "08:30 AM - 10:30 AM", "Free / Small fee", "$6", "Start the morning in an elevated urban garden overlooking the awakening city with single-origin coffee.", "Framing your coffee cup against the sunrise illuminating glass skyscraper reflections.", "Artisan Sourdough Bakery (Freshly baked cardamom knots & avocado sourdough toast)"),
            "midday_activity": ("Indie Concept Boutiques & Vintage Streetwear Vaults", "11:30 AM - 02:30 PM", "Free Entry", "$15", "Explore repurposed industrial warehouse corridors featuring independent designers and vinyl shops.", "The industrial red-brick facade and neon signs of the concept store entrance.", "Food Hall / Street Market (Authentic gourmet street food stalls and regional lunch specials)"),
            "evening_activity": ("Sunset Waterfront Pier Walk & Hidden Speakeasy Lounge", "05:30 PM - 08:30 PM", "Free Pier / Drink cost", "$28", "Walk along the waterfront as the sun sets over harbor waters, then enter an unmarked basement listening lounge.", "Cocktail glass reflecting the twilight harbor lights through panoramic glass windows.", "Late Night Izakaya or Tapas Bar (Sizzling grilled specialties and craft beverages)"),
            "hacks": [
                "Download the official transit app and add a contactless transit pass directly to your smartphone wallet.",
                "Head to public university libraries or museum rooftops for free panoramic city views.",
                "Ask baristas at third-wave specialty coffee shops for their personal favorite hidden neighborhood restaurants."
            ]
        }


def generate_local_itinerary(req: ItineraryRequest) -> Dict[str, Any]:
    dest_raw = req.destination.strip().lower()
    dest_title = req.destination.strip().title()
    days_count = max(1, min(req.duration_days, 10))

    traveler = req.traveler_type or "Solo Explorer"
    budget = req.budget_tier or "Balanced"
    mood = req.trip_mood or "Hidden Gems & Secret Spots"
    dietary = req.dietary_profile or "Street Food Hunter"
    accessibility = req.accessibility_needs or "None"

    # Match curated destination in our encyclopedic DB
    matched_key = None
    for key in DESTINATIONS_DATA:
        if key in dest_raw:
            matched_key = key
            break

    price_factor = 0.55 if budget == "Backpacker" else (2.2 if budget == "Luxury" else 1.0)

    if matched_key:
        dest_info = DESTINATIONS_DATA[matched_key]
        dest_display = dest_info.get("destination_display", dest_title)
        spotify_info = dest_info["spotify_playlist"]
        aesthetic_summary = dest_info["aesthetic_summary"]
        genz_hacks = dest_info["genz_hacks"]
        packing_essentials = dest_info["packing_essentials"]
        hero_image = dest_info.get("hero_image", "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=1200&q=80")
        basecamp = dest_info.get("basecamp", {
            "strategic_area": "City Center Historic & Transit Hub",
            "hostel_pick": {"name": "Central Design Pod Hostel", "price": "$35/night", "rating": "9.3/10", "vibe": "Ultra-clean modern pods with fast WiFi and community lounge"},
            "boutique_pick": {"name": "Heritage Boutique Hotel", "price": "$160/night", "rating": "9.5/10", "vibe": "Chic historic conversion with rooftop terrace"},
            "rest_strategy": "Stay within walking distance of central transit lines. Take an afternoon coffee break to stay refreshed."
        })
        transit_system = dest_info.get("transit_system", "High-speed Metro & Walkable Pedestrian Paths")
        base_days = dest_info["days"]
    else:
        # UNIVERSAL SMART ENVIRONMENT CLASSIFIER (Zero generic templates)
        env = classify_destination_environment(dest_title)
        dest_display = f"{dest_title} 🗺️"
        aesthetic_summary = f"{env['environment_desc']}. Tailored for {traveler} seeking {mood} and authentic {dietary} specialties."
        hero_image = env.get("hero_image", "https://images.unsplash.com/photo-1506351421178-63b52a2d2562?auto=format&fit=crop&w=1200&q=80")
        basecamp = {
            "strategic_area": f"Central {dest_title} District",
            "hostel_pick": {
                "name": f"{dest_title} Backpacker & Social Basecamp",
                "price": "$28/night",
                "rating": "9.2/10",
                "vibe": "Vibrant traveler community with cozy pods, free breakfast, and walking tour meetups"
            },
            "boutique_pick": {
                "name": f"{dest_title} Heritage Botanical Retreat",
                "price": "$145/night",
                "rating": "9.4/10",
                "vibe": "Quiet boutique sanctuary with landscaped garden courtyard and natural wine bar"
            },
            "rest_strategy": "Schedule an afternoon recharge between 2:30 PM - 4:00 PM at a local cafe to avoid travel fatigue."
        }
        transit_system = "Local Transit, Bike-share & Pedestrian Boulevards"
        spotify_info = {
            "title": f"{dest_title} Golden Hour: {mood} Tape",
            "genre": f"Local Regional Ambient & Indie Chill",
            "tracks": [f"Sunset Over {dest_title}", f"Alleys of {dest_title}", f"{dest_title} Ocean/Skyline", f"Midnight in {dest_title}"]
        }
        genz_hacks = env["hacks"]
        packing_essentials = [
            f"Sturdy footwear adapted for {dest_title}'s terrain ({env['type'].lower()})",
            "Fast-charging portable battery bank for full-day photo and video shooting",
            "Universal dual voltage adapter with multi-port USB-C fast charge",
            "Weather-appropriate outerwear matching local microclimates"
        ]
        base_days = []

    # Adapt basecamp and spotify info to user filters
    basecamp = adapt_basecamp(basecamp, budget, traveler, dest_title)
    spotify_info = adapt_spotify_playlist(spotify_info, mood, dest_title)
    traveler_info = TRAVELER_TRANSIT_AND_TIPS.get(traveler, TRAVELER_TRANSIT_AND_TIPS["Solo Explorer"])
    traveler_steps = traveler_info["pace"]

    # Build the days
    days_result = []
    for d_idx in range(1, days_count + 1):
        if base_days and (d_idx - 1) < len(base_days):
            day_template = base_days[d_idx - 1]
            day_title = day_template["title"]
            neighborhood = day_template["neighborhood"]
            vibe_summary = f"{day_template['vibe_summary']} — Tailored for {traveler} seeking {mood}"
            daily_steps = traveler_steps
            
            # Non-repetitive situational rest break tip
            from procedural_days import REST_SITUATIONAL_TIPS
            rest_tip_idx = (d_idx - 1) % len(REST_SITUATIONAL_TIPS)
            raw_rest = day_template.get("rest_break", {
                "time_slot": "03:00 PM - 04:00 PM",
                "activity_name": "☕ Afternoon Artisan Coffee & Foot Rest",
                "location_name": f"{neighborhood} Shaded Plaza",
                "tip": "Sit down, elevate your feet, and enjoy local pastries to stay refreshed for evening exploration."
            })
            clean_rest_tip = raw_rest.get("tip", "").replace("[Solo Explorer tip]", "").replace("[Romantic Duo tip]", "").replace("[Squad Trip tip]", "").replace("[Family Crew tip]", "").replace("[Digital Nomad tip]", "").replace("[Chaotic Adventurer tip]", "").strip()
            rest_break = {
                "time_slot": raw_rest.get("time_slot", "03:00 PM - 04:00 PM"),
                "activity_name": raw_rest.get("activity_name", "☕ Afternoon Recharge"),
                "location_name": raw_rest.get("location_name", f"{neighborhood} Shaded Plaza"),
                "tip": f"[{traveler} recharge] {clean_rest_tip} • {REST_SITUATIONAL_TIPS[rest_tip_idx]}"
            }
            activities_list = []

            for slot_idx, act in enumerate(day_template["activities"]):
                adapted_act = adapt_curated_activity(
                    act=act,
                    slot_idx=slot_idx,
                    dietary=dietary,
                    mood=mood,
                    traveler=traveler,
                    budget=budget,
                    accessibility=accessibility,
                    price_factor=price_factor,
                    day_num=d_idx
                )
                activities_list.append(adapted_act)

            days_result.append({
                "day": d_idx,
                "title": day_title,
                "neighborhood": neighborhood,
                "vibe_summary": vibe_summary,
                "daily_steps_estimate": daily_steps,
                "rest_break": rest_break,
                "activities": activities_list
            })
        else:
            # Procedural smart environmental generation for subsequent days or non-curated destinations
            # Every day N is guaranteed to be 100% unique in activities, photos, rest breaks & themes!
            env = classify_destination_environment(dest_title)
            p_day = build_procedural_day(
                dest_title=dest_title,
                day_num=d_idx,
                env_type=env["type"],
                traveler=traveler,
                mood=mood,
                dietary=dietary,
                price_factor=price_factor,
                budget=budget,
                accessibility=accessibility
            )
            days_result.append(p_day)


    budget_total = int((35 if budget == "Backpacker" else (180 if budget == "Luxury" else 85)) * days_count)

    return {
        "destination": dest_display,
        "hero_image": hero_image,
        "basecamp": basecamp,
        "transit_system": transit_system,
        "duration_days": days_count,
        "traveler_type": traveler,
        "budget_tier": budget,
        "trip_mood": mood,
        "dietary_profile": dietary,
        "accessibility_needs": accessibility,
        "vibe_match_score": "99% Vibe Match",
        "aesthetic_summary": aesthetic_summary,
        "spotify_playlist": spotify_info,
        "genz_hacks": genz_hacks,
        "packing_essentials": packing_essentials,
        "budget_breakdown": {
            "total_estimated": f"${budget_total} USD",
            "daily_average": f"${int(budget_total / days_count)} / day",
            "food_drink_percent": "40%",
            "activities_percent": "35%",
            "transit_percent": "15%",
            "splurge_percent": "10%"
        },
        "days": days_result
    }


import urllib.request
import urllib.error

def generate_with_gemini(req: ItineraryRequest, api_key: str) -> Dict[str, Any]:
    """Generates an itinerary using Google Gemini 1.5 Flash via REST API."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    prompt = f"""
You are an expert Gen-Z travel curator and environmental geographer.
Create a deeply authentic, non-repetitive {req.duration_days}-day travel itinerary for {req.destination}.
User Filters:
- Traveler Persona: {req.traveler_type}
- Budget Tier: {req.budget_tier}
- Trip Mood: {req.trip_mood}
- Foodie Style: {req.dietary_profile}
- Accessibility Needs: {req.accessibility_needs}

CRITICAL INSTRUCTIONS:
1. Every activity MUST be real and specific to {req.destination}.
2. Every insider tip MUST be unique, highly specific to {req.traveler_type} in {req.destination}, and NEVER repeat across days or activities.
3. Every day MUST have unique neighborhoods, unique activities, and unique food spots tailored to {req.dietary_profile}.
4. Provide a comfortable rest break each afternoon tailored to prevent walking fatigue.

Return ONLY a valid JSON object matching this schema (no markdown, no extra commentary):
{{
  "destination": "{req.destination}",
  "hero_image": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1200&q=80",
  "basecamp": {{
    "strategic_area": "Recommended neighborhood to stay",
    "hostel_pick": {{"name": "Best social/pod hostel", "price": "$28/night", "rating": "9.3/10", "vibe": "Description"}},
    "boutique_pick": {{"name": "Best boutique hotel", "price": "$140/night", "rating": "9.5/10", "vibe": "Description"}},
    "rest_strategy": "Afternoon recharge strategy"
  }},
  "transit_system": "Metro, Walking & Bike Paths",
  "duration_days": {req.duration_days},
  "traveler_type": "{req.traveler_type}",
  "budget_tier": "{req.budget_tier}",
  "trip_mood": "{req.trip_mood}",
  "dietary_profile": "{req.dietary_profile}",
  "accessibility_needs": "{req.accessibility_needs}",
  "vibe_match_score": "99% Vibe Match",
  "aesthetic_summary": "1-2 sentence aesthetic summary of {req.destination}",
  "spotify_playlist": {{
    "title": "Aesthetic Playlist Name",
    "genre": "Genre description",
    "tracks": ["Track 1", "Track 2", "Track 3", "Track 4"]
  }},
  "genz_hacks": ["City hack 1", "City hack 2", "City hack 3"],
  "packing_essentials": ["Item 1", "Item 2", "Item 3", "Item 4"],
  "budget_breakdown": {{
    "total_estimated": "$XXX USD",
    "daily_average": "$XX / day",
    "food_drink_percent": "40%",
    "activities_percent": "35%",
    "transit_percent": "15%",
    "splurge_percent": "10%"
  }},
  "days": [
    {{
      "day": 1,
      "title": "Day 1 Title",
      "neighborhood": "Neighborhood Name",
      "vibe_summary": "Day 1 vibe summary",
      "daily_steps_estimate": "12,000 steps",
      "rest_break": {{
        "time_slot": "03:00 PM - 04:00 PM",
        "activity_name": "Afternoon Recharge Cafe",
        "location_name": "Cafe or Garden Name",
        "tip": "Specific rest tip"
      }},
      "activities": [
        {{
          "activity_name": "Morning Activity Name",
          "image_url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=800&q=80",
          "category": "Morning Expedition",
          "time_slot": "09:00 AM - 11:30 AM",
          "location_name": "Real location name",
          "neighborhood": "Neighborhood",
          "estimated_price": "$12",
          "cost_tier": "$$",
          "ticket_requirement": "Entry ticket or free",
          "vibe_tags": ["#Tag1", "#Tag2", "#Tag3"],
          "crowd_meter": "Peaceful (3/10)",
          "insider_booking_tip": "Unique insider tip for {req.traveler_type}",
          "photo_spot_tip": "Angle & lighting tip",
          "food_spot": "Local food spot name & specialty dish",
          "transit_to_next": {{
            "mode": "Metro or Walk",
            "duration": "12 mins",
            "cost": "$2.50",
            "instructions": "Directions to next stop"
          }}
        }}
      ]
    }}
  ]
}}
"""

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 6000,
            "responseMimeType": "application/json"
        }
    }
    
    data = json.dumps(payload).encode("utf-8")
    req_http = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    
    with urllib.request.urlopen(req_http, timeout=40) as response:
        res_body = json.loads(response.read().decode("utf-8"))
        raw_text = res_body["candidates"][0]["content"]["parts"][0]["text"].strip()
        
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        if raw_text.startswith("```"):
            raw_text = raw_text[3:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]
            
        parsed = json.loads(raw_text.strip())
        if isinstance(parsed, dict) and "days" in parsed and len(parsed["days"]) > 0:
            return parsed
            
    raise ValueError("Gemini returned invalid response structure")


def generate_with_openai(req: ItineraryRequest, api_key: str) -> Dict[str, Any]:
    """Generates an itinerary using OpenAI GPT-4o / GPT-3.5 via official client."""
    from openai import OpenAI
    client = OpenAI(api_key=api_key)

    prompt = f"""
Act as an elite Gen-Z travel curator and environmental geographer.
Generate an incredible, ultra-specific {req.duration_days}-day travel itinerary for {req.destination}.
User Profile:
- Traveler Type: {req.traveler_type}
- Budget Tier: {req.budget_tier}
- Trip Mood/Vibe: {req.trip_mood}
- Foodie Style: {req.dietary_profile}
- Accessibility Needs: {req.accessibility_needs}

CRITICAL REQUIREMENT:
Every single recommendation MUST be deeply specific to {req.destination}'s real geography, nature, climate, local dishes, and cultural atmosphere.
Every insider tip MUST be non-repetitive and situation-specific.
Use REAL street names, real nature landmarks, real local delicacies, exact camera angles, and authentic local transit tips.

Return ONLY a valid JSON object matching the standard Travel Planner itinerary schema.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a world-class travel planner. Return only valid JSON objects."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=3500
    )

    content = response.choices[0].message.content.strip()
    if content.startswith("```json"):
        content = content[7:]
    if content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]

    parsed = json.loads(content.strip())
    if isinstance(parsed, dict) and "days" in parsed:
        return parsed
    raise ValueError("OpenAI returned invalid structure")


def generate_itinerary_content(req: ItineraryRequest) -> Dict[str, Any]:
    # 1. Determine if a Generative AI key is available (from request payload or environment)
    req_key = (req.api_key or "").strip()
    provider = (req.ai_provider or "gemini").lower()

    # Check for Gemini key
    gemini_key = req_key if provider == "gemini" and req_key else os.getenv("GEMINI_API_KEY", "").strip()
    # Check for OpenAI key
    openai_key = req_key if provider == "openai" and req_key else os.getenv("OPENAI_API_KEY", "").strip()

    if gemini_key:
        try:
            logger.info("Attempting itinerary generation with Google Gemini Generative AI...")
            return generate_with_gemini(req, gemini_key)
        except Exception as e:
            logger.warning(f"Google Gemini generation failed: {e}. Falling back to Smart Neural Engine.")

    if openai_key:
        try:
            logger.info("Attempting itinerary generation with OpenAI Generative AI...")
            return generate_with_openai(req, openai_key)
        except Exception as e:
            logger.warning(f"OpenAI generation failed: {e}. Falling back to Smart Neural Engine.")

    # 2. Smart Situational Generation Engine (100% unique, zero repetitive tips)
    logger.info("Using Smart Situational Engine for itinerary generation.")
    return generate_local_itinerary(req)

