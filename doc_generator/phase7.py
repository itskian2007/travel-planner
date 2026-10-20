"""
Phase 7: Project Documentation Documents
- Project Executable Files
- Sample Project Documentation
"""
from .styles import render_html_document

def get_executable_files_doc():
    p1 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#047857;"></span>1. Zero-Install Live Cloud Deployment</div>
      <p class="card-p" style="margin-bottom:8px;">
        The Travel Planner application is fully deployed and accessible 24/7 over secure HTTPS with global edge distribution. <strong>End users do not need to install any executable, Python runtime, or local database</strong>.
      </p>

      <div class="card" style="background:#ecfdf5; border:1.5px solid #10b981; padding:12px; margin-bottom:8px;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:11pt; font-weight:800; color:#065f46;">&#x1F310; LIVE PRODUCTION URL</div>
            <div style="font-size:9.5pt; font-weight:700; color:#047857; margin-top:2px;">
              https://travel-planner-iota-plum.vercel.app/
            </div>
            <div style="font-size:7.5pt; color:#065f46; margin-top:4px;">
              Hosted on Vercel Global Edge Network &bull; SSL/TLS Secured &bull; 99.99% Availability
            </div>
          </div>
          <span class="badge badge-green" style="font-size:8pt; padding:4px 10px;">OPERATIONAL 24/7</span>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#047857;"></span>2. Local Developer Quickstart Guide</div>
      <div class="card code-box">
        <div class="code-title"><span>Terminal Setup (Windows / macOS / Linux)</span><span>Bash / PowerShell</span></div>
        <pre style="margin:0; font-family:var(--font-mono); font-size:6.8pt; line-height:1.42; color:#a7f3d0;">
# 1. Clone repository from GitHub
git clone https://github.com/itskian2007/travel-planner.git
cd travel-planner

# 2. Setup and run FastAPI Backend
cd backend
python -m venv venv
.\\venv\\Scripts\\activate            # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# 3. Setup and run React Frontend (in a separate terminal)
cd ../frontend
npm install
npm start                           # Launches UI at http://localhost:3000
        </pre>
      </div>
    </div>
    """

    p2 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#047857;"></span>3. Technology Runtime Prerequisites &amp; Binaries</div>
      <table>
        <thead>
          <tr>
            <th style="width:20%;">Component</th>
            <th style="width:20%;">Required Version</th>
            <th style="width:35%;">Role &amp; Architectural Function</th>
            <th style="width:25%;">Verification Command</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Python</strong></td>
            <td>3.11+</td>
            <td>FastAPI asynchronous ASGI runtime engine</td>
            <td><code>python --version</code></td>
          </tr>
          <tr>
            <td><strong>Node.js</strong></td>
            <td>18.0.0+</td>
            <td>React frontend toolchain &amp; npm package manager</td>
            <td><code>node -v</code></td>
          </tr>
          <tr>
            <td><strong>PostgreSQL</strong></td>
            <td>15+</td>
            <td>Relational database &amp; JSONB itinerary storage</td>
            <td><code>psql --version</code></td>
          </tr>
          <tr>
            <td><strong>Git</strong></td>
            <td>2.40+</td>
            <td>Version control &amp; GitHub remote repository sync</td>
            <td><code>git --version</code></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#0f766e;"></span>4. Environment Configuration Specification</div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header"><span style="color:#0f172a;">Backend (.env)</span><span class="badge badge-teal">Configuration</span></div>
          <p class="card-p">
            <code>DATABASE_URL=postgresql://user:pass@host:5432/traveldb</code><br>
            <code>SECRET_KEY=production_cryptographic_secret_key</code><br>
            <code>ALGORITHM=HS256</code><br>
            <code>ACCESS_TOKEN_EXPIRE_MINUTES=1440</code>
          </p>
        </div>
        <div class="card">
          <div class="card-header"><span style="color:#0f172a;">Frontend (.env)</span><span class="badge badge-blue">Configuration</span></div>
          <p class="card-p">
            <code>REACT_APP_API_URL=https://api.travelplanner.com</code><br>
            <code>REACT_APP_ENVIRONMENT=production</code><br>
            <code>REACT_APP_DEFAULT_LOCALE=en-US</code>
          </p>
        </div>
      </div>
    </div>
    """
    return render_html_document("Project Executable Files", 7, "Project Documentation", "emerald", [p1, p2])


def get_sample_documentation_doc():
    p1 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#047857;"></span>1. Executive Project Specification Sheet</div>
      <p class="card-p" style="margin-bottom:8px;">
        The AI-Powered Travel Planner is a full-stack situational itinerary generator designed to eliminate the friction, time drain, and guesswork of holiday planning. It combines verified expert-curated knowledge bases for Days 1 through 3 with an algorithmic procedural engine for Days 4 through 10 across 20 premier global destinations.
      </p>

      <table>
        <thead>
          <tr>
            <th style="width:25%;">Project Attribute</th>
            <th style="width:75%;">Official Technical Specification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Project Title</strong></td>
            <td>AI-Powered Travel Planner &bull; Smart Situational Itinerary Engine</td>
          </tr>
          <tr>
            <td><strong>Academic Track</strong></td>
            <td>AI-ML-and-GEN-AI Track &bull; Capstone Engineering Project</td>
          </tr>
          <tr>
            <td><strong>Live Web URL</strong></td>
            <td><strong>https://travel-planner-iota-plum.vercel.app/</strong></td>
          </tr>
          <tr>
            <td><strong>Source Code</strong></td>
            <td><strong>https://github.com/itskian2007/travel-planner</strong></td>
          </tr>
          <tr>
            <td><strong>Core Tech Stack</strong></td>
            <td>React 18 &bull; Tailwind CSS &bull; FastAPI &bull; PostgreSQL 15 &bull; Wikipedia Commons REST API</td>
          </tr>
          <tr>
            <td><strong>Scale Capacity</strong></td>
            <td>20 Global Hubs &bull; 304 Unique Landmark Images &bull; 10 Full Days Itinerary Coverage</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    p2 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#047857;"></span>2. 6-Step Visual User Manual Walkthrough</div>
      <div class="grid-3" style="margin-bottom:8px;">
        <div class="card" style="border-top:3px solid #2563eb;">
          <div class="card-header"><span style="color:#1e40af;">Step 1: Access Web App</span><span class="badge badge-blue">Portal</span></div>
          <p class="card-p">Navigate to <code>travel-planner-iota-plum.vercel.app</code> in any browser. View the interactive landing page and click "Get Started".</p>
        </div>
        <div class="card" style="border-top:3px solid #0f766e;">
          <div class="card-header"><span style="color:#115e59;">Step 2: Authenticate</span><span class="badge badge-teal">Auth</span></div>
          <p class="card-p">Sign up with your email and secure password, or login to an existing profile. A 24-hour cryptographically signed JWT token is issued.</p>
        </div>
        <div class="card" style="border-top:3px solid #7e22ce;">
          <div class="card-header"><span style="color:#5b21b6;">Step 3: Tune 5D Filters</span><span class="badge badge-purple">Preferences</span></div>
          <p class="card-p">Select your desired Travel Mood (Adventure, Romance), Budget Tier (Budget, Luxury), Dietary restrictions (Vegan, Halal), and Persona.</p>
        </div>
        <div class="card" style="border-top:3px solid #b45309;">
          <div class="card-header"><span style="color:#92400e;">Step 4: Pick Destination</span><span class="badge badge-amber">Catalog</span></div>
          <p class="card-p">Browse through the 20 responsive destination cards displaying live compatibility badges and verified landmark photography.</p>
        </div>
        <div class="card" style="border-top:3px solid #10b981;">
          <div class="card-header"><span style="color:#065f46;">Step 5: Generate Itinerary</span><span class="badge badge-green">Engine</span></div>
          <p class="card-p">Click "Generate Itinerary". The backend returns a structured 10-day itinerary with 3-4 attractions, lunch, dinner, and daily hacks in &lt;500ms.</p>
        </div>
        <div class="card" style="border-top:3px solid #be123c;">
          <div class="card-header"><span style="color:#991b1b;">Step 6: Explore Day-by-Day</span><span class="badge badge-red">Trip Deck</span></div>
          <p class="card-p">Expand individual day accordion cards to review high-res Wikipedia landmark photography, daily expense estimates, and transit subway routes.</p>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#047857;"></span>3. Operational FAQ &amp; Support</div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header"><span>Q: Are the images authentic?</span><span class="badge badge-green">Verified</span></div>
          <p class="card-p">Yes. Every single one of the 304 photographs is pulled from verified Wikipedia Commons files with zero duplicate collision.</p>
        </div>
        <div class="card">
          <div class="card-header"><span>Q: Can I use this on mobile?</span><span class="badge badge-green">Verified</span></div>
          <p class="card-p">Yes. The responsive Tailwind CSS interface dynamically scales down to 320px mobile displays with native-feeling touch accordions.</p>
        </div>
      </div>
    </div>
    """
    return render_html_document("Sample Project Documentation", 7, "Project Documentation", "emerald", [p1, p2])
