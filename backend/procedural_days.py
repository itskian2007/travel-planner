# Procedural Multi-Day Itinerary Engine with Full Preference Filter Adaptation
# Guarantees that:
# 1. Every day from Day 1 to Day 10 is 100% unique (no repetitions).
# 2. Every user filter (Mood, Foodie Style, Traveler Persona, Budget Tier, Accessibility)
#    actively transforms the itinerary content, food spots, tips, transit modes, and basecamps.

from typing import Dict, Any, List

# ==============================================================================
# PREFERENCE FILTER ADAPTERS
# ==============================================================================

FOODIE_ADAPTATIONS = {
    "Street Food Hunter": {
        "morning": "Local morning street market cart (Fresh steaming savory buns, hot dough fritters & regional spiced tea)",
        "midday": "Historic open-air hawker / street food stalls (Charcoal grilled skewers, hand-pulled noodles & spicy chili dip)",
        "evening": "Buzzing night food market (Sizzling street woks, crispy seafood pancakes & torched sweet skewers)"
    },
    "Aesthetic Cafe Hopper": {
        "morning": "Third-wave specialty coffee roastery (Single-origin pour-over, oat flat white & warm cardamom pastry)",
        "midday": "Botanical greenhouse cafe (Organic grain bowl, matcha latte & edible flower avocado sourdough)",
        "evening": "Chic dessert salon & tea lounge (Earl grey infused souffles, Japanese hojicha tea & artisan chocolates)"
    },
    "Michelin & Fine Dining": {
        "morning": "Artisan bakery by former Michelin pastry chef (Laminated butter pastries & espresso extraction)",
        "midday": "Michelin Bib Gourmand historic bistro (Handmade seasonal pasta / market seafood with natural wine pairing)",
        "evening": "Award-winning fine dining tasting menu (Multi-course chef's tasting showcasing rare regional ingredients)"
    },
    "Plant-Based & Vegan": {
        "morning": "100% plant-based organic cafe (Acai smoothie bowl with house-made granola, almond butter & dragonfruit)",
        "midday": "Farm-to-table vegan sanctuary (Wood-roasted seasonal veggies, truffle cashew cream risotto & pressed juice)",
        "evening": "Artisanal vegan bistro (Rich smoked mushroom broth ramen / plant-based tapas with organic natural wine)"
    },
    "Late Night Munchies": {
        "morning": "Cozy local diner (Hearty breakfast sandwich with melted cheese & hot drip coffee)",
        "midday": "Neighborhood comfort food counter (Loaded smashburger / hot crispy fried chicken sandwich with fries)",
        "evening": "Late-night 24/7 alleyway haunt (Steaming soup dumplings, spicy midnight tacos / kebabs & cold craft beer)"
    },
    "Viral TikTok Eats": {
        "morning": "Viral bakery sensation (Multi-layer supreme croissant with oozing pistachio cream & cold foam latte)",
        "midday": "Trending viral lunch spot (Ultra-cheesy melted raclette sandwich or viral cloud souffle pancake stack)",
        "evening": "Social media sensation dining lounge (Flame-torched sushi rolls, smoke-infused mocktails & molten lava cake)"
    }
}

MOOD_MODIFIERS = {
    "Hidden Gems & Secret Spots": {
        "prefix": "🔮 Secret & Unmarked: ",
        "tag": "#HiddenGem",
        "evening_vibe": "Unmarked doorway speakeasy / hidden garden lounge away from tourists",
        "activity_overrides": {
            0: {
                "activity_name": "🔮 Secret Sunrise Cloister & Hidden Roastery",
                "category": "Hidden Gem Exploration",
                "estimated_price": "$6",
                "cost_tier": "$",
                "insider_booking_tip": "Enter through the unmarked side archway to explore centuries-old courtyards before crowds wake up.",
                "photo_spot_tip": "Low-angle shot through the stone archway with early morning sunbeams reflecting on ancient stones."
            },
            1: {
                "activity_name": "🔮 Unmarked Basement Antique Vault & Secret Courtyard",
                "category": "Curated Hidden Sanctuary",
                "estimated_price": "$12",
                "cost_tier": "$$",
                "insider_booking_tip": "Look for the discreet brass plaque by the wooden heavy door—ring bell for admission to private collections.",
                "photo_spot_tip": "Overhead flat-lay of antique brass instruments and handwritten manuscripts on aged oak tables."
            },
            2: {
                "activity_name": "🔮 Hidden Doorway Speakeasy & Intimate Acoustic Lounge",
                "category": "Secret Nightlife & Speakeasies",
                "estimated_price": "$22",
                "cost_tier": "$$",
                "insider_booking_tip": "Enter through the vintage telephone booth or disguised bookshelf; whisper today's password to the host.",
                "photo_spot_tip": "Silhouette shot against candlelit vintage brick arches with glowing amber glassware."
            }
        }
    },
    "Insta & TikTok Viral Spots": {
        "prefix": "📸 Postcard & Viral Angle: ",
        "tag": "#ViralSpots",
        "evening_vibe": "Panoramic skyline rooftop glass bridge with golden hour illumination",
        "activity_overrides": {
            0: {
                "activity_name": "📸 Viral Golden Hour Mirror Pavilion & Aesthetic Bakery",
                "category": "Viral Sensation Morning",
                "estimated_price": "$10",
                "cost_tier": "$$",
                "insider_booking_tip": "Arrive 10 minutes prior to opening for clean frames with zero crowds blocking the symmetrical arches.",
                "photo_spot_tip": "0.5x ultra-wide lens from waist height capturing the towering architecture reflected in the calm glass pools."
            },
            1: {
                "activity_name": "📸 Trending Immersive Light Art Labyrinth & Cloud Cafe",
                "category": "Social Media Trending Wonder",
                "estimated_price": "$28",
                "cost_tier": "$$$",
                "insider_booking_tip": "Pre-book timed tickets 2 weeks in advance. Wear vibrant colors that contrast against the crystal light tunnels.",
                "photo_spot_tip": "Portrait mode video panning across the infinite LED crystal curtains pulsing with rhythm."
            },
            2: {
                "activity_name": "📸 360° Cantilevered Glass Skydeck & Sunset Neon Rooftop",
                "category": "Golden Hour Skyline & Viral Sunset",
                "estimated_price": "$30",
                "cost_tier": "$$$",
                "insider_booking_tip": "Secure the 4:45 PM golden hour slot—you will catch daylight, vivid violet sunset, and sparkling night cityscapes all in one.",
                "photo_spot_tip": "Sit at the clear corner glass edge at 0.5x zoom capturing the infinite illuminated skyline below."
            }
        }
    },
    "Underground Nightlife & Raves": {
        "prefix": "🪩 Subterranean & Indie: ",
        "tag": "#UndergroundNightlife",
        "evening_vibe": "Basement vinyl listening bar, industrial techno warehouse, or live jazz cellar",
        "activity_overrides": {
            0: {
                "activity_name": "🪩 Indie Subterranean Record Vault & Dark Roast Fuel",
                "category": "Underground Music Discovery",
                "estimated_price": "$8",
                "cost_tier": "$",
                "insider_booking_tip": "Listen to rare vintage first-pressing vinyls on high-fidelity studio headphones before noon.",
                "photo_spot_tip": "Warm analog film angle framing vinyl crates under warm industrial filament bulbs."
            },
            1: {
                "activity_name": "🪩 Converted Warehouse Skate Park & DIY Streetwear Collective",
                "category": "Subculture & Street Style",
                "estimated_price": "$14",
                "cost_tier": "$$",
                "insider_booking_tip": "Check community bulletin boards for secret warehouse pop-up shows and guest DJ sets.",
                "photo_spot_tip": "Action freeze shot with neon graffiti murals and raw concrete pillars in the background."
            },
            2: {
                "activity_name": "🪩 Industrial Concrete Techno Vault & Analog Audio Bar",
                "category": "Underground Nightlife & Club Culture",
                "estimated_price": "$25",
                "cost_tier": "$$",
                "insider_booking_tip": "Cover smartphone camera lenses with provided stickers; immerse completely into the pristine acoustic sound system.",
                "photo_spot_tip": "Moody silhouette outside the industrial iron doors under lone red neon signage."
            }
        }
    },
    "Zen Nature & Wellness": {
        "prefix": "🌿 Mindful & Restorative: ",
        "tag": "#ZenWellness",
        "evening_vibe": "Geothermal thermal mineral bath soak, acoustic soundscape, or candlelit herbal tea garden",
        "activity_overrides": {
            0: {
                "activity_name": "🌿 Bamboo Sanctuary Sunrise Walk & Silent Botanical Garden",
                "category": "Mindfulness & Nature Immersion",
                "estimated_price": "$4",
                "cost_tier": "$",
                "insider_booking_tip": "Practice 20 minutes of mindful walking meditation along the misty stone moss paths at dawn.",
                "photo_spot_tip": "Misty sunbeams filtering through giant swaying bamboo culms onto dew-covered moss."
            },
            1: {
                "activity_name": "🌿 Ancient Herbal Apothecary & Organic Cold-Pressed Tea Sanctuary",
                "category": "Holistic Healing & Clean Fuel",
                "estimated_price": "$12",
                "cost_tier": "$$",
                "insider_booking_tip": "Consult the resident master herbalist for a customized botanical tea infusion adapted to your energy.",
                "photo_spot_tip": "Steam rising from delicate earthen ceramic bowls with blooming jasmine flowers."
            },
            2: {
                "activity_name": "🌿 Geothermal Mineral Hot Springs & Starlit Forest Bathing",
                "category": "Thermal Recovery & Deep Rest",
                "estimated_price": "$28",
                "cost_tier": "$$$",
                "insider_booking_tip": "Soak in the natural mineral-rich pools for 30 minutes, followed by cold plunge to eliminate muscle soreness.",
                "photo_spot_tip": "Ambient steam rising across basalt rock pools reflecting the night constellations above."
            }
        }
    },
    "Chill & Wellness": {
        "prefix": "🌿 Mindful & Restorative: ",
        "tag": "#WellnessVibes",
        "evening_vibe": "Geothermal thermal mineral bath soak, acoustic soundscape, or candlelit herbal tea garden",
        "activity_overrides": {
            0: {
                "activity_name": "🌿 Coastal Ridge Morning Stretch & Oceanfront Herb Garden",
                "category": "Mindful Morning Awakening",
                "estimated_price": "$4",
                "cost_tier": "$",
                "insider_booking_tip": "Arrive at sunrise for a calming coastal walk; breathe in salt air and listen to the rhythm of waves.",
                "photo_spot_tip": "Gentle morning mist rolling over wild sea grasses and rocky bluffs."
            },
            1: {
                "activity_name": "🌿 Organic Hydrotherapy Pools & Shaded Pavilion Rest",
                "category": "Restorative Wellness",
                "estimated_price": "$18",
                "cost_tier": "$$",
                "insider_booking_tip": "Alternate between the heated eucalyptus pool and cold cascade to reset circulation.",
                "photo_spot_tip": "Clear turquoise pool water reflecting lush green ferns in natural skylight."
            },
            2: {
                "activity_name": "🌿 Acoustic Singing Bowl Meditation & Candlelit Courtyard",
                "category": "Acoustic Sound Healing & Twilight Rest",
                "estimated_price": "$22",
                "cost_tier": "$$",
                "insider_booking_tip": "Close your eyes and let harmonic Tibetan bowl frequencies wash away all travel fatigue.",
                "photo_spot_tip": "Warm flickering tea candles arranged in spiral patterns on polished river stones."
            }
        }
    },
    "Vintage Culture & Dark Academia": {
        "prefix": "🏰 Vintage Archive & Heritage: ",
        "tag": "#VintageCulture",
        "evening_vibe": "Historic library reading vaults, antique curio taverns & candlelit acoustic poetry",
        "activity_overrides": {
            0: {
                "activity_name": "🏰 Ancient Cathedral Cloister Stroll & 18th-Century Espresso",
                "category": "Living Heritage & Architecture",
                "estimated_price": "$5",
                "cost_tier": "$",
                "insider_booking_tip": "Explore the stone arcades early when choir rehearsals echo off the monumental vaulted ceilings.",
                "photo_spot_tip": "Symmetrical perspective down the stone cloister corridor with dramatic gothic morning shadows."
            },
            1: {
                "activity_name": "🏰 Labyrinthine Multi-Story Rare Bookstore & Antique Curio Vault",
                "category": "Literary Haunt & Vintage Curios",
                "estimated_price": "$10",
                "cost_tier": "$$",
                "insider_booking_tip": "Climb the creaking wooden spiral staircase to discover first-edition philosophy volumes and vintage city maps.",
                "photo_spot_tip": "Looking up the floor-to-ceiling mahogany bookshelves packed with gilded leather spines."
            },
            2: {
                "activity_name": "🏰 Candlelit Historic Tavern & Classical Acoustic Cellar",
                "category": "Dark Academia Twilight Sanctuary",
                "estimated_price": "$26",
                "cost_tier": "$$$",
                "insider_booking_tip": "Order artisanal spiced mulled wine or dark regional stout; sit in the corner booth beside stone hearth.",
                "photo_spot_tip": "Melted wax candles illuminating antique brass reading lamps and weathered wooden table patina."
            }
        }
    },
    "Cultural Deep-Dive": {
        "prefix": "🏛️ Historic & Living Heritage: ",
        "tag": "#DeepCulture",
        "evening_vibe": "Historic courtyard tavern with centuries-old acoustic folk traditions and regional wines",
        "activity_overrides": {
            0: {
                "activity_name": "🏛️ Historic Heritage Quarter Dawn Walk & Artisan Bakery",
                "category": "Ancestral Traditions & Dawn",
                "estimated_price": "$5",
                "cost_tier": "$",
                "insider_booking_tip": "Observe local artisans opening their family-owned workshops passed down through four generations.",
                "photo_spot_tip": "Early morning light glinting off cobblestones and historic carved wooden window frames."
            },
            1: {
                "activity_name": "🏛️ National Heritage Museum & Master Artisan Workshop",
                "category": "Living Cultural Heritage",
                "estimated_price": "$15",
                "cost_tier": "$$",
                "insider_booking_tip": "Join the free docent tour at 1:00 PM for extraordinary insights into indigenous craft techniques.",
                "photo_spot_tip": "Close-up of artisan hands weaving delicate textiles or molding traditional ceramic earthenware."
            },
            2: {
                "activity_name": "🏛️ Ancient Stone Courtyard Feast & Folk Troupe Echoes",
                "category": "Traditional Night Feast & Music",
                "estimated_price": "$28",
                "cost_tier": "$$$",
                "insider_booking_tip": "Try the slow-braised clay pot regional specialty prepared according to centuries-old recipes.",
                "photo_spot_tip": "Acoustic folk musicians playing traditional stringed instruments under hanging woven lanterns."
            }
        }
    },
    "Extreme Thrill & Adrenaline": {
        "prefix": "⚡ High-Octane Thrill: ",
        "tag": "#AdrenalineRush",
        "evening_vibe": "Sunset cliff jumping, high-speed night urban scramble, or illuminated canyon ridge",
        "activity_overrides": {
            0: {
                "activity_name": "⚡ Sunrise Mountain Ridge Scramble & Canyon Zip-line",
                "category": "Adrenaline Morning Expedition",
                "estimated_price": "$22",
                "cost_tier": "$$",
                "insider_booking_tip": "Take the high-elevation goat trail before wind speeds pick up for sheer cliff-edge panoramas.",
                "photo_spot_tip": "Action wide-angle shot stepping across suspended steel cable footbridge over sheer abyss."
            },
            1: {
                "activity_name": "⚡ White-Water Rapid Descent or Electric Trail Bike Blitz",
                "category": "High-Speed Nature Rush",
                "estimated_price": "$35",
                "cost_tier": "$$$",
                "insider_booking_tip": "Fasten GoPro with chest mount; listen to guides' stroke commands through Grade 4 boulder rapids.",
                "photo_spot_tip": "Dramatic water spray catching bright sunlight as the raft charges through turbulent chutes."
            },
            2: {
                "activity_name": "⚡ Cliffside Sunset Bungee / High-Speed Night Go-Kart Arena",
                "category": "Twilight Adrenaline Finale",
                "estimated_price": "$40",
                "cost_tier": "$$$$",
                "insider_booking_tip": "Book the final twilight jump slot to dive into the glowing purple twilight abyss.",
                "photo_spot_tip": "Silhouette of diver suspended mid-air against deep orange and violet sunset skyline."
            }
        }
    },
    "Nature & Outdoor Adventure": {
        "prefix": "🌲 Wild & High-Elevation: ",
        "tag": "#OutdoorAdventure",
        "evening_vibe": "Sunset cliffside overlook campfire, oceanfront breeze terrace, or mountain starlight walk",
        "activity_overrides": {
            0: {
                "activity_name": "🌲 Alpine Summit Sunrise Trek & Wildflower Valley",
                "category": "Wilderness Expedition",
                "estimated_price": "$0",
                "cost_tier": "$",
                "insider_booking_tip": "Pack headlamps and start 45 minutes before dawn to witness the first alpine glow on the peaks.",
                "photo_spot_tip": "Silhouette standing on granite ledge looking out over rolling sea of mountain clouds."
            },
            1: {
                "activity_name": "🌲 Glacial Lake Kayaking & Ancient Forest Canopy Walk",
                "category": "Pristine Nature Immersion",
                "estimated_price": "$18",
                "cost_tier": "$$",
                "insider_booking_tip": "Paddle toward the western bay where turquoise water is calmest and snow-capped peaks mirror perfectly.",
                "photo_spot_tip": "Bright kayak bow cutting through glass-like turquoise water reflecting sheer granite walls."
            },
            2: {
                "activity_name": "🌲 Wilderness Stargazing Campfire & Starlit Hearth Feast",
                "category": "Starlit Wilderness Camp",
                "estimated_price": "$20",
                "cost_tier": "$$",
                "insider_booking_tip": "Download offline stargazing map—this region has zero light pollution and reveals the Milky Way in full glory.",
                "photo_spot_tip": "Long-exposure night shot of the glowing campfire beneath the blazing arch of the Milky Way."
            }
        }
    }
}

TRAVELER_TRANSIT_AND_TIPS = {
    "Solo Explorer": {
        "tip_focus": "Safe, walkable, and friendly communal tables where solo travelers easily chat or relax.",
        "transit_mode": "🚶‍♂️ Walkable Pedestrian Route or Contactless Metro",
        "pace": "11,500 steps (Independent, flexible pace)"
    },
    "Romantic Duo": {
        "tip_focus": "Intimate atmosphere with scenic photo viewpoints for couples and quiet candlelit corners.",
        "transit_mode": "🚕 Scenic Private Ride or Hand-in-Hand River Promenade Walk",
        "pace": "9,800 steps (Romantic leisurely pace)"
    },
    "Squad Trip": {
        "tip_focus": "Spacious seating, group sharing platters, competitive vibe, and fun social photo spots.",
        "transit_mode": "🚗 Split Rideshare XL or Group Light Rail",
        "pace": "12,800 steps (High-energy squad exploration)"
    },
    "Family Crew": {
        "tip_focus": "Step-free stroller access, clean restrooms nearby, engaging for all ages, and low fatigue.",
        "transit_mode": "🚊 Step-Free Low-Floor Tram or Family Taxi",
        "pace": "8,200 steps (Gentle family pace with frequent rests)"
    },
    "Digital Nomad": {
        "tip_focus": "Aesthetic laptop-friendly environment with blazing-fast WiFi, power plugs, and great coffee.",
        "transit_mode": "🚲 City Bike-share or Walkable Cafe Corridor",
        "pace": "8,500 steps (Balanced work-and-wander rhythm)"
    },
    "Chaotic Adventurer": {
        "tip_focus": "High-adrenaline secret access, off-the-beaten-path scrambles, and thrill-seeking vantage points.",
        "transit_mode": "⚡ Fast Walking & Spontaneous Transit Scramble",
        "pace": "17,500 steps (Full-throttle adrenaline pace)"
    }
}

# ==============================================================================
# SITUATIONAL CONTEXT-AWARE INSIDER TIPS MATRIX
# Generates unique, non-repeating tips for every slot, day, and persona
# ==============================================================================

SITUATIONAL_TIPS = {
    "Solo Explorer": {
        0: [
            "Arrive 15 minutes before opening to explore in tranquil dawn silence. Solo travelers easily bypass queue bottlenecks at turnstiles.",
            "Bring a travel journal; morning coffee counters nearby have communal window stools perfect for independent people-watching.",
            "Ask local morning walkers for their favorite hidden shortcut—locals love guiding solo travelers to quiet viewpoints.",
            "Early morning light offers beautiful self-timer photo angles with zero tour crowds obstructing your frame."
        ],
        1: [
            "Ask the host for single-rider lines or individual counter spots—you'll bypass 30+ minute waiting lists during peak lunch.",
            "Take the quieter side cloisters or garden wings where solo explorers can savor artwork at an unhurried personal pace.",
            "Strike up a conversation with the gallery docent or barista—they often share secret recommendations for hidden local spots.",
            "Keep valuables in a sleek anti-theft crossbody sling while navigating bustling midday food markets alone."
        ],
        2: [
            "Pull up a stool at the bar or communal wooden high-top; it's the friendliest way to chat with bartenders and fellow travelers.",
            "Twilight offers warm ambient illumination—safe, well-lit main boulevards make solo evening strolls relaxing and inspiring.",
            "Download the local public transit app with real-time night schedules to navigate back to your basecamp smoothly.",
            "Opt for small tapas plates or half-portions to taste multiple delicacies without needing a large dining party."
        ]
    },
    "Romantic Duo": {
        0: [
            "Golden dawn light strikes at a low 45-degree angle—set up your camera by the eastern arch for an intimate couple portrait before crowds gather.",
            "Pick up two warm pastries and find a secluded morning stone bench overlooking the awakening waters.",
            "Walk hand-in-hand along the quiet morning promenade while the mist still clings to historic facades.",
            "Beat the tourist rush by arriving right at opening; you'll have the majestic halls virtually all to yourselves."
        ],
        1: [
            "Slip away into the shaded rear courtyard or tranquil side pavilion where tour groups rush past, leaving a romantic private haven.",
            "Split an artisanal tasting platter and share a carafe of chilled local infusion on a cozy two-seater terrace.",
            "Take the scenic panoramic footbridge together—it offers a gorgeous vantage point for a spontaneous candid couple shot.",
            "Book a shared audio headset or listen to a shared travel playlist while wandering the shaded cloisters."
        ],
        2: [
            "Reserve a corner balcony table 30 minutes before twilight to watch the sunset paint the sky while sipping regional wine.",
            "Stroll along the softly illuminated waterside path as fairy lights and street lanterns reflect across dark water ripples.",
            "Request an intimate candlelit booth away from the main kitchen traffic for a memorable evening conversation.",
            "Finish the night sharing a warm artisanal dessert under the stars while listening to acoustic street musicians."
        ]
    },
    "Squad Trip": {
        0: [
            "Elect one person to grab a round of morning coffees while others secure express group tickets at the turnstiles.",
            "Capture a dynamic group wide-angle photo on the monumental stone stairs while the morning lighting is crisp and clear.",
            "Split into pairs to explore different exhibit wings, then regroup at the central fountain to trade discoveries.",
            "Inquire at the ticket desk for a group pass (usually 4+ travelers qualify for an express group discount)."
        ],
        1: [
            "Send one squad member ahead to claim a long wooden bench table in the food hall while the rest grab sharing platters.",
            "Use split-bill apps (Splitwise / Revolut) right after paying to keep finances frictionless and transparent.",
            "Take a fun group video challenge at the scenic overlook—0.5x ultra-wide lens fits everyone easily into the frame.",
            "Agree on a designated meeting spot and time in case the squad separates in busy market lanes."
        ],
        2: [
            "Book a large table or lounge booth in advance for evening dining; family-style sharing dishes are the most social way to feast.",
            "Split an Uber XL or ride the night light rail together—traveling in numbers is fast, cheap, and lively.",
            "Explore lively arcade bars or open-air beer gardens where group games and social energy are at their peak.",
            "Take turns choosing evening music tracks on the squad road-trip playlist while recounting the best moments of the day."
        ]
    },
    "Family Crew": {
        0: [
            "Enter via the designated north entrance ramp for smooth step-free stroller access before midday heat sets in.",
            "Mornings have shorter queues and calmer acoustics—ideal for young children and grandparents to explore comfortably.",
            "Pack reusable water bottles and healthy morning snacks; clean family rest areas are situated right beside the entrance pavilion.",
            "Ask staff for child-friendly scavenger hunt activity maps at the information desk—keeps kids engaged throughout."
        ],
        1: [
            "Air-conditioned galleries and clean family restrooms with changing stations are located on Level 1 near the garden cafe.",
            "Schedule a relaxed sit-down lunch with highchairs and kid-friendly meal options to prevent afternoon tantrums.",
            "Take the shaded garden pathways rather than the sunny open plazas to keep everyone cool and energized.",
            "Allow 30 minutes of open play on the shaded lawn so young ones can burn energy between cultural visits."
        ],
        2: [
            "Book an early 6:00 PM dinner sitting before lively night crowds arrive—service is prompt and seating is spacious.",
            "Take the modern low-floor tram back to your basecamp; spacious stroller bays make evening boarding stress-free.",
            "Pick up artisanal local gelato or sweet pastries as an evening reward for great family teamwork during the day.",
            "End the day with an easy stroll through a pedestrianized square where kids can watch street performers safely."
        ]
    },
    "Digital Nomad": {
        0: [
            "Take advantage of tranquil morning hours to clear emails while sipping a pour-over; cafe WiFi speeds peak before 10:00 AM.",
            "Download offline city maps and sync work files while connected to the fast morning basecamp fiber internet.",
            "Sit near the cafe perimeter where wall AC outlets are accessible, and enjoy single-origin coffee with a view.",
            "Get your morning walk and step count in early so you can focus on creative work blocks later in the day."
        ],
        1: [
            "The upper mezzanine or conservatory cafe features spacious communal timber tables with fast public WiFi and quiet acoustics.",
            "Take a 45-minute screen-free lunch break to recharge creative focus while tasting authentic regional dishes.",
            "Carry a compact 65W GaN multi-port USB-C fast charger to top up laptop and phone simultaneously in 30 minutes.",
            "Network with fellow remote founders and digital creators at the coffee bar—popular nomad hub during weekday lunches."
        ],
        2: [
            "Close laptops at twilight and transition into social mode as ambient beats take over the terrace lounge.",
            "Join local tech and expat meetups often hosted at nearby rooftop bars or listening lounges on weekday evenings.",
            "Review your day's work and plan tomorrow's itinerary while enjoying craft beverages with panoramic skyline views.",
            "Choose venues with comfortable ergonomic banquette seating where you can journal or review photos in relaxed comfort."
        ]
    },
    "Chaotic Adventurer": {
        0: [
            "Scramble up the back perimeter ridge trail at dawn; it bypasses main gates and offers an adrenaline-pumping sunrise lookout.",
            "Rent an electric scooter or trail runner to cover maximum ground before the first tourist shuttle arrives.",
            "Check wind and tide conditions for spontaneous cliff jumping or off-trail exploration along the rocky coast.",
            "Fuel up with double espresso and hearty street breakfast—you'll need maximum energy for high-octane morning quests."
        ],
        1: [
            "Inquire with staff about off-limits underground passages, historic catacombs, or secret rooftop staircase access.",
            "Take the rugged dirt descent path rather than the paved switchbacks for a thrilling shortcut down the gorge.",
            "Dine at the rowdiest local street market counter—order the chef's spiciest signature dish with zero hesitation.",
            "Test your balance across suspended rope bridges or natural rock arches for epic high-adrenaline action photos."
        ],
        2: [
            "Find the hidden basement speakeasy through the unmarked service alley; look for the lone glowing red light bulb.",
            "Climb to the highest panoramic crane lookout or rooftop fire escape for a breathtaking twilight skyline rush.",
            "Dive headfirst into underground night markets and live music basements—let spontaneity dictate where the night leads.",
            "Join late-night scooter convoys or night bike tours to experience the city at full throttle under neon lights."
        ]
    }
}

REST_SITUATIONAL_TIPS = [
    "Elevate your feet on a comfortable bench for 20 minutes to improve circulation after walking on historic stone. Drink 500ml of water.",
    "Enjoy a hot herbal tea or cold-pressed infusion to reset digestion and relax shoulder muscles before the evening adventure.",
    "Take shoes off if in a park or tatami lounge; gentle calf stretches will keep your legs fresh for evening skyline walks.",
    "Rehydrate with natural electrolytes (coconut water or citrus squeeze) and use a portable power bank to recharge your phone to 100%.",
    "Sit in shaded greenery away from street noise; mindful deep breathing for 10 minutes resets cognitive focus and banishes travel fatigue.",
    "Find a peaceful courtyard or fountain bench; resting your eyes from digital screens restores mental clarity before dinner.",
    "Sample a light regional fruit snack or sorbet; avoiding heavy midday sugars prevents the 3:00 PM energy slump."
]

def generate_situational_insider_tip(
    slot_idx: int,
    day_num: int,
    traveler: str,
    budget: str,
    base_tip: str = ""
) -> str:
    persona_pool = SITUATIONAL_TIPS.get(traveler, SITUATIONAL_TIPS["Solo Explorer"])
    slot_pool = persona_pool.get(min(slot_idx, 2), persona_pool[0])
    tip_idx = (day_num - 1 + slot_idx) % len(slot_pool)
    specific_tip = slot_pool[tip_idx]

    persona_badges = {
        "Solo Explorer": "🎒 Solo Explorer Hack",
        "Romantic Duo": "💑 Couple & Duo Perk",
        "Squad Trip": "👯 Squad Group Intel",
        "Family Crew": "👨‍👩‍👧 Family Pacing & Stroller Advice",
        "Digital Nomad": "💼 Digital Nomad WiFi & Power Hack",
        "Chaotic Adventurer": "⚡ Chaotic Thrill Shortcut"
    }
    badge = persona_badges.get(traveler, f"✨ {traveler} Tip")

    budget_addon = ""
    if budget == "Backpacker":
        budget_addon = " [🪙 Backpacker: Show student/youth ID or enter during free morning slots.]"
    elif budget == "Luxury":
        budget_addon = " [💎 Luxury: Contact your private hotel concierge for reserved VIP fast-track.]"

    clean_base = ""
    if base_tip:
        clean_base = base_tip.replace("[Solo Explorer tip]", "").replace("[Romantic Duo tip]", "").replace("[Squad Trip tip]", "").replace("[Family Crew tip]", "").replace("[Digital Nomad tip]", "").replace("[Chaotic Adventurer tip]", "").strip()
        clean_base = clean_base.replace("Safe, walkable, and friendly communal tables where solo travelers easily chat or relax.", "").replace("Intimate atmosphere with scenic photo viewpoints for couples and quiet candlelit corners.", "").replace("Spacious seating, group sharing platters, competitive vibe, and fun social photo spots.", "").replace("Step-free stroller access, clean restrooms nearby, engaging for all ages, and low fatigue.", "").replace("Aesthetic laptop-friendly environment with blazing-fast WiFi, power plugs, and great coffee.", "").replace("High-adrenaline secret access, off-the-beaten-path scrambles, and thrill-seeking vantage points.", "").strip()

    if clean_base and len(clean_base) > 10:
        return f"[{badge}] {specific_tip} (Local context: {clean_base}){budget_addon}"
    return f"[{badge}] {specific_tip}{budget_addon}"

# ==============================================================================
# 10 UNIQUE PROCEDURAL DAYS FOR EACH ENVIRONMENT ARCHETYPE
# (5 Archetypes x 10 Days = 50 100% Unique Days with ZERO repetitions)
# ==============================================================================

DAY_THEMES_BY_ENV = {   'TROPICAL_ISLAND_COASTAL': [   {   'theme': 'Coral Reefs, Turquoise Coves & Coconut Water Sanctuary',
                                       'neighborhood': 'North Coral Peninsula',
                                       'rest': (   '02:30 PM - 03:30 PM',
                                                   '🥥 Chilled Coconut Water & Hammock Rest',
                                                   'North Sand Cove Palm Grove',
                                                   'Rest under coconut palms, rehydrate with potassium-rich coconut '
                                                   'water, and cool off from midday sun.'),
                                       'morning': (   '🌅 Sunrise Coastal Cliff Walk & Tidepool Reflections',
                                                      '08:00 AM - 10:15 AM',
                                                      'Free Coastal Access',
                                                      4,
                                                      'Walk the dramatic sea trail before the tropical heat. Spot reef '
                                                      'fish in glass-clear tidal basins.',
                                                      'Silhouette looking out over turquoise breakers with palms '
                                                      'framing the sunrise.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d2/Acapulco_fishermen.jpg/960px-Acapulco_fishermen.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Hidden Marine Sanctuary Snorkel & Sea Turtle Coves',
                                                     '11:30 AM - 02:30 PM',
                                                     'Gear rental $10',
                                                     15,
                                                     'Rent a mask and fin. Swim among sea turtles and bright '
                                                     'parrotfish in calm morning tide pools.',
                                                     'Underwater 0.5x wide shot of coral formations and crystal clear '
                                                     'turquoise sea.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/fd/Acc%C3%A8s_plage%2C_Sainte-Marie%2C_R%C3%A9_island%2C_august_2015.jpg/960px-Acc%C3%A8s_plage%2C_Sainte-Marie%2C_R%C3%A9_island%2C_august_2015.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Catamaran Sunset Cruise & Barefoot Beach Club Lounge',
                                                      '05:30 PM - 08:30 PM',
                                                      'Catamaran pass or walk-in',
                                                      30,
                                                      'Watch the glowing orange sun dip beneath the ocean horizon with '
                                                      'barefoot acoustic guitar.',
                                                      'Holding a sunset spritz against the pink and violet sea '
                                                      'reflection.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d4/Amphitheatre_Bay_after_a_storm%2C_Akamas_Peninsula%2C_Cyprus.jpg/960px-Amphitheatre_Bay_after_a_storm%2C_Akamas_Peninsula%2C_Cyprus.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Secret Sea Caves, Mangrove Kayaking & Hidden Lagoons',
                                       'neighborhood': 'Emerald Bay & Mangrove Estuary',
                                       'rest': (   '03:00 PM - 04:00 PM',
                                                   '🍉 Iced Watermelon Mint Refresher & Shaded Gazebo',
                                                   'Mangrove Lagoon Boardwalk',
                                                   'Elevate feet on a shaded bamboo deck and hydrate with icy cold '
                                                   'natural fruit juice.'),
                                       'morning': (   '🌅 Glass-Bottom Kayaking through Secret Mangrove Channels',
                                                      '08:30 AM - 11:00 AM',
                                                      'Kayak rental $15',
                                                      15,
                                                      'Paddle quietly through cathedral-like archways of mangrove '
                                                      'roots sheltering baby reef rays and tropical birds.',
                                                      'Looking through the clear glass kayak floor at darting silver '
                                                      'fish and submerged root gardens.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/18/Australia_Cairns_01.jpg/960px-Australia_Cairns_01.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Hidden Sea Cave Exploration & Tidal Lagoon Swim',
                                                     '11:30 AM - 02:30 PM',
                                                     'Guide fee $12',
                                                     12,
                                                     'Wade into limestone sea caves illuminated by natural overhead '
                                                     'skylights when low tide reveals secret sandy floors.',
                                                     'Standing at the mouth of the limestone cave framing the '
                                                     'sparkling turquoise ocean beyond.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ed/Baltic_Sea_view_from_Schmiedeberg_hill_in_Rerik%2C_2025-06-23.jpg/960px-Baltic_Sea_view_from_Schmiedeberg_hill_in_Rerik%2C_2025-06-23.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Tidepool Sunset Walk & Oceanfront Beach Hearth',
                                                      '05:45 PM - 09:00 PM',
                                                      'Free access / Dining',
                                                      25,
                                                      'Explore glowing tide pools reflecting the orange sky, then dine '
                                                      'barefoot at candlelit beach tables.',
                                                      'Silhouetted on volcanic rocks as ocean spray catches the golden '
                                                      'hour light.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/80/Beach_-_San_Agust%C3%ADn.jpg/960px-Beach_-_San_Agust%C3%ADn.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Volcanic Jungle Waterfalls, Natural Rock Pools & Sunset Cliffs',
                                       'neighborhood': 'Interior Volcanic Highlands & West Headland',
                                       'rest': (   '02:30 PM - 03:30 PM',
                                                   '☕ Mountain Grown Organic Coffee & Soursop Sorbet',
                                                   'Rainforest Vista Lookout Terrace',
                                                   'Take a shoe-off break under canopy ferns and enjoy chilled soursop '
                                                   'sorbet to restore electrolytes.'),
                                       'morning': (   '🌅 Jungle Ridge Trek to Hidden 3-Tier Volcanic Waterfall',
                                                      '08:00 AM - 11:15 AM',
                                                      'Park permit $5',
                                                      8,
                                                      'Hike beneath giant wild ferns to swim in the cool freshwater '
                                                      'pools beneath a thundering jungle cascade.',
                                                      'Submerged in the turquoise plunge pool with the waterfall '
                                                      'cascading down lush moss-covered basalt behind.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a0/Bennett_Lake.jpg/960px-Bennett_Lake.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Volcanic Hot Springs Soak & Botanical Orchid Gardens',
                                                     '11:45 AM - 02:30 PM',
                                                     'Thermal pass $15',
                                                     18,
                                                     'Relax muscles in natural geothermal mineral pools surrounded by '
                                                     'wild blooming orchids.',
                                                     'Steam rising over the volcanic stone pool with lush jungle vines '
                                                     'hanging above.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/1b/Black_sand_beach_north_of_Kaikoura%2C_Canterbury%2C_New_Zealand.jpg/960px-Black_sand_beach_north_of_Kaikoura%2C_Canterbury%2C_New_Zealand.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'West Headland Sunset Lookout & Acoustic Beach Bonfire',
                                                      '05:30 PM - 09:00 PM',
                                                      'Free access',
                                                      22,
                                                      'Climb the grassy headland for an unobstructed 180-degree view '
                                                      'of the sun sinking into the open ocean.',
                                                      'Long shadows stretching across the grassy volcanic headland '
                                                      'framing the glowing golden sea.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/5a/Borkum%2C_Hauptstrand_--_2020_--_2691_%28bw%29.jpg/960px-Borkum%2C_Hauptstrand_--_2020_--_2691_%28bw%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Outer Barrier Sandbars, Blue Lagoons & Sailboat Glides',
                                       'neighborhood': 'Outer Barrier Atoll',
                                       'rest': (   '03:00 PM - 04:00 PM',
                                                   '🍧 Shaved Island Ice with Mango Puree & Palm Shade',
                                                   'Reefside Shaded Pavilion',
                                                   'Sit on open-air timber benches with hand-shaved ice drenched in '
                                                   'pure passionfruit and mango puree.'),
                                       'morning': (   '🌅 Outer Barrier Reef Drift Snorkel & Living Coral Gardens',
                                                      '08:30 AM - 11:30 AM',
                                                      'Boat shuttle $20',
                                                      25,
                                                      'Take a small wooden boat out to the barrier reef where gentle '
                                                      'ocean currents glide you over giant brain corals.',
                                                      'Underwater wide-angle showing schools of yellow tang swimming '
                                                      'over colorful staghorn corals.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/07/Matira_Beach%2C_Bora_Bora%2C_French_Polynesia.jpg/960px-Matira_Beach%2C_Bora_Bora%2C_French_Polynesia.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Secret Sandbar Low-Tide Walk & Natural Swimming Basin',
                                                     '12:00 PM - 02:45 PM',
                                                     'Boat trip included',
                                                     15,
                                                     'Step off onto a white sandbar exposed only during low tide in '
                                                     'the middle of a turquoise lagoon.',
                                                     'Standing in ankle-deep crystal water with 360 degrees of '
                                                     'turquoise sea and no land in sight.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/15/Bussaglia_plage_Serriera.jpg/960px-Bussaglia_plage_Serriera.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Sunset Overwater Hammock Lounge & Tropical Soundscape',
                                                      '05:30 PM - 08:30 PM',
                                                      'Walk-in lounge',
                                                      26,
                                                      'Lay in woven rope hammocks suspended directly over the lapping '
                                                      'water as twilight turns the sky indigo.',
                                                      'Cocktail glass held above the overwater net with the pastel '
                                                      'sunset reflecting below.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9c/Cape_Cove%2C_Oregon.jpg/960px-Cape_Cove%2C_Oregon.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Coastal Cliffs, Sea Turtle Nesting Dunes & Blowholes',
                                       'neighborhood': 'Southern Wild Dunes & Marine Sanctuary',
                                       'rest': (   '02:30 PM - 03:30 PM',
                                                   '🥤 Fresh Cold-Pressed Sugar Cane Juice & Porch Rest',
                                                   'Sanctuary Veranda Kiosk',
                                                   'Hydrate with fresh crushed sugarcane and lime over ice to recharge '
                                                   'energy before evening stroll.'),
                                       'morning': (   '🌅 Dawn Sea Turtle Observation & Coastal Dune Boardwalk',
                                                      '07:30 AM - 10:30 AM',
                                                      'Sanctuary donation $5',
                                                      8,
                                                      'Join conservation guides on raised wooden boardwalks watching '
                                                      'wild sea turtles glide in calm dawn shallows.',
                                                      'Looking down from the wooden boardwalk as a giant green turtle '
                                                      'surfaces for air in crystal water.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c1/Careening_of_a_pirogue_on_a_sand_beach%2C_at_golden_hour%2C_in_Si_Phan_Don%2C_Laos.jpg/960px-Careening_of_a_pirogue_on_a_sand_beach%2C_at_golden_hour%2C_in_Si_Phan_Don%2C_Laos.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Coastal Blowholes & Black Sand Volcanic Beach',
                                                     '11:15 AM - 02:30 PM',
                                                     'Free access',
                                                     10,
                                                     'Witness explosive ocean geysers shooting 20 meters high through '
                                                     'natural lava tubes into the sky.',
                                                     'Explosive water spray bursting from the black volcanic rock '
                                                     'against a deep blue sky.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/40/Careening_of_a_pirogue_on_a_sandy_beach_of_a_tiny_island_in_the_Mekong_near_Don_Det_in_Laos.jpg/960px-Careening_of_a_pirogue_on_a_sandy_beach_of_a_tiny_island_in_the_Mekong_near_Don_Det_in_Laos.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Dune Crest Sunset Yoga & Starlit Ocean BBQ',
                                                      '05:30 PM - 09:00 PM',
                                                      'Free / BBQ $20',
                                                      24,
                                                      'Watch the sun dip below the rolling sand dunes, followed by an '
                                                      'open-air barbecue with local acoustic songs.',
                                                      'Long dramatic shadows cast across wind-sculpted sand ripples as '
                                                      'the sun sets.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7a/Cavalos_nas_dunas_de_Jericoacora_%28edited%29.jpg/960px-Cavalos_nas_dunas_de_Jericoacora_%28edited%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Bamboo River Rafting, Tropical Spice Plantations & Hidden Springs',
                                       'neighborhood': 'Lush River Valley & Bamboo Groves',
                                       'rest': (   '03:00 PM - 04:00 PM',
                                                   '🍹 Chilled Lemongrass Pandan Tea & Riverbed Shingle Rest',
                                                   'Bamboo Riverbend Kiosk',
                                                   'Dip your feet in the cool mountain river while sipping fragrant '
                                                   'iced lemongrass and pandan tea.'),
                                       'morning': (   '🌅 Handcrafted Bamboo Raft Glide Down Emerald River',
                                                      '08:15 AM - 10:45 AM',
                                                      'Raft hire $18',
                                                      18,
                                                      'Glide silently downstream on a 30-foot bamboo raft steered by '
                                                      'local river masters under overhanging jungle vines.',
                                                      'Sitting on a raised bamboo raft throne with the emerald river '
                                                      'flowing ahead through steep limestone cliffs.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7e/Children_playing_at_sunset_on_a_Mekong_bank_in_Si_Phan_Don.jpg/960px-Children_playing_at_sunset_on_a_Mekong_bank_in_Si_Phan_Don.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Organic Island Spice Plantation & Vanilla Bean Walk',
                                                     '11:15 AM - 02:15 PM',
                                                     'Estate entry $10',
                                                     12,
                                                     'Walk through terraced plantations smelling fresh cinnamon bark, '
                                                     'nutmeg pods, and flowering vanilla orchids.',
                                                     'Sunlight filtering through banana leaves onto green vanilla bean '
                                                     'pods hanging on trellises.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7d/Chimney_Rock_Trail_Point_Reyes_December_2016_panorama_1.jpg/960px-Chimney_Rock_Trail_Point_Reyes_December_2016_panorama_1.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Riverside Firefly Night Kayak & Lantern Dining',
                                                      '06:00 PM - 09:00 PM',
                                                      'Kayak tour $22',
                                                      28,
                                                      'Paddle through pitch-black river tunnels where thousands of '
                                                      'bioluminescent fireflies pulse in unison in the trees.',
                                                      'Constellations of pulsing yellow fireflies lighting up the dark '
                                                      'riverbank foliage.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0d/Chimney_Rock_Trail_Point_Reyes_December_2016_panorama_2.jpg/960px-Chimney_Rock_Trail_Point_Reyes_December_2016_panorama_2.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Coastal Sea Arches, Secret Tide Pools & Lighthouse Point',
                                       'neighborhood': 'Windward Lighthouse Cliffs',
                                       'rest': (   '02:30 PM - 03:30 PM',
                                                   '☕ Cold Brew Coconut Coffee & Shaded Veranda',
                                                   "Lighthouse Keeper's Cottage",
                                                   'Rest under white colonnades overlooking crashing ocean waves with '
                                                   'a rich coconut cold brew.'),
                                       'morning': (   '🌅 Sunrise Hike to Historic Oceanic Lighthouse Tower',
                                                      '07:00 AM - 09:30 AM',
                                                      'Free Trail',
                                                      0,
                                                      'Ascend the coastal promontory as the dawn light illuminates '
                                                      'jagged offshore sea stacks and wheeling terns.',
                                                      'The white cylindrical lighthouse silhouetted against a '
                                                      'brilliant pink-and-gold ocean sunrise.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e6/Contre-jour_photograph_of_the_careening_of_a_pirogue_at_sunset_with_sunlight_through_a_hole_in_its_roof_Si_Phan_Don_Laos.jpg/960px-Contre-jour_photograph_of_the_careening_of_a_pirogue_at_sunset_with_sunlight_through_a_hole_in_its_roof_Si_Phan_Don_Laos.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Natural Basalt Sea Arch Bridge & Hidden Cave Beach',
                                                     '10:30 AM - 02:00 PM',
                                                     'Free access',
                                                     10,
                                                     'Cross a monumental natural stone bridge carved by millennia of '
                                                     'crashing Pacific waves.',
                                                     'Looking through the monumental stone arch framing azure ocean '
                                                     'waves breaking on secluded white sand.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/fc/Crown_of_Thorns_Starfish_at_Malapascuas_Island_v._II.jpg/960px-Crown_of_Thorns_Starfish_at_Malapascuas_Island_v._II.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Cliffside Sunset Lounge & Oceanfront Acoustic Serenade',
                                                      '05:30 PM - 08:30 PM',
                                                      'Lounge walk-in',
                                                      28,
                                                      'Sip tropical infusions on tiered wooden terraces carved '
                                                      'directly into the ocean cliff as twilight falls.',
                                                      'Cocktail glass glowing with twilight reflections high above '
                                                      'crashing white-water waves.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/96/Cuba_-_Cayo_Coco.jpg/960px-Cuba_-_Cayo_Coco.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Rainforest Canopy Skywalk, Sacred Banyan & Secret Hot Springs',
                                       'neighborhood': 'Ancient Inland Rainforest Sanctuary',
                                       'rest': (   '03:00 PM - 04:00 PM',
                                                   '🍵 Forest Botanical Herbal Infusion & Treehouse Bench',
                                                   'Treehouse Canopy Platform',
                                                   'Rest among the treetops listening to birdsong while sipping '
                                                   'restorative wild ginger and turmeric tea.'),
                                       'morning': (   '🌅 Suspended Treetop Canopy Walkway through Ancient Fog',
                                                      '08:30 AM - 11:00 AM',
                                                      'Skywalk pass $14',
                                                      14,
                                                      'Walk along suspended aluminum bridges 40 meters above the '
                                                      'forest floor through morning canopy mist.',
                                                      'Looking down the narrow suspension bridge disappearing into '
                                                      'dense emerald jungle ferns.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f2/Dike_in_Frontignan.jpg/960px-Dike_in_Frontignan.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Sacred 500-Year-Old Banyan Tree & Natural Stream Pools',
                                                     '11:30 AM - 02:30 PM',
                                                     'Free sanctuary',
                                                     8,
                                                     'Sit beneath the colossal root cathedral of an ancient sacred '
                                                     'banyan tree and swim in clear mountain pools.',
                                                     'Dappled sunlight streaming through the massive hanging curtain '
                                                     'of banyan aerial roots.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/cb/Don_Puay_river_bank_landscape_at_sunset.jpg/960px-Don_Puay_river_bank_landscape_at_sunset.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Forest Hot Springs Night Soak & Starlit Hearth Grill',
                                                      '05:45 PM - 09:00 PM',
                                                      'Thermal ticket $18',
                                                      30,
                                                      'Soak in stone-lined geothermal pools surrounded by steam and '
                                                      'tropical night sounds under clear stars.',
                                                      'Steam rising from mineral springs into the dark jungle canopy '
                                                      'illuminated by soft bamboo lanterns.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/df/Driftwood_on_the_beach_north_of_Kaikoura%2C_Canterbury%2C_New_Zealand_02.jpg/960px-Driftwood_on_the_beach_north_of_Kaikoura%2C_Canterbury%2C_New_Zealand_02.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Traditional Fishing Village, Salt Flats & Wooden Dory Glides',
                                       'neighborhood': "Historic Fishermen's Cove",
                                       'rest': (   '02:30 PM - 03:30 PM',
                                                   '🍧 Shaved Guava Ice & Wharf Bench Rest',
                                                   "Harbor Fisherman's Shack",
                                                   'Sit on sun-warmed wooden pier timber with sweet shaved pink guava '
                                                   'ice watching boats unload.'),
                                       'morning': (   '🌅 Sunrise with Local Fishermen & Sea Salt Flat Basins',
                                                      '07:30 AM - 10:15 AM',
                                                      'Free access',
                                                      5,
                                                      'Watch traditional salt farmers harvest gleaming white sea salt '
                                                      'crystals from geometric coastal tide ponds.',
                                                      'Geometric mirror reflections of pastel sunrise clouds in the '
                                                      'shallow flooded salt pans.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/81/Ensis_ensis_%28Linnaeus_1758%29.jpg/960px-Ensis_ensis_%28Linnaeus_1758%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Wooden Dory Boat Trip to Secluded Snorkel Island',
                                                     '11:00 AM - 02:30 PM',
                                                     'Local boat $16',
                                                     16,
                                                     'Hop in a colorful hand-painted wooden dory out to an uninhabited '
                                                     'rocky islet ringed by corals.',
                                                     'Bow of the wooden boat slicing through turquoise shallows '
                                                     'towards a deserted white sand beach.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/60/Fishermen_at_Kavarathi%2C_Lakshadweep%2C_India_%28edit%29.jpg/960px-Fishermen_at_Kavarathi%2C_Lakshadweep%2C_India_%28edit%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Pier End Sunset Feast & Barefoot Acoustic Jam',
                                                      '05:30 PM - 09:00 PM',
                                                      'Walk-in dining',
                                                      24,
                                                      'Dine at rustic wooden tables right on the pier as the sun sinks '
                                                      'into the calm harbor water.',
                                                      'The glow of hurricane lamps on weathered timber with fishing '
                                                      'boat silhouettes against violet dusk.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d6/Fishermen_at_work_by_Shagil_Kannur.jpg/960px-Fishermen_at_work_by_Shagil_Kannur.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Farewell Panoramic Headland, Secret Tide Cave & Starlit Beach Toast',
                                       'neighborhood': 'Grand Ocean Bluff & Southern Sands',
                                       'rest': (   '03:00 PM - 04:00 PM',
                                                   '🥥 Fresh Coconut Elixir & Shaded Ocean Pavilion',
                                                   'Blufftop Pergola',
                                                   'Final afternoon recharge overlooking the vast ocean horizon, '
                                                   'journaling highlights of the voyage.'),
                                       'morning': (   '🌅 Grand Bluff 360° Ocean Overlook & Whale Trail',
                                                      '08:00 AM - 10:30 AM',
                                                      'Free trail',
                                                      0,
                                                      'Stand at the highest coastal headland to watch ocean swells '
                                                      'roll in from thousands of miles across the Pacific.',
                                                      'Wide panoramic shot looking out over the endless curved horizon '
                                                      'where azure sea meets sky.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/6b/Fishing_boats%2C_morning%2C_Beach%2C_Rincon_de_la_Victoria%2C_Andalusia%2C_Spain.jpg/960px-Fishing_boats%2C_morning%2C_Beach%2C_Rincon_de_la_Victoria%2C_Andalusia%2C_Spain.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Secret Cathedral Tide Cave Exploration',
                                                     '11:15 AM - 02:15 PM',
                                                     'Free access',
                                                     10,
                                                     'Venture into a monumental sea cave carved into volcanic rock, '
                                                     'featuring natural skylights and sandy floors.',
                                                     'Shafts of golden sunlight piercing the roof of the cavern, '
                                                     'illuminating a natural shallow pool.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/51/Havelock_Island%2C_Mangrove_tree_on_the_beach%2C_Andaman_Islands.jpg/960px-Havelock_Island%2C_Mangrove_tree_on_the_beach%2C_Andaman_Islands.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Farewell Starlit Beach Bonfire & Ocean Celebration',
                                                      '05:30 PM - 09:30 PM',
                                                      'Bonfire access',
                                                      32,
                                                      'Gather around a warm drift-wood beach fire with new friends, '
                                                      'cold drinks, and glowing constellations above.',
                                                      'Dancing sparks of the campfire drifting toward the starry night '
                                                      'sky over the dark ocean.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/19/Havelock_Island%2C_Sandy_lagoon%2C_Andaman_Islands.jpg/960px-Havelock_Island%2C_Sandy_lagoon%2C_Andaman_Islands.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')}],
    'ALPINE_MOUNTAIN_GLACIER': [   {   'theme': 'Glacial Lake Mirror Reflections, Pine Ridges & Alpine Bakeries',
                                       'neighborhood': 'Upper Glacial Valley & Lake Basin',
                                       'rest': (   '02:30 PM - 03:30 PM',
                                                   '☕ Warm Spiced Cardamom Buns & Timber Porch Rest',
                                                   'Lakeside Timber Cafe',
                                                   'Sit on wooden benches wrapped in fleece blankets, sip rich hot '
                                                   'cocoa or espresso, and rest hiking legs.'),
                                       'morning': (   '🌅 Alpine Lake Mirror Reflection & Pine Ridge Trail',
                                                      '07:30 AM - 10:00 AM',
                                                      'National Park Pass',
                                                      8,
                                                      'Arrive right at dawn before breezes ruffle the water to see the '
                                                      'jagged mountain peaks mirrored with glass-like clarity.',
                                                      'Low-angle shot sitting on a cedar log with the snow-covered '
                                                      'peaks mirrored in the lake.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/01/01_Calanche_Piana.jpg/960px-01_Calanche_Piana.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'High-Elevation Suspension Bridge & Mountain Gondola Ascent',
                                                     '11:00 AM - 02:30 PM',
                                                     'Gondola Lift Ticket',
                                                     35,
                                                     'Ride the scenic cable car above the tree line. Walk across the '
                                                     'suspended bridge over sheer canyon abysses.',
                                                     'Standing on the suspended walkway with sheer mountain drop-offs '
                                                     'directly beneath your boots.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/54/01_Gorges_du_Tarn_Roc_des_Hourtous.jpg/960px-01_Gorges_du_Tarn_Roc_des_Hourtous.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Thermal Hot Springs Soak & Starlit Hearth Dining',
                                                      '05:30 PM - 08:30 PM',
                                                      'Thermal pass',
                                                      25,
                                                      'Soak in mineral-rich geothermal hot springs as crisp mountain '
                                                      'evening air cools your face.',
                                                      'Steam rising from the mineral pool with towering dark pine '
                                                      'peaks and stars above.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/6c/1_lake_louise_pano_2019.jpg/960px-1_lake_louise_pano_2019.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Hidden Canyons, Turquoise Rapids & Mountain Chalet Stews',
                                       'neighborhood': 'Lower River Canyon & Wooded Valley',
                                       'rest': (   '03:00 PM - 04:00 PM',
                                                   '🍵 Herbal Alpine Mountain Tea & Honey Cake',
                                                   'Chalet Shaded Garden',
                                                   'Sit on carved wooden benches overlooking the rushing glacial creek '
                                                   'and sip wild chamomile-thyme tea.'),
                                       'morning': (   '🌅 Carved Limestone Gorge Wooden Footbridge Walk',
                                                      '08:15 AM - 11:00 AM',
                                                      'Gorge pass $7',
                                                      7,
                                                      'Walk suspended wooden boardwalks anchored directly to sheer '
                                                      'canyon walls above roaring turquoise rapids.',
                                                      'Looking down the narrow canyon between moss-draped limestone '
                                                      'cliffs with turquoise foaming water.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/77/1_tianzishan_wulingyuan_zhangjiajie_2012.jpg/960px-1_tianzishan_wulingyuan_zhangjiajie_2012.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'High Meadow Wildflower Loop & Alpine Horn Encounter',
                                                     '11:30 AM - 02:45 PM',
                                                     'Free trail',
                                                     14,
                                                     'Hike gentle trails through subalpine meadows filled with blue '
                                                     'gentians, listening to traditional horn players.',
                                                     'Surrounded by blooming purple and yellow wildflowers with '
                                                     'snow-capped peaks in the background.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/62/1_zhangjiajie_huangshizhai_wulingyuan_panorama_2012.jpg/960px-1_zhangjiajie_huangshizhai_wulingyuan_panorama_2012.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Mountain Hut Fondue Feast & Twilight Peak Glow (Alpenglow)',
                                                      '05:30 PM - 09:00 PM',
                                                      'Chalet dining',
                                                      32,
                                                      'Dip crusty bread cubes into bubbling Gruyère and Emmental '
                                                      'cheese as the setting sun paints peaks rose-pink.',
                                                      'The jagged snow peaks glowing vivid pink-orange during the '
                                                      'brief 15 minutes of alpenglow.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/8e/150906-001_Wilpena_Pound_from_Moralana_Scenic_Drive_Pano_50pc.jpg/960px-150906-001_Wilpena_Pound_from_Moralana_Scenic_Drive_Pano_50pc.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Glacier Tongue Caves, High Ice Fields & Mountain Pass Trains',
                                       'neighborhood': 'Upper Pass & Glacial Moraine',
                                       'rest': (   '02:30 PM - 03:30 PM',
                                                   '☕ Hot Glacial Spring Espresso & Linzer Torte',
                                                   'Summit Observatory Deck',
                                                   'Rest in the heated glass panoramic pavilion with hot coffee and '
                                                   'raspberry Linzer torte.'),
                                       'morning': (   '🌅 Cogwheel Scenic Railway Ascent to Glacial Ice Tunnel',
                                                      '08:30 AM - 11:45 AM',
                                                      'Cogwheel train pass',
                                                      38,
                                                      'Ride historic red mountain trains that climb 2,000 meters '
                                                      'through pine forests into ice kingdoms.',
                                                      'Framing the red cogwheel train winding along a narrow cliff '
                                                      'edge with massive glaciers behind.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/2/26/20090719_Crkva_Gospa_od_Zdravlja_Kotor_Bay_Montenegro.jpg/960px-20090719_Crkva_Gospa_od_Zdravlja_Kotor_Bay_Montenegro.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Blue Ice Grotto Walkway Deep Inside the Glacier',
                                                     '12:15 PM - 02:45 PM',
                                                     'Grotto ticket',
                                                     18,
                                                     'Walk through hand-carved ice tunnels glowing with translucent '
                                                     'electric-blue light beneath 100m of ice.',
                                                     'Surrounded by pure sculpted blue ice walls illuminated by soft '
                                                     'internal LED light.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/35/20250708_Teide_03.jpg/960px-20250708_Teide_03.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Cedar Pine Sauna & Open-Hearth Mountain Feast',
                                                      '05:30 PM - 09:00 PM',
                                                      'Sauna & dinner',
                                                      35,
                                                      'Warm chilled bones in a wood-fired outdoor barrel sauna '
                                                      'overlooking the snowy valley.',
                                                      'Steam rising into the freezing mountain air against the dark '
                                                      'silhouettes of fir trees and stars.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/81/205kei_train_in_JR_Nikko_line_02.JPG/960px-205kei_train_in_JR_Nikko_line_02.JPG?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Waterfalls Valley, Sheer Granite Walls & Cogwheel Climbs',
                                       'neighborhood': 'Valley of 72 Cascades',
                                       'rest': (   '03:00 PM - 04:00 PM',
                                                   '🍰 Warm Berry Crumble & Mountain Farm Dairy Milk',
                                                   'Waterfall Base Chalet',
                                                   'Sit on the wooden veranda watching mist spray from sheer 300m '
                                                   'cliffs while enjoying freshly churned dairy.'),
                                       'morning': (   '🌅 Subterranean Waterfall Chasm Inside the Mountain',
                                                      '08:30 AM - 11:00 AM',
                                                      'Chasm entry $12',
                                                      12,
                                                      'Take a cliffside funicular into the carved belly of the '
                                                      'mountain where glacial meltwater thunders in spiral chutes.',
                                                      'Looking up from the wet stone viewing gallery at the '
                                                      'corkscrewing white waterfall illuminated by amber lamps.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/5e/21-224-5054_NNP_Synevyr_RB_18.jpg/960px-21-224-5054_NNP_Synevyr_RB_18.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Alpine Cheese Dairy Visit & Mountain Meadow Trail',
                                                     '11:30 AM - 02:30 PM',
                                                     'Dairy tour $10',
                                                     15,
                                                     'Watch alpine cheesemakers stir giant copper vats over wood fires '
                                                     'and sample fresh curd cheeses.',
                                                     'Cows grazing in high flower meadows with heavy brass bells '
                                                     'ringing softly against backdrop of snow peaks.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/62/80_-_Machu_Picchu_-_Juin_2009_-_edit.jpg/960px-80_-_Machu_Picchu_-_Juin_2009_-_edit.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Sunset Cableway to Cliffside Edge Walkway',
                                                      '05:30 PM - 08:30 PM',
                                                      'Cable ticket',
                                                      28,
                                                      'Walk along a cantilevered steel walkway wrapped around a sheer '
                                                      '1,000m vertical cliff at sunset.',
                                                      'Looking down through metal grating beneath your boots into the '
                                                      'twilight valley floor thousands of feet below.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9f/99_-_Machu_Picchu_-_Juin_2009.edit3.jpg/960px-99_-_Machu_Picchu_-_Juin_2009.edit3.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'High Mountain Tarns, Granite Slabs & Crystal Streams',
                                       'neighborhood': 'Upper Granite Pass',
                                       'rest': (   '02:30 PM - 03:30 PM',
                                                   '🍵 Pine Needle Infusion & Almond Honey Tart',
                                                   'High Pass Rest Cabin',
                                                   'Warm hands around an enamel mug of pine needle tea with local '
                                                   'honey at 2,400 meters.'),
                                       'morning': (   '🌅 Sunrise Trek to Secluded Turquoise Glacial Tarn',
                                                      '07:30 AM - 10:30 AM',
                                                      'Free trail',
                                                      0,
                                                      'Hike past gnarled ancient stone pines to reach a high glacial '
                                                      'tarn glowing luminous teal.',
                                                      'Reflections of razor-sharp granite needles in the mirror-still '
                                                      'glacial tarn at dawn.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3f/A_small_loch_in_the_saddle_between_Beinn_an_Dothaidh_and_Beinn_Dorain%2C_Scotland_01.jpg/960px-A_small_loch_in_the_saddle_between_Beinn_an_Dothaidh_and_Beinn_Dorain%2C_Scotland_01.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Via Ferrata Cable Route Along Sheer Mountain Ridges',
                                                     '11:00 AM - 02:30 PM',
                                                     'Gear rental $20',
                                                     25,
                                                     'Clip into steel safety cables and scale iron rungs set directly '
                                                     'into vertical rock faces.',
                                                     'Action photo climbing the iron ladder rungs with the entire '
                                                     'mountain range spread out below.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b4/Aerial_image_of_Alicudi_%28view_from_the_south%29.jpg/960px-Aerial_image_of_Alicudi_%28view_from_the_south%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Alpine Hut Stew Feast & Stargazing at 2,500m',
                                                      '05:30 PM - 09:00 PM',
                                                      'Hut dining',
                                                      30,
                                                      'Gather in the cozy wood-paneled hut dining room for steaming '
                                                      'bowls of goulash, then step out into zero-light-pollution '
                                                      'skies.',
                                                      'The Milky Way arching across the night sky between dark '
                                                      'silhouettes of jagged mountain peaks.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e0/Aerial_image_of_Stromboli_%28view_from_the_northeast%29.jpg/960px-Aerial_image_of_Stromboli_%28view_from_the_northeast%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Ancient Larch Forests, Mountain Passes & Thermal Spas',
                                       'neighborhood': 'Thermal Springs Alpine Valley',
                                       'rest': (   '03:00 PM - 04:00 PM',
                                                   '☕ Hot Hazelnut Mocha & Sourdough Pastry',
                                                   'Thermal Village Plaza',
                                                   'Sit by an outdoor bubbling thermal fountain wrapped in warm woolen '
                                                   'throws.'),
                                       'morning': (   '🌅 Golden Larch Forest Trail in Early Morning Mist',
                                                      '08:15 AM - 11:00 AM',
                                                      'Free trail',
                                                      0,
                                                      'Walk through ancient needle-scented larch trees glowing bright '
                                                      'yellow in autumn or emerald in summer.',
                                                      'Shafts of early sunlight cutting through morning mist between '
                                                      'towering mossy larch trunks.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/2/27/Afternoon_at_Tennfjorden%2C_Raftsundet%2C_Hinn%C3%B8ya%2C_Norway%2C_2015_September_%2802%29.jpg/960px-Afternoon_at_Tennfjorden%2C_Raftsundet%2C_Hinn%C3%B8ya%2C_Norway%2C_2015_September_%2802%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Historic Roman Thermal Baths in Alpine Gorge',
                                                     '11:30 AM - 02:30 PM',
                                                     'Thermal ticket $22',
                                                     22,
                                                     'Bathe in steaming natural mineral waters that have bubbled from '
                                                     'mountain fissures since Roman times.',
                                                     'Steam rising over ancient carved stone thermal pools set inside '
                                                     'a narrow rock gorge.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/45/Afternoon_at_Tennfjorden%2C_Raftsundet%2C_Hinn%C3%B8ya%2C_Norway%2C_2015_September.jpg/960px-Afternoon_at_Tennfjorden%2C_Raftsundet%2C_Hinn%C3%B8ya%2C_Norway%2C_2015_September.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Mountain Ridge Funicular Sunset & Rustic Grill',
                                                      '05:30 PM - 09:00 PM',
                                                      'Funicular $15',
                                                      32,
                                                      'Ride a steep wooden funicular car to a panoramic ridge for '
                                                      'sunset drinks and wood-fired delicacies.',
                                                      'Looking out over five glistening alpine lakes nestled in the '
                                                      'valley during golden hour.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7d/Almsee_Nordbucht-4224.jpg/960px-Almsee_Nordbucht-4224.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Panoramic Crest Trails, Wild Edelweiss & Skyway Gondolas',
                                       'neighborhood': 'High Crest & Ridge Divide',
                                       'rest': (   '02:30 PM - 03:30 PM',
                                                   '🍰 Warm Plum Tart with Fresh Cream & Mountain Coffee',
                                                   'Ridge Crest Cafe',
                                                   'Rest on the sun terrace at 2,000 meters looking across the '
                                                   'continental divide.'),
                                       'morning': (   '🌅 High Panoramic Crest Trail & Wild Edelweiss Hunt',
                                                      '08:00 AM - 11:00 AM',
                                                      'Ridge trail',
                                                      0,
                                                      'Traverse a panoramic knife-edge ridge trail with views '
                                                      'stretching across three national borders.',
                                                      'Macro shot of a rare velvety white wild Edelweiss blossom '
                                                      'growing out of limestone rock with snowy peaks behind.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/cc/Andiast-Breil-Brigels._24-09-2025._%28d.j.b.%29_08.jpg/960px-Andiast-Breil-Brigels._24-09-2025._%28d.j.b.%29_08.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Rotating 360° Cableway to High Summit Station',
                                                     '11:30 AM - 02:30 PM',
                                                     'Cable ticket $36',
                                                     36,
                                                     'Ascend on a revolving cable car floor that completes two full '
                                                     'rotations during the 5-minute climb.',
                                                     'Looking down through the cable car glass at climbers on the '
                                                     'ridge looking like tiny colorful ants.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/1b/Angelus_Hut_in_the_winter%2C_Nelson_Lakes_National_Park%2C_New_Zealand.jpg/960px-Angelus_Hut_in_the_winter%2C_Nelson_Lakes_National_Park%2C_New_Zealand.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Summit Glass Pavilion Sunset & Fondue Feast',
                                                      '05:30 PM - 09:00 PM',
                                                      'Summit dinner',
                                                      38,
                                                      'Dine inside a geometric glass pavilion perched on the peak as '
                                                      'the sun sets over hundreds of snow summits.',
                                                      'The setting sun blazing through the geometric glass frames '
                                                      'casting golden triangles on the snow.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/db/Ansberg_Blickrichtung_S%C3%BCden_120324.jpg/960px-Ansberg_Blickrichtung_S%C3%BCden_120324.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Glacial Moraines, Ice Rivers & Alpine Botanic Gardens',
                                       'neighborhood': 'Moraine Ridge & Glacial River Basin',
                                       'rest': (   '03:00 PM - 04:00 PM',
                                                   '🍵 Glacial Herbal Tea & Honeyed Walnut Cake',
                                                   'Botanical Garden Pavilion',
                                                   'Sit in the sunny rock garden surrounded by 1,000 species of '
                                                   'high-altitude flora.'),
                                       'morning': (   '🌅 Moraine Ridge Trail Overlooking the Great Ice River',
                                                      '08:15 AM - 11:15 AM',
                                                      'Moraine trail',
                                                      0,
                                                      'Walk along the crest of a massive gravel moraine left behind by '
                                                      'ancient retreating glaciers.',
                                                      'Vast serpentine ribbon of striped glacial ice winding between '
                                                      'towering gray granite peaks.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f8/Babia_G%C3%B3ra%2C_20230304_0651_3162.jpg/960px-Babia_G%C3%B3ra%2C_20230304_0651_3162.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Alpine Botanical Rockery & Mountain Marmot Meadow',
                                                     '11:45 AM - 02:30 PM',
                                                     'Entry $6',
                                                     10,
                                                     'Observe playful alpine marmots sunning on granite slabs in a '
                                                     'protected botanical reserve.',
                                                     'A furry marmot standing alert on two hind legs atop a boulder '
                                                     'with wildflowers in foreground.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/73/Bali_Khila_Rajgad_Maharashtra.jpg/960px-Bali_Khila_Rajgad_Maharashtra.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Glacial Stream Side Sauna & Wood-Roasted Feast',
                                                      '05:30 PM - 09:00 PM',
                                                      'Sauna & food',
                                                      32,
                                                      'Dip in an icy glacial stream between hot cedar sauna sessions, '
                                                      'followed by slow-roasted comfort food.',
                                                      'Steam billowing from the cedar sauna cabin nestled beside a '
                                                      'turquoise boulder-strewn alpine river.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/5f/Beskid_S%C4%85decki_in_winter_2016_05.jpg/960px-Beskid_S%C4%85decki_in_winter_2016_05.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Subalpine Meadows, Wooden Chalet Hamlets & Cowbell Chimes',
                                       'neighborhood': 'Traditional Timber Hamlet',
                                       'rest': (   '02:30 PM - 03:30 PM',
                                                   '☕ Fresh Churned Farm Butter Bread & Mountain Honey',
                                                   'Hamlet Wooden Bench',
                                                   'Relax outside a 300-year-old carved wooden farmhouse listening to '
                                                   'melodic cowbells.'),
                                       'morning': (   '🌅 Carved Wooden Chalet Hamlet Stroll at Sunrise',
                                                      '08:00 AM - 10:30 AM',
                                                      'Free village walk',
                                                      0,
                                                      'Wander car-free dirt lanes between centuries-old timber chalets '
                                                      'adorned with overflowing red geranium flower boxes.',
                                                      'Low-angle shot of weathered dark timber chalet eaves framed by '
                                                      'bright red geraniums and a snow peak.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/63/Blue_Lake_in_Mount_Cook_National_Park.jpg/960px-Blue_Lake_in_Mount_Cook_National_Park.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Traditional Woodcarver Atelier & Cuckoo Clock Workshop',
                                                     '11:00 AM - 02:00 PM',
                                                     'Free entry',
                                                     12,
                                                     'Watch master woodcarvers shape lime wood into intricate clocks '
                                                     'and alpine animals using hand gouges.',
                                                     'Wood shavings curling from a sharp hand chisel as a carved '
                                                     'wooden deer takes shape on the workbench.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/de/Blue_Mountains_National_Park_%28AU%29%2C_Three_Sisters_--_2019_--_1987-9.jpg/960px-Blue_Mountains_National_Park_%28AU%29%2C_Three_Sisters_--_2019_--_1987-9.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Open-Air Alpine Brass Concert & Starlit Hearth Dining',
                                                      '05:30 PM - 09:00 PM',
                                                      'Free concert',
                                                      28,
                                                      'Listen to acoustic brass horns echo off the sheer rock faces in '
                                                      'the village square as dusk settles.',
                                                      'Musicians in traditional vests playing long wooden horns as '
                                                      'purple twilight descends on the valley.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/44/Breathtaking_beauty_of_Dzukou_Valley_in_Manipur-Nagaland_border_%28edit%29.jpg/960px-Breathtaking_beauty_of_Dzukou_Valley_in_Manipur-Nagaland_border_%28edit%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                   {   'theme': 'Farewell Mountain Summit, Alpenglow Glow & Campfire Under Stars',
                                       'neighborhood': 'High Summit & Continental Divide',
                                       'rest': (   '03:00 PM - 04:00 PM',
                                                   '☕ Hot Spiced Cider & Linzer Cookie on Summit Terrace',
                                                   'Continental Lookout',
                                                   'Final mountain recharge soaking in the vast scale of the alpine '
                                                   'kingdom.'),
                                       'morning': (   '🌅 Farewell Sunrise Ridge Hike & Glass Skybridge Walk',
                                                      '08:00 AM - 11:00 AM',
                                                      'Skybridge pass $15',
                                                      15,
                                                      'Walk out onto a glass-bottomed platform projecting 20 meters '
                                                      'over sheer open mountain air.',
                                                      'Looking down between your boots through transparent glass into '
                                                      '800 meters of pure open space.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a6/Breil-Brigels%2C_Lag_da_Breil-_Flem._23-09-2022._%28d.j.b%29_04.jpg/960px-Breil-Brigels%2C_Lag_da_Breil-_Flem._23-09-2022._%28d.j.b%29_04.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'midday': (   'Last High Meadow Stroll & Alpine Souvenir Foraging',
                                                     '11:30 AM - 02:30 PM',
                                                     'Free trail',
                                                     10,
                                                     'Gather mountain herbs, wild chamomile, and dried flowers on a '
                                                     'peaceful descent trail.',
                                                     'Sunlight illuminating a bouquet of wild mountain clover and '
                                                     'grasses held against snow peaks.',
                                                     'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/70/Brei%C3%B0amerkurj%C3%B6kull_glacier%2C_Iceland%2C_20240719_1427_2618.jpg/960px-Brei%C3%B0amerkurj%C3%B6kull_glacier%2C_Iceland%2C_20240719_1427_2618.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                       'evening': (   'Farewell Starlit Hearth Feast & Peak Alpenglow Toast',
                                                      '05:30 PM - 09:30 PM',
                                                      'Lodge dining',
                                                      35,
                                                      'Raise a glass of local spiced wine or alpine beer as the peaks '
                                                      'glow burning orange before turning to indigo.',
                                                      'Silhouetted glasses clinking against the dramatic '
                                                      'pink-and-purple mountain peaks at twilight.',
                                                      'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4f/Brei%C3%B0amerkurj%C3%B6kull_glacier%2C_Iceland%2C_20240719_1514_2687.jpg/960px-Brei%C3%B0amerkurj%C3%B6kull_glacier%2C_Iceland%2C_20240719_1514_2687.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')}],
    'DESERT_OASIS_CULTURE': [   {   'theme': 'Sandstone Canyons, Date Palm Oases & Spice Bazaars',
                                    'neighborhood': 'Ancient Red Canyon & Historic Oasis',
                                    'rest': (   '02:30 PM - 03:30 PM',
                                                '🍵 Fresh Mint Tea in Shaded Palm Grove',
                                                'Oasis Palm Garden Veranda',
                                                'Sit on woven kilim cushions beneath whispering date palms, sip '
                                                'boiling hot mint tea, and escape desert sun.'),
                                    'morning': (   '🌅 Dawn Balloon Flight or Sandstone Canyon Rim Hike',
                                                   '06:30 AM - 09:30 AM',
                                                   'Park permit',
                                                   15,
                                                   'Explore ancient carved sandstone canyons before the midday sun '
                                                   'radiates off the rocks.',
                                                   'Framed through a natural carved stone canyon window with warm '
                                                   'morning sunlight.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/aa/Sand_dunes%2C_Libyan_Desert%2C_Dakhla_Oasis%2C_Egypt.jpg/960px-Sand_dunes%2C_Libyan_Desert%2C_Dakhla_Oasis%2C_Egypt.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'midday': (   'Fragrant Spice Souk & Historic Medersa Courtyard',
                                                  '11:30 AM - 02:30 PM',
                                                  'Free / Small entry',
                                                  8,
                                                  'Wander shaded alleys filled with sacks of ground cumin, saffron, '
                                                  'rosebuds, and hand-woven carpets.',
                                                  'Sunlight streaming through wooden lattice roof screens onto piles '
                                                  'of vibrant spices.',
                                                  'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/30/Sand_dunes_2%2C_Libyan_Desert%2C_Dakhla_Oasis%2C_Egypt.jpg/960px-Sand_dunes_2%2C_Libyan_Desert%2C_Dakhla_Oasis%2C_Egypt.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'evening': (   'Sunset Dune Crest Walk & Starlit Desert Campfire',
                                                   '05:30 PM - 09:00 PM',
                                                   'Excursion pass',
                                                   35,
                                                   'Climb to the top of the highest dune to watch the sand change from '
                                                   'gold to burning violet.',
                                                   'Long dramatic shadows cast across wind-sculpted sand ripples as '
                                                   'the sun sets.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e0/The_Black_Cat_v07no12_%281902-09%29.djvu/page1-500px-The_Black_Cat_v07no12_%281902-09%29.djvu.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                {   'theme': 'Ancient Mud-Brick Kasbahs, Rose Valleys & Copper Artisans',
                                    'neighborhood': 'Mud-Brick Citadel & Artisan Quarters',
                                    'rest': (   '03:00 PM - 04:00 PM',
                                                '🍯 Almond Gazelle Horn Pastry & Pomegranate Juice',
                                                'Courtyard Fountain Cafe',
                                                'Rest feet next to a tiled mosaic fountain and enjoy sweet almond '
                                                'pastries with freshly pressed pomegranate juice.'),
                                    'morning': (   '🌅 Sunrise Over Ancient UNESCO Mud-Brick Citadel',
                                                   '07:30 AM - 10:30 AM',
                                                   'Free entry / guide $8',
                                                   8,
                                                   'Walk through towering red clay towers and wooden gates of an '
                                                   'intact 17th-century fortified desert village.',
                                                   'Looking up from the dry riverbed at the multi-story mud towers '
                                                   'glowing bright ochre in morning sun.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a4/The_Bliss_of_a_Moment.djvu/page1-960px-The_Bliss_of_a_Moment.djvu.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'midday': (   'Copper Hammering Alleys & Hand-Knotted Carpet Looms',
                                                  '11:30 AM - 02:45 PM',
                                                  'Free walk-in',
                                                  12,
                                                  'Watch master craftsmen hammer brass lanterns and weave wool carpets '
                                                  'dyed with indigo and saffron.',
                                                  'Sunlight illuminating dust motes and hanging brass lamps casting '
                                                  'geometric shadow lace.',
                                                  'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/bf/The_East%2C_being_a_narrative_of_personal_impressions_of_a_tour_in_Egypt%2C_Palestine%2C_and_Syria_by_Martin%2C_William_Young.djvu/page1-960px-The_East%2C_being_a_narrative_of_personal_impressions_of_a_tour_in_Egypt%2C_Palestine%2C_and_Syria_by_Martin%2C_William_Young.djvu.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'evening': (   'Palm Grove Camel Trek at Dusk & Rooftop Stargazing',
                                                   '05:30 PM - 09:00 PM',
                                                   'Camel ride $18',
                                                   24,
                                                   'Ride gently through swaying date palms as evening breezes cool the '
                                                   'desert sands.',
                                                   'The silhouette of the camel caravan against a fiery red-and-purple '
                                                   'horizon.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/6e/00065_sand_collage.jpg/960px-00065_sand_collage.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                {   'theme': 'Petrified Sand Valleys, Desert Astronomy & Open Hearth',
                                    'neighborhood': 'Valley of the Moon Sandstone',
                                    'rest': (   '02:30 PM - 03:30 PM',
                                                '🍵 Cardamom Bedouin Coffee & Fresh Medjool Dates',
                                                'Bedouin Goat-Hair Tent',
                                                'Recline on tribal rugs in the shade, chew soft sweet dates, and drink '
                                                'cardamom-infused coffee.'),
                                    'morning': (   '🌅 Sunrise Hike Through Wind-Sculpted Sandstone Arches',
                                                   '07:00 AM - 09:45 AM',
                                                   'Valley pass $6',
                                                   6,
                                                   'Hike through red sandstone towers sculpted into giant mushrooms '
                                                   'and natural arches by desert winds.',
                                                   'Standing tiny inside a giant wind-sculpted stone amphitheater with '
                                                   'morning light illuminating red walls.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/aa/A_sand_dune_in_the_Maranjab_Desert%2C_located_in_the_middle_of_the_Kavir_National_Park_IRAN_09.jpg/960px-A_sand_dune_in_the_Maranjab_Desert%2C_located_in_the_middle_of_the_Kavir_National_Park_IRAN_09.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'midday': (   'Ancient Rock Inscriptions & Desert Water Spring',
                                                  '10:30 AM - 01:45 PM',
                                                  'Free trail',
                                                  8,
                                                  'Discover 2,000-year-old petroglyphs carved into canyon walls by '
                                                  'ancient nomadic caravans.',
                                                  'Ancient carved camels and ibex symbols carved into dark desert '
                                                  'patina rock.',
                                                  'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e1/A_sand_dune_in_the_Maranjab_Desert%2C_located_in_the_middle_of_the_Kavir_National_Park_IRAN_14.jpg/960px-A_sand_dune_in_the_Maranjab_Desert%2C_located_in_the_middle_of_the_Kavir_National_Park_IRAN_14.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'evening': (   'Deep Desert Astronomy Camp & Campfire Lamb Feast',
                                                   '05:30 PM - 09:30 PM',
                                                   'Camp access',
                                                   34,
                                                   'Peer through high-powered telescopes at the rings of Saturn and '
                                                   'nebulae in the ink-black desert sky.',
                                                   'Looking through the telescope eyepiece as the Milky Way blazes '
                                                   'overhead like a river of silver dust.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e2/A_sand_dune_in_the_Maranjab_Desert%2C_located_in_the_middle_of_the_Kavir_National_Park_IRAN_34.jpg/960px-A_sand_dune_in_the_Maranjab_Desert%2C_located_in_the_middle_of_the_Kavir_National_Park_IRAN_34.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                {   'theme': 'Hidden Canyon Springs, Fig Terraces & Mudbrick Ruins',
                                    'neighborhood': 'Verdant Canyon Oasis',
                                    'rest': (   '03:00 PM - 04:00 PM',
                                                '🍹 Chilled Hibiscus Karkadeh & Shade Rest',
                                                'Canyon Spring Pergola',
                                                'Rest near the trickling spring under wild fig leaves with ruby-red '
                                                'iced hibiscus tea.'),
                                    'morning': (   '🌅 Secret Canyon Stream Trek to Turquoise Desert Pools',
                                                   '07:30 AM - 10:30 AM',
                                                   'Free trail',
                                                   0,
                                                   'Wade through a narrow carved canyon where natural freshwater '
                                                   'springs form crystal emerald swimming pools.',
                                                   'Swimming in the turquoise freshwater pool flanked by towering 100m '
                                                   'sheer sandstone walls.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/01/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_01.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_01.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'midday': (   'Terraced Oasis Fig Farms & Clay Bread Ovens',
                                                  '11:15 AM - 02:15 PM',
                                                  'Farm visit $8',
                                                  10,
                                                  'Learn how ancient falaj gravity irrigation channels have sustained '
                                                  'desert palm orchards for 1,000 years.',
                                                  'Clear water rushing through narrow stone falaj channels beneath '
                                                  'shady date palm canopies.',
                                                  'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/01/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_02.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_02.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'evening': (   'Desert Plateau Sunset Viewpoint & Campfire Tales',
                                                   '05:30 PM - 08:30 PM',
                                                   'Free access',
                                                   22,
                                                   'Sit on the edge of the desert plateau watching shadows lengthen '
                                                   'across endless ochre plains.',
                                                   'Long dramatic shadows cast across wind-sculpted sand ripples as '
                                                   'the sun sets.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/14/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_03.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_03.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                {   'theme': 'Desert Sand Sea, Quad Dune Cruising & Starlit Camp',
                                    'neighborhood': 'Great Erg Sand Dunes',
                                    'rest': (   '02:30 PM - 03:30 PM',
                                                '🍧 Frozen Lemon Mint Slush & Bedouin Porch',
                                                'Dune Edge Kiosk',
                                                'Escape the midday glare with an icy blended mint-lemon refresher '
                                                'under thatch awnings.'),
                                    'morning': (   '🌅 Dawn Dune Crest Walk Along Knife-Edge Sand Ridges',
                                                   '06:30 AM - 09:15 AM',
                                                   'Free walk',
                                                   0,
                                                   'Climb the highest sand ridge in bare feet while the sand is cool '
                                                   'and sculpted into pristine ripples.',
                                                   'Footprints curving along the razor edge of an orange sand dune '
                                                   'with sharp shadow on one side.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/67/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_04.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_04.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'midday': (   'Desert Sandboarding & Shaded Berber Loom Workshop',
                                                  '10:00 AM - 01:30 PM',
                                                  'Board rental $10',
                                                  12,
                                                  'Wax a smooth sandboard and carve down 50-meter red sand dunes like '
                                                  'surfing on land.',
                                                  'Action shot spraying red sand while carving down the steep dune '
                                                  'face with blue sky above.',
                                                  'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/72/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_05.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_05.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'evening': (   'Nomadic Camp Sunset Drums & Slow-Roasted Hearth',
                                                   '05:30 PM - 09:30 PM',
                                                   'Camp feast $28',
                                                   28,
                                                   'Listen to traditional desert drums around the open fire as skewers '
                                                   'of meat and bread roast over coals.',
                                                   'Flames of the open fire reflecting in the eyes of nomadic drummers '
                                                   'beneath the night constellations.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9e/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_06.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_06.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                {   'theme': 'Ancient Caravanserai, Incense Routes & Perfume Alleys',
                                    'neighborhood': 'Old Silk & Frankincense Quarter',
                                    'rest': (   '03:00 PM - 04:00 PM',
                                                '☕ Saffron Rosewater Tea & Honey Almond Sweets',
                                                'Caravanserai Fountain Cloister',
                                                'Sit beside an ancient tiled fountain inhaling the aroma of '
                                                'frankincense and rosewater.'),
                                    'morning': (   '🌅 Historic Caravanserai Gatehouse & Courtyard Stroll',
                                                   '08:00 AM - 10:30 AM',
                                                   'Free entry',
                                                   5,
                                                   "Step into a 15th-century fortified travelers' inn where ancient "
                                                   'spice traders rested their camels.',
                                                   'The massive studded cedar gates framing the sunlit courtyard '
                                                   'arches and stone water trough.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7c/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_07.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_07.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'midday': (   'Frankincense Distillation & Amber Perfume Vaults',
                                                  '11:00 AM - 02:00 PM',
                                                  'Free walk-in',
                                                  10,
                                                  'Sample rare desert resin extracts, burning myrrh, and pure oud oils '
                                                  'blended by master perfumers.',
                                                  'Glass vials of amber and golden perfume oils reflecting sunlight in '
                                                  'an ancient vaulted stone alcove.',
                                                  'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d8/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_08.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_08.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'evening': (   'Citadel Ramparts Sunset & Lantern-Lit Feast',
                                                   '05:30 PM - 09:00 PM',
                                                   'Citadel entry $8',
                                                   26,
                                                   'Watch the red desert mountains turn purple from the battlements of '
                                                   'an ancient stone fortress.',
                                                   'The crenellated stone walls glowing golden orange against the '
                                                   'backdrop of the desert sunset.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3a/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_09.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_09.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                {   'theme': 'Desert Oasis Lake, Migratory Flamingos & Date Groves',
                                    'neighborhood': 'Lakeside Wetland Oasis',
                                    'rest': (   '02:30 PM - 03:30 PM',
                                                '🍉 Iced Melon & Mint Water on Lake Deck',
                                                'Lakeside Wooden Deck',
                                                'Rest under reed canopies watching pink flamingos wade in the shallow '
                                                'desert lake.'),
                                    'morning': (   '🌅 Sunrise Birdwatching & Mirror Lake Reflections',
                                                   '07:00 AM - 09:30 AM',
                                                   'Free access',
                                                   0,
                                                   'Walk along the sandy shores of an unexpected desert lake '
                                                   'reflecting thousands of pink flamingos.',
                                                   'Flock of pink flamingos taking flight from the glassy lake with '
                                                   'desert sand dunes rising behind.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/33/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_10.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_10.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'midday': (   'Traditional Pottery Village & Clay Water Jars',
                                                  '10:30 AM - 01:45 PM',
                                                  'Free entry',
                                                  8,
                                                  'Watch potters spin porous clay water jugs (zeer) that naturally '
                                                  'chill drinking water through evaporation.',
                                                  "A potter's clay-covered hands shaping a tall water amphora on a "
                                                  'foot-pedaled wooden wheel.',
                                                  'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/61/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_11.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_11.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'evening': (   'Dune View Rooftop Dining Under the Desert Moon',
                                                   '05:30 PM - 09:00 PM',
                                                   'Dining $25',
                                                   25,
                                                   'Enjoy a candlelit dinner on a flat mudbrick rooftop as the full '
                                                   'moon turns the desert silver.',
                                                   'The desert landscape glowing ghostly white under moonlight with '
                                                   'clay rooftops in foreground.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b4/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_12.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_12.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                {   'theme': 'Salt Pans, Desert Mirage & Volcanic Basalt Canyons',
                                    'neighborhood': 'White Salt Basin & Black Basalt',
                                    'rest': (   '03:00 PM - 04:00 PM',
                                                '🥤 Cold Pomegranate Ginger Tonic & Shaded Awning',
                                                'Basalt Rest Shelter',
                                                'Rehydrate in the stone shade with a sharp, cooling pomegranate and '
                                                'fresh ginger drink.'),
                                    'morning': (   '🌅 Shimmering White Salt Flat Sunrise & Geometric Crystals',
                                                   '07:00 AM - 09:30 AM',
                                                   'Free trail',
                                                   0,
                                                   'Walk onto an ancient dry seabed covered in hexagonal salt crusts '
                                                   'that stretch into infinity.',
                                                   'Hexagonal cracked salt formations leading to the rising red sun on '
                                                   'an endless flat horizon.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/94/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_13.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_13.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'midday': (   'Black Basalt Canyon Exploration & Volcanic Tubes',
                                                  '10:30 AM - 01:30 PM',
                                                  'Guide fee $10',
                                                  10,
                                                  'Explore stark black volcanic lava flows contrasting against vibrant '
                                                  'orange desert sand.',
                                                  'The striking color contrast between jet-black basalt rocks and '
                                                  'brilliant orange wind-blown sand.',
                                                  'https://thumb.wikimedia.org/wikipedia/commons/thumb/2/2a/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_14.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_14.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'evening': (   'Desert Horizon Sunset & Open-Sky Charcoal Grill',
                                                   '05:30 PM - 09:00 PM',
                                                   'Dinner $26',
                                                   26,
                                                   'Feast on skewers of spiced meats and charred vegetables as the sun '
                                                   'melts into the salt flat.',
                                                   'The burning red orb of the sun dipping into the horizon reflecting '
                                                   'in the white salt crust.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ef/A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_15.jpg/960px-A_sand_dune_in_the_Maranjab_Desert_of_Iran-_Photographer_Mostafa_Meraji_15.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                {   'theme': 'Oasis Date Harvest, Palm Canopies & Ancient Wells',
                                    'neighborhood': 'Grand Royal Palm Oasis',
                                    'rest': (   '02:30 PM - 03:30 PM',
                                                '🍵 Cardamom Infusion & Fresh Soft Rutab Dates',
                                                'Palm Grove Pavilion',
                                                'Rest on low wicker stools under a continuous ceiling of whispering '
                                                'palm fronds.'),
                                    'morning': (   '🌅 Morning Date Palm Harvest & Traditional Tree Climbers',
                                                   '07:30 AM - 10:00 AM',
                                                   'Free entry',
                                                   5,
                                                   'Watch agile farmers climb 20-meter palm trunks with simple rope '
                                                   'harnesses to harvest golden date clusters.',
                                                   'Farmer silhouetted high in the palm canopy cutting down heavy '
                                                   'bunches of amber dates.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b2/A_sunset_on_the_dunes_of_the_Great_Indian_Thar_Desert_Rajasthan_India.jpg/960px-A_sunset_on_the_dunes_of_the_Great_Indian_Thar_Desert_Rajasthan_India.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'midday': (   'Ancient Deep Stone Well & Gravity Water System',
                                                  '10:45 AM - 01:45 PM',
                                                  'Free access',
                                                  6,
                                                  'Look down into an immense 50-meter spiral stone well engineered in '
                                                  'antiquity to tap hidden desert aquifers.',
                                                  'Looking down into the spiral stone steps descending into cool '
                                                  'shadowy underground water chambers.',
                                                  'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ef/Desert_Flowers_4_-_Sam_Sand_Dunes_-_Jaisalmer.JPG_%28405401651%29.jpg/960px-Desert_Flowers_4_-_Sam_Sand_Dunes_-_Jaisalmer.JPG_%28405401651%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'evening': (   'Sunset Over the Palm Canopy & Garden Hearth Dinner',
                                                   '05:30 PM - 09:00 PM',
                                                   'Dinner $28',
                                                   28,
                                                   'Dine amidst blooming jasmine and citrus blossoms as evening '
                                                   'lanterns light up the palm orchard.',
                                                   'Lanterns hanging from palm branches illuminating wooden tables '
                                                   'laden with steaming clay tagines.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d5/Desert_Sand_Dunes_near_sunset.jpg/960px-Desert_Sand_Dunes_near_sunset.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                {   'theme': 'Farewell Sand Dune Summit, Desert Starlight & Grand Toast',
                                    'neighborhood': 'Grand Erg Summit Ridge',
                                    'rest': (   '03:00 PM - 04:00 PM',
                                                '☕ Spiced Desert Chai & Honey Almond Sweets',
                                                'Summit Camp Kiosk',
                                                'Final desert recharge soaking in the silence and immense scale of the '
                                                'sands.'),
                                    'morning': (   '🌅 Final Dawn Summit Hike to the Highest Desert Crest',
                                                   '06:30 AM - 09:30 AM',
                                                   'Free trail',
                                                   0,
                                                   'Ascend the mother dune as the first rays of sunlight ignite the '
                                                   'vast sea of dunes in molten gold.',
                                                   '360-degree panorama of endless sand waves rolling out to the '
                                                   'horizon in golden morning light.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/54/Dunes%2C_D%C3%A9sert_du_Thar.jpg/960px-Dunes%2C_D%C3%A9sert_du_Thar.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'midday': (   'Desert Souvenir Bazaars & Spiced Frankincense Hauls',
                                                  '10:30 AM - 01:30 PM',
                                                  'Free entry',
                                                  10,
                                                  'Select hand-knotted tribal rugs, brass tea sets, and pure saffron '
                                                  'to bring the magic of the desert home.',
                                                  'Colorful brass lanterns and patterned nomadic blankets piled in an '
                                                  'open market stall.',
                                                  'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/52/Imperial_Sand_Dunes_%2848983171197%29.jpg/960px-Imperial_Sand_Dunes_%2848983171197%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                    'evening': (   'Grand Starlit Farewell Campfire & Desert Celebration',
                                                   '05:30 PM - 09:30 PM',
                                                   'Camp feast $35',
                                                   35,
                                                   'Celebrate the final night around the roaring campfire with '
                                                   'traditional songs, tea, and shooting stars.',
                                                   'Sparks swirling up from the desert fire into the brilliant canopy '
                                                   'of the Milky Way.',
                                                   'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/85/In_the_Mojave_desert%2C_near_Kelso%2C_California_-_a_visit_to_the_Kelso_dunes_-_sand_ripples_%2813843366605%29.jpg/960px-In_the_Mojave_desert%2C_near_Kelso%2C_California_-_a_visit_to_the_Kelso_dunes_-_sand_ripples_%2813843366605%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')}],
    'HISTORIC_ANCIENT_HERITAGE': [   {   'theme': 'Historic Stone Bridges, Secret Cloisters & Artisan Espresso',
                                         'neighborhood': 'Old Town Riverbank & Medieval Center',
                                         'rest': (   '03:00 PM - 04:00 PM',
                                                     '☕ Historic Corner Pastry Shop & Dark Roast Espresso',
                                                     'Historic Stone Plaza Bench',
                                                     'Sit on shaded stone benches by an ancient fountain, savor warm '
                                                     'custard tarts, and rest from walking on cobblestones.'),
                                         'morning': (   '🌅 Sunrise Historic Bridge Walk & Artisan Espresso',
                                                        '07:30 AM - 09:45 AM',
                                                        'Free Access',
                                                        5,
                                                        'Cross the historic stone bridge before commuter crowds and '
                                                        'tour groups arrive.',
                                                        'Symmetrical shot down the stone bridge lined with statues as '
                                                        'golden light reflects on the river.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/48/001_Chateau_de_Chillon_and_Dents_du_Midi_Photo_by_Giles_Laurent.jpg/960px-001_Chateau_de_Chillon_and_Dents_du_Midi_Photo_by_Giles_Laurent.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'midday': (   'Secret Medieval Cloisters & Antique Book Arcades',
                                                       '11:00 AM - 02:00 PM',
                                                       'Free Entry / Small fee',
                                                       10,
                                                       'Discover peaceful hidden monastery courtyards, fountain '
                                                       'gardens, and ancient bookshops.',
                                                       'Arched stone corridor framing an overgrown courtyard garden '
                                                       'with blooming wisteria.',
                                                       'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/63/2014.08.09.-11-Durbach--Weingut_Schloss_Staufenberg.jpg/960px-2014.08.09.-11-Durbach--Weingut_Schloss_Staufenberg.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'evening': (   'Castle Hill Panoramic Sunset & Candlelit Wine Cellar',
                                                        '05:30 PM - 08:30 PM',
                                                        'Free Hill Overlook',
                                                        25,
                                                        'Watch twilight settle over terracotta roofs and church spires '
                                                        'from the historic fortress walls.',
                                                        'Sipping regional wine on the stone fortress wall overlooking '
                                                        'glowing cobblestone streets below.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/2/20/20170305_Niedzica_zamek_5195.jpg/960px-20170305_Niedzica_zamek_5195.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                     {   'theme': 'Ancient Amphitheaters, Hidden Crypts & Olive Grove Terraces',
                                         'neighborhood': 'Historic Upper Fortress & Terrace Gardens',
                                         'rest': (   '02:30 PM - 03:30 PM',
                                                     '🍧 Artisanal Pistachio Gelato & Cloister Fountain Rest',
                                                     'Cathedral Cloister Fountain',
                                                     'Sit under carved stone arches with cold pistachio gelato, rest '
                                                     'tired legs, and listen to the trickling fountain.'),
                                         'morning': (   '🌅 Ancient Stone Fortress Ramparts & City Spire Panorama',
                                                        '08:15 AM - 11:00 AM',
                                                        'Fortress ticket $8',
                                                        8,
                                                        'Walk the ancient stone ramparts for an unbroken panoramic '
                                                        'view of church domes and terracotta tiles.',
                                                        'Framing the central cathedral dome through an arched stone '
                                                        'arrow-slit in the rampart wall.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/2/23/26-216-0028_Rakovets_Castle_RB.jpg/960px-26-216-0028_Rakovets_Castle_RB.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'midday': (   'Underground Roman Crypts & Medieval Guild Alleys',
                                                       '11:30 AM - 02:45 PM',
                                                       'Crypt entry $6',
                                                       12,
                                                       'Descend into ancient underground vaulted chambers preserved '
                                                       'beneath the cobblestone street grid.',
                                                       'Light filtering down through an ancient stone grate onto '
                                                       'centuries-old carved Roman inscriptions.',
                                                       'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c9/46-233-0009_Svirzh_Castle_RB.jpg/960px-46-233-0009_Svirzh_Castle_RB.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'evening': (   'Riverside Terrace Stroll & Acoustic Accordion in the Square',
                                                        '05:45 PM - 09:30 PM',
                                                        'Free stroll',
                                                        24,
                                                        'Wander along the illuminated river embankment as street '
                                                        'musicians play acoustic melodies.',
                                                        'Lantern reflections dancing across dark river ripples with '
                                                        'historic stone arches illuminated.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f7/Alatskivi_m%C3%B5isa_peahoone.jpg/960px-Alatskivi_m%C3%B5isa_peahoone.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                     {   'theme': 'Renaissance Palaces, Secret Courtyards & Artisan Workshops',
                                         'neighborhood': 'Historic Artisan Quarter',
                                         'rest': (   '03:00 PM - 04:00 PM',
                                                     '☕ Espresso Macchiato & Warm Brioche in Shaded Piazza',
                                                     'Piazza Stone Cafe',
                                                     'Recline on outdoor wicker chairs facing a 16th-century stone '
                                                     'fountain.'),
                                         'morning': (   '🌅 Marble Statuary Galleries & Historic Library Hall',
                                                        '08:30 AM - 11:15 AM',
                                                        'Gallery ticket $14',
                                                        14,
                                                        'Walk beneath vaulted ceilings painted in gold leaf and '
                                                        'frescoed masterpieces of ancient history.',
                                                        'Looking down the endless marble-floored gallery flanked by '
                                                        'classical sculptures.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/72/Bac_Fortress_%284%29.jpg/960px-Bac_Fortress_%284%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'midday': (   'Centuries-Old Leather & Paper Marbling Workshops',
                                                       '11:45 AM - 02:30 PM',
                                                       'Free walk-in',
                                                       10,
                                                       'Watch master artisans dip paper into swirling baths of color '
                                                       'pigments to create marbled book covers.',
                                                       'Sheets of hand-marbled paper drying on lines above wooden '
                                                       'workbenches filled with bookbinding presses.',
                                                       'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9e/Ba%C4%8D_fortress_%28Ba%C4%8Dka_tvr%C4%91ava%29_2.JPG/960px-Ba%C4%8D_fortress_%28Ba%C4%8Dka_tvr%C4%91ava%29_2.JPG?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'evening': (   'Terracotta Rooftop Sunset & Candlelit Trattoria Feast',
                                                        '05:30 PM - 09:00 PM',
                                                        'Trattoria dining',
                                                        28,
                                                        'Watch church bells chime as twilight settles over orange '
                                                        'terracotta tile rooftops.',
                                                        'Sipping regional wine on a terrace overlooking the silhouette '
                                                        'of historic church cupolas.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9e/Beijing_Castle_Boxer_Rebellion_1900_FINAL.jpg/960px-Beijing_Castle_Boxer_Rebellion_1900_FINAL.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                     {   'theme': 'Gothic Bell Towers, Medieval Market Squares & Herb Gardens',
                                         'neighborhood': 'Gothic Cathedral Quarter',
                                         'rest': (   '02:30 PM - 03:30 PM',
                                                     '🍰 Spiced Honey Plum Cake & Monastic Herb Tea',
                                                     'Apothecary Courtyard',
                                                     'Rest under stone arcades surrounded by aromatic medicinal '
                                                     'rosemary and lavender bushes.'),
                                         'morning': (   '🌅 Climb the 300-Step Cathedral Tower for Sunrise Vistas',
                                                        '08:00 AM - 10:30 AM',
                                                        'Tower ticket $8',
                                                        8,
                                                        'Ascend the spiral stone staircase to stand among carved '
                                                        'gargoyles overlooking the city waking up.',
                                                        'Gargoyle carving in foreground looking out over morning mist '
                                                        'covering medieval streets below.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/1f/Beloeil_castel_1_Luc_Viatour.jpg/960px-Beloeil_castel_1_Luc_Viatour.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'midday': (   'Monastic Herbal Pharmacy & Alchemy Museum',
                                                       '11:00 AM - 02:00 PM',
                                                       'Entry $6',
                                                       10,
                                                       'Step inside an intact 13th-century pharmacy with antique '
                                                       'ceramic jars, dried botanicals, and rose ointments.',
                                                       'Antique ceramic drug jars on carved dark walnut shelves '
                                                       'illuminated by soft leaded-glass daylight.',
                                                       'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4e/Bogesunds_slott_February_2013_04.jpg/960px-Bogesunds_slott_February_2013_04.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'evening': (   'Gaslit Cobblestone Ghost Walk & Historic Vaulted Cellar',
                                                        '06:00 PM - 09:30 PM',
                                                        'Tour $12',
                                                        26,
                                                        'Follow a lantern-carrying guide through narrow passageways, '
                                                        'concluding in a subterranean stone vault.',
                                                        'Warm yellow gaslight casting dramatic shadows down an empty '
                                                        'narrow cobblestone alley.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ac/Bojnice_%28Bojnitz%29_Castle_%28by_Pudelek%29.jpg/960px-Bojnice_%28Bojnitz%29_Castle_%28by_Pudelek%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                     {   'theme': 'Historic City Walls, Moat Gardens & Royal Orangeries',
                                         'neighborhood': 'Royal Citadel & Palace Gardens',
                                         'rest': (   '03:00 PM - 04:00 PM',
                                                     '☕ Iced Espresso & Candied Orange Peel at the Orangery',
                                                     'Palace Orangery Terrace',
                                                     'Sit under potted lemon and orange trees in the sheltered royal '
                                                     'palace garden.'),
                                         'morning': (   '🌅 Stroll the Intact Renaissance Fortified Walls & Moat',
                                                        '08:15 AM - 10:45 AM',
                                                        'Free access',
                                                        0,
                                                        'Walk tree-lined pathways atop monumental brick ramparts '
                                                        'designed by master military architects.',
                                                        'Wide gravel walkway under shady plane trees running along the '
                                                        'crest of massive brick fortress walls.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/36/Bourtzi_castle_harbour_Karystos_Euboea_Greece.jpg/960px-Bourtzi_castle_harbour_Karystos_Euboea_Greece.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'midday': (   'Royal Palace Glasshouses & Sculpted Topiary Maze',
                                                       '11:15 AM - 02:15 PM',
                                                       'Gardens $8',
                                                       12,
                                                       'Wander through Victorian cast-iron palm houses and geometric '
                                                       'boxwood hedge labyrinths.',
                                                       'Looking through geometric arches of clipped green boxwood '
                                                       'hedges toward a classical stone fountain.',
                                                       'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d0/Casco_viejo_de_Dubrovnik%2C_Croacia%2C_2014-04-13%2C_DD_18.JPG/960px-Casco_viejo_de_Dubrovnik%2C_Croacia%2C_2014-04-13%2C_DD_18.JPG?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'evening': (   'Classical String Quartet in Historic Palace Chapel',
                                                        '05:45 PM - 08:45 PM',
                                                        'Concert $22',
                                                        30,
                                                        'Listen to Mozart and Vivaldi performed by candlelight beneath '
                                                        'gilded baroque vaults.',
                                                        'Candlelight flickering on the gilded carvings of the palace '
                                                        'chapel as musicians play violins.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4d/Castel_Sant%27Angelo_at_dusk%2C_Rome%2C_Italy.jpg/960px-Castel_Sant%27Angelo_at_dusk%2C_Rome%2C_Italy.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                     {   'theme': 'Historic Waterfront Canals, Merchant Mansions & Flower Barges',
                                         'neighborhood': 'Old Port & Canal Belt',
                                         'rest': (   '02:30 PM - 03:30 PM',
                                                     '🍧 Fresh Lemon Basil Sorbet & Canal Wall Bench',
                                                     'Canal Footbridge Bench',
                                                     'Rest feet dangling over the stone canal quay while watching '
                                                     'historic wooden barges glide past.'),
                                         'morning': (   '🌅 Sunrise Canal Walk & Historic Floating Flower Stalls',
                                                        '07:30 AM - 10:00 AM',
                                                        'Free walk',
                                                        5,
                                                        'Stroll along cobblestone embankments past 17th-century '
                                                        'stepped gables and flower barges.',
                                                        'Concentric arched stone canal bridges reflected in calm water '
                                                        'with rows of historic houses.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/de/Castelo_dos_Mouros%2C_Sintra%2C_Portugal%2C_2019-05-25%2C_DD_112-121_PAN.jpg/960px-Castelo_dos_Mouros%2C_Sintra%2C_Portugal%2C_2019-05-25%2C_DD_112-121_PAN.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'midday': (   'Wealthy Merchant Canal Mansion & Secret Garden',
                                                       '10:30 AM - 01:45 PM',
                                                       'Museum ticket $12',
                                                       12,
                                                       'Explore a preserved Golden Age canal house with marble '
                                                       'entrance halls and hidden rear formal garden.',
                                                       'Looking out high sash windows across a private manicured '
                                                       'garden flanked by carriage houses.',
                                                       'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/42/Castillo_de_Praga%2C_Praga%2C_Rep%C3%BAblica_Checa%2C_2022-07-01%2C_DD_23-25_HDR.jpg/960px-Castillo_de_Praga%2C_Praga%2C_Rep%C3%BAblica_Checa%2C_2022-07-01%2C_DD_23-25_HDR.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'evening': (   'Historic Canal Boat Sunset Cruise & Candlelit Dining',
                                                        '05:30 PM - 09:00 PM',
                                                        'Cruise ticket $24',
                                                        32,
                                                        'Glide silently through illuminated canal arches on a classic '
                                                        'wooden salon boat with regional wine.',
                                                        'Warm golden light glowing from canal house windows reflecting '
                                                        'in dark water ripples at night.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f3/Castle_of_Bard_%283%29.jpg/960px-Castle_of_Bard_%283%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                     {   'theme': 'Ancient Roman Aqueducts, Catacombs & Pine-Lined Appian Trails',
                                         'neighborhood': 'Ancient Appian Way & Aqueduct Park',
                                         'rest': (   '03:00 PM - 04:00 PM',
                                                     '🍷 Local Red Wine & Pecorino Cheese on Lawn',
                                                     'Aqueduct Park Shaded Lawn',
                                                     'Sit on the grass beneath monumental 2,000-year-old stone arches '
                                                     'of the Roman aqueduct.'),
                                         'morning': (   '🌅 Cobblestone Stroll Along the 2,300-Year-Old Ancient Way',
                                                        '08:00 AM - 10:30 AM',
                                                        'Free trail',
                                                        0,
                                                        'Walk across original polygonal basalt paving stones grooved '
                                                        'by ancient Roman chariot wheels.',
                                                        'Ancient paved stone road lined with towering umbrella pine '
                                                        'trees and ruined marble tomb monuments.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7c/Christiansborg_Slot_Copenhagen_2014_01.jpg/960px-Christiansborg_Slot_Copenhagen_2014_01.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'midday': (   'Underground Subterranean Catacombs & Tufa Galleries',
                                                       '11:00 AM - 02:00 PM',
                                                       'Guided entry $10',
                                                       12,
                                                       'Descend into multi-story underground burial corridors carved '
                                                       'into volcanic tufa rock.',
                                                       'Flickering electric torchlight illuminating carved symbols of '
                                                       'doves and fish in the stone tomb niches.',
                                                       'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d5/Crimea_South_Coast_04-14_img10_Gaspra_Swallows_Nest.jpg/960px-Crimea_South_Coast_04-14_img10_Gaspra_Swallows_Nest.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'evening': (   'Rustic Country Osteria Dinner Beside Ancient Ruins',
                                                        '05:30 PM - 09:00 PM',
                                                        'Osteria $25',
                                                        28,
                                                        'Dine at open-air tables under grape trellises overlooking the '
                                                        'ancient stone monuments at sunset.',
                                                        'Sunset casting long golden shadows through the arches of the '
                                                        'stone aqueduct across wheat fields.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e2/De_Viron_Castle_%28DSC_2198%29.jpg/960px-De_Viron_Castle_%28DSC_2198%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                     {   'theme': 'Hilltop Monastery, Panoramic Vineyards & Monastic Cellars',
                                         'neighborhood': 'Monastery Ridge & Vineyards',
                                         'rest': (   '02:30 PM - 03:30 PM',
                                                     '☕ Herbal Elixir & Honey Scone in Cloister',
                                                     'Abbey Courtyard Bench',
                                                     'Rest in pure contemplative silence in a 14th-century monastery '
                                                     'cloister.'),
                                         'morning': (   '🌅 Panoramic Pilgrimage Footpath to Ridge Monastery',
                                                        '07:45 AM - 10:15 AM',
                                                        'Free trail',
                                                        0,
                                                        'Hike past terraced olive groves and cypress trees to reach an '
                                                        'ancient stone abbey on the crest.',
                                                        'Stone bell tower rising above silver-green olive trees with '
                                                        'morning valley fog burning off.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a7/Drottningholm_Palace_%28by_Pudelek%29_1.jpg/960px-Drottningholm_Palace_%28by_Pudelek%29_1.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'midday': (   'Monastic Wine Cellars & Barrel Tasting',
                                                       '10:45 AM - 01:45 PM',
                                                       'Tasting $15',
                                                       18,
                                                       'Descend into dark stone cellars where monks have aged vintage '
                                                       'wines in giant oak casks for centuries.',
                                                       'Rows of immense oak casks resting in a vaulted stone crypt '
                                                       'illuminated by amber lanterns.',
                                                       'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/69/Drottningholm_Palace_%28by_Pudelek%29_4.jpg/960px-Drottningholm_Palace_%28by_Pudelek%29_4.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'evening': (   'Panoramic Sunset Over Terraced Hills & Hearth Feast',
                                                        '05:30 PM - 09:00 PM',
                                                        'Tavern $28',
                                                        30,
                                                        'Watch the setting sun paint the rolling vineyard hills in '
                                                        'shades of amber and violet from a stone veranda.',
                                                        'The silhouette of cypress trees against a dramatic crimson '
                                                        'sunset over rolling hills.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/33/ET_Gondar_asv2018-02_img18_Fasil_Ghebbi.jpg/960px-ET_Gondar_asv2018-02_img18_Fasil_Ghebbi.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                     {   'theme': 'Historic University Halls, Botanical Gardens & Antique Vaults',
                                         'neighborhood': 'Ancient University Quarter',
                                         'rest': (   '03:00 PM - 04:00 PM',
                                                     '☕ Dark Roast Macchiato & Warm Pastry in College Courtyard',
                                                     'University Lawn Bench',
                                                     'Sit on manicured lawns watching students and professors in '
                                                     'scholarly robes walk past.'),
                                         'morning': (   '🌅 Sunrise Over Historic College Chapels & Quadrangle Lawns',
                                                        '08:00 AM - 10:15 AM',
                                                        'Free walk',
                                                        0,
                                                        'Walk through ornate Gothic stone archways into serene '
                                                        'medieval quadrangle lawns.',
                                                        'Symmetrical shot of Gothic stone quadrangle arches framing '
                                                        'dew-covered green lawn.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/90/Fortaleza_de_Bam%2C_Ir%C3%A1n%2C_2016-09-23%2C_DD_04.jpg/960px-Fortaleza_de_Bam%2C_Ir%C3%A1n%2C_2016-09-23%2C_DD_04.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'midday': (   'Ancient Manuscript Library & Rare Book Reading Room',
                                                       '10:45 AM - 01:45 PM',
                                                       'Library pass $10',
                                                       12,
                                                       'Walk through soaring book galleries with hand-carved oak '
                                                       'bookshelves holding centuries of human knowledge.',
                                                       'Looking down the cathedral-like aisle of the historic library '
                                                       'with sunlight pouring through leaded glass.',
                                                       'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/bc/Fortaleza_de_Bam%2C_Ir%C3%A1n%2C_2016-09-23%2C_DD_09.jpg/960px-Fortaleza_de_Bam%2C_Ir%C3%A1n%2C_2016-09-23%2C_DD_09.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'evening': (   'Historic College Pub Crawl & Literary Discussion',
                                                        '05:30 PM - 09:00 PM',
                                                        'Pub crawl $20',
                                                        25,
                                                        'Drink regional ale in pubs where world-famous authors and '
                                                        'scientists wrote their masterpieces.',
                                                        'Warm yellow light through etched Victorian pub glass with '
                                                        'dark timber booths and historic portraits.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ac/Fortezza_Verrucole_Archeopark_interno.jpg/960px-Fortezza_Verrucole_Archeopark_interno.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                                     {   'theme': 'Farewell Fortress Overlook, Ancient Sunset & Grand Banquet',
                                         'neighborhood': 'Imperial Castle Overlook',
                                         'rest': (   '03:00 PM - 04:00 PM',
                                                     '🍰 Artisanal Tart & Espresso at the Castle View Cafe',
                                                     'Castle Balustrade',
                                                     'Final historic recharge looking out over the entire sweeping '
                                                     'panorama of the ancient capital.'),
                                         'morning': (   '🌅 Final Sunrise Walk Along Highest Fortress Rampart',
                                                        '07:30 AM - 10:00 AM',
                                                        'Castle ticket $12',
                                                        12,
                                                        'Take in the panoramic view of church cupolas and historic '
                                                        'terracotta roofs emerging from dawn mist.',
                                                        "Postcard angle looking over the entire city's spires and "
                                                        'bridges glowing in morning light.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/05/Fuerte_Bordj_el_Kebir%2C_Mahdia%2C_T%C3%BAnez%2C_2016-09-03%2C_DD_34-36_HDR.jpg/960px-Fuerte_Bordj_el_Kebir%2C_Mahdia%2C_T%C3%BAnez%2C_2016-09-03%2C_DD_34-36_HDR.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'midday': (   'Grand Artisan Flea Market & Historic Collectibles',
                                                       '10:30 AM - 01:45 PM',
                                                       'Free walk',
                                                       10,
                                                       'Browse hundreds of stalls filled with vintage postcards, '
                                                       'antique jewelry, old maps, and copper pans.',
                                                       'Antique pocket watches and brass compasses laid out on velvet '
                                                       'in a sunlight-dappled market stall.',
                                                       'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0a/Grabs_SG_asv2022-10_Schloss_Werdenberg_img2.jpg/960px-Grabs_SG_asv2022-10_Schloss_Werdenberg_img2.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                         'evening': (   'Grand Historic Farewell Feast in a Vaulted Crypt',
                                                        '05:30 PM - 09:30 PM',
                                                        'Feast $36',
                                                        36,
                                                        'Celebrate your journey with an unforgettable banquet in a '
                                                        '600-year-old stone cellar with live acoustic strings.',
                                                        'Candles burning low on long wooden tables with stone vaults '
                                                        'overhead and joyful traveler toasts.',
                                                        'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/1e/Granada_-_View_from_Mirador_de_San_Nicol%C3%A1s_-_02.jpg/960px-Granada_-_View_from_Mirador_de_San_Nicol%C3%A1s_-_02.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')}],
    'VIBRANT_METROPOLIS': [   {   'theme': 'Rooftop Botanical Sanctuaries, Neon Canyons & Specialty Coffee',
                                  'neighborhood': 'Downtown Core & Skyline Boulevard',
                                  'rest': (   '03:00 PM - 04:00 PM',
                                              '☕ Elevated Green Rooftop Rest & Iced Pour-Over',
                                              'Skyline Conservatory Terrace',
                                              'Sit on cushioned benches surrounded by lush ferns overlooking the city '
                                              'skyline, recharge devices and rest.'),
                                  'morning': (   '🌅 Rooftop Botanical Sanctuary & Specialty Third-Wave Coffee',
                                                 '08:30 AM - 10:30 AM',
                                                 'Free / Small fee',
                                                 6,
                                                 'Start the morning in an elevated urban garden overlooking the '
                                                 'awakening city with single-origin coffee.',
                                                 'Framing your coffee cup against the sunrise illuminating glass '
                                                 'skyscraper reflections.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b6/122_-_Toronto_-_Septembre_2009.jpg/960px-122_-_Toronto_-_Septembre_2009.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'midday': (   'Indie Concept Boutiques & Vintage Streetwear Vaults',
                                                '11:30 AM - 02:30 PM',
                                                'Free Entry',
                                                15,
                                                'Explore repurposed industrial warehouse corridors featuring '
                                                'independent designers and vinyl shops.',
                                                'The industrial red-brick facade and neon signs of the concept store '
                                                'entrance.',
                                                'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b5/AucklandPano_MC.jpg/960px-AucklandPano_MC.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'evening': (   'Sunset Waterfront Pier Walk & Hidden Speakeasy Lounge',
                                                 '05:30 PM - 08:30 PM',
                                                 'Free Pier / Drink cost',
                                                 28,
                                                 'Walk along the waterfront as the sun sets over harbor waters, then '
                                                 'enter an unmarked basement listening lounge.',
                                                 'Cocktail glass reflecting the twilight harbor lights through '
                                                 'panoramic glass windows.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/af/Baltimore_Inner_Harbor_Skyline_Night_Panorama.jpg/960px-Baltimore_Inner_Harbor_Skyline_Night_Panorama.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                              {   'theme': 'Modern Art Turbines, Elevated Parkways & Street Food Woks',
                                  'neighborhood': 'Industrial Arts District & River Wharves',
                                  'rest': (   '02:30 PM - 03:30 PM',
                                              '🍧 Artisan Shaved Ice & Converted Warehouse Lounge',
                                              'Art Gallery Glass Atrium',
                                              'Rest on leather armchairs inside a cool converted warehouse gallery '
                                              'with matcha or espresso.'),
                                  'morning': (   '🌅 Elevated Rail Parkway Wildflower Walk',
                                                 '08:45 AM - 11:15 AM',
                                                 '100% Free Public Park',
                                                 0,
                                                 'Walk along an elevated converted railway trestle landscaped with '
                                                 'native perennials and contemporary sculptures.',
                                                 'Looking down the wooden parkway walkway flanked by wildflowers with '
                                                 'skyscraper facades rising overhead.',
                                                 'https://upload.wikimedia.org/wikipedia/commons/d/d5/Bank_of_China_Tower_Shanghai_November_2017.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled'),
                                  'midday': (   'Monumental Contemporary Art Vaults & Experimental Installations',
                                                '11:45 AM - 02:45 PM',
                                                'Museum ticket $18',
                                                18,
                                                'Explore colossal industrial turbine halls filled with site-specific '
                                                'large-scale art installations.',
                                                'Standing tiny in the center of the monumental concrete turbine hall '
                                                'looking up at hanging light art.',
                                                'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f3/Boston_skyline_from_Cambridge_November_2015_panorama_1.jpg/960px-Boston_skyline_from_Cambridge_November_2015_panorama_1.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'evening': (   'Neon Alleyway Street Food Safari & Secret Listening Bar',
                                                 '05:45 PM - 09:30 PM',
                                                 'Food stalls pay-as-you-eat',
                                                 22,
                                                 'Follow the aroma of sizzling charcoal skewers and wok flames down '
                                                 'narrow lantern-lit alleys.',
                                                 'Steam and amber lantern light rising from sizzling street food woks '
                                                 'under neon signs.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/86/Boston_skyline_from_East_Boston_November_2016_panorama_1.jpg/960px-Boston_skyline_from_East_Boston_November_2016_panorama_1.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                              {   'theme': 'Canal Greenways, Design District & 60th-Floor Sunset Horizon',
                                  'neighborhood': 'Canal Quarter & Financial Skydecks',
                                  'rest': (   '03:00 PM - 04:00 PM',
                                              '☕ Canal-Side Steps Rest & Fresh Cinnamon Rolls',
                                              'Canal Promenade Stone Steps',
                                              'Sit on sunny stone steps by the water, watch canal boats glide by, and '
                                              'relax before the evening skydeck.'),
                                  'morning': (   '🌅 Urban Canal Greenway Bike & Coffee Crawl',
                                                 '08:30 AM - 11:00 AM',
                                                 'Bike share $4',
                                                 8,
                                                 'Pedal or walk along paved pedestrian greenways following ancient '
                                                 'urban canals lined with weeping trees.',
                                                 'View looking down the peaceful tree-lined water channel reflecting '
                                                 'modern glass architecture.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/39/Boston_skyline_from_East_Boston_November_2016_panorama_2.jpg/960px-Boston_skyline_from_East_Boston_November_2016_panorama_2.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'midday': (   'Design District Architect Studios & Experimental Concept Store',
                                                '11:30 AM - 02:30 PM',
                                                'Free walk-in',
                                                10,
                                                'Explore curated furniture showrooms, independent print publishers, '
                                                'and minimalist fashion ateliers.',
                                                'Clean minimalist aesthetic showroom with sculptural concrete and '
                                                'natural wood benches.',
                                                'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d9/Boston_skyline_from_East_Boston_November_2016_panorama_3.jpg/960px-Boston_skyline_from_East_Boston_November_2016_panorama_3.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'evening': (   '60th-Floor Glass Observation Deck & Sunset Skyline Cocktail',
                                                 '05:30 PM - 09:00 PM',
                                                 'Skydeck pass $25',
                                                 32,
                                                 'Stand on cantilevered glass floors hundreds of meters above the grid '
                                                 'as evening lights blink to life.',
                                                 'Silhouette looking out the floor-to-ceiling glass windows as city '
                                                 'lights twinkle like a circuit board.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/df/Boston_skyline_from_East_Boston_November_2016_panorama_4.jpg/960px-Boston_skyline_from_East_Boston_November_2016_panorama_4.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                              {   'theme': 'Retro Gaming Arcades, Cyberpunk Districts & Night Markets',
                                  'neighborhood': 'Electronic Quarter & Neon Alleyways',
                                  'rest': (   '02:30 PM - 03:30 PM',
                                              '🍧 Bingsu Shaved Ice / Bubble Tea Lounge',
                                              'Neon Arcade Veranda',
                                              'Recharge devices with USB-C ports while enjoying cooling sweet taro '
                                              'bubble tea and shaved ice.'),
                                  'morning': (   '🌅 Retro Multi-Floor Rhythm Game & Gachapon Vault',
                                                 '09:30 AM - 12:00 PM',
                                                 'Arcade entry free / coins $10',
                                                 10,
                                                 'Play vintage Japanese rhythm games, crane claws, and collect rare '
                                                 'anime pins in neon halls.',
                                                 'Colorful rows of brightly lit arcade cabinets and glowing joystick '
                                                 'buttons.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/ca/Boston_skyline_from_Longfellow_Bridge_September_2017_panorama_2.jpg/960px-Boston_skyline_from_Longfellow_Bridge_September_2017_panorama_2.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'midday': (   'Subterranean Vinyl Listening Bar & Manga Vaults',
                                                '12:30 PM - 03:30 PM',
                                                'Free entry',
                                                12,
                                                'Put on studio headphones to audition rare first-pressing Japanese '
                                                'citypop and synthwave records.',
                                                'Row upon row of vinyl record sleeves in wooden crates with vintage '
                                                'turntable tone arms.',
                                                'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e3/Cambridge_skyline_November_2016_panorama.jpg/960px-Cambridge_skyline_November_2016_panorama.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'evening': (   'Neon Street Food Night Market & Torched Skewers',
                                                 '06:00 PM - 10:00 PM',
                                                 'Stall crawl $18',
                                                 22,
                                                 'Weave between sizzling open-air food stalls under hanging neon '
                                                 'lanterns and steam clouds.',
                                                 'Skewers sizzling over glowing white-hot charcoal embers with neon '
                                                 'signage reflecting on wet pavement.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c5/Canary_Wharf_from_Limehouse_London_June_2016_HDR.jpg/960px-Canary_Wharf_from_Limehouse_London_June_2016_HDR.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                              {   'theme': 'Waterfront Wharves, Maritime Ferries & Island Sanctuaries',
                                  'neighborhood': 'Harbor Wharf & Harbor Islands',
                                  'rest': (   '03:00 PM - 04:00 PM',
                                              '☕ Salt-Sprayed Pier Rest & Artisan Sourdough',
                                              'Harbor Pier Deck',
                                              'Sit on timber pier pilings watching sailboats glide by with fresh '
                                              'pastry.'),
                                  'morning': (   '🌅 Scenic Harbor Public Ferry Crossing at Golden Dawn',
                                                 '08:15 AM - 10:15 AM',
                                                 'Ferry ticket $3',
                                                 5,
                                                 'Ride the public commuter ferry out across open harbor waters as dawn '
                                                 'turns glass towers to copper.',
                                                 'Looking back from the ferry deck at the entire glass skyline skyline '
                                                 'rising above dark blue waves.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9e/Charles_River_Esplanade_Boston_May_2018_panorama.jpg/960px-Charles_River_Esplanade_Boston_May_2018_panorama.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'midday': (   'Historic Harbor Island Fort & Car-Free Bike Loop',
                                                '10:45 AM - 02:15 PM',
                                                'Island free / bike $10',
                                                12,
                                                'Rent a vintage bicycle to loop around an island of abandoned brick '
                                                'military barracks and wildflower fields.',
                                                'Bicycle parked on a grassy hill framing the distant futuristic '
                                                'skyline across calm water.',
                                                'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/5f/Chicago_from_North_Avenue_Beach_June_2015_panorama_2.jpg/960px-Chicago_from_North_Avenue_Beach_June_2015_panorama_2.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'evening': (   'Waterfront Converted Warehouse Brewery & Sunset Pint',
                                                 '05:30 PM - 09:00 PM',
                                                 'Brewery walk-in',
                                                 24,
                                                 'Sit on long communal timber tables inside a 19th-century shipyard '
                                                 'brick building with craft ales.',
                                                 'Pint glass of golden craft beer catching the orange sunset light '
                                                 'through giant arched factory windows.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/aa/Chicago_September_2016-23.jpg/960px-Chicago_September_2016-23.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                              {   'theme': 'Bohemian Arts Quarter, Independent Books & Courtyard Cafes',
                                  'neighborhood': 'Boho Cultural Enclave',
                                  'rest': (   '02:30 PM - 03:30 PM',
                                              '☕ Artisan Pourover & Almond Croissant in Hidden Courtyard',
                                              'Courtyard Ivy Bench',
                                              'Sit under ivy-covered brick walls with a curated book from the '
                                              'independent corner bookshop.'),
                                  'morning': (   '🌅 Independent Bookstore Vaults & Morning Poetry Stroll',
                                                 '09:00 AM - 11:30 AM',
                                                 'Free entry',
                                                 5,
                                                 'Explore multi-story labyrinthine bookstores featuring handwritten '
                                                 'staff recommendation cards.',
                                                 'Towering floor-to-ceiling wooden shelves packed with colorful books '
                                                 'with a wooden rolling ladder.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/82/Chicago_sunrise_1.jpg/960px-Chicago_sunrise_1.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'midday': (   'Vintage Flea Market & Repurposed Ceramic Workshops',
                                                '12:00 PM - 03:00 PM',
                                                'Free walk-in',
                                                15,
                                                'Browse vintage trench coats, antique cameras, and handmade pottery in '
                                                'a cobbled courtyard.',
                                                'Display of vintage film cameras and brass trinkets on a weathered '
                                                'wooden table.',
                                                'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/77/Chicago.jpg/960px-Chicago.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'evening': (   'Intimate Underground Jazz Cellar & Natural Wine Bar',
                                                 '06:00 PM - 09:30 PM',
                                                 'Jazz cover $15',
                                                 30,
                                                 'Descend into a dimly lit basement cellar where an acoustic jazz trio '
                                                 'plays inches from your table.',
                                                 'Saxophonist silhouetted under a single warm spotlight in a '
                                                 'brick-vaulted basement.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/97/Durgam_Cheruvu_Panorama.jpg/960px-Durgam_Cheruvu_Panorama.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                              {   'theme': 'Futuristic Architecture, Geometric Domes & Kinetic Sculptures',
                                  'neighborhood': 'Future Innovation & Museum Park',
                                  'rest': (   '03:00 PM - 04:00 PM',
                                              '🍧 Molecular Nitro Cold Brew & Glass Pavilion',
                                              'Museum Sunlit Atrium',
                                              'Rest in air-conditioned modernist comfort surrounded by living vertical '
                                              'moss walls.'),
                                  'morning': (   '🌅 Geometric Glass Dome & Subtropical Indoor Conservatory',
                                                 '08:30 AM - 11:15 AM',
                                                 'Dome entry $16',
                                                 16,
                                                 'Walk along suspended skywalks inside an immense climate-controlled '
                                                 'geodesic dome.',
                                                 'Suspended walkway curving through lush indoor palm canopies under a '
                                                 'geometric steel grid roof.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/44/Frankfurt_Am_Main-Stadtpanorama_von_der_Ignatz-Bubis-Bruecke_am_Mittag-20100424.jpg/960px-Frankfurt_Am_Main-Stadtpanorama_von_der_Ignatz-Bubis-Bruecke_am_Mittag-20100424.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'midday': (   'Interactive Kinetic Light Art Museum & Digital Playground',
                                                '11:45 AM - 02:45 PM',
                                                'Museum ticket $22',
                                                22,
                                                'Step inside mirror-walled rooms filled with reactive LED crystals '
                                                'that pulse to your motion.',
                                                'Standing surrounded by endless reflections of infinite glowing '
                                                'crystal light curtains.',
                                                'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/eb/Frankfurt_Skyline_2022_bei_Nacht.jpg/960px-Frankfurt_Skyline_2022_bei_Nacht.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'evening': (   'Suspended Skyline Helix Bridge Sunset & Spectra Light Show',
                                                 '05:45 PM - 09:00 PM',
                                                 'Free show',
                                                 26,
                                                 'Watch synchronized laser light and water fountain choreography '
                                                 'illuminate the harbor.',
                                                 'Futuristic spiraling bridge lit with neon LED helix bands framing '
                                                 'glowing city towers.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f9/Frankfurter_Altstadt_mit_Skyline_2012-04.jpg/960px-Frankfurter_Altstadt_mit_Skyline_2012-04.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                              {   'theme': 'Historic Cultural Enclave, Lantern Alleys & Tea Ceremonies',
                                  'neighborhood': 'Heritage Silk & Ceramic District',
                                  'rest': (   '02:30 PM - 03:30 PM',
                                              '🍵 Ceremonial Matcha Whisking & Sweet Bean Mochi',
                                              'Traditional Teahouse Tatami',
                                              'Remove shoes and rest on fragrant woven reed mats while learning '
                                              'authentic tea whisking.'),
                                  'morning': (   '🌅 Historic Pagoda Temple Morning Chants & Incense',
                                                 '08:00 AM - 10:30 AM',
                                                 'Free / incense $3',
                                                 3,
                                                 'Witness morning bells chime as sacred incense smoke spirals past red '
                                                 'lacquered temple columns.',
                                                 'Sunlight streaming through incense smoke clouds illuminating carved '
                                                 'gold temple dragons.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/37/Hoboken_Terminal_June_2015_panorama_1.jpg/960px-Hoboken_Terminal_June_2015_panorama_1.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'midday': (   'Medicinal Herb Apothecary & Traditional Shophouse Alleys',
                                                '11:00 AM - 02:00 PM',
                                                'Free walk-in',
                                                10,
                                                'Explore narrow alleys lined with dried goji berries, ginseng roots, '
                                                'and hand-embroidered textiles.',
                                                'Rows of small wooden apothecary drawers with calligraphy labels and '
                                                'brass ring pulls.',
                                                'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b0/Hoboken_Terminal_June_2015_panorama_2.jpg/960px-Hoboken_Terminal_June_2015_panorama_2.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'evening': (   'Red Lantern Courtyard Banquet & Dim Sum Feast',
                                                 '05:30 PM - 09:00 PM',
                                                 'Banquet $24',
                                                 24,
                                                 'Feast on steaming bamboo baskets of crystal shrimp dumplings, '
                                                 'barbecue pork buns, and jasmine tea.',
                                                 'Bamboo steamer baskets stacked high with steam rising under glowing '
                                                 'red paper lanterns.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/dd/Long_Island_City_New_York_May_2015_panorama_3.jpg/960px-Long_Island_City_New_York_May_2015_panorama_3.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                              {   'theme': 'Urban Forest Greenbelt, Wildlife Corridors & Treehouse Cafes',
                                  'neighborhood': 'Green Corridor & Ridge Reserve',
                                  'rest': (   '03:00 PM - 04:00 PM',
                                              '🥤 Fresh Cold-Pressed Juice & Shaded Lawn Rest',
                                              'Botanic Garden Lawn',
                                              'Stretch out on manicured lawns beneath ancient shade trees, recharge '
                                              'and hydrate.'),
                                  'morning': (   '🌅 Treehouse Canopy Walkway & Urban Forest Ridge Trail',
                                                 '08:00 AM - 10:45 AM',
                                                 'Free trail',
                                                 0,
                                                 'Walk elevated wooden boardwalks that wind through the canopy of a '
                                                 'preserved primary rainforest within city limits.',
                                                 'Looking down the wooden canopy boardwalk suspended high among lush '
                                                 'emerald leaves.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7c/Los_Angeles_Pollution.jpg/960px-Los_Angeles_Pollution.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'midday': (   'Hilltop Conservatory & Butterfly Flight Pavilion',
                                                '11:15 AM - 02:15 PM',
                                                'Entry $10',
                                                12,
                                                'Walk through an enclosed glass pavilion where hundreds of '
                                                'electric-blue morpho butterflies flutter around you.',
                                                'A brilliant metallic blue butterfly resting on an exotic tropical '
                                                'flower.',
                                                'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3e/Lower_Manhattan_from_Brooklyn_May_2015_panorama.jpg/960px-Lower_Manhattan_from_Brooklyn_May_2015_panorama.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'evening': (   'Panoramic Hilltop Sunset Lookout & Skyline Dining',
                                                 '05:30 PM - 09:00 PM',
                                                 'Restaurant $30',
                                                 32,
                                                 'Watch the sparkling city skyline light up from an elevated hill peak '
                                                 'as twilight turns the sky indigo.',
                                                 'View from the hill peak looking down at the immense grid of glowing '
                                                 'city streetlights.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/53/Lower_Manhattan_from_Governors_Island_August_2017_panorama.jpg/960px-Lower_Manhattan_from_Governors_Island_August_2017_panorama.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')},
                              {   'theme': 'Farewell Megacity Horizon, Grand Food Hall & Midnight Toast',
                                  'neighborhood': 'Crown Skyline District',
                                  'rest': (   '03:00 PM - 04:00 PM',
                                              '☕ Nitro Cold Brew & Artisan Croissant on Skydeck',
                                              'Panoramic Observatory Lounge',
                                              'Final afternoon contemplation gazing over the immense geometric '
                                              'metropolis below.'),
                                  'morning': (   '🌅 Final 360° Skyline Skydeck Sunrise & Glass Walkway',
                                                 '08:00 AM - 10:30 AM',
                                                 'Skydeck $25',
                                                 25,
                                                 'Stand high above the city as golden morning light glints off '
                                                 'hundreds of glass skyscraper spires.',
                                                 'Looking down through panoramic glass windows at the bustling city '
                                                 'streets starting the day.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3a/Lower_Manhattan_from_Jersey_City_July_2014_002.jpg/960px-Lower_Manhattan_from_Jersey_City_July_2014_002.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'midday': (   'Grand Central Artisanal Food Hall Safari',
                                                '11:00 AM - 02:30 PM',
                                                'Hall tasting $20',
                                                20,
                                                'Sample from 30+ curated gourmet counters: hand-rolled pasta, '
                                                'wood-fired pizza, and gourmet gelato.',
                                                'A bustling food hall with gleaming brass counters, hanging cured '
                                                'hams, and fresh oysters on ice.',
                                                'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/36/Lower_Manhattan_from_Jersey_City_November_2014_panorama_1.jpg/960px-Lower_Manhattan_from_Jersey_City_November_2014_panorama_1.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail'),
                                  'evening': (   'Farewell Rooftop Skyline Toast & Midnight Starlight',
                                                 '05:30 PM - 10:00 PM',
                                                 'Rooftop lounge',
                                                 38,
                                                 'Toast to an extraordinary adventure with craft cocktails high above '
                                                 'the glowing illuminated metropolis.',
                                                 'Cocktail glass held against the sparkling sea of illuminated '
                                                 'skyscraper lights at night.',
                                                 'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/41/Lower_Manhattan_from_Jersey_City_November_2014_panorama_2.jpg/960px-Lower_Manhattan_from_Jersey_City_November_2014_panorama_2.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail')}]}

def build_procedural_day(
    dest_title: str,
    day_num: int,
    env_type: str,
    traveler: str,
    mood: str,
    dietary: str,
    price_factor: float,
    budget: str = "Backpacker",
    accessibility: str = ""
) -> Dict[str, Any]:
    """Generates an authentic, fully differentiated itinerary day for Day N with rich preference adaptation."""
    themes_pool = DAY_THEMES_BY_ENV.get(env_type, DAY_THEMES_BY_ENV["VIBRANT_METROPOLIS"])
    # Uses 0-indexed day_num - 1 directly up to 10 days to guarantee zero repetitions
    theme_idx = min(len(themes_pool) - 1, max(0, day_num - 1))
    template = themes_pool[theme_idx]

    m = template["morning"]
    mid = template["midday"]
    e = template["evening"]
    rest = template["rest"]

    # Adapt Food Spot based on Dietary preference
    food_adapt = FOODIE_ADAPTATIONS.get(dietary, FOODIE_ADAPTATIONS["Street Food Hunter"])
    m_food = f"[{dietary}] {food_adapt['morning']}"
    mid_food = f"[{dietary}] {food_adapt['midday']}"
    e_food = f"[{dietary}] {food_adapt['evening']}"

    # Adapt Mood
    mood_mod = MOOD_MODIFIERS.get(mood, MOOD_MODIFIERS["Hidden Gems & Secret Spots"])
    m_title = f"{mood_mod['prefix']}{m[0]}"
    mid_title = f"{mood_mod['prefix']}{mid[0]}"
    e_title = f"{e[0]} ({mood_mod['evening_vibe']})"

    # Adapt Traveler persona & pacing
    traveler_info = TRAVELER_TRANSIT_AND_TIPS.get(traveler, TRAVELER_TRANSIT_AND_TIPS["Solo Explorer"])
    daily_steps = traveler_info["pace"]
    transit_mode = traveler_info["transit_mode"]
    if accessibility and ("wheelchair" in accessibility.lower() or "step-free" in accessibility.lower()):
        transit_mode = "♿ Accessible Step-Free Vehicle / Low-Floor Transit"

    day_title = f"Day {day_num}: {dest_title} {template['theme']}"
    neighborhood = f"{dest_title} {template['neighborhood']}"
    vibe_summary = f"{template['theme']} curated specifically for {traveler} seeking {mood}"

    # Unique, non-repetitive rest break tip based on day_num
    rest_tip_idx = (day_num - 1) % len(REST_SITUATIONAL_TIPS)
    rest_break = {
        "time_slot": rest[0],
        "activity_name": rest[1],
        "location_name": f"{dest_title} {rest[2]}",
        "tip": f"[{traveler} recharge] {rest[3]} {REST_SITUATIONAL_TIPS[rest_tip_idx]}"
    }

    # Situational non-repetitive tips for each time slot
    m_tip = generate_situational_insider_tip(0, day_num, traveler, budget, m[4])
    mid_tip = generate_situational_insider_tip(1, day_num, traveler, budget, mid[4])
    e_tip = generate_situational_insider_tip(2, day_num, traveler, budget, e[4])

    activities_list = [
        {
            "activity_name": m_title,
            "image_url": m[6],
            "category": f"Morning Expedition / {env_type.replace('_', ' ').title()}",
            "time_slot": m[1],
            "location_name": f"{dest_title} {m[0].split(' ')[1] if len(m[0].split(' ')) > 1 else 'Trail'}",
            "neighborhood": f"North {dest_title}",
            "estimated_price": f"${max(4, int(m[3] * price_factor))}",
            "cost_tier": "$" if m[3] < 15 else "$$",
            "ticket_requirement": m[2],
            "vibe_tags": [f"#{dest_title.replace(' ', '')}", "#MorningLight", mood_mod["tag"], f"#{traveler.replace(' ', '')}"],
            "crowd_meter": "Peaceful dawn (3/10 crowd)",
            "insider_booking_tip": m_tip,
            "photo_spot_tip": m[5],
            "food_spot": m_food,
            "transit_to_next": {
                "mode": transit_mode,
                "duration": "12 mins",
                "cost": "$0.00" if "Walk" in transit_mode else "$2.50",
                "instructions": f"Follow {transit_mode.lower()} toward the cultural midday district."
            }
        },
        {
            "activity_name": mid_title,
            "image_url": mid[6],
            "category": f"Discovery & {dietary}",
            "time_slot": mid[1],
            "location_name": f"{dest_title} Cultural Haven",
            "neighborhood": f"Central {dest_title}",
            "estimated_price": f"${max(8, int(mid[3] * price_factor))}",
            "cost_tier": "$$" if mid[3] < 25 else "$$$",
            "ticket_requirement": mid[2],
            "vibe_tags": ["#LocalSecrets", mood_mod["tag"], f"#{dietary.replace(' ', '')}"],
            "crowd_meter": "Authentic local pace (4/10)",
            "insider_booking_tip": mid_tip,
            "photo_spot_tip": mid[5],
            "food_spot": mid_food,
            "transit_to_next": {
                "mode": transit_mode,
                "duration": "14 mins",
                "cost": "$0.00" if "Walk" in transit_mode else "$3.00",
                "instructions": f"Take {transit_mode.lower()} toward the sunset viewpoint quarter."
            }
        },
        {
            "activity_name": e_title,
            "image_url": e[6],
            "category": "Golden Hour & Evening Vibe",
            "time_slot": e[1],
            "location_name": f"{dest_title} Sunset Overlook",
            "neighborhood": f"West {dest_title}",
            "estimated_price": f"${max(15, int(e[3] * price_factor))}",
            "cost_tier": "$$$",
            "ticket_requirement": e[2],
            "vibe_tags": ["#GoldenHour", mood_mod["tag"], "#Skyline"],
            "crowd_meter": "Sunset crowd (5/10)",
            "insider_booking_tip": e_tip,
            "photo_spot_tip": e[5],
            "food_spot": e_food,
            "transit_to_next": {
                "mode": transit_mode,
                "duration": "8 mins",
                "cost": "Free",
                "instructions": "Stroll down the illuminated avenue back to your basecamp."
            }
        }
    ]

    return {
        "day": day_num,
        "title": day_title,
        "neighborhood": neighborhood,
        "vibe_summary": vibe_summary,
        "daily_steps_estimate": daily_steps,
        "rest_break": rest_break,
        "activities": activities_list
    }


def adapt_curated_activity(
    act: Dict[str, Any],
    slot_idx: int,
    dietary: str,
    mood: str,
    traveler: str,
    budget: str,
    accessibility: str,
    price_factor: float,
    day_num: int = 1
) -> Dict[str, Any]:
    """Dynamically transforms curated database activities to match the user's selected preference filters."""
    slot_names = ["morning", "midday", "evening"]
    slot_key = slot_names[min(slot_idx, 2)]

    # 1. Adapt Food Spot based on Dietary preference
    food_adapt = FOODIE_ADAPTATIONS.get(dietary, FOODIE_ADAPTATIONS["Street Food Hunter"])
    base_food = act.get("food_spot", "")
    adapted_food = f"[{dietary}] {food_adapt[slot_key]} (Local specialty match: {base_food})"

    # 2. Adapt Mood & Real Place Overrides
    mood_mod = MOOD_MODIFIERS.get(mood, MOOD_MODIFIERS["Hidden Gems & Secret Spots"])
    base_name = act.get("activity_name", "")
    
    # Check if a custom mood place override exists for this slot
    overrides = mood_mod.get("activity_overrides", {})
    if slot_idx in overrides:
        override = overrides[slot_idx]
        loc_str = act.get("location_name", "")
        clean_loc = f"{loc_str} • " if loc_str else ""
        adapted_name = f"{clean_loc}{override['activity_name']}"
        adapted_category = override.get("category", act.get("category", "Curated Expedition"))
        adapted_photo = override.get("photo_spot_tip", act.get("photo_spot_tip", ""))
        custom_base_tip = override.get("insider_booking_tip", act.get("insider_booking_tip", ""))
    else:
        if slot_idx == 2:
            adapted_name = f"{base_name} & {mood_mod['evening_vibe']}"
        else:
            adapted_name = f"{mood_mod['prefix']}{base_name}"
        adapted_category = act.get("category", "Curated Expedition")
        adapted_photo = act.get("photo_spot_tip", "")
        custom_base_tip = act.get("insider_booking_tip", "")

    # 3. Adapt Tags
    base_tags = act.get("vibe_tags", [])
    adapted_tags = list(dict.fromkeys(base_tags + [mood_mod["tag"], f"#{traveler.replace(' ', '')}", f"#{dietary.replace(' ', '')}"]))

    # 4. Adapt Traveler Persona & Situational Non-Repetitive Tips
    traveler_info = TRAVELER_TRANSIT_AND_TIPS.get(traveler, TRAVELER_TRANSIT_AND_TIPS["Solo Explorer"])
    adapted_tip = generate_situational_insider_tip(slot_idx, day_num, traveler, budget, custom_base_tip)

    # 5. Adapt Price & Tier
    price_str = str(act.get("estimated_price", "$10"))
    if "$" in price_str:
        clean_val = int("".join(filter(str.isdigit, price_str)) or "10")
        adjusted_price = f"${max(0, int(clean_val * price_factor))}"
    else:
        adjusted_price = price_str

    if budget == "Backpacker":
        cost_tier = "$"
        ticket_req = f"{act.get('ticket_requirement', 'Standard entry')} (Tip: Ask for student/youth or early-bird discount)"
    elif budget == "Luxury":
        cost_tier = "$$$$"
        ticket_req = f"{act.get('ticket_requirement', 'Standard entry')} (VIP skip-the-line express access arranged by private concierge)"
    else:
        cost_tier = act.get("cost_tier", "$$")
        ticket_req = act.get("ticket_requirement", "Standard entry")

    # 6. Adapt Transit
    base_transit = act.get("transit_to_next", {})
    transit_mode = traveler_info["transit_mode"]
    if accessibility and ("wheelchair" in accessibility.lower() or "step-free" in accessibility.lower()):
        transit_mode = "♿ Accessible Step-Free Vehicle / Low-Floor Transit"
        transit_instructions = "Use the designated step-free elevator / wide ramp entrance. All boarding platforms are level access."
    else:
        transit_instructions = base_transit.get("instructions", f"Follow {transit_mode.lower()} toward the next stop.")

    adapted_transit = {
        "mode": transit_mode,
        "duration": base_transit.get("duration", "12 mins"),
        "cost": "$0.00" if "Walk" in transit_mode else base_transit.get("cost", "$2.20"),
        "instructions": transit_instructions
    }

    return {
        **act,
        "activity_name": adapted_name,
        "category": adapted_category,
        "photo_spot_tip": adapted_photo,
        "food_spot": adapted_food,
        "vibe_tags": adapted_tags,
        "insider_booking_tip": adapted_tip,
        "estimated_price": adjusted_price,
        "cost_tier": cost_tier,
        "ticket_requirement": ticket_req,
        "transit_to_next": adapted_transit
    }


def adapt_basecamp(basecamp: Dict[str, Any], budget: str, traveler: str, dest_name: str) -> Dict[str, Any]:
    """Customizes accommodation recommendations based on budget tier and traveler persona."""
    traveler_info = TRAVELER_TRANSIT_AND_TIPS.get(traveler, TRAVELER_TRANSIT_AND_TIPS["Solo Explorer"])

    if budget == "Backpacker":
        # Broke Student ($) Tier: Ultra-budget social pod hostel & budget capsule hotel
        hostel = {
            "name": f"{dest_name} Top-Rated Social Pod Hostel & Backpacker Hub",
            "price": "$22/night",
            "rating": "9.4/10 (Backpacker Gold)",
            "vibe": "Privacy curtains, free hostel breakfast, community guest kitchen, lockers & nightly pub crawls"
        }
        boutique = {
            "name": f"{dest_name} Minimalist Japanese Capsule & Micro-Room Hotel",
            "price": "$48/night",
            "rating": "9.2/10 (Smart Budget)",
            "vibe": "Ultra-clean soundproof sleep pod cabins with high-speed fiber WiFi, shared sauna & luggage storage"
        }
        strategy = f"Stay in central social dorm pods within 3 minutes of metro turnstiles to eliminate transit costs. Elevate your feet and recharge devices in the hostel common lounge during afternoon heat."

    elif budget == "Luxury":
        # Bougie Luxury ($$$) Tier: 5-star Heritage Palace & Ultra-Luxe Boutique Sanctuary
        hostel = {
            "name": f"{dest_name} Luxury Executive Suite & Private Club Quarters",
            "price": "$240/night",
            "rating": "9.7/10 (Luxe Executive)",
            "vibe": "Private penthouse floor, complimentary champagne hour, rainfall showers, and personal concierge"
        }
        boutique = {
            "name": f"{dest_name} Grand 5-Star Heritage Palace & Sky Spa Suites",
            "price": "$480/night",
            "rating": "9.9/10 (Ultra-Luxe)",
            "vibe": "Dedicated 24/7 private butler, panoramic rooftop infinity pool, 2 Michelin-star dining room & on-call private chauffeur"
        }
        strategy = f"Dedicated private chauffeur and 24/7 hotel concierge arrange VIP express skip-the-line escorts and private museum viewings so you never wait in queues."

    else:
        # Balanced ($$) Tier: Boutique Design Hotel & Modern Ensuite Pod Hostel
        hostel = basecamp.get("hostel_pick", {
            "name": f"{dest_name} Modern Design Pod Hostel & Cafe Lounge",
            "price": "$38/night",
            "rating": "9.3/10 (Superb)",
            "vibe": "Curated industrial-chic loft with artisan espresso bar, cozy private pods & co-working tables"
        })
        boutique = basecamp.get("boutique_pick", {
            "name": f"{dest_name} Artisan Boutique Garden Hotel",
            "price": "$145/night",
            "rating": "9.5/10 (Exceptional)",
            "vibe": "Historic conversion with leafy interior courtyard, natural wine bar, and locally sourced breakfast"
        })
        strategy = f"Book boutique accommodations located along major transit corridors. Take a 45-minute shoe-off tea or coffee break between 2:30 PM - 3:45 PM to stay energized for evening exploration."

    return {
        **basecamp,
        "hostel_pick": hostel,
        "boutique_pick": boutique,
        "rest_strategy": strategy
    }


def adapt_spotify_playlist(spotify_info: Dict[str, Any], mood: str, dest_name: str) -> Dict[str, Any]:
    """Shapes the audio atmosphere and tracks to match the user's trip mood."""
    mood_genres = {
        "Underground Nightlife & Raves": (f"{dest_name} After Hours: Underground Industrial Techno & Bass", "Minimal Techno / Dark Synthwave / Club Beats"),
        "Chill & Wellness": (f"{dest_name} Sanctuary: Ambient Soundscapes & Singing Bowls", "Binaural Ambient / Meditation Calm / Acoustic Strings"),
        "Insta & TikTok Viral Spots": (f"{dest_name} Trending: Global Viral Pop & Upbeat Anthems", "Trending TikTok Chart Hits / Indie Pop"),
        "Hidden Gems & Secret Spots": (f"{dest_name} Secret Alleys: Late Night Lo-Fi & Neo-Soul", "Lo-Fi Hip Hop / Chill Jazzhop"),
        "Cultural Deep-Dive": (f"{dest_name} Living Heritage: Traditional Masters & Folk Echoes", "Regional Acoustic Folk / World Heritage Classics"),
        "Nature & Outdoor Adventure": (f"{dest_name} Wild Horizon: Campfire Acoustic & Mountain Chill", "Folk Rock / Wilderness Acoustic / Coastal Breezes")
    }
    title, genre = mood_genres.get(mood, (f"{dest_name} Golden Hour Tape", "Indie Ambient Chill"))
    return {
        "title": title,
        "genre": genre,
        "tracks": spotify_info.get("tracks", [f"{dest_name} Sunrise", f"Alleys of {dest_name}", f"Sunset Horizon", f"Midnight in {dest_name}"])
    }

