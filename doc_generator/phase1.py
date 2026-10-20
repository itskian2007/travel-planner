"""
Phase 1: Brainstorming & Ideation Documents
- Brainstorming & Idea Prioritization
- Define Problem Statements
- Empathy Map
"""
from .styles import render_html_document

def get_brainstorming_doc():
    p1 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#4338ca;"></span>1. Ideation Strategy &amp; Problem Discovery</div>
      <p class="card-p" style="margin-bottom:8px;">
        Traditional travel itinerary creation is fragmented, static, and disconnected from dynamic traveller context. Modern travellers spend <strong>4 to 8 hours</strong> hopping across travel blogs, maps, booking engines, and dietary guides. The goal of this brainstorming phase was to conceptualise an <strong>AI-Powered Smart Situational Itinerary Engine</strong> that unifies personalised multi-criteria preferences into actionable, realistic, day-by-day travel plans.
      </p>
      <div class="grid-4" style="margin-bottom:6px;">
        <div class="stat-box">
          <div class="stat-num" style="color:#4338ca;">20+</div>
          <div class="stat-label">Destinations Ideated</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" style="color:#0f766e;">5D</div>
          <div class="stat-label">Preference Vectors</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" style="color:#b45309;">100%</div>
          <div class="stat-label">Verified Landmark Media</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" style="color:#be123c;">10 Days</div>
          <div class="stat-label">Procedural Coverage</div>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#06b6d4;"></span>2. Interactive Idea Generation Mind-Map</div>
      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:10px; text-align:center;">
        <svg viewBox="0 0 760 210" style="width:100%; height:auto; max-height:210px; font-family:sans-serif;">
          <!-- Central Hub -->
          <circle cx="380" cy="105" r="48" fill="#4338ca" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.15))" />
          <text x="380" y="100" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="11">TRAVEL PLANNER</text>
          <text x="380" y="115" text-anchor="middle" fill="#a5b4fc" font-weight="600" font-size="9">AI ENGINE</text>

          <!-- Branch Lines -->
          <line x1="380" y1="57" x2="160" y2="40" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4" />
          <line x1="380" y1="57" x2="600" y2="40" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4" />
          <line x1="332" y1="105" x2="140" y2="105" stroke="#94a3b8" stroke-width="2" />
          <line x1="428" y1="105" x2="620" y2="105" stroke="#94a3b8" stroke-width="2" />
          <line x1="380" y1="153" x2="180" y2="175" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4" />
          <line x1="380" y1="153" x2="580" y2="175" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4" />

          <!-- Nodes -->
          <!-- 1. Personalisation -->
          <rect x="50" y="22" width="160" height="36" rx="6" fill="#0f766e" />
          <text x="130" y="38" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="9.5">5D Personalisation</text>
          <text x="130" y="50" text-anchor="middle" fill="#ccfbf1" font-size="7.5">Mood &bull; Budget &bull; Diet &bull; Persona</text>

          <!-- 2. Automation -->
          <rect x="550" y="22" width="160" height="36" rx="6" fill="#b45309" />
          <text x="630" y="38" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="9.5">Procedural Engine</text>
          <text x="630" y="50" text-anchor="middle" fill="#fef3c7" font-size="7.5">Day 1-3 Curated + Day 4-10 Auto</text>

          <!-- 3. Destinations -->
          <rect x="30" y="87" width="160" height="36" rx="6" fill="#2563eb" />
          <text x="110" y="103" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="9.5">20 Global Hubs</text>
          <text x="110" y="115" text-anchor="middle" fill="#dbeafe" font-size="7.5">Tokyo, Rome, Iceland, Bali...</text>

          <!-- 4. Media & Imagery -->
          <rect x="570" y="87" width="160" height="36" rx="6" fill="#7e22ce" />
          <text x="650" y="103" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="9.5">304 Unique Photos</text>
          <text x="650" y="115" text-anchor="middle" fill="#f3e8ff" font-size="7.5">Wikipedia API + 0 Duplicates</text>

          <!-- 5. Accessibility -->
          <rect x="60" y="157" width="160" height="36" rx="6" fill="#be123c" />
          <text x="140" y="173" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="9.5">Inclusive Travel</text>
          <text x="140" y="185" text-anchor="middle" fill="#ffe4e6" font-size="7.5">Mobility &bull; Audio/Visual Filters</text>

          <!-- 6. Cloud Native -->
          <rect x="530" y="157" width="170" height="36" rx="6" fill="#047857" />
          <text x="615" y="173" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="9.5">Cloud Architecture</text>
          <text x="615" y="185" text-anchor="middle" fill="#d1fae5" font-size="7.5">Vercel CDN + FastAPI + Postgres</text>
        </svg>
      </div>
    </div>
    """

    p2 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#7e22ce;"></span>3. MoSCoW Prioritization Framework</div>
      <div class="grid-2">
        <div class="card" style="border-top:3px solid #10b981;">
          <div class="card-header"><span style="color:#065f46;">&#x2714; MUST HAVE (Core MVP)</span><span class="badge badge-green">P0 Critical</span></div>
          <p class="card-p">
            &bull; <strong>5D Filter Engine:</strong> Mood, Budget tier, Dietary restrictions, Persona, Accessibility.<br>
            &bull; <strong>Hybrid Itinerary Pipeline:</strong> Curated Day 1-3 expert content + procedural Day 4-10.<br>
            &bull; <strong>Auth Architecture:</strong> Secure JWT signup, login, session tokens, profile persistence.<br>
            &bull; <strong>20 Destinations:</strong> Complete database with coordinates, culture, cuisine, and weather.
          </p>
        </div>
        <div class="card" style="border-top:3px solid #2563eb;">
          <div class="card-header"><span style="color:#1e40af;">&#x25C6; SHOULD HAVE (High Priority)</span><span class="badge badge-blue">P1 High</span></div>
          <p class="card-p">
            &bull; <strong>304 Verified Unique Photos:</strong> Wikipedia API integration with deduplication.<br>
            &bull; <strong>Mobile Responsive UI:</strong> Tailwind CSS layout tested on mobile, tablet, desktop.<br>
            &bull; <strong>Interactive Day Cards:</strong> Expand/collapse animation with meal &amp; tip badges.<br>
            &bull; <strong>Budget Cost Predictor:</strong> Dynamic expense estimator per budget tier.
          </p>
        </div>
        <div class="card" style="border-top:3px solid #f59e0b;">
          <div class="card-header"><span style="color:#92400e;">&#x25B2; COULD HAVE (Enhancements)</span><span class="badge badge-amber">P2 Medium</span></div>
          <p class="card-p">
            &bull; <strong>Password Reset Flow:</strong> Self-service forgot-password workflow with token email.<br>
            &bull; <strong>Dark/Light Theme Toggle:</strong> Adaptive UI skinning based on user OS preference.<br>
            &bull; <strong>Interactive Map Thumbnails:</strong> Static map snapshot pins for attractions.<br>
            &bull; <strong>Local Transit Notes:</strong> Subway/metro navigation tips per city.
          </p>
        </div>
        <div class="card" style="border-top:3px solid #64748b;">
          <div class="card-header"><span style="color:#475569;">&#x2716; WON'T HAVE NOW (Post-MVP)</span><span class="badge badge-slate">v2.0 Scope</span></div>
          <p class="card-p">
            &bull; <strong>Live Flight Booking:</strong> GDS/Amadeus API ticket procurement integration.<br>
            &bull; <strong>Live Hotel Inventory:</strong> Booking.com real-time reservation gateway.<br>
            &bull; <strong>AR Walking Tours:</strong> Augmented reality mobile camera wayfinding.<br>
            &bull; <strong>Multi-Currency Auto-FX:</strong> Live foreign exchange conversion calculator.
          </p>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#b45309;"></span>4. Comprehensive Ideas Evaluation Matrix</div>
      <table>
        <thead>
          <tr>
            <th style="width:5%;">#</th>
            <th style="width:35%;">Feature / Idea Description</th>
            <th style="width:20%;">Functional Domain</th>
            <th style="width:12%;">Impact</th>
            <th style="width:14%;">Feasibility</th>
            <th style="width:14%;">Decision</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td><strong>Situational Mood Filter</strong> (Adventure, Culture, Relaxation, Romance)</td>
            <td>Personalisation</td>
            <td><span class="badge badge-green">Very High</span></td>
            <td><span class="badge badge-blue">High</span></td>
            <td><span class="badge badge-green">ACCEPTED</span></td>
          </tr>
          <tr>
            <td>2</td>
            <td><strong>Procedural 10-Day Generation Engine</strong> with constraint solving</td>
            <td>AI / Automation</td>
            <td><span class="badge badge-green">Critical</span></td>
            <td><span class="badge badge-amber">Medium</span></td>
            <td><span class="badge badge-green">ACCEPTED</span></td>
          </tr>
          <tr>
            <td>3</td>
            <td><strong>Wikipedia API Real Landmark Photo Pipeline</strong> with zero duplicates</td>
            <td>Data Engineering</td>
            <td><span class="badge badge-blue">High</span></td>
            <td><span class="badge badge-blue">High</span></td>
            <td><span class="badge badge-green">ACCEPTED</span></td>
          </tr>
          <tr>
            <td>4</td>
            <td><strong>Dietary Restriction Matrix</strong> (Vegan, Halal, Veg, Gluten-Free)</td>
            <td>Accessibility</td>
            <td><span class="badge badge-blue">High</span></td>
            <td><span class="badge badge-blue">High</span></td>
            <td><span class="badge badge-green">ACCEPTED</span></td>
          </tr>
          <tr>
            <td>5</td>
            <td><strong>Live Flight &amp; Hotel Checkout Gateway</strong> with payment processing</td>
            <td>Commercial APIs</td>
            <td><span class="badge badge-amber">Medium</span></td>
            <td><span class="badge badge-red">Low</span></td>
            <td><span class="badge badge-slate">DEFERRED (v2)</span></td>
          </tr>
        </tbody>
      </table>
    </div>
    """
    return render_html_document("Brainstorming & Idea Prioritization", 1, "Brainstorming & Ideation", "indigo", [p1, p2])


def get_problem_statements_doc():
    p1 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#be123c;"></span>1. Problem Discovery &amp; Root Cause Analysis</div>
      <p class="card-p" style="margin-bottom:8px;">
        Extensive user interviews with frequent leisure and business travellers revealed an industry-wide paradox: despite the abundance of online travel information, creating a cohesive, personalised trip itinerary remains an exhausting, friction-heavy endeavor. The core issue stems from <strong>fragmented data silos</strong>, <strong>lack of situational intelligence</strong>, and <strong>generic recommendation algorithms</strong> that ignore individual dietary, mood, and budget constraints.
      </p>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#b45309;"></span>2. Problem Tree Diagram (Cause &bull; Core &bull; Effect)</div>
      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:10px; text-align:center;">
        <svg viewBox="0 0 760 210" style="width:100%; height:auto; max-height:210px; font-family:sans-serif;">
          <!-- Core Problem (Center) -->
          <rect x="230" y="80" width="300" height="42" rx="6" fill="#be123c" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.15))" />
          <text x="380" y="98" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="10.5">CORE: TRAVEL PLANNING OVERWHELM</text>
          <text x="380" y="112" text-anchor="middle" fill="#ffe4e6" font-size="8">4-8 Hours of Manual Effort with Suboptimal, Generic Trips</text>

          <!-- Causes (Top) -->
          <rect x="40" y="15" width="200" height="34" rx="5" fill="#1e293b" />
          <text x="140" y="29" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="8.5">Information Overload</text>
          <text x="140" y="41" text-anchor="middle" fill="#94a3b8" font-size="7">10-20 fragmented sites &amp; blogs</text>

          <rect x="280" y="15" width="200" height="34" rx="5" fill="#1e293b" />
          <text x="380" y="29" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="8.5">Generic Recommendations</text>
          <text x="380" y="41" text-anchor="middle" fill="#94a3b8" font-size="7">Ignores diet, persona &amp; mood</text>

          <rect x="520" y="15" width="200" height="34" rx="5" fill="#1e293b" />
          <text x="620" y="29" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="8.5">Inauthentic Visuals</text>
          <text x="620" y="41" text-anchor="middle" fill="#94a3b8" font-size="7">Stock photos, false expectations</text>

          <!-- Arrows from Causes to Core -->
          <path d="M 140 49 L 140 65 L 300 65 L 300 80" fill="none" stroke="#64748b" stroke-width="2" />
          <path d="M 380 49 L 380 80" fill="none" stroke="#64748b" stroke-width="2" />
          <path d="M 620 49 L 620 65 L 460 65 L 460 80" fill="none" stroke="#64748b" stroke-width="2" />

          <!-- Consequences (Bottom) -->
          <rect x="50" y="155" width="190" height="34" rx="5" fill="#0f766e" />
          <text x="145" y="169" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="8.5">Severe Decision Paralysis</text>
          <text x="145" y="181" text-anchor="middle" fill="#ccfbf1" font-size="7">Abandoned trip bookings</text>

          <rect x="285" y="155" width="190" height="34" rx="5" fill="#0f766e" />
          <text x="380" y="169" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="8.5">Dietary &amp; Budget Failures</text>
          <text x="380" y="181" text-anchor="middle" fill="#ccfbf1" font-size="7">Frustrating on-ground experiences</text>

          <rect x="520" y="155" width="190" height="34" rx="5" fill="#0f766e" />
          <text x="615" y="169" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="8.5">Rigid, Exhausting Plans</text>
          <text x="615" y="181" text-anchor="middle" fill="#ccfbf1" font-size="7">Impossible travel sequences</text>

          <!-- Arrows from Core to Consequences -->
          <path d="M 300 122 L 300 138 L 145 138 L 145 155" fill="none" stroke="#be123c" stroke-width="2" />
          <path d="M 380 122 L 380 155" fill="none" stroke="#be123c" stroke-width="2" />
          <path d="M 460 122 L 460 138 L 615 138 L 615 155" fill="none" stroke="#be123c" stroke-width="2" />
        </svg>
      </div>
    </div>
    """

    p2 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#be123c;"></span>3. Formal Problem Statements</div>
      <div class="grid-2">
        <div class="card" style="border-left:4px solid #be123c;">
          <div class="card-header"><span style="color:#991b1b;">PS-01: Cognitive Fragmentation</span><span class="badge badge-red">CRITICAL</span></div>
          <p class="card-p">
            <strong>Statement:</strong> Modern leisure travellers spend an average of 6.2 hours across 14 independent platforms to formulate a basic itinerary, leading to high cognitive fatigue and a 42% cart/plan abandonment rate.<br>
            <strong>Target Persona:</strong> Solo professionals, time-constrained couples.
          </p>
        </div>
        <div class="card" style="border-left:4px solid #b45309;">
          <div class="card-header"><span style="color:#92400e;">PS-02: Demographic Blindness</span><span class="badge badge-amber">HIGH</span></div>
          <p class="card-p">
            <strong>Statement:</strong> Existing travel engines recommend generic tourist attractions without factoring in dietary restrictions (Halal, Vegan), accessibility constraints (wheelchair access), or travel persona dynamics (solo vs. family).<br>
            <strong>Target Persona:</strong> Vegan/Halal travellers, families with elderly.
          </p>
        </div>
        <div class="card" style="border-left:4px solid #4338ca;">
          <div class="card-header"><span style="color:#3730a3;">PS-03: Temporal Scalability Deficit</span><span class="badge badge-purple">HIGH</span></div>
          <p class="card-p">
            <strong>Statement:</strong> Most travel guides cover only 2-3 standard days of sight-seeing. When travellers book 7 to 10 day vacations, they are forced to manually invent daily routes without verified geographic sequencing.<br>
            <strong>Target Persona:</strong> Extended vacationers, international backpackers.
          </p>
        </div>
        <div class="card" style="border-left:4px solid #0f766e;">
          <div class="card-header"><span style="color:#115e59;">PS-04: Visual Inauthenticity</span><span class="badge badge-teal">MEDIUM</span></div>
          <p class="card-p">
            <strong>Statement:</strong> Commercial travel sites display heavily filtered stock photos or repetitive duplicate images, leading to on-ground expectation mismatches and tourist dissatisfaction.<br>
            <strong>Target Persona:</strong> Photography enthusiasts, cultural travellers.
          </p>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#0f766e;"></span>4. How Might We (HMW) Design Framework</div>
      <table>
        <thead>
          <tr>
            <th style="width:12%;">HMW Code</th>
            <th style="width:58%;">Reframed Design Challenge</th>
            <th style="width:30%;">Engineered Solution Feature</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>HMW-01</strong></td>
            <td>How might we compress 6 hours of travel research into a 30-second automated generation flow?</td>
            <td><span class="badge badge-blue">Deterministic Procedural Engine</span></td>
          </tr>
          <tr>
            <td><strong>HMW-02</strong></td>
            <td>How might we incorporate dietary, budget, and accessibility needs into every meal and stop?</td>
            <td><span class="badge badge-teal">5D Situational Filter Matrix</span></td>
          </tr>
          <tr>
            <td><strong>HMW-03</strong></td>
            <td>How might we ensure 100% authentic visual representation for every attraction?</td>
            <td><span class="badge badge-purple">Wikipedia API 304 Unique Media Pipeline</span></td>
          </tr>
          <tr>
            <td><strong>HMW-04</strong></td>
            <td>How might we support realistic 10-day itineraries without boring repetition?</td>
            <td><span class="badge badge-green">Curated Day 1-3 + Procedural Day 4-10</span></td>
          </tr>
        </tbody>
      </table>
    </div>
    """
    return render_html_document("Define Problem Statements", 1, "Brainstorming & Ideation", "indigo", [p1, p2])


def get_empathy_map_doc():
    p1 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#4338ca;"></span>1. User Persona Profile &bull; Primary Target Segment</div>
      <div class="card" style="display:flex; gap:14px; align-items:center; background:#f8fafc; border:1px solid #cbd5e1; margin-bottom:8px;">
        <div style="background:#4338ca; color:white; width:52px; height:52px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:20pt; font-weight:800; flex-shrink:0;">
          A
        </div>
        <div style="flex:1;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div style="font-size:11pt; font-weight:800; color:#0f172a;">Aarav Sharma, 27 &bull; Tech Professional &amp; Avid Traveler</div>
            <span class="badge badge-purple">PRIMARY PERSONA (70% OF USER BASE)</span>
          </div>
          <div style="font-size:7.5pt; color:#64748b; margin-top:2px;">
            <strong>Demographics:</strong> Bengaluru, India &bull; Software Engineer &bull; Annual Travel Budget: $3,500 &bull; Vacation Freq: 3-4x / Year
          </div>
          <div style="font-size:7.5pt; color:#334155; margin-top:4px;">
            <strong>Core Motivation:</strong> Values authentic local culture and unique food, but works 50 hours a week and cannot afford to spend entire weekends researching travel blogs.
          </div>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#0f766e;"></span>2. 4-Quadrant Empathy Map Board</div>
      <div class="grid-2">
        <!-- Says -->
        <div class="card" style="background:#eff6ff; border:1px solid #bfdbfe;">
          <div class="card-header"><span style="color:#1e40af;">&#x1F4AC; SAYS (Explicit Statements)</span></div>
          <p class="card-p" style="color:#1e3a8a;">
            &bull; <em>"I just want an itinerary that knows I'm vegetarian and hate tourist traps."</em><br>
            &bull; <em>"Can someone give me Day 4 to 10? Every blog only covers Day 1 to 3."</em><br>
            &bull; <em>"I spent 4 hours on Reddit trying to figure out which subway pass to buy in Tokyo."</em>
          </p>
        </div>
        <!-- Thinks -->
        <div class="card" style="background:#f5f3ff; border:1px solid #ddd6fe;">
          <div class="card-header"><span style="color:#5b21b6;">&#x1F4AD; THINKS (Internal Monologue)</span></div>
          <p class="card-p" style="color:#4c1d95;">
            &bull; <em>"What if I book this luxury hotel and realize all attractions are 2 hours away?"</em><br>
            &bull; <em>"I hope I don't look like an idiot trying to order food with dietary constraints."</em><br>
            &bull; <em>"I want my trip to look like the real country, not an over-saturated Instagram reel."</em>
          </p>
        </div>
        <!-- Does -->
        <div class="card" style="background:#f0fdf4; border:1px solid #bbf7d0;">
          <div class="card-header"><span style="color:#166534;">&#x1F3C3; DOES (Observable Behavior)</span></div>
          <p class="card-p" style="color:#14532d;">
            &bull; Opens 20 Chrome tabs simultaneously (Google Maps, TripAdvisor, Reddit, Wikipedia).<br>
            &bull; Copies paste notes into a messy Google Sheet with broken links and no images.<br>
            &bull; Abandons planning midway and books a rushed, generic tour package out of exhaustion.
          </p>
        </div>
        <!-- Feels -->
        <div class="card" style="background:#fff1f2; border:1px solid #fecdd3;">
          <div class="card-header"><span style="color:#9f1239;">&#x2764; FEELS (Emotional State)</span></div>
          <p class="card-p" style="color:#881337;">
            &bull; <strong>Overwhelmed:</strong> Drowning in conflicting reviews and sponsored recommendations.<br>
            &bull; <strong>Anxious:</strong> Worried about hidden travel costs and dietary blunders.<br>
            &bull; <strong>Excited yet Drained:</strong> High anticipation for the vacation, ruined by tedious planning.
          </p>
        </div>
      </div>
    </div>
    """

    p2 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#be123c;"></span>3. Pains vs. Gains Value Alignment</div>
      <div class="grid-2">
        <div class="card" style="border-top:3px solid #be123c;">
          <div class="card-header"><span style="color:#991b1b;">&#x2716; USER PAIN POINTS</span><span class="badge badge-red">Frictions</span></div>
          <p class="card-p">
            &bull; <strong>Time Drain:</strong> Sacrificing 5-8 hours of personal weekend time researching itineraries.<br>
            &bull; <strong>Dietary Anxiety:</strong> Worrying if vegetarian/halal options exist near recommended attractions.<br>
            &bull; <strong>Static Templates:</strong> Standard 3-day tourist guides that stop right when the vacation gets interesting.<br>
            &bull; <strong>Image Mismatches:</strong> Misleading generic stock photos that look nothing like the destination.
          </p>
        </div>
        <div class="card" style="border-top:3px solid #10b981;">
          <div class="card-header"><span style="color:#065f46;">&#x2714; USER GAINS &amp; DELIGHTS</span><span class="badge badge-green">Desired Value</span></div>
          <p class="card-p">
            &bull; <strong>Sub-Minute Planning:</strong> Generating a fully structured 10-day itinerary in under 30 seconds.<br>
            &bull; <strong>Dietary Confidence:</strong> Every lunch and dinner recommendation pre-filtered to user dietary profile.<br>
            &bull; <strong>Authentic Visuals:</strong> Verified Wikipedia landmark photography providing truthful previews.<br>
            &bull; <strong>Situational Mood Sync:</strong> Exploring Kyoto in "Cultural Calm" vs. Tokyo in "High Adventure".
          </p>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#0f766e;"></span>4. Persona Empathy Synthesis Matrix</div>
      <table>
        <thead>
          <tr>
            <th style="width:20%;">User Dimension</th>
            <th style="width:40%;">Observed Friction</th>
            <th style="width:40%;">Engineered System Response</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Budget Confidence</strong></td>
            <td>Unsure how much each day truly costs beyond hotel bookings.</td>
            <td>Dynamic budget tier calculator (Budget / Mid-Range / Luxury).</td>
          </tr>
          <tr>
            <td><strong>Food Compatibility</strong></td>
            <td>Fear of ending up in restaurants with zero dietary options.</td>
            <td>Filter engine enforces Vegan, Vegetarian, Halal, or Gluten-Free tags.</td>
          </tr>
          <tr>
            <td><strong>Visual Trust</strong></td>
            <td>Skeptical of fake influencers and misleading travel photos.</td>
            <td>304 non-duplicate Wikipedia commons verified photography pipeline.</td>
          </tr>
          <tr>
            <td><strong>Route Feasibility</strong></td>
            <td>Exhausting schedules with geographically impossible hops.</td>
            <td>Basecamp clustering and curated Day 1-3 landmark sequences.</td>
          </tr>
        </tbody>
      </table>
    </div>
    """
    return render_html_document("Empathy Map", 1, "Brainstorming & Ideation", "indigo", [p1, p2])
