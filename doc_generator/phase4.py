"""
Phase 4: Project Planning Phase Documents
- Project Planning
"""
from .styles import render_html_document

def get_project_planning_doc():
    p1 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#b45309;"></span>1. Project Lifecycle &amp; Sprint Gantt Timeline</div>
      <p class="card-p" style="margin-bottom:8px;">
        The Travel Planner was engineered over a disciplined <strong>10-week lifecycle</strong> partitioned into five 2-week Agile sprints. The Gantt chart below highlights the sequence from requirements discovery to final cloud deployment and automated performance validation.
      </p>

      <!-- 10-Week Sprint Gantt Chart SVG -->
      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:10px; text-align:center;">
        <svg viewBox="0 0 760 145" style="width:100%; height:auto; max-height:145px; font-family:sans-serif;">
          <!-- Week Header -->
          <rect x="140" y="8" width="58" height="18" fill="#1e293b" /><text x="169" y="20" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Wk 1</text>
          <rect x="200" y="8" width="58" height="18" fill="#1e293b" /><text x="229" y="20" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Wk 2</text>
          <rect x="260" y="8" width="58" height="18" fill="#1e293b" /><text x="289" y="20" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Wk 3</text>
          <rect x="320" y="8" width="58" height="18" fill="#1e293b" /><text x="349" y="20" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Wk 4</text>
          <rect x="380" y="8" width="58" height="18" fill="#1e293b" /><text x="409" y="20" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Wk 5</text>
          <rect x="440" y="8" width="58" height="18" fill="#1e293b" /><text x="469" y="20" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Wk 6</text>
          <rect x="500" y="8" width="58" height="18" fill="#1e293b" /><text x="529" y="20" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Wk 7</text>
          <rect x="560" y="8" width="58" height="18" fill="#1e293b" /><text x="589" y="20" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Wk 8</text>
          <rect x="620" y="8" width="58" height="18" fill="#1e293b" /><text x="649" y="20" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Wk 9</text>
          <rect x="680" y="8" width="58" height="18" fill="#1e293b" /><text x="709" y="20" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Wk 10</text>

          <!-- Sprint 1 -->
          <text x="15" y="42" fill="#0f172a" font-weight="bold" font-size="7.5">Sprint 1: Scope &amp; Architecture</text>
          <rect x="140" y="32" width="118" height="16" rx="3" fill="#4338ca" />
          <text x="199" y="43" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">&#x2714; Research &amp; Schemas</text>

          <!-- Sprint 2 -->
          <text x="15" y="64" fill="#0f172a" font-weight="bold" font-size="7.5">Sprint 2: Auth &amp; Core Backend</text>
          <rect x="260" y="54" width="118" height="16" rx="3" fill="#2563eb" />
          <text x="319" y="65" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">&#x2714; FastAPI + PostgreSQL</text>

          <!-- Sprint 3 -->
          <text x="15" y="86" fill="#0f172a" font-weight="bold" font-size="7.5">Sprint 3: 20 Cities &amp; 5D Filters</text>
          <rect x="380" y="76" width="118" height="16" rx="3" fill="#0f766e" />
          <text x="439" y="87" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">&#x2714; React Catalog + Filters</text>

          <!-- Sprint 4 -->
          <text x="15" y="108" fill="#0f172a" font-weight="bold" font-size="7.5">Sprint 4: 10-Day Hybrid Engine</text>
          <rect x="500" y="98" width="118" height="16" rx="3" fill="#b45309" />
          <text x="559" y="109" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">&#x2714; Procedural Day 4-10</text>

          <!-- Sprint 5 -->
          <text x="15" y="130" fill="#0f172a" font-weight="bold" font-size="7.5">Sprint 5: Testing &amp; Vercel Edge</text>
          <rect x="620" y="120" width="118" height="16" rx="3" fill="#047857" />
          <text x="679" y="131" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">&#x2714; Live Cloud Production</text>
        </svg>
      </div>
    </div>
    """

    p2 = """
    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#b45309;"></span>2. Agile Sprint Deliverables &amp; Milestones</div>
      <div class="grid-3">
        <div class="card" style="border-top:3px solid #4338ca;">
          <div class="card-header"><span style="color:#3730a3;">Sprint 1 (Wk 1-2)</span><span class="badge badge-purple">DONE</span></div>
          <p class="card-p">
            &bull; Problem statements &amp; user persona.<br>
            &bull; 4-Quadrant empathy mapping.<br>
            &bull; DFD Level 0 &amp; Level 1 design.<br>
            &bull; Tech stack selection &amp; justification.
          </p>
        </div>
        <div class="card" style="border-top:3px solid #2563eb;">
          <div class="card-header"><span style="color:#1e40af;">Sprint 2 (Wk 3-4)</span><span class="badge badge-blue">DONE</span></div>
          <p class="card-p">
            &bull; FastAPI backend structure setup.<br>
            &bull; PostgreSQL database &amp; migrations.<br>
            &bull; User registration &amp; login endpoints.<br>
            &bull; JWT token issuance &amp; auth middleware.
          </p>
        </div>
        <div class="card" style="border-top:3px solid #0f766e;">
          <div class="card-header"><span style="color:#115e59;">Sprint 3 (Wk 5-6)</span><span class="badge badge-teal">DONE</span></div>
          <p class="card-p">
            &bull; 20 destination dataset curation.<br>
            &bull; 5D filtering module (Mood, Diet).<br>
            &bull; React DestinationCard grid.<br>
            &bull; Real-time interactive filter UI.
          </p>
        </div>
        <div class="card" style="border-top:3px solid #b45309;">
          <div class="card-header"><span style="color:#92400e;">Sprint 4 (Wk 7-8)</span><span class="badge badge-amber">DONE</span></div>
          <p class="card-p">
            &bull; Curated Day 1-3 expert itineraries.<br>
            &bull; Procedural Day 4-10 engine algorithm.<br>
            &bull; Wikipedia API 304 unique photos.<br>
            &bull; Zero duplicate image verification.
          </p>
        </div>
        <div class="card" style="border-top:3px solid #047857;">
          <div class="card-header"><span style="color:#065f46;">Sprint 5 (Wk 9-10)</span><span class="badge badge-green">DONE</span></div>
          <p class="card-p">
            &bull; JMeter load &amp; latency testing.<br>
            &bull; Security penetration audit.<br>
            &bull; Vercel edge deployment &amp; CDN.<br>
            &bull; Complete project documentation.
          </p>
        </div>
        <div class="card" style="border-top:3px solid #10b981;">
          <div class="card-header"><span style="color:#065f46;">Launch Status</span><span class="badge badge-green">LIVE</span></div>
          <p class="card-p">
            &bull; URL: travel-planner-iota-plum.vercel.app<br>
            &bull; 100% Sprint goals achieved.<br>
            &bull; Zero blocking bugs reported.<br>
            &bull; Git repository synced to main.
          </p>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title"><span class="section-indicator" style="background:#be123c;"></span>3. Risk Management &amp; Mitigation Register</div>
      <table>
        <thead>
          <tr>
            <th style="width:10%;">Risk ID</th>
            <th style="width:30%;">Identified Risk Scenario</th>
            <th style="width:15%;">Severity</th>
            <th style="width:45%;">Engineered Mitigation Strategy</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>RSK-01</strong></td>
            <td>Wikipedia Commons API Rate Limiting</td>
            <td><span class="badge badge-amber">MEDIUM</span></td>
            <td>Pre-cached media metadata in static database layer with local SVG fallbacks.</td>
          </tr>
          <tr>
            <td><strong>RSK-02</strong></td>
            <td>PostgreSQL Cloud Connection Exhaustion</td>
            <td><span class="badge badge-red">HIGH</span></td>
            <td>Configured SQLAlchemy connection pooling (pool_size=10, max_overflow=20).</td>
          </tr>
          <tr>
            <td><strong>RSK-03</strong></td>
            <td>Duplicate Landmark Image Collision</td>
            <td><span class="badge badge-red">HIGH</span></td>
            <td>Built strict deduplication validation script checking MD5 hash &amp; landmark keys.</td>
          </tr>
          <tr>
            <td><strong>RSK-04</strong></td>
            <td>CORS Failure between Frontend &amp; API</td>
            <td><span class="badge badge-blue">LOW</span></td>
            <td>Configured FastAPI CORSMiddleware with explicit origin whitelists.</td>
          </tr>
        </tbody>
      </table>
    </div>
    """
    return render_html_document("Project Planning", 4, "Project Planning Phase", "amber", [p1, p2])
