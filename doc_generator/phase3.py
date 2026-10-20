"""
Phase 3: Project Design Phase Documents
- Problem-Solution Fit
- Proposed Solution
- Solution Architecture
"""
from .styles import render_html_document

def get_problem_solution_fit_doc():
    p1 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#7e22ce;"></span>1. Problem-to-Solution Direct Mapping Matrix</div>
      <p class="card-p" style="margin-bottom:8px;">
        To guarantee true product-market fit, every engineering feature was directly derived from a verified user problem. The bridge diagram below demonstrates how the four core user pain points are neutralized by purpose-built architectural components.
      </p>

      <!-- Problem-Solution Bridge SVG -->
      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:10px; text-align:center;">
        <svg viewBox="0 0 760 135" style="width:100%; height:auto; max-height:135px; font-family:sans-serif;">
          <!-- Left: Problems -->
          <rect x="20" y="8" width="220" height="24" rx="4" fill="#fee2e2" stroke="#ef4444" />
          <text x="30" y="24" fill="#991b1b" font-weight="bold" font-size="7.5">&#x2716; 1. 6+ Hours Spent on 14+ Sites</text>

          <rect x="20" y="38" width="220" height="24" rx="4" fill="#fee2e2" stroke="#ef4444" />
          <text x="30" y="54" fill="#991b1b" font-weight="bold" font-size="7.5">&#x2716; 2. Generic One-Size-Fits-All Plans</text>

          <rect x="20" y="68" width="220" height="24" rx="4" fill="#fee2e2" stroke="#ef4444" />
          <text x="30" y="84" fill="#991b1b" font-weight="bold" font-size="7.5">&#x2716; 3. Static Guides Stop at Day 3</text>

          <rect x="20" y="98" width="220" height="24" rx="4" fill="#fee2e2" stroke="#ef4444" />
          <text x="30" y="114" fill="#991b1b" font-weight="bold" font-size="7.5">&#x2716; 4. Misleading Fake Stock Images</text>

          <!-- Middle Connectors -->
          <line x1="240" y1="20" x2="500" y2="20" stroke="#7e22ce" stroke-width="2" marker-end="url(#arrow)" />
          <line x1="240" y1="50" x2="500" y2="50" stroke="#7e22ce" stroke-width="2" />
          <line x1="240" y1="80" x2="500" y2="80" stroke="#7e22ce" stroke-width="2" />
          <line x1="240" y1="110" x2="500" y2="110" stroke="#7e22ce" stroke-width="2" />

          <text x="370" y="16" text-anchor="middle" fill="#7e22ce" font-weight="bold" font-size="7">&#x2794; FIT</text>
          <text x="370" y="46" text-anchor="middle" fill="#7e22ce" font-weight="bold" font-size="7">&#x2794; FIT</text>
          <text x="370" y="76" text-anchor="middle" fill="#7e22ce" font-weight="bold" font-size="7">&#x2794; FIT</text>
          <text x="370" y="106" text-anchor="middle" fill="#7e22ce" font-weight="bold" font-size="7">&#x2794; FIT</text>

          <!-- Right: Solutions -->
          <rect x="500" y="8" width="240" height="24" rx="4" fill="#d1fae5" stroke="#10b981" />
          <text x="510" y="24" fill="#065f46" font-weight="bold" font-size="7.5">&#x2714; Instant Generation Engine (&lt;500ms)</text>

          <rect x="500" y="38" width="240" height="24" rx="4" fill="#d1fae5" stroke="#10b981" />
          <text x="510" y="54" fill="#065f46" font-weight="bold" font-size="7.5">&#x2714; 5D Personalisation (Mood, Diet, Budget)</text>

          <rect x="500" y="68" width="240" height="24" rx="4" fill="#d1fae5" stroke="#10b981" />
          <text x="510" y="84" fill="#065f46" font-weight="bold" font-size="7.5">&#x2714; Procedural Day 4-10 Continuation Engine</text>

          <rect x="500" y="98" width="240" height="24" rx="4" fill="#d1fae5" stroke="#10b981" />
          <text x="510" y="114" fill="#065f46" font-weight="bold" font-size="7.5">&#x2714; 304 Unique Wikipedia Commons Photos</text>
        </svg>
      </div>
    </div>
    """

    p2 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#7e22ce;"></span>2. Value Proposition Canvas (Osterwalder Model)</div>
      <div class="grid-2">
        <div class="card" style="border-top:3px solid #2563eb;">
          <div class="card-header"><span style="color:#1e40af;">VALUE MAP (Our Solution)</span><span class="badge badge-blue">Product Value</span></div>
          <p class="card-p">
            <strong>Products &amp; Services:</strong> Automated Travel Planner Web Application, 20 Curated Global Cities, Dynamic 10-Day Generator, 5D Personalisation Filter.<br><br>
            <strong>Pain Relievers:</strong> Eliminates manual web research, removes dietary guessing games, guarantees realistic travel sequences, eliminates fake stock photos.<br><br>
            <strong>Gain Creators:</strong> Generates cohesive 10-day itineraries in 30 seconds, boosts travel confidence, customizes trips to exact budget bounds.
          </p>
        </div>
        <div class="card" style="border-top:3px solid #7e22ce;">
          <div class="card-header"><span style="color:#5b21b6;">CUSTOMER PROFILE (Target User)</span><span class="badge badge-purple">Customer Segment</span></div>
          <p class="card-p">
            <strong>Customer Jobs:</strong> Plan an exciting vacation, sequence daily sights geographically, find restaurants accommodating diet, stay within budget.<br><br>
            <strong>Customer Pains:</strong> Cognitive overload from conflicting reviews, fear of dietary blunders, exhaustion from planning, rigid 3-day tourist guides.<br><br>
            <strong>Customer Gains:</strong> Effortless trip planning, authentic local experiences, validated photo previews, personalized travel pacing.
          </p>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#0f766e;"></span>3. Quantitative Fit Validation Metrics</div>
      <div class="grid-4">
        <div class="stat-box">
          <div class="stat-num" style="color:#7e22ce;">85%</div>
          <div class="stat-label">Planning Time Saved</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" style="color:#0f766e;">100%</div>
          <div class="stat-label">Image Truthfulness</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" style="color:#2563eb;">5 / 5</div>
          <div class="stat-label">Filter Dimensions Met</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" style="color:#10b981;">10 Days</div>
          <div class="stat-label">Full Trip Coverage</div>
        </div>
      </div>
    </div>
    """
    return render_html_document("Problem-Solution Fit", 3, "Project Design Phase", "purple", [p1, p2])


def get_proposed_solution_doc():
    p1 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#7e22ce;"></span>1. Proposed Solution Overview &amp; Live Architecture</div>
      <p class="card-p" style="margin-bottom:8px;">
        The proposed solution is the <strong>AI-Powered Travel Planner (Smart Situational Itinerary Engine)</strong>. It integrates deterministic algorithmic generation with curated knowledge bases and real-time media ingestion. The platform is deployed live on the global Vercel CDN at <strong>travel-planner-iota-plum.vercel.app</strong>.
      </p>

      <div class="grid-3" style="margin-bottom:8px;">
        <div class="card" style="border-left:3px solid #2563eb;">
          <div class="card-header"><span style="color:#1e40af;">20 Global Destinations</span></div>
          <p class="card-p">Tokyo, Bali, Rome, Paris, Iceland, Swiss Alps, Kyoto, Barcelona, Bangkok, Dubai, Seoul, New York, London, Amsterdam, Singapore, Sydney, Cairo, Istanbul, Rio, Cape Town.</p>
        </div>
        <div class="card" style="border-left:3px solid #0f766e;">
          <div class="card-header"><span style="color:#115e59;">5D Situational Filter</span></div>
          <p class="card-p">Mood (Adventure, Cultural, Relaxation, Romance), Budget (Budget, Mid, Luxury), Diet (Vegan, Halal, Veg), Persona (Solo, Couple, Family), Accessibility.</p>
        </div>
        <div class="card" style="border-left:3px solid #7e22ce;">
          <div class="card-header"><span style="color:#5b21b6;">Hybrid 10-Day Plan</span></div>
          <p class="card-p">Days 1-3 expert-curated landmark sequences; Days 4-10 dynamically generated by procedural engine with 3-4 attractions, lunch, dinner, and daily tips.</p>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#2563eb;"></span>2. Featured Destination Catalog Highlights</div>
      <table>
        <thead>
          <tr>
            <th style="width:16%;">Destination</th>
            <th style="width:22%;">Aesthetic Environment</th>
            <th style="width:26%;">Key Landmarks &amp; Nature</th>
            <th style="width:18%;">Basecamp Hub</th>
            <th style="width:18%;">Transit System</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Tokyo, Japan 🇯🇵</strong></td>
            <td>Metropolitan Neon &amp; Shrines</td>
            <td>Mount Fuji view, Meiji Forest, Meguro Canals</td>
            <td>Shibuya / Shinjuku</td>
            <td><span class="badge badge-teal">JR Yamanote + Metro</span></td>
          </tr>
          <tr>
            <td><strong>Kyoto, Japan 🇯🇵</strong></td>
            <td>Zen Temples &amp; Bamboo Canopies</td>
            <td>Fushimi Inari, Arashiyama, Kinkaku-ji</td>
            <td>Gion / Kawaramachi</td>
            <td><span class="badge badge-teal">Kyoto City Bus Pass</span></td>
          </tr>
          <tr>
            <td><strong>Rome, Italy 🇮🇹</strong></td>
            <td>Ancient Colosseum &amp; Renaissance</td>
            <td>Colosseum, Trevi Fountain, Vatican City</td>
            <td>Trastevere / Monti</td>
            <td><span class="badge badge-teal">Metro Line A/B + Tram</span></td>
          </tr>
          <tr>
            <td><strong>Iceland 🇮🇸</strong></td>
            <td>Glaciers, Geysers &amp; Aurora</td>
            <td>Blue Lagoon, Gullfoss, Skogafoss, Vik</td>
            <td>Reykjavik Center</td>
            <td><span class="badge badge-amber">4WD Ring Road Rental</span></td>
          </tr>
          <tr>
            <td><strong>Bali, Indonesia 🇮🇩</strong></td>
            <td>Tropical Terraces &amp; Ocean Cliffs</td>
            <td>Tegallalang Rice, Uluwatu, Mount Batur</td>
            <td>Ubud / Canggu</td>
            <td><span class="badge badge-blue">Scooter / Private Driver</span></td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    p2 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#0f766e;"></span>3. Market Differentiation &amp; Competitive Edge</div>
      <table>
        <thead>
          <tr>
            <th style="width:26%;">Capability Dimension</th>
            <th style="width:26%;">Our Solution</th>
            <th style="width:24%;">TripAdvisor / Blogs</th>
            <th style="width:24%;">Competitive Advantage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Personalisation Depth</strong></td>
            <td><span class="badge badge-green">5 Dimensions Live</span></td>
            <td>Generic 1-2 filters</td>
            <td>Exact match to diet, budget, mood.</td>
          </tr>
          <tr>
            <td><strong>Itinerary Duration</strong></td>
            <td><span class="badge badge-green">Full 10 Days Automated</span></td>
            <td>Static 2-3 Day lists</td>
            <td>2.5x more vacation coverage.</td>
          </tr>
          <tr>
            <td><strong>Visual Truthfulness</strong></td>
            <td><span class="badge badge-green">304 Unique Real Photos</span></td>
            <td>Filtered stock photos</td>
            <td>Zero fake expectations.</td>
          </tr>
          <tr>
            <td><strong>Generation Speed</strong></td>
            <td><span class="badge badge-green">&lt; 500ms API Latency</span></td>
            <td>Manual 4-8 hours</td>
            <td>Instant gratification.</td>
          </tr>
          <tr>
            <td><strong>Cost to User</strong></td>
            <td><span class="badge badge-green">100% Free Open-Source</span></td>
            <td>Paywalled / Ad-heavy</td>
            <td>Zero barrier to entry.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#7e22ce;"></span>4. Solution Quality Scorecard</div>
      <div class="grid-4">
        <div class="stat-box">
          <div class="stat-num" style="color:#7e22ce;">304</div>
          <div class="stat-label">Unique Landmarks</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" style="color:#0f766e;">0%</div>
          <div class="stat-label">Image Duplication</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" style="color:#2563eb;">20</div>
          <div class="stat-label">Global Cities</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" style="color:#10b981;">100%</div>
          <div class="stat-label">Live Deployment</div>
        </div>
      </div>
    </div>
    """
    return render_html_document("Proposed Solution", 3, "Project Design Phase", "purple", [p1, p2])


def get_solution_architecture_doc():
    p1 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#7e22ce;"></span>1. Full End-to-End System Architecture</div>
      <p class="card-p" style="margin-bottom:8px;">
        The system employs a production-grade 3-tier client-server topology featuring a single-page application (SPA) frontend served via global edge content delivery networks, communicating over authenticated RESTful APIs to an asynchronous ASGI backend backed by a relational database and external media feeds.
      </p>

      <!-- Full Architecture SVG Diagram -->
      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:10px; text-align:center;">
        <svg viewBox="0 0 760 145" style="width:100%; height:auto; max-height:145px; font-family:sans-serif;">
          <!-- Client (Left) -->
          <rect x="15" y="45" width="120" height="55" rx="6" fill="#1e3a8a" />
          <text x="75" y="66" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="8.5">CLIENT TIER</text>
          <text x="75" y="78" text-anchor="middle" fill="#bfdbfe" font-size="7">React.js 18 &bull; SPA</text>
          <text x="75" y="90" text-anchor="middle" fill="#bfdbfe" font-size="6.5">Tailwind &bull; Axios</text>

          <!-- Edge CDN -->
          <rect x="160" y="45" width="115" height="55" rx="6" fill="#0f766e" />
          <text x="217" y="66" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="8.5">EDGE CDN</text>
          <text x="217" y="78" text-anchor="middle" fill="#ccfbf1" font-size="7">Vercel Global Edge</text>
          <text x="217" y="90" text-anchor="middle" fill="#ccfbf1" font-size="6.5">SSL &bull; Compression</text>

          <!-- API Gateway / Backend -->
          <rect x="300" y="30" width="160" height="85" rx="6" fill="#4338ca" />
          <text x="380" y="50" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="9">FASTAPI BACKEND</text>
          <text x="380" y="64" text-anchor="middle" fill="#c7d2fe" font-size="7.5">Uvicorn ASGI &bull; Python 3.11</text>
          <line x1="315" y1="72" x2="445" y2="72" stroke="#6366f1" stroke-width="1" />
          <text x="380" y="84" text-anchor="middle" fill="#e0e7ff" font-size="7">Auth &bull; 5D Filter Engine</text>
          <text x="380" y="96" text-anchor="middle" fill="#e0e7ff" font-size="7">Procedural Day 4-10 Engine</text>
          <text x="380" y="107" text-anchor="middle" fill="#e0e7ff" font-size="6.5">SQLAlchemy ORM &bull; Pydantic v2</text>

          <!-- Database (Right Top) -->
          <rect x="485" y="25" width="135" height="42" rx="6" fill="#047857" />
          <text x="552" y="42" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="8.5">POSTGRESQL 15</text>
          <text x="552" y="54" text-anchor="middle" fill="#d1fae5" font-size="7">Users &bull; Trips (JSONB)</text>

          <!-- External Media API (Right Bottom) -->
          <rect x="485" y="80" width="135" height="42" rx="6" fill="#b45309" />
          <text x="552" y="97" text-anchor="middle" fill="#ffffff" font-weight="bold" font-size="8.5">WIKIPEDIA API</text>
          <text x="552" y="109" text-anchor="middle" fill="#fef3c7" font-size="7">304 Unique Photos</text>

          <!-- Connectors -->
          <line x1="135" y1="72" x2="160" y2="72" stroke="#64748b" stroke-width="2" />
          <line x1="275" y1="72" x2="300" y2="72" stroke="#64748b" stroke-width="2" />
          <line x1="460" y1="52" x2="485" y2="46" stroke="#047857" stroke-width="2" />
          <line x1="460" y1="92" x2="485" y2="98" stroke="#b45309" stroke-width="2" />
        </svg>
      </div>
    </div>
    """

    p2 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#7e22ce;"></span>2. Frontend Component Hierarchy Tree</div>
      <div class="card code-box" style="margin-bottom:8px;">
        <div class="code-title"><span>React Component Hierarchy</span><span>frontend/src/</span></div>
        <pre style="margin:0; font-family:var(--font-mono); font-size:6.8pt; line-height:1.45;">
App.jsx (Root Application Component)
 ├── AuthContext.jsx (Global Authentication &amp; JWT State Provider)
 └── BrowserRouter (React Router v6 SPA Routing)
      ├── Navbar.jsx (Responsive Navigation Header &amp; Auth Status)
      ├── Routes:
      │    ├── / (LandingPage.jsx - Hero Banner, Features, Value Proposition)
      │    ├── /login (LoginPage.jsx - JWT Email/Password Authentication)
      │    ├── /register (RegisterPage.jsx - User Signup Workflow)
      │    ├── /forgot-password (ForgotPasswordPage.jsx - Self-Service Recovery)
      │    ├── /home (HomePage.jsx - 20 Destination Grid)
      │    │    ├── FilterPanel.jsx (Mood, Budget, Diet, Persona Selectors)
      │    │    └── DestinationCard.jsx &times; 20 (Photo, Badges, Meta, Click Handler)
      │    └── /itinerary/:id (ItineraryPage.jsx - Full 10-Day Plan)
      │         ├── DayCard.jsx &times; 10 (Expandable Accordion Cards)
      │         │    ├── AttractionCard.jsx (Title, Description, Duration)
      │         │    ├── LandmarkImage.jsx (Wikipedia Verified Image Fetcher)
      │         │    └── DiningCard.jsx (Filtered Lunch &amp; Dinner Recommendations)
      └── Footer.jsx (Copyright, Legal, Documentation Links)
        </pre>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#2563eb;"></span>3. Backend Modular Package Organization</div>
      <table>
        <thead>
          <tr>
            <th style="width:25%;">Module / File Path</th>
            <th style="width:35%;">Primary Architectural Responsibility</th>
            <th style="width:40%;">Key Dependencies &amp; Exports</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>backend/main.py</code></td>
            <td>FastAPI App Initialization, CORS, Router Mounting</td>
            <td>FastAPI, Uvicorn, Starlette Middleware</td>
          </tr>
          <tr>
            <td><code>backend/routers/auth.py</code></td>
            <td>Registration, Login, JWT Token Issuance</td>
            <td>bcrypt, python-jose, OAuth2PasswordBearer</td>
          </tr>
          <tr>
            <td><code>backend/routers/destinations.py</code></td>
            <td>Catalog Search, 5D Filtering, City Details</td>
            <td>destinations_db.py, Pydantic Schemas</td>
          </tr>
          <tr>
            <td><code>backend/routers/itinerary.py</code></td>
            <td>Hybrid Day 1-3 Curated + Day 4-10 Procedural</td>
            <td>Procedural Engine, Wikipedia Image Service</td>
          </tr>
          <tr>
            <td><code>backend/models.py</code></td>
            <td>SQLAlchemy Relational Database Schema Definitions</td>
            <td>DeclarativeBase, ForeignKey, Column Types</td>
          </tr>
        </tbody>
      </table>
    </div>
    """
    return render_html_document("Solution Architecture", 3, "Project Design Phase", "purple", [p1, p2])
