# Encyclopedic Destination Knowledge Base for AI Travel Planner
# Fully enriched with High-Resolution Photography, Curated Hostel/Rest Basecamps,
# Inter-Activity Transit Legs (Walking/Metro/Taxi routes), and Fatigue-Prevention Rest Breaks.

from typing import Dict, Any

DESTINATIONS_DATA: Dict[str, Dict[str, Any]] = {
    "tokyo": {
        "destination_display": "Tokyo, Japan 🇯🇵",
        "environment_type": "Metropolitan Neon Wonderland & Ancient Shrines",
        "hero_image": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Mount Fuji distant view", "Meiji Jingu Sacred Forest", "Meguro River Weeping Canals", "Shinjuku Gyoen National Garden", "Sumida River Waterfront"],
        "basecamp": {
            "strategic_area": "Shibuya or Shinjuku (Direct JR Yamanote Line access)",
            "hostel_pick": {
                "name": "Nui. Hostel & Bar Lounge (Kuramae)",
                "price": "$38/night",
                "rating": "9.3/10 (Superb)",
                "vibe": "Converted riverside toy warehouse with woodfire cafe, quiet sleep pods & laptop desks"
            },
            "boutique_pick": {
                "name": "Trunk (Hotel) Cat Street Shibuya",
                "price": "$160/night",
                "rating": "9.5/10 (Exceptional)",
                "vibe": "Eco-luxury design sanctuary with quiet terrace bar tucked away from scramble crowds"
            },
            "rest_strategy": "Stay within 5 minutes of a JR Yamanote station. Tokyo averages 18,000 steps/day—use station coin lockers to drop bags and take a 45-min shoe-off tea break at 3:30 PM."
        },
        "transit_system": "Tokyo Metro & JR Lines (100% contactless via Apple/Google Wallet Suica)",
        "spotify_playlist": {
            "title": "Tokyo Neon Nights & Citypop Dream",
            "genre": "Japanese Citypop / Lofi Beats",
            "tracks": ["Plastic Love - Mariya Takeuchi", "Stay With Me - Miki Matsubara", "Midnight Pretenders - Tomoko Aran", "Shibuya Morning - Lofi Soundlab"]
        },
        "aesthetic_summary": "Thrift store hauls in vintage Shimokitazawa, tranquil forest shrines, lantern-lit drinking alleys, and sensory digital art.",
        "genz_hacks": [
            "Add a digital Suica or Pasmo IC card directly to your smartphone wallet before you fly.",
            "Use Google Maps transit filter for 'least walking' if you plan on averaging 20k steps.",
            "Bring a compact coin purse—gachapon capsule toys and local izakayas still run on 100-yen coins.",
            "Most tiny 6-seater Omoide Yokocho and Golden Gai bars have a small ¥500 table charge (otoushi)."
        ],
        "packing_essentials": [
            "Slip-on sneakers (temples, ryokans, and fitting rooms require shoes off)",
            "10,000mAh magnetic portable power bank (heavy navigation & camera usage)",
            "Foldable canvas tote bag (Japanese convenience stores charge for bags)",
            "Pocket Wi-Fi or local e-SIM card"
        ],
        "days": [
            {
                "title": "Neon Horizons, Ancient Shrines & Indie Thrift Hauls",
                "neighborhood": "Harajuku, Shibuya & Shimokitazawa",
                "vibe_summary": "Electric pop energy to cozy retro alleyways",
                "daily_steps_estimate": "12,800 steps (Balanced pace with train legs)",
                "rest_break": {
                    "time_slot": "03:15 PM - 04:15 PM",
                    "activity_name": "☕ Cat Street Foot Rest & Siphon Brew Recharge",
                    "location_name": "Chop Coffee or Fuglen Bench Lounge",
                    "tip": "Sit down, elevate your feet, and recharge your phone. Avoid museum fatigue before the sunset skydeck!"
                },
                "activities": [
                    {
                        "activity_name": "🌅 Sunrise Coffee & Secret Meiji Jingu Forest Walk",
                        "image_url": "https://images.unsplash.com/photo-1542051841857-5f90071e7989?auto=format&fit=crop&w=800&q=80",
                        "category": "Hidden Nature / Morning Fuel",
                        "time_slot": "08:30 AM - 10:15 AM",
                        "location_name": "Meiji Jingu & Fuglen Tokyo",
                        "neighborhood": "Yoyogi / Harajuku",
                        "estimated_price": "$6",
                        "cost_tier": "$",
                        "ticket_requirement": "Free Entry (Walk-in)",
                        "vibe_tags": ["#Serene", "#MorningRoutine", "#SpecialtyCoffee"],
                        "crowd_meter": "Peaceful (2/10 crowd)",
                        "insider_booking_tip": "Enter through the North Torii gate to dodge tour groups. Grab a cardamom bun at Fuglen right afterwards.",
                        "photo_spot_tip": "Low-angle shot through the 12-meter cedar Torii gate with golden sunlight streaming through the canopy.",
                        "food_spot": "Fuglen Tokyo (Nordic pour-over & cinnamon pastries)",
                        "transit_to_next": {
                            "mode": "🚇 Metro Train (Chiyoda Line)",
                            "duration": "14 mins",
                            "cost": "$1.40 (¥180 via Suica)",
                            "instructions": "Walk 300m to Meiji-Jingumae Station. Take Chiyoda Line to Yoyogi-Uehara (1 stop), cross platform to Odakyu Line to Shimokitazawa (4 mins)."
                        }
                    },
                    {
                        "activity_name": "Vintage Archive Thrifting & Record Hunting",
                        "image_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=800&q=80",
                        "category": "Gen-Z Thrift Culture",
                        "time_slot": "11:00 AM - 01:30 PM",
                        "location_name": "Shimokitazawa South Exit Alleys (New York Joe Exchange, Chicago, Garage)",
                        "neighborhood": "Shimokitazawa",
                        "estimated_price": "$25",
                        "cost_tier": "$$",
                        "ticket_requirement": "Free Entry",
                        "vibe_tags": ["#Y2KArchive", "#VintageFinds", "#IndieVibes"],
                        "crowd_meter": "Vibrant (5/10 crowd)",
                        "insider_booking_tip": "Look for shops located in basements (B1F) or upper floors—that's where the rarest 90s streetwear gems hide.",
                        "photo_spot_tip": "The ivy-covered exterior of New York Joe Exchange (a former public bathhouse turned thrift temple).",
                        "food_spot": "Magic Spice (Hokkaido soul food soup curry with spice scale up to 'Nirvana')",
                        "transit_to_next": {
                            "mode": "🚇 Train (Keio Inokashira Line)",
                            "duration": "8 mins (Express)",
                            "cost": "$1.20 (¥140)",
                            "instructions": "Hop on the Keio Inokashira Line Express direct from Shimokitazawa Station to Shibuya Station (4 stops, zero transfers)."
                        }
                    },
                    {
                        "activity_name": "Shibuya Sky Sunset Glass Cantilever Observation Deck",
                        "image_url": "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?auto=format&fit=crop&w=800&q=80",
                        "category": "Panoramic Skyline / Golden Hour",
                        "time_slot": "04:45 PM - 06:30 PM",
                        "location_name": "Shibuya Scramble Square 47F",
                        "neighborhood": "Shibuya",
                        "estimated_price": "$18",
                        "cost_tier": "$$",
                        "ticket_requirement": "Book 4 weeks ahead online for sunset slot",
                        "vibe_tags": ["#GoldenHour", "#Skyline", "#BladeRunnerVibes"],
                        "crowd_meter": "Busy (8/10 crowd)",
                        "insider_booking_tip": "Reserve the 4:40 PM entry ticket. You get daylight, sunset, and twilight neon all in one visit.",
                        "photo_spot_tip": "The corner glass edge 'Sky Edge'—shoot at 0.5x wide angle sitting on the artificial lawn.",
                        "food_spot": "Ichiran Shibuya or Standing Sushi Bar Uogashi Nihon-Ichi",
                        "transit_to_next": {
                            "mode": "🚇 Train (JR Yamanote Line)",
                            "duration": "7 mins",
                            "cost": "$1.30 (¥160)",
                            "instructions": "Take the JR Yamanote green loop line northbound from Shibuya Track 2 directly to Shinjuku Station (3 stops)."
                        }
                    },
                    {
                        "activity_name": "Omoide Yokocho (Memory Lane) Lantern Alley Izakaya Crawl",
                        "image_url": "https://images.unsplash.com/photo-1554797589-7241bb691973?auto=format&fit=crop&w=800&q=80",
                        "category": "Late Night Underground Munchies",
                        "time_slot": "07:30 PM - 10:30 PM",
                        "location_name": "Omoide Yokocho & Golden Gai Bar Micro-Alleys",
                        "neighborhood": "Shinjuku",
                        "estimated_price": "$30",
                        "cost_tier": "$$",
                        "ticket_requirement": "Cash only, walk-in",
                        "vibe_tags": ["#NeonNoir", "#StreetFood", "#IzakayaVibes"],
                        "crowd_meter": "Buzzing (7/10 crowd)",
                        "insider_booking_tip": "Pick the tiny stalls grilling yakitori over binchotan charcoal. Order tare (sweet soy) chicken skin and a highball.",
                        "photo_spot_tip": "Stand at the mouth of the alley framed by glowing red chochin lanterns and steam billowing from exhaust fans.",
                        "food_spot": "Toriyoshi Yakitori Stall (Charcoal-grilled tsukune skewers & cold Kirin draft)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk back to Basecamp",
                            "duration": "8 mins walk (600m)",
                            "cost": "Free",
                            "instructions": "Stroll down the quiet western exit of Shinjuku Station toward your boutique hostel or hotel."
                        }
                    }
                ]
            }
        ]
    },
    "bali": {
        "destination_display": "Bali, Indonesia 🇮🇩",
        "environment_type": "Tropical Jungle Ravines, Sacred Volcanic Terraces & Ocean Cliffs",
        "hero_image": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Mount Batur Volcano", "Tegallalang Emerald Rice Terraces", "Uluwatu Sunset Cliffs", "Tukad Cepung Cave Waterfall", "Sacred Monkey Forest Sanctuary"],
        "basecamp": {
            "strategic_area": "Central Ubud (Days 1-2 for culture & jungles) + Bingin/Uluwatu (Day 3 for cliffs & surf)",
            "hostel_pick": {
                "name": "Arya Wellness Retreat / Kos One Hostel Canggu",
                "price": "$24/night",
                "rating": "9.4/10 (Superb)",
                "vibe": "Mediterranean white-washed villa with lagoon pool, yoga deck & vegan cafe"
            },
            "boutique_pick": {
                "name": "Bambu Indah Eco Resort (Ubud)",
                "price": "$125/night",
                "rating": "9.6/10 (Exceptional)",
                "vibe": "Antique Javanese bridal homes built over natural spring-fed river pools"
            },
            "rest_strategy": "Do not attempt to cross from Ubud to Uluwatu in midday heat. Book your basecamp in Ubud first, then move to the coast. Rest during the 1:00 PM - 3:00 PM tropical sun peak."
        },
        "transit_system": "Scooter Rental / Private Driver / Gojek & Grab app motorbike taxis",
        "spotify_playlist": {
            "title": "Bali Boho Sunset & Island House",
            "genre": "Organic Deep House / Island Acoustic",
            "tracks": ["Canggu Sunset - Island Soul", "Uluwatu Waves - Deep Echoes", "Ubud Rain - Jungle Soundscape", "Sunbeam Cave - Tropical Lofi"]
        },
        "aesthetic_summary": "Emerald tiered rice paddies, cliffside ocean temples with breaking barrels, jungle infinity dayclubs, and roadside coconut warungs.",
        "genz_hacks": [
            "Download 'Gojek' or 'Grab' for 50-cent scooter taxi rides to bypass narrow bottleneck traffic.",
            "Never drink tap water—avoid 'Bali Belly' by brushing teeth with bottled water and drinking only sealed coconuts.",
            "Wear a sarong (provided at ticket gates) and cover shoulders whenever stepping into Hindu temple compounds.",
            "Book daybeds at cliff clubs (Uluwatu/Canggu) 1 week ahead for guaranteed golden hour front-row views."
        ],
        "packing_essentials": [
            "Reef-safe biodegradable sunscreen (protect coral ecosystems)",
            "Waterproof phone dry-bag for waterfall river treks",
            "Quick-drying breathable linen shirts and shorts",
            "Activated charcoal tablets & electrolyte hydration powder"
        ],
        "days": [
            {
                "title": "Misty Rice Valleys, Cave Sunbeams & Jungle Dayclubs",
                "neighborhood": "Ubud, Tegallalang & Tampaksiring",
                "vibe_summary": "Lush spiritual greenery to luxury bamboo jungle architecture",
                "daily_steps_estimate": "9,200 steps (Moderate hiking + scooter transit)",
                "rest_break": {
                    "time_slot": "01:00 PM - 02:00 PM",
                    "activity_name": "🥥 Midday Coconut Siesta & Shaded Hammock Rest",
                    "location_name": "Shaded bamboo warung overlooking river ravine",
                    "tip": "Escape the high UV tropical noon heat with an ice-cold young coconut and fresh lemongrass towel."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Sunrise Stroll Through Tegallalang Emerald Rice Terraces",
                        "image_url": "https://images.unsplash.com/photo-1512100356356-de1b84283e18?auto=format&fit=crop&w=800&q=80",
                        "category": "Sacred Terraces & Morning Light",
                        "time_slot": "06:30 AM - 08:30 AM",
                        "location_name": "Tegallalang Terraced Valley & Kawi Coffee",
                        "neighborhood": "North Ubud",
                        "estimated_price": "$4",
                        "cost_tier": "$",
                        "ticket_requirement": "Entrance fee at gate (50k IDR cash)",
                        "vibe_tags": ["#RiceTerraces", "#TropicalSunrise", "#UbudMagic"],
                        "crowd_meter": "Peaceful early (2/10), scorching by 10 AM",
                        "insider_booking_tip": "Arrive at 6:30 AM right when morning mist hovers over the palm trees. Walk down into the bottom valley to dodge tourists on top swings.",
                        "photo_spot_tip": "Position camera low along the narrow earthen ridge between terraces, capturing morning sun rays cutting through coconut palms.",
                        "food_spot": "Warung Kawi (Iced Balinese Robusta coffee with fresh dragon fruit smoothie bowl)",
                        "transit_to_next": {
                            "mode": "🛵 Scooter / Grab Bike Ride",
                            "duration": "25 mins through scenic palm roads",
                            "cost": "$2.50 (40k IDR)",
                            "instructions": "Ride east through lush Tampaksiring backroads towards Bangli to the Tukad Cepung entrance."
                        }
                    },
                    {
                        "activity_name": "Hidden Sunbeam Cave Waterfall Expedition",
                        "image_url": "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?auto=format&fit=crop&w=800&q=80",
                        "category": "Natural Wonders & Cave Pools",
                        "time_slot": "10:00 AM - 12:30 PM",
                        "location_name": "Tukad Cepung Waterfall",
                        "neighborhood": "Bangli",
                        "estimated_price": "$3",
                        "cost_tier": "$",
                        "ticket_requirement": "Pay at entrance (30k IDR)",
                        "vibe_tags": ["#CaveWaterfall", "#SecretSpot", "#AdventureMode"],
                        "crowd_meter": "Moderate (4/10 crowd)",
                        "insider_booking_tip": "Wear water shoes or strap sandals—you wade through ankle-deep canyon streams inside a dramatic limestone cavern.",
                        "photo_spot_tip": "Stand on the boulder inside the cavern right between 10:30 AM and 11:30 AM when direct sunbeams shoot through the open roof.",
                        "food_spot": "Local Roadside Warung (Nasi Campur Bali with spicy shredded chicken, tempeh manis & sambal matah)",
                        "transit_to_next": {
                            "mode": "🚗 Air-Conditioned Car / Scooter",
                            "duration": "20 mins",
                            "cost": "$3.00",
                            "instructions": "Head west back toward Alas Harum entrance for the tiered jungle infinity club."
                        }
                    },
                    {
                        "activity_name": "Cretya Ubud Tiered Jungle Infinity Pools & DJ Lounge",
                        "image_url": "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?auto=format&fit=crop&w=800&q=80",
                        "category": "Luxury Bamboo Dayclub / Vibe Lounge",
                        "time_slot": "02:00 PM - 05:30 PM",
                        "location_name": "Cretya Ubud at Alas Harum",
                        "neighborhood": "Tegallalang",
                        "estimated_price": "$25",
                        "cost_tier": "$$",
                        "ticket_requirement": "Minimum spend on daybed or entrance pass",
                        "vibe_tags": ["#JunglePool", "#DayclubVibes", "#BaliAesthetics"],
                        "crowd_meter": "Lively & Trendy (6/10 crowd)",
                        "insider_booking_tip": "Pre-book a cabana on the 2nd tier pool for the best view over the cascading waterfall and terraced palm hills.",
                        "photo_spot_tip": "Sitting on the edge of the glass-bottom pool with the deep green jungle ravine dropping off directly beneath you.",
                        "food_spot": "Cretya Dayclub Bistro (Crispy duck sliders & passionfruit coconut mocktail)",
                        "transit_to_next": {
                            "mode": "🛵 Quick Scooter Ride to Town",
                            "duration": "18 mins downhill",
                            "cost": "$1.80",
                            "instructions": "Cruise south along Jalan Raya Tegallalang straight into central Ubud Palace."
                        }
                    },
                    {
                        "activity_name": "Traditional Balinese Suckling Pig & Fire Dance",
                        "image_url": "https://images.unsplash.com/photo-1537953773345-d172ccf13cf1?auto=format&fit=crop&w=800&q=80",
                        "category": "Cultural Heritage & Authentic Dining",
                        "time_slot": "06:30 PM - 09:30 PM",
                        "location_name": "Ubud Palace Fire Dance & Ibu Oka Babi Guling",
                        "neighborhood": "Central Ubud",
                        "estimated_price": "$12",
                        "cost_tier": "$",
                        "ticket_requirement": "Buy dance ticket outside palace courtyard",
                        "vibe_tags": ["#FireDance", "#Kecak", "#FoodieHeaven"],
                        "crowd_meter": "Cultural crowd (5/10)",
                        "insider_booking_tip": "Arrive 20 minutes before the 7:00 PM Kecak Fire Dance to secure front-row seats on the woven mats.",
                        "photo_spot_tip": "Burst shot of the flame-thrower dancer kicking burning coconut husks across the cobblestones.",
                        "food_spot": "Warung Babi Guling Ibu Oka (Crispy crackling roast pork skin with blood sausage & lemongrass broth)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk to Ubud Basecamp",
                            "duration": "5 mins walk",
                            "cost": "Free",
                            "instructions": "Stroll down Monkey Forest road to your quiet boutique eco-resort."
                        }
                    }
                ]
            }
        ]
    },
    "rome": {
        "destination_display": "Rome, Italy 🇮🇹",
        "environment_type": "Ancient Stone Monuments, Fragrant Orange Groves & Cobblestone Alleys",
        "hero_image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Giardino degli Aranci (Orange Groves)", "Tiber River Embankments", "Villa Borghese Lake & Pines", "Seven Hills of Rome", "Appian Way Roman Stone Trail"],
        "basecamp": {
            "strategic_area": "Monti or Trastevere (Walk to Colosseum, Forum & all dinner spots)",
            "hostel_pick": {
                "name": "The RomeHello Hostel / YellowSquare Rome",
                "price": "$42/night",
                "rating": "9.5/10 (Top Rated)",
                "vibe": "Ultra-modern hostel with private ensuite pods, beer garden, and cooking classes"
            },
            "boutique_pick": {
                "name": "The Hoxton Rome (Parioli) / Chapter Roma",
                "price": "$175/night",
                "rating": "9.3/10 (Superb)",
                "vibe": "Mid-century Italian design, botanical terrace, and natural wine bar"
            },
            "rest_strategy": "Roman cobblestones (sanpietrini) are unforgiving on joints. Avoid crossing the Tiber River during the 2:00 PM - 4:00 PM heat. Schedule a gelato and fountain bench rest in Villa Borghese."
        },
        "transit_system": "Walking + Metro Line A/B + Contactless ATAC Bus tap",
        "spotify_playlist": {
            "title": "Roman Holiday: Acoustic Accordion & Italian Disco",
            "genre": "Italian Vintage / Acoustic Jazz",
            "tracks": ["Tu Vuo' Fa' L'Americano - Renato Carosone", "Felicità - Al Bano & Romina", "Via Con Me - Paolo Conte", "Roma Capoccia - Antonello Venditti"]
        },
        "aesthetic_summary": "Creeping ivy over bohemian Trastevere cobblestones, sunset orange groves overlooking St. Peter's Dome, and steaming skillet Cacio e Pepe.",
        "genz_hacks": [
            "Drink for free from over 2,500 historic curved bronze 'Nasoni' public fountains across Rome—pure cold mountain aqueduct water.",
            "Never order a cappuccino after 11:00 AM—Italians consider milk after lunch a digestion crime; order 'un caffè' (espresso).",
            "Book the Colosseum Underground / Arena access exactly 30 days in advance at midnight CET on the official CoopCulture portal.",
            "Water in carafes is standard, and 'coperto' (cover charge) is normal in authentic trattorias."
        ],
        "packing_essentials": [
            "Supportive cushioned walking sneakers (ancient uneven Roman cobblestones / sanpietrini)",
            "Refillable metal water bottle to fill at historic Nasoni fountains",
            "Light shawl or scarf to cover shoulders inside cathedrals and basilicas",
            "Crossbody bag worn in front for crowded metro rides"
        ],
        "days": [
            {
                "title": "Hidden Keyholes, Bohemian Trastevere & Skillet Cacio e Pepe",
                "neighborhood": "Aventine Hill, Trastevere & Campo de' Fiori",
                "vibe_summary": "Secret panoramic viewpoints into ivy-draped evening wine taverns",
                "daily_steps_estimate": "13,500 steps (Pedestrian cobblestone stroll)",
                "rest_break": {
                    "time_slot": "03:30 PM - 04:30 PM",
                    "activity_name": "🍨 Gelato Siesta on Piazza Santa Maria Steps",
                    "location_name": "Piazza Santa Maria in Trastevere",
                    "tip": "Sit around the 8-sided fountain in the heart of Trastevere with a dark chocolate gelato cup to rest your feet."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Aventine Keyhole Secret & Fragrant Orange Grove Panorama",
                        "image_url": "https://images.unsplash.com/photo-1531572753322-ad063cecc140?auto=format&fit=crop&w=800&q=80",
                        "category": "Hidden Architectural Wonder & Nature",
                        "time_slot": "08:00 AM - 10:00 AM",
                        "location_name": "Piazza dei Cavalieri di Malta & Giardino degli Aranci",
                        "neighborhood": "Aventine Hill",
                        "estimated_price": "$0",
                        "cost_tier": "$",
                        "ticket_requirement": "Free Public Access",
                        "vibe_tags": ["#AventineKeyhole", "#OrangeGarden", "#SecretRome"],
                        "crowd_meter": "Serene morning (2/10 crowd)",
                        "insider_booking_tip": "Peek directly through the brass keyhole on the heavy green wooden door of the Priory. You'll see St. Peter's Basilica framed perfectly through manicured laurel hedges.",
                        "photo_spot_tip": "Align your phone camera lens flush against the brass keyhole aperture at 1.5x zoom for the viral framed shot.",
                        "food_spot": "Roscioli Caffè (Hot pistachio-stuffed cornetto & velvety double espresso)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Scenic Walk across Tiber Bridge",
                            "duration": "14 mins walk (950m)",
                            "cost": "Free",
                            "instructions": "Walk down the Aventine hill through the rose garden, cross the historic stone Ponte Sublicio over the Tiber River into Trastevere."
                        }
                    },
                    {
                        "activity_name": "Trastevere Bohemian Ivy Alleys & Trapizzino Pocket Pizza",
                        "image_url": "https://images.unsplash.com/photo-1529260830199-42c24126f198?auto=format&fit=crop&w=800&q=80",
                        "category": "Ancient Alleys & Street Food Innovation",
                        "time_slot": "11:30 AM - 02:00 PM",
                        "location_name": "Vicolo del Cinque, Piazza Santa Maria & Trapizzino",
                        "neighborhood": "Trastevere",
                        "estimated_price": "$8",
                        "cost_tier": "$",
                        "ticket_requirement": "Free walk-in",
                        "vibe_tags": ["#Trastevere", "#CobblestoneAlleys", "#Trapizzino"],
                        "crowd_meter": "Cozy & vibrant (4/10)",
                        "insider_booking_tip": "Trapizzino serves triangular pouches of warm Roman pizza bianca stuffed with braised oxtail (coda alla vaccinara) or chicken cacciatore.",
                        "photo_spot_tip": "Standing in front of the ivy-draped terracotta arches along Vicolo del Cinque holding a steaming Trapizzino cone.",
                        "food_spot": "Da Enzo al 29 (Arrive at 12:15 PM before opening for the creamiest Cacio e Pepe served in hot skillet with crispy artichoke carciofi alla giudia)",
                        "transit_to_next": {
                            "mode": "🚌 Electric Minibus / Metro Line A",
                            "duration": "15 mins",
                            "cost": "$1.60 (€1.50 ticket)",
                            "instructions": "Take electric bus 116 or walk across Ponte Sisto to Piazza del Popolo Metro for Villa Borghese park."
                        }
                    },
                    {
                        "activity_name": "Villa Borghese Lake Rowboats & Pincio Sunset Terrace",
                        "image_url": "https://images.unsplash.com/photo-1515542622106-78bda8ba0e5b?auto=format&fit=crop&w=800&q=80",
                        "category": "Classical Nature & Violet Twilight Skyline",
                        "time_slot": "05:00 PM - 07:30 PM",
                        "location_name": "Laghetto di Villa Borghese & Terrazza del Pincio",
                        "neighborhood": "Piazza del Popolo Overlook",
                        "estimated_price": "$5",
                        "cost_tier": "$",
                        "ticket_requirement": "Free park, €5 for 20-min wooden rowboat rental",
                        "vibe_tags": ["#BorghesePines", "#Rowboat", "#PincioSunset"],
                        "crowd_meter": "Sunset crowd (5/10)",
                        "insider_booking_tip": "Rent a wooden rowboat on the tranquil lake surrounded by weeping willows and the Temple of Asclepius. Walk to Terrazza del Pincio for sunset.",
                        "photo_spot_tip": "The dome of St. Peter's Basilica silhouetted in violet sunset clouds from the Pincio stone balustrade.",
                        "food_spot": "Frigidarium (Dark chocolate dipped gelato with whipped panna on top)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Stroll back to Monti / Trastevere Basecamp",
                            "duration": "18 mins downhill stroll",
                            "cost": "Free",
                            "instructions": "Walk through the illuminated Piazza del Popolo and Via del Corso back to your basecamp hostel."
                        }
                    }
                ]
            }
        ]
    },
    "paris": {
        "destination_display": "Paris, France 🇫🇷",
        "environment_type": "Grand Haussmann Boulevards, Historic River Seine & Glass Covered Arcades",
        "hero_image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["River Seine Embankments", "Jardin des Tuileries & Luxembourg", "Parc des Buttes-Chaumont Temple", "Canal Saint-Martin Weeping Willows", "Bois de Boulogne"],
        "basecamp": {
            "strategic_area": "Le Marais (3rd/4th Arr.) or Canal Saint-Martin (10th Arr.)",
            "hostel_pick": {
                "name": "Les Piaules / The People Belleville",
                "price": "$45/night",
                "rating": "9.1/10",
                "vibe": "Rooftop bar overlooking Montmartre, custom artisan bunk pods & French craft beer"
            },
            "boutique_pick": {
                "name": "Hôtel Providence (10th Arr.)",
                "price": "$180/night",
                "rating": "9.4/10",
                "vibe": "Velvet Parisian chic with in-room cocktail bars and cobblestone terrace dining"
            },
            "rest_strategy": "The Paris Metro involves extensive stair climbs. Plan your day geographically by Arrondissement (1st & 2nd morning, 10th evening) to minimize transfers."
        },
        "transit_system": "Paris Metro (Navigo Easy card / contactless phone tap)",
        "spotify_playlist": {
            "title": "Midnight in Paris: French Cafe Accordion & Nu-Disco",
            "genre": "French Touch / Parisian Jazz",
            "tracks": ["Quelqu'un m'a dit - Carla Bruni", "La Javanaise - Serge Gainsbourg", "Lady (Hear Me Tonight) - Modjo", "Amélie Theme - Yann Tiersen"]
        },
        "aesthetic_summary": "Morning croissants on cobblestone corners, hidden covered glass arcades, sunset wine picnics along Canal Saint-Martin, and secret courtyard gardens.",
        "genz_hacks": [
            "Never wait in the Louvre pyramid line—use the secret underground Carrousel du Louvre shopping entrance with zero wait.",
            "Always greet shopkeepers with 'Bonjour Madame/Monsieur' before saying anything else, or prepare for chilly service.",
            "Download the 'Citymapper' app for Paris Metro instead of Google Maps—it tells you the exact wagon to enter for quickest transfers.",
            "Water in Parisian restaurants is free by law—ask for 'une carafe d'eau' rather than bottled water."
        ],
        "packing_essentials": [
            "Chic trench coat or oversized blazer (instant Parisian chic)",
            "Comfortable leather loafers or minimalist clean white sneakers",
            "Reusable cotton tote for fresh baguettes and flea market finds",
            "Universal dual voltage adapter with USB-C PD fast charge"
        ],
        "days": [
            {
                "title": "Golden Arcades, Flaky Escargot Pastries & Bohemian Marais",
                "neighborhood": "1st Arrondissement & Le Marais",
                "vibe_summary": "Old-world aristocratic glamour transitioning to vibrant indie boutiques",
                "daily_steps_estimate": "12,000 steps (Paved sidewalks & park walks)",
                "rest_break": {
                    "time_slot": "03:30 PM - 04:30 PM",
                    "activity_name": "☕ Green Metal Chair Siesta in Jardin des Tuileries",
                    "location_name": "Jardin des Tuileries Fountain Basin",
                    "tip": "Pull two green reclining chairs together around the central octagonal fountain to rest your legs in the afternoon sun."
                },
                "activities": [
                    {
                        "activity_name": "Pistachio Escargot Pastry & Secret Jardin du Palais-Royal",
                        "image_url": "https://images.unsplash.com/photo-1509299349698-dd22323b5963?auto=format&fit=crop&w=800&q=80",
                        "category": "Iconic Bakery & Quiet Gardens",
                        "time_slot": "08:30 AM - 10:30 AM",
                        "location_name": "Du Pain et des Idées & Palais-Royal Courtyard",
                        "neighborhood": "Canal Saint-Martin / 1st Arr.",
                        "estimated_price": "$8",
                        "cost_tier": "$",
                        "ticket_requirement": "Free garden entry, walk-in bakery",
                        "vibe_tags": ["#PastryHeaven", "#JardinDuPalaisRoyal", "#EmilyInParisReal"],
                        "crowd_meter": "Peaceful early morning (3/10)",
                        "insider_booking_tip": "Order the 'Escargot Pistache Chocolat' (swirled pistachio chocolate pastry). Eat it sitting on the green park chairs at Palais-Royal.",
                        "photo_spot_tip": "The monochrome striped Buren Columns (Colonnes de Buren) at 8:45 AM before tour groups arrive.",
                        "food_spot": "Du Pain et des Idées (Award-winning 1875 bakery with hand-painted ceilings)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk through Historic Covered Alleys",
                            "duration": "8 mins walk (600m)",
                            "cost": "Free",
                            "instructions": "Walk through the northern exit of Palais-Royal straight into the entrance of Galerie Vivienne."
                        }
                    },
                    {
                        "activity_name": "Passages Couverts Secret 19th-Century Glass Arcades",
                        "image_url": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=800&q=80",
                        "category": "Hidden Architectural Gems",
                        "time_slot": "11:00 AM - 01:30 PM",
                        "location_name": "Passage des Panoramas, Galerie Vivienne & Passage Jouffroy",
                        "neighborhood": "2nd Arrondissement",
                        "estimated_price": "$15",
                        "cost_tier": "$$",
                        "ticket_requirement": "Free Entry",
                        "vibe_tags": ["#HiddenGem", "#DarkAcademia", "#VintageBooks"],
                        "crowd_meter": "Quiet (3/10 crowd)",
                        "insider_booking_tip": "These 1820s heated glass passages sheltered aristocrats from muddy streets. Check out the antique stamp and rare manuscript shops.",
                        "photo_spot_tip": "The mosaic tiled floor and rotunda glass dome inside Galerie Vivienne looking down the symmetrical corridor.",
                        "food_spot": "Marché des Enfants Rouges (Oldest covered market in Paris—try the legendary Moroccan couscous stand)",
                        "transit_to_next": {
                            "mode": "🚇 Metro Line 3 to 11",
                            "duration": "12 mins",
                            "cost": "$2.20 (€2.15)",
                            "instructions": "Take Metro Line 3 from Bourse to Arts et Métiers, transfer to Line 11 to Goncourt for Canal Saint-Martin."
                        }
                    },
                    {
                        "activity_name": "Sunset Natural Wine & Baguette Picnic on Canal Saint-Martin",
                        "image_url": "https://images.unsplash.com/photo-1520939817895-060bdef4ad1b?auto=format&fit=crop&w=800&q=80",
                        "category": "Authentic Local Gen-Z Sunset Vibe",
                        "time_slot": "06:30 PM - 09:30 PM",
                        "location_name": "Quai de Valmy & Iron Footbridges",
                        "neighborhood": "10th Arrondissement",
                        "estimated_price": "$22",
                        "cost_tier": "$$",
                        "ticket_requirement": "BYO wine & cheese",
                        "vibe_tags": ["#AestheticPicnic", "#NaturalWine", "#GoldenHourParis"],
                        "crowd_meter": "Buzzing youth hangout (6/10 crowd)",
                        "insider_booking_tip": "Stop by a local fromagerie and natural wine cave for a chilled Pet-Nat bottle. Sit on the stone edge dangling your legs over the canal.",
                        "photo_spot_tip": "Silhouette shot on the arched cast-iron footbridge as canal tour boats pass underneath the golden sunset reflection.",
                        "food_spot": "Pink Mamma (Truffle pasta under a four-story glass botanical skylight) or Le Comptoir Général",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk back to Canal Basecamp",
                            "duration": "6 mins walk",
                            "cost": "Free",
                            "instructions": "Follow Quai de Jemmapes along the illuminated canal directly back to your boutique hotel or hostel."
                        }
                    }
                ]
            }
        ]
    },
    "iceland": {
        "destination_display": "Iceland (Reykjavik & South Coast) 🇮🇸",
        "environment_type": "Glacial Blue Ice, Black Basalt Sands & Roaring Waterfalls",
        "hero_image": "https://images.unsplash.com/photo-1504893524553-b855bce32c67?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Reynisfjara Black Sand Beach", "Seljalandsfoss Walk-Behind Waterfall", "Sólheimajökull Blue Glacier", "Skógafoss Colossal Waterfall", "Sky Lagoon Geothermal Ocean Pool"],
        "basecamp": {
            "strategic_area": "Vík í Mýrdal (South Coast base) or Downtown Reykjavik (Laugavegur)",
            "hostel_pick": {
                "name": "Kex Hostel Reykjavik / The Barn Vík",
                "price": "$48/night",
                "rating": "9.2/10 (Superb)",
                "vibe": "Vintage industrial biscuit factory with ocean views, craft pub & heated sleeping pods"
            },
            "boutique_pick": {
                "name": "ION Adventure Hotel (Nesjavellir)",
                "price": "$240/night",
                "rating": "9.5/10 (Exceptional)",
                "vibe": "Cantilevered glass hotel over lava fields with northern lights bar"
            },
            "rest_strategy": "Icelandic weather and wind can drain energy fast. Do not schedule more than 3 major stops per day. Use thermal lagoon soaking at the end of the day to eliminate muscle soreness."
        },
        "transit_system": "Rental 4x4 SUV or South Coast Guided Minibus Excursion",
        "spotify_playlist": {
            "title": "Nordic Horizons: Sigur Rós & Ambient Glacier",
            "genre": "Nordic Ambient / Cinematic Post-Rock",
            "tracks": ["Hoppípolla - Sigur Rós", "Breathe - Ólafur Arnalds", "Glacier Trail - Arctic Sound", "Aurora Sky - Nordic Chill"]
        },
        "aesthetic_summary": "Walking behind roaring waterfall curtains, trekking blue glacial crevasses, and soaking in ocean-edge geothermal thermal pools.",
        "genz_hacks": [
            "Never turn your back on the ocean at Reynisfjara Black Sand Beach—'sneaker waves' surge 30 meters up the sand without warning.",
            "Download the 'Vedur' (weather) and 'SafeTravel' apps—Icelandic weather can turn from sunshine to whiteout blizzards in 20 minutes.",
            "Waterproof everything: waterfall mist will soak regular coats; bring a phone waterproof lanyard.",
            "Iceland is 100% cashless—you don't need a single Icelandic Króna banknote; Apple Pay/cards work everywhere."
        ],
        "packing_essentials": [
            "Gore-Tex waterproof outer shell jacket and waterproof rain pants",
            "Ankle-support waterproof hiking boots with Vibram soles",
            "Thermal merino wool base layers and wool socks",
            "Swimsuit for geothermal lagoon soaking"
        ],
        "days": [
            {
                "title": "Roaring Water Curtains, Basalt Sea Stacks & Glacial Lagoons",
                "neighborhood": "South Coast & Vík í Mýrdal",
                "vibe_summary": "Raw primal volcanic earth meeting the North Atlantic Ocean",
                "daily_steps_estimate": "10,500 steps (Waterfall trails + glacier crampon hike)",
                "rest_break": {
                    "time_slot": "02:45 PM - 03:45 PM",
                    "activity_name": "☕ Warm Arctic Lamb Soup Recharge in Skógar Country Lodge",
                    "location_name": "Skógar Country Lodge",
                    "tip": "Dry off from waterfall mist by the log stove with steaming lamb soup and unlimited crusty bread refills."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Walk Behind the Cascading Veil of Seljalandsfoss",
                        "image_url": "https://images.unsplash.com/photo-1476610182048-b716b8518aae?auto=format&fit=crop&w=800&q=80",
                        "category": "Glacial Waterfall Wonder",
                        "time_slot": "08:30 AM - 10:30 AM",
                        "location_name": "Seljalandsfoss & Gljúfrabúi Hidden Canyon Falls",
                        "neighborhood": "South Coast Highway 1",
                        "estimated_price": "$7",
                        "cost_tier": "$",
                        "ticket_requirement": "Free waterfall, parking fee (1000 ISK)",
                        "vibe_tags": ["#Seljalandsfoss", "#WaterfallVeil", "#RawNature"],
                        "crowd_meter": "Morning serenity (3/10 crowd)",
                        "insider_booking_tip": "Put on full waterproof gear before entering the path. Follow the path behind the 60-meter crashing water column into the mossy cave.",
                        "photo_spot_tip": "From inside the cave behind the waterfall looking out through the sheet of falling water toward the golden green coastal plain.",
                        "food_spot": "Rye Bread Bakery (Geothermally baked rúgbrauð served warm with butter and smoked Arctic char)",
                        "transit_to_next": {
                            "mode": "🚗 Scenic Ring Road Highway 1 Drive",
                            "duration": "25 mins along dramatic sea cliffs",
                            "cost": "Rental gas",
                            "instructions": "Drive east along Route 1 passing the Eyjafjallajökull volcano glacier directly to Sólheimajökull glacier parking."
                        }
                    },
                    {
                        "activity_name": "Sólheimajökull Blue Ice Glacier Hike & Crevasse Exploration",
                        "image_url": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=800&q=80",
                        "category": "Glacier Expedition & Ancient Ice",
                        "time_slot": "11:30 AM - 02:30 PM",
                        "location_name": "Sólheimajökull Glacier Tongue",
                        "neighborhood": "Mýrdalsjökull Ice Cap",
                        "estimated_price": "$75",
                        "cost_tier": "$$$",
                        "ticket_requirement": "Crampons & certified glacier guide mandatory",
                        "vibe_tags": ["#GlacierHike", "#BlueIce", "#CramponsOn"],
                        "crowd_meter": "Guided groups only (3/10)",
                        "insider_booking_tip": "Drink the meltwater directly from clean glacial streams with your hands—it is the purest 800-year-old water on Earth.",
                        "photo_spot_tip": "Framed inside a deep blue ice canyon with crampons dug into the ancient crystal ice.",
                        "food_spot": "Skógar Country Cafe (Hearty traditional Icelandic lamb meat soup kjötsúpa with unlimited refills)",
                        "transit_to_next": {
                            "mode": "🚗 Highway 1 Eastbound to the Coast",
                            "duration": "22 mins",
                            "cost": "Rental gas",
                            "instructions": "Follow Highway 1 through volcanic sand plains straight to the black sand coast of Reynisfjara."
                        }
                    },
                    {
                        "activity_name": "Reynisfjara Black Sand Beach & Basalt Columns",
                        "image_url": "https://images.unsplash.com/photo-1529963183134-61a90db47eaf?auto=format&fit=crop&w=800&q=80",
                        "category": "Volcanic Basalt Pillars & Atlantic Ocean",
                        "time_slot": "04:00 PM - 06:30 PM",
                        "location_name": "Reynisfjara Beach & Reynisdrangar Sea Stacks",
                        "neighborhood": "Vík",
                        "estimated_price": "$0",
                        "cost_tier": "$",
                        "ticket_requirement": "Free Access (Respect yellow/red warning lights)",
                        "vibe_tags": ["#BlackSandBeach", "#BasaltColumns", "#VíkIceland"],
                        "crowd_meter": "Eerie atmosphere (5/10)",
                        "insider_booking_tip": "Look up at the cliff face in summer to see nesting puffins. Marvel at the Gardar hexagonal basalt column cliff resembling an organ pipe.",
                        "photo_spot_tip": "Sitting on the natural geometric stepped basalt columns with the black sand and sea stacks framed in the background.",
                        "food_spot": "Smiðjan Brugghús in Vík (Smoked pulled pork burgers & local Icelandic craft IPA)",
                        "transit_to_next": {
                            "mode": "🚗 5-min drive to Vík Village Basecamp",
                            "duration": "5 mins",
                            "cost": "Free",
                            "instructions": "Drive over the headland into the quiet coastal village of Vík to your heated cabin or design hostel."
                        }
                    }
                ]
            }
        ]
    },
    "swiss alps": {
        "destination_display": "Swiss Alps (Lauterbrunnen / Mürren / Zermatt) 🇨🇭",
        "environment_type": "Glacial Mountain Peaks, 300-Meter Waterfalls & Alpine Wildflower Valleys",
        "hero_image": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["The Matterhorn Jagged Peak", "Staubbach 300m Waterfall", "Lake Brienz Turquoise Glacial Waters", "Eiger North Face", "Aletsch Glacier Ice Stream"],
        "basecamp": {
            "strategic_area": "Lauterbrunnen Valley (Central hub connecting all mountain trains and cable cars)",
            "hostel_pick": {
                "name": "Valley Hostel Lauterbrunnen",
                "price": "$46/night",
                "rating": "9.4/10 (Legendary)",
                "vibe": "Traditional wooden chalet sitting right at the foot of the 300m Staubbach waterfall with guest kitchen"
            },
            "boutique_pick": {
                "name": "Hotel Eiger Mürren",
                "price": "$210/night",
                "rating": "9.6/10",
                "vibe": "Car-free cliffside luxury with indoor panoramic pool facing the Eiger mountain"
            },
            "rest_strategy": "Mountain hiking causes high muscle fatigue due to elevation gains. Use the cable cars and mountain trains to ascend, and do gentle downhill walks. Schedule a 4:00 PM hot cocoa/fondue rest."
        },
        "transit_system": "Swiss Federal Railways (SBB) + Mountain Cogwheels & Cable Cars",
        "spotify_playlist": {
            "title": "Swiss Alpine Serenade: Acoustic Echoes & Mountain Air",
            "genre": "Acoustic Folk / Cinematic Alpine Ambient",
            "tracks": ["Lauterbrunnen Mist - Alpine Strings", "Matterhorn Mirror - Chill Guitar", "Cowbell Valley - Swiss Folk", "Glacier Breeze - Mountain Air"]
        },
        "aesthetic_summary": "Wooden chalets framed by plunging 300-meter waterfall cliffs in Lauterbrunnen, mirror reflections of the Matterhorn in alpine lakes, and bubbling cheese fondue by the fire.",
        "genz_hacks": [
            "Download the 'SBB' Swiss Railways app—trains connect to mountain cogwheels and cable cars with second-exact precision.",
            "Never buy bottled water—fill your water bottle for free from any village carved wooden trough; it is pure melted alpine glacier water.",
            "Take the early 07:30 AM cogwheel train to Gornergrat or Jungfraujoch before clouds gather over the mountain peaks.",
            "Buy a Swiss Half Fare Card if staying more than 3 days to cut all train and mountain cable car costs in half."
        ],
        "packing_essentials": [
            "Sturdy waterproof hiking shoes with deep tread soles",
            "Windproof and waterproof shell jacket (alpine weather shifts quickly)",
            "Refillable metal water bottle for crystal glacier trough refills",
            "High-protection SPF50 sunblock (high altitude UV radiation is intense)"
        ],
        "days": [
            {
                "title": "Waterfall Valley of 72 Cascades, Cliff Walks & Bubbling Fondue",
                "neighborhood": "Lauterbrunnen & Mürren Valley",
                "vibe_summary": "Tolkien's Rivendell come to life beneath vertical limestone peaks",
                "daily_steps_estimate": "11,000 steps (Gentle alpine paved walk + cable cars)",
                "rest_break": {
                    "time_slot": "03:45 PM - 04:45 PM",
                    "activity_name": "🍫 Hot Swiss Cocoa & Alpine Terrace Rest",
                    "location_name": "Hotel Regina Mürren Sun Terrace",
                    "tip": "Sit on the wooden sun deck wrapped in a wool blanket, sipping hot Swiss chocolate while watching paragliders float over the valley."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Staubbach Waterfall Stroll & Alpine Chalet Meadow Walk",
                        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
                        "category": "Colossal Waterfall & Alpine Valley",
                        "time_slot": "08:00 AM - 10:30 AM",
                        "location_name": "Lauterbrunnen Valley & Staubbach Falls",
                        "neighborhood": "Bernese Oberland",
                        "estimated_price": "$0",
                        "cost_tier": "$",
                        "ticket_requirement": "Free Public Access",
                        "vibe_tags": ["#Lauterbrunnen", "#StaubbachFalls", "#AlpineDream"],
                        "crowd_meter": "Serene dawn (2/10 crowd)",
                        "insider_booking_tip": "Lauterbrunnen has 72 waterfalls plunging down sheer 300-meter cliffs. Walk the paved valley trail towards Stechelberg listening to the distant chime of cowbells.",
                        "photo_spot_tip": "Looking down the village road with traditional flower-box wooden chalets on both sides and Staubbach Falls plunging from the cliff directly behind.",
                        "food_spot": "Airtime Cafe Lauterbrunnen (Freshly baked warm blueberry scones & Swiss roast coffee)",
                        "transit_to_next": {
                            "mode": "🚠 Stechelberg Mountain Cable Car",
                            "duration": "10 mins soaring up the vertical cliff",
                            "cost": "$8.00 (Free with Swiss Pass)",
                            "instructions": "Take postbus 141 to Stechelberg cable car station. Board the cable car up to the car-free cliff village of Mürren."
                        }
                    },
                    {
                        "activity_name": "Car-Free Mürren Cliff Walk & Paraglider Launch Overlook",
                        "image_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80",
                        "category": "Cliffside Alpine Village & Paragliding Vibe",
                        "time_slot": "11:30 AM - 02:30 PM",
                        "location_name": "Mürren Village & Allmendhubel",
                        "neighborhood": "Mürren (1638m altitude)",
                        "estimated_price": "$15",
                        "cost_tier": "$$",
                        "ticket_requirement": "Cable car from Stechelberg to Mürren",
                        "vibe_tags": ["#Murren", "#CarFreeVillage", "#EigerView"],
                        "crowd_meter": "Peaceful hikers (3/10)",
                        "insider_booking_tip": "Mürren has no cars—only electric luggage carts. Sit on the wooden bench at the cliff edge watching colorful tandem paragliders leap into the abyss.",
                        "photo_spot_tip": "Sitting on the cliff edge wooden fence with the snow-covered Eiger, Mönch, and Jungfrau peaks rising directly opposite across the valley.",
                        "food_spot": "Restaurant Stägerstübli (Traditional Swiss potato rösti with melted raclette cheese, smoked bacon and fried farm egg)",
                        "transit_to_next": {
                            "mode": "🚠 Mountain Train & Cable Car Descent",
                            "duration": "14 mins scenic descent",
                            "cost": "$6.00",
                            "instructions": "Take the scenic mountain cogwheel train to Grütschalp, then float down in the cable car back into Lauterbrunnen valley."
                        }
                    },
                    {
                        "activity_name": "Bubbling Gruyère Cheese Fondue by the Open Log Fire",
                        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80",
                        "category": "Authentic Alpine Gastronomy",
                        "time_slot": "06:30 PM - 09:30 PM",
                        "location_name": "Hotel Oberland Fondue Stübli",
                        "neighborhood": "Lauterbrunnen",
                        "estimated_price": "$38",
                        "cost_tier": "$$$",
                        "ticket_requirement": "Table reservation recommended",
                        "vibe_tags": ["#FondueNight", "#SwissCheese", "#AlpineWarmth"],
                        "crowd_meter": "Cozy & warm (4/10)",
                        "insider_booking_tip": "Swirl your cube of crusty rustic bread in a figure-eight motion through the bubbling molten Gruyère and Vacherin Fribourgeois cheese. Drink hot black tea or white Fendant wine, never cold water.",
                        "photo_spot_tip": "The dramatic cheese pull lifting the crusty bread cube from the bubbling cast-iron caquelon pot.",
                        "food_spot": "Läderach Boutique (Hand-broken slabs of fresh Swiss chocolate studded with roasted Piedmont hazelnuts)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk back to Valley Hostel Basecamp",
                            "duration": "4 mins walk through village",
                            "cost": "Free",
                            "instructions": "Short lantern-lit walk through Lauterbrunnen village with the mist of the illuminated waterfall in the evening air."
                        }
                    }
                ]
            }
        ]
    },
    "kyoto": {
        "destination_display": "Kyoto, Japan 🎋",
        "environment_type": "Ancient Cedar Forests, Bamboo Groves & Sacred Mountain Torii Gates",
        "hero_image": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Arashiyama Bamboo Grove", "Mount Inari Sacred Trail", "Kamo River Waterway", "Hozu River Ravine", "Philosopher's Path Canal"],
        "basecamp": {
            "strategic_area": "Gion-Shijo or Kawaramachi (Walkable to riverside dining & Hankyu/Keihan lines)",
            "hostel_pick": {
                "name": "Len Kyoto Kawaramachi / Piece Hostel Sanjo",
                "price": "$34/night",
                "rating": "9.4/10 (Superb)",
                "vibe": "Artistic cafe-lounge with natural wood finishes, quiet tatami dorm pods & specialty barista roastery"
            },
            "boutique_pick": {
                "name": "Sowaka Ryokan & Heritage Hotel",
                "price": "$220/night",
                "rating": "9.7/10 (Exceptional)",
                "vibe": "Restored 100-year-old traditional sukiya-style teahouse estate with private moss garden courtyards"
            },
            "rest_strategy": "Kyoto temple complexes feature long gravel paths. Rest during the 1:30 PM - 3:00 PM tour rush with a ceremonial matcha bowl in a shaded temple veranda."
        },
        "transit_system": "Kyoto City Bus & Hankyu/Keihan Subways (Contactless IC card / Suica / Pasmo accepted)",
        "spotify_playlist": {
            "title": "Kyoto Zen: Shamisen & Rain on Cedar",
            "genre": "Traditional Japanese Ambient / Zen Lofi",
            "tracks": ["Bamboo Rain - Koto Solo", "Fushimi Dawn - Zen Bells", "Pontocho Evening - Shamisen Drift", "Gion Moonlit Walk"]
        },
        "aesthetic_summary": "Whispering bamboo groves at early dawn, 10,000 orange mountain torii gates, riverside dining on elevated wooden decks, and authentic Uji matcha ceremonies.",
        "genz_hacks": [
            "Fushimi Inari Torii Gates are open 24/7—visit at 6:30 AM or 10:00 PM for an eerie, quiet walk with zero crowds.",
            "Rent a retro bicycle to cruise along the flat, scenic Kamo River path from Gion up to the Imperial Palace.",
            "Respect Geiko & Maiko in Gion—it is illegal to take photos of them on private streets (¥10,000 fine); admire from a polite distance.",
            "Book a kawayuka (open-air wooden veranda over the Kamogawa river) for dinner between May and September."
        ],
        "packing_essentials": [
            "Easy slip-on walking shoes (frequent shoe removal in temples and Zen gardens)",
            "Small hand towel (many traditional Japanese public restrooms do not have paper towels)",
            "Coin pouch for temple ema prayer plaques and fortunes (omikuji)",
            "UV parasol for gravel courtyard walks"
        ],
        "days": [
            {
                "title": "Whispering Bamboo Groves, Zen Rock Gardens & Riverside Matcha",
                "neighborhood": "Arashiyama & Sagano",
                "vibe_summary": "Verdant bamboo canopies and tranquil Zen rock reflections",
                "daily_steps_estimate": "12,200 steps (Paved paths + mountain slopes)",
                "rest_break": {
                    "time_slot": "02:30 PM - 03:30 PM",
                    "activity_name": "🍵 Ceremonial Uji Matcha & Moss Garden Rest",
                    "location_name": "Okochi Sanso Garden Teahouse",
                    "tip": "Sit on the open tatami veranda sipping freshly whisked frothy matcha overlooking the cedar forest."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Dawn Stroll Through Whispering Arashiyama Bamboo Grove",
                        "image_url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=800&q=80",
                        "category": "Sacred Nature & Towering Bamboo",
                        "time_slot": "07:00 AM - 09:00 AM",
                        "location_name": "Arashiyama Bamboo Grove & Okochi Sanso Villa",
                        "neighborhood": "Sagano / Arashiyama",
                        "estimated_price": "$7",
                        "cost_tier": "$",
                        "ticket_requirement": "Free bamboo path; ¥1000 for Okochi Sanso Villa garden (includes matcha)",
                        "vibe_tags": ["#BambooGrove", "#ZenMorning", "#Arashiyama"],
                        "crowd_meter": "Peaceful at 7am (2/10), swarmed by 10am",
                        "insider_booking_tip": "Arrive before 7:30 AM. Walk into Okochi Sanso Villa at the path's end—95% of tourists skip it, and you get an authentic cup of matcha and sweet bean cake overlooking Kyoto valley.",
                        "photo_spot_tip": "Look straight up at the 20-meter bamboo stalks swaying in the breeze at 0.5x wide angle to capture the circular sky opening.",
                        "food_spot": "% Arabica Kyoto Arashiyama (Iconic minimalist coffee bar sitting directly on the riverbank)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk along Riverbank",
                            "duration": "10 mins (700m)",
                            "cost": "Free",
                            "instructions": "Follow the riverside willow path east to Tenryu-ji Temple World Heritage garden."
                        }
                    },
                    {
                        "activity_name": "Tenryu-ji Temple Sogenchi Pond & Zen Reflections",
                        "image_url": "https://images.unsplash.com/photo-1545569341-9eb8b30979d9?auto=format&fit=crop&w=800&q=80",
                        "category": "World Heritage Zen Garden",
                        "time_slot": "10:30 AM - 01:00 PM",
                        "location_name": "Tenryu-ji Temple & Kosoan Teahouse",
                        "neighborhood": "Arashiyama",
                        "estimated_price": "$12",
                        "cost_tier": "$",
                        "ticket_requirement": "¥500 temple garden ticket",
                        "vibe_tags": ["#MatchaRitual", "#ZenGarden", "#Tenryuji"],
                        "crowd_meter": "Serene (4/10)",
                        "insider_booking_tip": "Sit quietly on the wooden veranda of the Hojo hall looking out across Sogenchi Pond with reflection of the Arashiyama mountains.",
                        "photo_spot_tip": "Framed silhouette through the sliding shoji paper screen looking into the moss and gravel rock garden.",
                        "food_spot": "Shigetsu inside Tenryu-ji (Temple vegetarian shojin ryori cuisine cooked by Zen monks)",
                        "transit_to_next": {
                            "mode": "🚋 Keifuku Randen Vintage Tram",
                            "duration": "22 mins scenic tram ride",
                            "cost": "$1.80 (¥250)",
                            "instructions": "Take the charming retro purple Randen tram from Arashiyama Station directly into central Kyoto."
                        }
                    },
                    {
                        "activity_name": "Pontocho Narrow Lantern Alley Kawayuka Dining",
                        "image_url": "https://images.unsplash.com/photo-1509099836639-18ba1795216d?auto=format&fit=crop&w=800&q=80",
                        "category": "Atmospheric Evening Dining on the River",
                        "time_slot": "06:30 PM - 09:30 PM",
                        "location_name": "Pontocho Alley & Kamo River Veranda",
                        "neighborhood": "Gion / Kawaramachi",
                        "estimated_price": "$35",
                        "cost_tier": "$$$",
                        "ticket_requirement": "Reserve riverside terrace table ahead",
                        "vibe_tags": ["#PontochoAlley", "#KawayukaDining", "#Lanterns"],
                        "crowd_meter": "Atmospheric (6/10)",
                        "insider_booking_tip": "Walk down the cobblestone alley only 2 meters wide lit by red paper lanterns. Listen for the sound of the wooden river platforms.",
                        "photo_spot_tip": "Standing in Pontocho Alley as red chochin lanterns illuminate the aged cedar facades and stone pavement.",
                        "food_spot": "Gion Duck Noodles (Award-winning French-Japanese duck ramen with white broth and sansho pepper)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk back to Basecamp",
                            "duration": "5 mins walk across bridge",
                            "cost": "Free",
                            "instructions": "Cross Shijo Bridge over the Kamo River straight back into your Kawaramachi boutique hostel."
                        }
                    }
                ]
            }
        ]
    },
    "barcelona": {
        "destination_display": "Barcelona, Spain 🇪🇸",
        "environment_type": "Mediterranean Beach Promenade, Gothic Quarter Alleys & Surrealist Gaudí Architecture",
        "hero_image": "https://images.unsplash.com/photo-1583422409516-2895a77efded?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Montjuïc Hill & Mediterranean Overlook", "Bogatell & Barceloneta Beaches", "Parc de la Ciutadella Palm Gardens", "Tibidabo Mountain Peak", "Carmel Bunkers Panoramic Vista"],
        "basecamp": {
            "strategic_area": "El Born or Eixample (Walkable to Gothic Quarter, Ciutadella park and beaches)",
            "hostel_pick": {
                "name": "Yeah Hostel Barcelona / Casa Gracia",
                "price": "$36/night",
                "rating": "9.5/10 (Top Rated)",
                "vibe": "Design boutique hostel with pod beds, communal family paella dinners & swimming pool roof terrace"
            },
            "boutique_pick": {
                "name": "Yurbban Passage Hotel & Spa",
                "price": "$175/night",
                "rating": "9.4/10",
                "vibe": "Industrial-chic sanctuary in El Born with 360-degree rooftop pool overlooking the Sagrada Família"
            },
            "rest_strategy": "The Spanish siesta is a necessity: do not push through the 2:00 PM - 5:00 PM heat. Rest in a shaded plaza or beachfront cafe before the late 9:00 PM dinner culture."
        },
        "transit_system": "TMB Metro & Bicing city bike sharing (T-Casual 10-ride contactless ticket)",
        "spotify_playlist": {
            "title": "Barcelona Sun: Mediterranean Deep House & Flamenco Chill",
            "genre": "Spanish Chillout / Balearic House",
            "tracks": ["Barcelona Sun - Acoustic Guitar", "Bogatell Breeze - Sunset Deep", "El Born Night - Latin Grooves", "Gaudí Dreams - Ambient Chill"]
        },
        "aesthetic_summary": "Intricate stone spires of Sagrada Família bathed in stained-glass rainbow light, bustling tapas counters in El Born, and sunset views from Bunkers del Carmel.",
        "genz_hacks": [
            "Book Sagrada Família tickets 3 weeks ahead for the 4:30 PM slot—afternoon sunlight blasts through red and amber stained glass.",
            "Watch your phone in Metro stations and Las Ramblas—wear a crossbody bag strapped to your front.",
            "Head to Bunkers del Carmel for the finest free 360° sunset view over the entire city and Mediterranean sea.",
            "Dinner before 8:30 PM is only for tourists—locals arrive at tapas bars at 9:30 PM."
        ],
        "packing_essentials": [
            "Anti-theft crossbody bag or secure zip sling",
            "Polarized sunglasses for Mediterranean sea glare",
            "Breathable espadrilles or walking sneakers",
            "Light beach towel for impromptu sunset swims"
        ],
        "days": [
            {
                "title": "Rainbow Stained Glass, Gothic Labyrinths & Seaside Tapas",
                "neighborhood": "Eixample, Gothic Quarter & Barceloneta",
                "vibe_summary": "Surrealist architectural awe into sun-drenched coastal tapas culture",
                "daily_steps_estimate": "13,000 steps (Flat walking & coastal boardwalk)",
                "rest_break": {
                    "time_slot": "03:30 PM - 04:30 PM",
                    "activity_name": "☕ Shaded Siesta in Plaça Reial under Palm Trees",
                    "location_name": "Plaça Reial Fountain Arcade",
                    "tip": "Sit on the stone fountain terrace enjoying an icy café con hielo and watching street musicians under royal palms."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Sagrada Família Stained Glass Light Symphony",
                        "image_url": "https://images.unsplash.com/photo-1583422409516-2895a77efded?auto=format&fit=crop&w=800&q=80",
                        "category": "Masterpiece Architecture",
                        "time_slot": "09:00 AM - 11:30 AM",
                        "location_name": "Basílica de la Sagrada Família",
                        "neighborhood": "Eixample",
                        "estimated_price": "$28",
                        "cost_tier": "$$",
                        "ticket_requirement": "Online booking mandatory with timed audio entry",
                        "vibe_tags": ["#SagradaFamilia", "#GaudiMagic", "#RainbowLight"],
                        "crowd_meter": "Moderate morning (4/10)",
                        "insider_booking_tip": "Look up at the tree-trunk columns branching into leafy stone canopies. The eastern windows shine cool blues and greens, while western windows blaze fiery red and orange.",
                        "photo_spot_tip": "Position phone camera in portrait mode looking straight up from the central nave to catch the kaleidoscope ceiling.",
                        "food_spot": "Pastisseria Escribà (Legendary Catalan crema catalana pastries & fresh orange juice)",
                        "transit_to_next": {
                            "mode": "🚇 Metro Line L4",
                            "duration": "12 mins",
                            "cost": "$1.20 (T-Casual)",
                            "instructions": "Take Metro Line 4 from Verdaguer to Jaume I directly into the Gothic Quarter."
                        }
                    },
                    {
                        "activity_name": "Gothic Quarter Secret Courtyards & El Born Tapas Crawl",
                        "image_url": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?auto=format&fit=crop&w=800&q=80",
                        "category": "Medieval Alleys & Culinary Delights",
                        "time_slot": "12:00 PM - 03:00 PM",
                        "location_name": "Plaça del Rei, El Born & Santa Maria del Mar",
                        "neighborhood": "El Born / Barri Gòtic",
                        "estimated_price": "$18",
                        "cost_tier": "$$",
                        "ticket_requirement": "Free walk-in",
                        "vibe_tags": ["#GothicQuarter", "#ElBorn", "#TapasTime"],
                        "crowd_meter": "Lively (5/10)",
                        "insider_booking_tip": "Order 'Patatas Bravas' with smoky salsa and garlic aioli, paired with pan con tomate (toasted bread rubbed with garlic and ripe tomato pulp).",
                        "photo_spot_tip": "The neo-Gothic Bishop's Bridge (Pont del Bisbe) on Carrer del Bisbe framing the cobblestone alley.",
                        "food_spot": "El Xampanyet (Iconic bustling sparkling cava bar with cured Iberian ham and anchovies)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk through Ciutadella Park",
                            "duration": "15 mins stroll under palm trees",
                            "cost": "Free",
                            "instructions": "Walk through the ornate gates of Parc de la Ciutadella directly south to Barceloneta beach."
                        }
                    },
                    {
                        "activity_name": "Bogatell Beach Sunset Swim & Mediterranean Paella",
                        "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
                        "category": "Coastal Sunset & Seafood Feast",
                        "time_slot": "06:00 PM - 09:30 PM",
                        "location_name": "Bogatell Beach & Xiringuito Escribà",
                        "neighborhood": "Poblenou / Barceloneta",
                        "estimated_price": "$32",
                        "cost_tier": "$$$",
                        "ticket_requirement": "Table reservation for beachside paella recommended",
                        "vibe_tags": ["#BeachSunset", "#SeafoodPaella", "#MediterraneanVibes"],
                        "crowd_meter": "Golden hour glow (5/10)",
                        "insider_booking_tip": "Skip noisy Barceloneta beach—Bogatell is cleaner, wider, and filled with local volleyball players. Enjoy authentic socarrat (crispy caramelized rice crust) at the bottom of the paella pan.",
                        "photo_spot_tip": "Sitting on the golden sand with the Mediterranean waves and the distant silhouette of the W Hotel Sail in the golden twilight.",
                        "food_spot": "Xiringuito Escribà (Open-air beachfront charcoal paella with king prawns and saffron rice)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk back to Basecamp",
                            "duration": "12 mins walk",
                            "cost": "Free",
                            "instructions": "Stroll down the tree-lined Rambla del Poblenou back to your boutique basecamp."
                        }
                    }
                ]
            }
        ]
    },
    "bangkok": {
        "destination_display": "Bangkok, Thailand 🇹🇭",
        "environment_type": "Tropical River Canals, Golden Stupas & Sizzling Night Woks",
        "hero_image": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Chao Phraya River & Canal Waterways", "Lumphini Park Tropical Lake & Monitor Lizards", "Bang Kachao 'Green Lung' Jungle Peninsula", "Historic Klong Canals"],
        "basecamp": {
            "strategic_area": "Thonglor or Sathorn / Riverside (Easy BTS skytrain & river boat connections)",
            "hostel_pick": {
                "name": "The Yard Hostel Ari / Lub d Bangkok Siam",
                "price": "$22/night",
                "rating": "9.4/10 (Superb)",
                "vibe": "Eco-friendly shipping-container design oasis set in a quiet lush garden with hammocks & craft beer"
            },
            "boutique_pick": {
                "name": "The Mustang Blu (Chinatown)",
                "price": "$110/night",
                "rating": "9.5/10 (Exceptional)",
                "vibe": "Colonial 19th-century bank turned vintage botanical wonderland with curved iron balconies & roll-top tubs"
            },
            "rest_strategy": "Midday Bangkok heat and humidity can lead to heat exhaustion. Retreat into air-conditioned shopping galleries, botanical cafes, or a 1-hour Thai massage between 1:00 PM and 3:30 PM."
        },
        "transit_system": "BTS Skytrain + Chao Phraya Express Boat (Orange Flag Boat 16 THB cash) + Grab app",
        "spotify_playlist": {
            "title": "Bangkok Night Neon & Thai Funk",
            "genre": "Thai Funk / Molam Beats / Rooftop Chill",
            "tracks": ["Chao Phraya Sunset - Thai Funk", "Yaowarat Neon - Bangkok Lofi", "Tichuca High - Tropical House", "Floating Market Beat"]
        },
        "aesthetic_summary": "Golden river stupas, tuk-tuk night food trails in Yaowarat Chinatown, leafy bicycle jungle sanctuaries, and glowing rooftop jellyfish bars.",
        "genz_hacks": [
            "Use the Chao Phraya Express Orange Flag Boat for 16 THB ($0.45)—it is the fastest, breeziest open-air river transport.",
            "Never believe tuk-tuk drivers who say the Grand Palace is 'closed today for a holiday'—it's a scam to take you to gem shops.",
            "Download 'Grab' or 'Bolt' for upfront fair taxi pricing; if taking a street taxi, always demand 'meter please'.",
            "Book a sunset table at Tichuca Rooftop Bar 5 days in advance to get right beneath the massive glowing LED jellyfish canopy."
        ],
        "packing_essentials": [
            "Loose, lightweight cotton/linen pants (mandatory to cover knees inside temples)",
            "Slip-on shoes for temple steps",
            "Pocket hand-held electric fan for Bangkok afternoon humidity",
            "Mosquito repellent for canal and park strolls"
        ],
        "days": [
            {
                "title": "Golden Porcelain Spires, Michelin Street Woks & Glowing Jungle Rooftop",
                "neighborhood": "Rattanakosin, Yaowarat & Thonglor",
                "vibe_summary": "Sacred riverside majesty into world-renowned street food fever",
                "daily_steps_estimate": "10,800 steps (Riverboats + street food walking)",
                "rest_break": {
                    "time_slot": "02:00 PM - 03:30 PM",
                    "activity_name": "💆 Traditional Royal Thai Foot Massage & Herbal Tea",
                    "location_name": "Wat Pho Traditional Massage School",
                    "tip": "Rest in an air-conditioned historic sanctuary for a 60-min authentic acupressure foot massage to eliminate fatigue."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Wat Arun Temple of Dawn Morning Porcelain Ascent",
                        "image_url": "https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=800&q=80",
                        "category": "Sacred Architectural Stupa",
                        "time_slot": "08:30 AM - 10:30 AM",
                        "location_name": "Wat Arun (Temple of Dawn)",
                        "neighborhood": "Bangkok Yai Riverbank",
                        "estimated_price": "$3",
                        "cost_tier": "$",
                        "ticket_requirement": "Entrance ticket (100 THB cash)",
                        "vibe_tags": ["#WatArun", "#PorcelainTemple", "#ChaoPhraya"],
                        "crowd_meter": "Pleasant morning (3/10)",
                        "insider_booking_tip": "Marvel at the millions of colorful broken Chinese porcelain ceramics decorating the 70-meter stupa. Rent a traditional Thai silk costume outside for viral photos.",
                        "photo_spot_tip": "Mid-tier steep staircase of the main stupa with the blue sky and Chao Phraya river framed behind you.",
                        "food_spot": "Mae Varee Sweet Mango Stand (Legendary mango sticky rice with warm coconut cream and crispy mung beans)",
                        "transit_to_next": {
                            "mode": "🚤 Chao Phraya Cross-River Ferry",
                            "duration": "5 mins breezy river crossing",
                            "cost": "$0.15 (5 THB)",
                            "instructions": "Board the local wooden cross-river ferry directly from Wat Arun pier across the water to Tha Tien pier for Wat Pho."
                        }
                    },
                    {
                        "activity_name": "Yaowarat Chinatown Tuk-Tuk Street Food Sizzle",
                        "image_url": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?auto=format&fit=crop&w=800&q=80",
                        "category": "World's Best Street Food Crawl",
                        "time_slot": "06:00 PM - 08:30 PM",
                        "location_name": "Yaowarat Road (Chinatown)",
                        "neighborhood": "Samphanthawong",
                        "estimated_price": "$12",
                        "cost_tier": "$",
                        "ticket_requirement": "Cash only at street stalls",
                        "vibe_tags": ["#StreetFoodKing", "#Yaowarat", "#PadThai"],
                        "crowd_meter": "Sensory overload & energetic (8/10)",
                        "insider_booking_tip": "Follow the open flame woks. Try Guay Tiew Kua Gai (stir-fried chicken flat noodles with runny egg) and toasted crispy buns stuffed with pandan custard.",
                        "photo_spot_tip": "Standing in the middle of Yaowarat Road with towering vertical neon Chinese signs glowing in red and gold in both directions.",
                        "food_spot": "Thip Samai Pad Thai (Egg-wrapped Pad Thai with giant prawns cooked over roaring charcoal woks)",
                        "transit_to_next": {
                            "mode": "🛺 Neon Tuk-Tuk Ride to Thonglor",
                            "duration": "20 mins wind in your hair",
                            "cost": "$4.50 (150 THB)",
                            "instructions": "Hail a neon LED lit tuk-tuk to weave through Bangkok traffic straight to T-One Building in Thonglor."
                        }
                    },
                    {
                        "activity_name": "Tichuca 46th-Floor Jungle Rooftop & Glowing Jellyfish Bar",
                        "image_url": "https://images.unsplash.com/photo-1519451241324-20b4ea2c4220?auto=format&fit=crop&w=800&q=80",
                        "category": "Viral Rooftop Lounge & Skyscraper Views",
                        "time_slot": "09:00 PM - 12:00 AM",
                        "location_name": "Tichuca Rooftop Bar at T-One Building",
                        "neighborhood": "Thonglor",
                        "estimated_price": "$22",
                        "cost_tier": "$$",
                        "ticket_requirement": "Walk-in with passport ID check (Expect queue after 9pm)",
                        "vibe_tags": ["#TichucaRooftop", "#JellyfishBar", "#BangkokNightlife"],
                        "crowd_meter": "Buzzing Gen-Z hotspot (7/10)",
                        "insider_booking_tip": "Order a signature tiki cocktail served in a whole fresh pineapple. Watch the 20-meter fiber-optic glowing tree change colors to the house music beat.",
                        "photo_spot_tip": "Looking up into the illuminated fiber-optic tendrils of the massive glowing tree with the Bangkok skyline lights below.",
                        "food_spot": "Late-night street noodle cart outside Thonglor BTS station",
                        "transit_to_next": {
                            "mode": "🚝 BTS Skytrain",
                            "duration": "6 mins",
                            "cost": "$0.90",
                            "instructions": "Ride the BTS Skytrain 2 stops back to your basecamp hotel or boutique hostel."
                        }
                    }
                ]
            }
        ]
    },
    "dubai": {
        "destination_display": "Dubai, UAE 🇦🇪",
        "environment_type": "Arabian Desert Dunes, Persian Gulf Waters & Futuristic Skyscraper Canyons",
        "hero_image": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Arabian Red Sand Desert", "Persian Gulf Coastal Reefs", "Dubai Creek Historic Estuary", "Palm Jumeirah Archipelago", "Al Marmoom Desert Conservation Reserve"],
        "basecamp": {
            "strategic_area": "Downtown Dubai or Dubai Marina (Direct driverless Red Line Metro access)",
            "hostel_pick": {
                "name": "Green Sky Hostel Dubai Marina / Rove Downtown",
                "price": "$38/night",
                "rating": "9.2/10",
                "vibe": "High-floor skyscraper hostel with panoramic marina yacht views, gym & swimming pool access"
            },
            "boutique_pick": {
                "name": "25hours Hotel One Central",
                "price": "$185/night",
                "rating": "9.6/10 (Exceptional)",
                "vibe": "Ultra-creative design hub overlooking Museum of the Future with pottery studio & rooftop pool"
            },
            "rest_strategy": "Midday desert temperatures are intense. Schedule outdoor desert safari or beach activities strictly after 4:30 PM. Spend 12:00 PM - 3:30 PM in climate-controlled architectural spaces."
        },
        "transit_system": "Dubai Metro (Driverless Red Line with Nol Silver Card) & 1-AED historic abra boats",
        "spotify_playlist": {
            "title": "Dubai Sunset Dunes: Desert Chill & Deep Tech",
            "genre": "Arabic Lounge / Desert Deep House",
            "tracks": ["Desert Mirage - Arabic Strings", "Burj Skyline - Deep House", "Souk Spice - Oriental Chill", "Gulf Breeze - Sunset Vibe"]
        },
        "aesthetic_summary": "Golden desert sand dunes at sunset, calligraphy architectural torus museums, 1-dirham historic wooden boat rides, and futuristic fountain choreography.",
        "genz_hacks": [
            "Ride the traditional wooden 'Abra' boat across Dubai Creek for just 1 AED ($0.27) to experience historic Old Dubai.",
            "Take the driverless Dubai Metro Gold Class (front car) for an unobstructed front-window view through the Sheikh Zayed Road futuristic skyscrapers.",
            "Museum of the Future sells out weeks in advance—book tickets 1 month ahead on the official portal.",
            "Drink plenty of water and wear breathable fabrics; midday outdoor sun can exceed 40°C in summer."
        ],
        "packing_essentials": [
            "High-grade sunglasses with polarized UV lenses (intense desert reflection)",
            "Light breathable linen shirts and modest clothing for visiting historic areas and mosques",
            "Refillable insulated water bottle to keep water ice-cold in heat",
            "Camera lens cleaning cloth for fine desert sand"
        ],
        "days": [
            {
                "title": "Calligraphy Horizons, Historic Creek Abras & Starlit Desert Dunes",
                "neighborhood": "Downtown Dubai, Old Deira & Arabian Desert",
                "vibe_summary": "Hyper-futuristic wonders into ancient spice souks and desert tranquility",
                "daily_steps_estimate": "10,200 steps (Metro rides + air-conditioned museum)",
                "rest_break": {
                    "time_slot": "02:30 PM - 03:30 PM",
                    "activity_name": "☕ Iced Arabic Saffron Latte in Arabian Tea House Courtyard",
                    "location_name": "Arabian Tea House in Al Fahidi Historic Quarter",
                    "tip": "Sit in a white-and-turquoise shaded courtyard under a historic banyan tree with cold mint lemonade and fresh dates."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Museum of the Future Aerodynamic Torus Exploration",
                        "image_url": "https://images.unsplash.com/photo-1580674684081-7617fbf3d745?auto=format&fit=crop&w=800&q=80",
                        "category": "Futuristic Architecture & Innovation",
                        "time_slot": "09:30 AM - 12:00 PM",
                        "location_name": "Museum of the Future",
                        "neighborhood": "Sheikh Zayed Road",
                        "estimated_price": "$40",
                        "cost_tier": "$$$",
                        "ticket_requirement": "Online booking required weeks ahead",
                        "vibe_tags": ["#MuseumOfTheFuture", "#CalligraphyBuilding", "#Architecture"],
                        "crowd_meter": "Timed entry (4/10)",
                        "insider_booking_tip": "Step onto the open-air viewing deck inside the oval void of the building. You stand inside the torus with Arabic calligraphy cut directly into the stainless steel walls.",
                        "photo_spot_tip": "Low-angle shot from the ground garden looking up at the 77-meter seamless stainless steel facade inscribed with Sheikh Mohammed's poems.",
                        "food_spot": "Al Fanar Emirati Restaurant (Traditional balaleet sweet cardamom vermicelli & warm khobz flatbread)",
                        "transit_to_next": {
                            "mode": "🚇 Metro Red Line (Driverless)",
                            "duration": "14 mins",
                            "cost": "$1.50 (5 AED via Nol Card)",
                            "instructions": "Ride Metro Red Line north from Emirates Towers Station directly to Union or Al Fahidi Station."
                        }
                    },
                    {
                        "activity_name": "1-Dirham Abra Ride Across Dubai Creek & Spice Souk",
                        "image_url": "https://images.unsplash.com/photo-1546412414-e1885259563a?auto=format&fit=crop&w=800&q=80",
                        "category": "Historic Heritage & Fragrant Bazaars",
                        "time_slot": "01:00 PM - 03:00 PM",
                        "location_name": "Dubai Creek Abra Station & Deira Spice Souk",
                        "neighborhood": "Old Deira / Al Fahidi",
                        "estimated_price": "$3",
                        "cost_tier": "$",
                        "ticket_requirement": "1 AED coin paid directly to boat captain",
                        "vibe_tags": ["#OldDubai", "#AbraBoat", "#SpiceSouk"],
                        "crowd_meter": "Bustling historic commerce (5/10)",
                        "insider_booking_tip": "Smell the fragrant saffron, dried Persian limes, frankincense, and cardamom in the covered alleys of the Spice Souk. Friendly haggling is expected.",
                        "photo_spot_tip": "Sitting on the low wooden bench of the abra boat as traditional dhow cargo ships pass by on the glistening creek.",
                        "food_spot": "Al Ustad Special Kabab (Legendary yogurt-marinated melt-in-mouth chicken and mutton skewers served since 1978)",
                        "transit_to_next": {
                            "mode": "🚙 4x4 Land Cruiser Desert Transport",
                            "duration": "45 mins highway drive",
                            "cost": "Included in desert safari tour",
                            "instructions": "Your licensed desert safari driver picks you up right outside Al Fahidi for the red dunes of Lahbab."
                        }
                    },
                    {
                        "activity_name": "Golden Hour Red Sand Desert Dune Bashing & Starlit Campfire",
                        "image_url": "https://images.unsplash.com/photo-1451337516015-6b6e9a44a8a3?auto=format&fit=crop&w=800&q=80",
                        "category": "Desert Nature & Sunset Horizon",
                        "time_slot": "05:00 PM - 08:30 PM",
                        "location_name": "Lahbab Red Dunes Desert",
                        "neighborhood": "Dubai Desert Conservation",
                        "estimated_price": "$45",
                        "cost_tier": "$$",
                        "ticket_requirement": "Pre-booked 4x4 desert excursion",
                        "vibe_tags": ["#RedDunes", "#DesertSunset", "#BedouinCamp"],
                        "crowd_meter": "Wide open desert (3/10)",
                        "insider_booking_tip": "Take off your shoes and walk barefoot up the sharp crest of a 50-meter red sand dune at golden hour. Sandboarding down the dune face is included.",
                        "photo_spot_tip": "Standing on the razor-sharp dune crest casting long evening shadows across the wind-rippled red sand at sunset.",
                        "food_spot": "Desert Camp BBQ (Grilled kofta skewers, warm garlic pita, creamy hummus & sweet mint tea)",
                        "transit_to_next": {
                            "mode": "🚙 4x4 Drive back to Hotel",
                            "duration": "40 mins night drive",
                            "cost": "Included in excursion",
                            "instructions": "Relax in air-conditioned comfort as your driver brings you straight back to your basecamp."
                        }
                    }
                ]
            }
        ]
    },
    "seoul": {
        "destination_display": "Seoul, South Korea 🇰🇷",
        "environment_type": "Surrealist Concrete Architecture, Ancient Royal Palaces & Neon Night Markets",
        "hero_image": "https://images.unsplash.com/photo-1538485399081-7191377e8241?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Namsan Mountain & Pine Forest", "Han River Park Waterfront", "Bukhansan Granite Peaks National Park", "Cheonggyecheon Stream Walkway", "Seoul Forest Eco-Park"],
        "basecamp": {
            "strategic_area": "Hongdae or Seongsu-dong (Young indie vibe, subway lines 2 & airport express)",
            "hostel_pick": {
                "name": "Zzzip Guesthouse Hongdae / Time Travelers Party Hostel",
                "price": "$30/night",
                "rating": "9.6/10 (Legendary)",
                "vibe": "Ultra-clean boutique guesthouse with warm heated ondol floors, free ramyeon bar & street busker proximity"
            },
            "boutique_pick": {
                "name": "Ryse, Autograph Collection Hongdae",
                "price": "$170/night",
                "rating": "9.5/10 (Exceptional)",
                "vibe": "Art-curated creative hotel with vinyl listening library, streetwear boutique & rooftop cocktail bar"
            },
            "rest_strategy": "Seoul involves numerous subway stairways and steep hillside neighborhoods. Plan an afternoon jjimjilbang (Korean traditional bathhouse) soak and heated salt room nap to recharge."
        },
        "transit_system": "Seoul Metro & T-Money Card (100% contactless across all subway lines, buses & convenience stores)",
        "spotify_playlist": {
            "title": "Seoul Nights: K-Indie & Rainy Hongdae Lofi",
            "genre": "Korean Indie / Chill R&B / Synthwave",
            "tracks": ["Hongdae Midnight - K-Indie", "Han River Bicycle - Chill Beats", "Seongsu Cafe - Aesthetic Lofi", "Dongdaemun Neon - Synthwave"]
        },
        "aesthetic_summary": "Hanbok palace walks through secret pine courtyards, factory-converted cafe hoppings in trendy Seongsu, sizzling samgyeopsal grills, and Han river sunset ramen.",
        "genz_hacks": [
            "Rent a traditional Hanbok near Gyeongbokgung Palace—entry to all Royal Palaces is 100% FREE when wearing hanbok.",
            "Google Maps does NOT work for walking directions in South Korea due to national security laws—download 'Naver Map' or 'KakaoMap'.",
            "Buy an instant Shin Ramyun cup at the Han River GS25 convenience store and use the automated boiling water foil cookers at the riverside picnic lawn.",
            "Subway Line 2 (Green Loop Line) connects Hongdae, Gangnam, and Seongsu without a single transfer."
        ],
        "packing_essentials": [
            "Comfortable sneakers with thick cushioning (Seoul has lots of steep hills and palace gravel)",
            "T-Money transportation card (buy at any convenience store upon landing)",
            "Portable pocket hand warmer (winter) or UV cooling umbrella (summer)",
            "Face sheet masks from Olive Young for nightly hydration"
        ],
        "days": [
            {
                "title": "Ancient Royal Pavilions, Seongsu Brooklyn Cafes & Han River Ramen",
                "neighborhood": "Jongno, Seongsu-dong & Yeouido Han River",
                "vibe_summary": "Elegance of Joseon royalty into cutting-edge Gen-Z design culture",
                "daily_steps_estimate": "13,800 steps (Palace gardens + riverside strolling)",
                "rest_break": {
                    "time_slot": "02:30 PM - 03:45 PM",
                    "activity_name": "♨️ Traditional Hanok Teahouse Rest in Bukchon",
                    "location_name": "Cha-Teau Bukchon Hanok Teahouse",
                    "tip": "Remove shoes and sit on the heated wooden floor with a bowl of warm roasted grain misutgaru tea overlooking curved tile roofs."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Gyeongbokgung Palace Royal Guard Hanbok Morning",
                        "image_url": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=800&q=80",
                        "category": "Ancient Royal Architecture",
                        "time_slot": "09:00 AM - 11:30 AM",
                        "location_name": "Gyeongbokgung Palace & Hyangwonjeong Pavilion",
                        "neighborhood": "Jongno-gu",
                        "estimated_price": "$12",
                        "cost_tier": "$",
                        "ticket_requirement": "Hanbok rental covers admission (Free entry in Hanbok)",
                        "vibe_tags": ["#Gyeongbokgung", "#HanbokExperience", "#JoseonDynasty"],
                        "crowd_meter": "Peaceful early morning (3/10)",
                        "insider_booking_tip": "Head to Hyangwonjeong, the two-story hexagonal wooden pavilion resting on a tranquil lotus pond with Mount Bugaksan rising directly behind.",
                        "photo_spot_tip": "Framed walking across the wooden Chwihyanggyo Bridge toward the lotus pavilion with colorful silk hanbok ribbons floating in the wind.",
                        "food_spot": "Tosokchon Samgyetang (Famous bubbling ginseng chicken soup stuffed with glutinous rice, chestnuts & ginseng roots)",
                        "transit_to_next": {
                            "mode": "🚇 Seoul Metro Line 2",
                            "duration": "18 mins",
                            "cost": "$1.10 (1400 KRW)",
                            "instructions": "Take Line 3 from Gyeongbokgung to Euljiro 3-ga, transfer to Line 2 Green Loop straight to Seongsu Station."
                        }
                    },
                    {
                        "activity_name": "Seongsu-dong 'Brooklyn of Seoul' Industrial Cafe & Streetwear Vaults",
                        "image_url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80",
                        "category": "Gen-Z Aesthetic Cafes & Architecture",
                        "time_slot": "12:30 PM - 04:00 PM",
                        "location_name": "Cafe Onion Seongsu, Daelim Changgo & Tamburins Flagship",
                        "neighborhood": "Seongsu-dong",
                        "estimated_price": "$16",
                        "cost_tier": "$$",
                        "ticket_requirement": "Free walk-in",
                        "vibe_tags": ["#SeongsuDong", "#CafeOnion", "#KoreanAesthetics"],
                        "crowd_meter": "Trendy & bustling (6/10)",
                        "insider_booking_tip": "Order the signature 'Pandoro' (powdered sugar mountain pastry) at Cafe Onion, a converted 1970s metal factory with an open-air rooftop.",
                        "photo_spot_tip": "The weathered exposed red brick walls and oversized rusted steel doors of Daelim Changgo gallery cafe.",
                        "food_spot": "Somunnan Seongsu Gamjatang (24-hour legendary pork backbone stew with perilla leaves and potato noodles)",
                        "transit_to_next": {
                            "mode": "🚇 Metro Line 2 to Line 5",
                            "duration": "24 mins",
                            "cost": "$1.20",
                            "instructions": "Take Line 2 to Wangsimni, transfer to Line 5 directly to Yeouinaru Station right on the Han River."
                        }
                    },
                    {
                        "activity_name": "Yeouido Han River Sunset Park & Automated Instant Ramen",
                        "image_url": "https://images.unsplash.com/photo-1506157786151-b8491531f063?auto=format&fit=crop&w=800&q=80",
                        "category": "Authentic Local Youth Sunset Tradition",
                        "time_slot": "06:00 PM - 09:30 PM",
                        "location_name": "Yeouido Hangang Park",
                        "neighborhood": "Yeouido Waterfront",
                        "estimated_price": "$8",
                        "cost_tier": "$",
                        "ticket_requirement": "Free park access, pay at convenience store",
                        "vibe_tags": ["#HanRiverRamen", "#HangangSunset", "#K-Vibe"],
                        "crowd_meter": "Lively local evening picnic (5/10)",
                        "insider_booking_tip": "Rent a picnic mat at the subway exit. Buy spicy ramyeon and draft beer at the floating 7-Eleven. Cook the ramyeon in 3 minutes on the induction foil machines.",
                        "photo_spot_tip": "Sitting on the picnic mat with steaming noodles in front of the illuminated Mapo Bridge and glittering river ferry.",
                        "food_spot": "Hangang GS25 Convenience Store (Instant ramen with raw egg crack + Chimaek crispy fried chicken delivered to your picnic mat)",
                        "transit_to_next": {
                            "mode": "🚇 Metro Line 5 to Line 2",
                            "duration": "12 mins",
                            "cost": "$1.10",
                            "instructions": "Take Line 5 to Yeongdeungpo-gu Office, transfer to Line 2 straight back to Hongdae basecamp."
                        }
                    }
                ]
            }
        ]
    },
    "new york": {
        "destination_display": "New York City, USA 🇺🇸",
        "environment_type": "Art Deco Skyscraper Canyons, Lush Central Park Woodlands & Waterfront Piers",
        "hero_image": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Central Park The Ramble & Lake", "The High Line Elevated Greenway", "Hudson River Waterfront Park", "Prospect Park Forest", "East River Waterfront Promenade"],
        "basecamp": {
            "strategic_area": "Lower East Side or Williamsburg, Brooklyn (Direct subway access, vibrant nightlife & vintage thrift)",
            "hostel_pick": {
                "name": "HI NYC Hostel (Upper West Side) / Pod 39 (Midtown)",
                "price": "$52/night",
                "rating": "9.1/10",
                "vibe": "Historic landmark brick building with massive private courtyard patio, free walking tours & game lounge"
            },
            "boutique_pick": {
                "name": "The Ludlow Hotel (Lower East Side)",
                "price": "$240/night",
                "rating": "9.5/10 (Exceptional)",
                "vibe": "Industrial loft with terracotta floors, exposed beams, Moroccan rugs & legendary garden lounge"
            },
            "rest_strategy": "NYC involves 20,000+ steps/day on hard concrete. Schedule a midday 45-minute book or bagel rest in Central Park Sheep Meadow or Washington Square Park fountain."
        },
        "transit_system": "MTA New York City Subway (100% contactless OMNY tap with Apple/Google Pay at turnstiles)",
        "spotify_playlist": {
            "title": "NYC Autumn Sunset: Indie Rock & Vinyl Lofi",
            "genre": "Indie Rock / Hip-Hop Lofi / Jazz",
            "tracks": ["Empire State - Classic Beat", "Brooklyn Bridge - Acoustic Lofi", "Central Park Walk - Jazz Trio", "Lower East Side - Midnight Soul"]
        },
        "aesthetic_summary": "Walking the High Line wildflower tracks above Manhattan streets, sunrise over the Brooklyn Bridge timber boardwalk, hot dollar pizza slices, and basement jazz basements.",
        "genz_hacks": [
            "Use OMNY contactless tap directly on the subway turnstiles with your smartphone—after 12 rides in a week, all subsequent subway rides are 100% free.",
            "Walk across the Brooklyn Bridge from BROOKLYN to MANHATTAN for the iconic skyline views straight ahead of you.",
            "Visit the Rooftop Garden at the Met Museum for an unobstructed view overlooking Central Park canopy and Manhattan towers.",
            "Joe's Pizza on Carmine St (West Village) or Scarr's Pizza (Lower East Side) for the real NYC slice."
        ],
        "packing_essentials": [
            "Heavy-cushioned running or walking sneakers (concrete impact fatigue is real)",
            "High-capacity magnetic power bank",
            "Compact fold-up tote bag",
            "Layered denim or leather jacket"
        ],
        "days": [
            {
                "title": "High Line Wildflower Tracks, West Village Brownstones & Brooklyn Sunset",
                "neighborhood": "Meatpacking District, West Village & DUMBO",
                "vibe_summary": "Elevated botanical architecture into storied bohemian jazz corridors",
                "daily_steps_estimate": "15,500 steps (High Line walk + bridge crossing)",
                "rest_break": {
                    "time_slot": "03:00 PM - 04:00 PM",
                    "activity_name": "☕ Washington Square Park Bench Rest & Jazz Buskers",
                    "location_name": "Washington Square Park Marble Arch",
                    "tip": "Sit by the central fountain with an iced latte watching eccentric NYU artists, chess masters, and live jazz upright bass players."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Sunrise Stroll Across the Elevated High Line Rail Greenway",
                        "image_url": "https://images.unsplash.com/photo-1534430480872-3498386e7856?auto=format&fit=crop&w=800&q=80",
                        "category": "Urban Botanical Trail",
                        "time_slot": "08:00 AM - 10:15 AM",
                        "location_name": "The High Line & Chelsea Market",
                        "neighborhood": "Meatpacking / Chelsea",
                        "estimated_price": "$0",
                        "cost_tier": "$",
                        "ticket_requirement": "Free Public Access",
                        "vibe_tags": ["#TheHighLine", "#UrbanGreenway", "#ManhattanMorning"],
                        "crowd_meter": "Peaceful early morning (2/10)",
                        "insider_booking_tip": "Enter at Gansevoort Street. Walk 1.45 miles north along the repurposed 1930s elevated freight railway adorned with native meadow grasses and modern sculptures.",
                        "photo_spot_tip": "10th Avenue Overlook amphitheater with glass windows looking straight down the traffic canyon.",
                        "food_spot": "Chelsea Market / Los Tacos No. 1 (Adobada spicy pork tacos with grilled pineapple on fresh corn tortillas)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk South into West Village",
                            "duration": "10 mins (800m)",
                            "cost": "Free",
                            "instructions": "Walk south along Hudson Street beneath tree-shaded brownstone townhouses into the heart of West Village."
                        }
                    },
                    {
                        "activity_name": "West Village Brownstone Stroll & Legendary Joe's Pizza Slice",
                        "image_url": "https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=800&q=80",
                        "category": "Historic Bohemian Quarters & Street Food",
                        "time_slot": "11:30 AM - 02:00 PM",
                        "location_name": "Bleecker Street & Joe's Pizza Carmine St",
                        "neighborhood": "West Village",
                        "estimated_price": "$10",
                        "cost_tier": "$",
                        "ticket_requirement": "Walk-in, cash/card",
                        "vibe_tags": ["#WestVillage", "#Brownstones", "#JoesPizza"],
                        "crowd_meter": "Vibrant village buzz (5/10)",
                        "insider_booking_tip": "Fold your hot plain cheese slice lengthwise in half like a true New Yorker to prevent cheese slide. Spritz with garlic powder and oregano.",
                        "photo_spot_tip": "The ivy-covered corner facade of Grove Street and Bedford Street (The 'Friends' apartment building).",
                        "food_spot": "Joe's Pizza (Iconic thin-crust cheese slice with sweet tomato sauce and blistered mozzarella)",
                        "transit_to_next": {
                            "mode": "🚇 Subway Train (A or C Line)",
                            "duration": "12 mins",
                            "cost": "$2.90 (OMNY Tap)",
                            "instructions": "Take the A/C train from West 4th St - Washington Square station southbound to High St - Brooklyn Bridge."
                        }
                    },
                    {
                        "activity_name": "DUMBO Waterfront Pebble Beach & Brooklyn Bridge Twilight",
                        "image_url": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=800&q=80",
                        "category": "Iconic Skyline Sunset & Waterfront",
                        "time_slot": "05:30 PM - 08:30 PM",
                        "location_name": "Pebble Beach & Brooklyn Bridge Promenade",
                        "neighborhood": "DUMBO, Brooklyn",
                        "estimated_price": "$15",
                        "cost_tier": "$$",
                        "ticket_requirement": "Free Public Access",
                        "vibe_tags": ["#DUMBO", "#BrooklynBridge", "#ManhattanSkyline"],
                        "crowd_meter": "Sunset gathering (6/10)",
                        "insider_booking_tip": "Stand at the intersection of Washington St and Water St in DUMBO where the steel Manhattan Bridge arches perfectly frame the distant Empire State Building.",
                        "photo_spot_tip": "Sitting on the rocks of Pebble Beach looking across the East River as the Manhattan financial skyscrapers light up in the dusk.",
                        "food_spot": "Time Out Market Rooftop (Pastrami on rye from Katz's or craft tacos with skyline views)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk across Brooklyn Bridge Boardwalk",
                            "duration": "25 mins iconic bridge walk",
                            "cost": "Free",
                            "instructions": "Walk the elevated pedestrian wooden boardwalk across the East River under stone Gothic arches back into Manhattan."
                        }
                    }
                ]
            }
        ]
    },
    "london": {
        "destination_display": "London, United Kingdom 🇬🇧",
        "environment_type": "Victorian Brick Arcades, Royal Royal Parks & River Thames Embankments",
        "hero_image": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1200&q=80",
        "nature_landmarks": ["Hyde Park & The Serpentine Lake", "Regent's Canal & Primrose Hill", "Richmond Deer Park Forest", "Hampstead Heath Bathing Ponds", "Kew Royal Botanic Gardens"],
        "basecamp": {
            "strategic_area": "Shoreditch or Soho / South Bank (Walking access to food halls, indie design & tube lines)",
            "hostel_pick": {
                "name": "Wombat's City Hostel London (Tower Bridge) / Generator London",
                "price": "$42/night",
                "rating": "9.2/10 (Superb)",
                "vibe": "Converted brick tea warehouse with vaulted basement beer cellar, courtyard hammocks & pod bunks"
            },
            "boutique_pick": {
                "name": "The Hoxton, Shoreditch",
                "price": "$190/night",
                "rating": "9.4/10",
                "vibe": "Pioneer East London design hotel with open log fireplaces, cocktail lobby & vibrant co-working crowd"
            },
            "rest_strategy": "London weather can be drizzly. Use world-class national museums (Tate Modern, British Museum) which are 100% FREE as warm, dry rest sanctuaries."
        },
        "transit_system": "London Underground (The Tube) & Red Double-Decker Buses (Contactless phone pay-as-you-go)",
        "spotify_playlist": {
            "title": "London Fog: Britpop & Shoreditch Electronic",
            "genre": "UK Garage / Indie Britpop / Chillhop",
            "tracks": ["Waterloo Sunset - The Kinks", "London Grammar - Nightcall", "Shoreditch Rain - UK Garage", "Camden Stroll - Acoustic Lofi"]
        },
        "aesthetic_summary": "Historic red double-decker bus front-seat rides, Borough Market sizzling toasted cheese sandwiches, vintage vinyl browsing in Brick Lane, and sunset views from Primrose Hill.",
        "genz_hacks": [
            "All national London museums (Tate Modern, British Museum, National Gallery, V&A) are completely FREE to enter.",
            "Always ride on the top deck, front row of a red double-decker bus for a £1.75 world-class sightseeing tour.",
            "Tap in and tap out with Apple Pay/Google Pay on Tube turnstiles—daily fares are automatically capped so you never overpay.",
            "Head to the Sky Garden (Walkie Talkie building)—it is 100% free with pre-booked tickets online, unlike the expensive Shard."
        ],
        "packing_essentials": [
            "Compact windproof umbrella (London drizzle appears out of nowhere)",
            "Comfortable waterproof leather boots or sneakers",
            "Layered wool or trench coat for variable UK weather",
            "Contactless card or smartphone for all transit gates"
        ],
        "days": [
            {
                "title": "Borough Food Sizzle, Tate Modern Turbine Hall & Thames Sunset",
                "neighborhood": "Southwark, London Bridge & Shoreditch",
                "vibe_summary": "Epicurean market fever into monumental industrial modern art",
                "daily_steps_estimate": "13,200 steps (River Thames path + art galleries)",
                "rest_break": {
                    "time_slot": "03:15 PM - 04:15 PM",
                    "activity_name": "☕ Tate Modern Level 6 River View Coffee Rest",
                    "location_name": "Tate Modern Cafe & Turbine Hall",
                    "tip": "Sit by the floor-to-ceiling glass windows overlooking St. Paul's Cathedral with a warm flat white coffee."
                },
                "activities": [
                    {
                        "activity_name": "🌅 Sizzling Raclette & Fresh Sourdough at Borough Market",
                        "image_url": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=800&q=80",
                        "category": "Historic Food Market Wonder",
                        "time_slot": "09:30 AM - 12:00 PM",
                        "location_name": "Borough Market beneath Victorian Railway Arches",
                        "neighborhood": "London Bridge",
                        "estimated_price": "$14",
                        "cost_tier": "$$",
                        "ticket_requirement": "Free Market Entry",
                        "vibe_tags": ["#BoroughMarket", "#FoodieHeaven", "#CheesePull"],
                        "crowd_meter": "Bustling (7/10)",
                        "insider_booking_tip": "Head to Kappacasein for molten Swiss Montgomery cheddar raclette scraped over hot baby potatoes and gherkins, or try bread ahead cream donuts.",
                        "photo_spot_tip": "The dramatic melted cheese scrape cascade in front of the Victorian cast-iron market roof.",
                        "food_spot": "Kappacasein Dairy (Legendary molten raclette & toasted sourdough cheese toastie)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Scenic Thames River Path Walk",
                            "duration": "12 mins river walk (900m)",
                            "cost": "Free",
                            "instructions": "Follow Queen's Walk along the south bank of the Thames past Shakespeare's Globe straight to Tate Modern."
                        }
                    },
                    {
                        "activity_name": "Tate Modern Monumental Turbine Hall & Millennium Bridge Walk",
                        "image_url": "https://images.unsplash.com/photo-1526129318478-62ed807ebdf9?auto=format&fit=crop&w=800&q=80",
                        "category": "World-Class Modern Art & Engineering",
                        "time_slot": "12:30 PM - 03:30 PM",
                        "location_name": "Tate Modern & Millennium Suspension Bridge",
                        "neighborhood": "Bankside",
                        "estimated_price": "$0",
                        "cost_tier": "$",
                        "ticket_requirement": "100% Free Admission",
                        "vibe_tags": ["#TateModern", "#MillenniumBridge", "#StPauls"],
                        "crowd_meter": "Spacious & inspiring (4/10)",
                        "insider_booking_tip": "Stand inside the cavernous Turbine Hall of this former power station. Walk across the steel Millennium footbridge perfectly framing the dome of St. Paul's Cathedral.",
                        "photo_spot_tip": "Standing on Millennium Bridge looking north as the steel suspension cables frame the classical stone dome of St. Paul's.",
                        "food_spot": "Padella at London Bridge (Hand-rolled fresh pici cacio e pepe pasta cooked in front of you)",
                        "transit_to_next": {
                            "mode": "🚌 Red Double-Decker Bus #78",
                            "duration": "16 mins top-deck ride",
                            "cost": "$2.20 (£1.75 flat bus fare)",
                            "instructions": "Hop on bus 78 from Tower Bridge north across the river directly into the vintage heart of Shoreditch."
                        }
                    },
                    {
                        "activity_name": "Shoreditch Street Art Vaults & Brick Lane Beigel Sizzle",
                        "image_url": "https://images.unsplash.com/photo-1520986606214-8b456906c813?auto=format&fit=crop&w=800&q=80",
                        "category": "Creative Culture & Nightlife",
                        "time_slot": "06:00 PM - 09:30 PM",
                        "location_name": "Brick Lane & Redchurch Street",
                        "neighborhood": "Shoreditch / Spitalfields",
                        "estimated_price": "$12",
                        "cost_tier": "$",
                        "ticket_requirement": "Free walk-in",
                        "vibe_tags": ["#Shoreditch", "#BrickLane", "#SaltBeefBeigel"],
                        "crowd_meter": "Buzzing East End youth (6/10)",
                        "insider_booking_tip": "Visit the 24-hour Beigel Bake on Brick Lane for hot salt beef bagel with fiery English mustard and pickles. Explore vintage vinyl records at Rough Trade East.",
                        "photo_spot_tip": "The colorful street art murals covering Chance Street and Redchurch Street brick warehouse walls.",
                        "food_spot": "Beigel Bake Brick Lane (Warm salted beef bagel with pickle & mustard served 24/7 since 1974)",
                        "transit_to_next": {
                            "mode": "🚶‍♂️ Walk back to Shoreditch Basecamp",
                            "duration": "6 mins walk",
                            "cost": "Free",
                            "instructions": "Stroll down Shoreditch High Street back to your boutique hotel or converted warehouse hostel."
                        }
                    }
                ]
            }
        ]
    }
}

try:
    from destinations_extra import EXTRA_DESTINATIONS
    DESTINATIONS_DATA.update(EXTRA_DESTINATIONS)
except ImportError:
    pass

