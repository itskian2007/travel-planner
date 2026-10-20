"""
Master Design System and HTML Page Template Generator for Documentation PDFs.
Ensures zero text overlap, modern typography, crisp tables, and rich graphics.
"""

GRADIENTS = {
    "indigo": ("#1e1b4b", "#4338ca", "#06b6d4"),   # Phase 1: Ideation
    "teal":   ("#0f172a", "#0f766e", "#14b8a6"),   # Phase 2: Requirements
    "purple": ("#3b0764", "#7e22ce", "#a855f7"),   # Phase 3: Design
    "amber":  ("#451a03", "#b45309", "#f59e0b"),   # Phase 4: Planning
    "blue":   ("#172554", "#2563eb", "#38bdf8"),   # Phase 5: Development
    "rose":   ("#4c0519", "#be123c", "#f43f5e"),   # Phase 6: Testing
    "emerald":("#022c22", "#047857", "#10b981"),   # Phase 7: Documentation
    "violet": ("#2e1065", "#6d28d9", "#ec4899"),   # Phase 8: Demonstration
}

MASTER_CSS = """
:root {
  --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}

@page {
  size: A4 portrait;
  margin: 10mm 12mm 12mm 12mm;
}

* {
  box-sizing: border-box;
}

body {
  font-family: var(--font-main);
  color: #1e293b;
  background: #ffffff;
  margin: 0;
  padding: 0;
  line-height: 1.45;
  font-size: 9pt;
  -webkit-print-color-adjust: exact !important;
  print-color-adjust: exact !important;
}

.page {
  page-break-after: always;
  display: flex;
  flex-direction: column;
  height: 270mm;
  max-height: 270mm;
  position: relative;
  overflow: hidden;
  padding-bottom: 8mm;
}

.page:last-child {
  page-break-after: auto;
}

/* Header Banner */
.doc-header {
  color: white;
  padding: 14px 18px;
  border-radius: 10px;
  margin-bottom: 14px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  flex-shrink: 0;
}

.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}

.phase-badge {
  background: rgba(255, 255, 255, 0.22);
  backdrop-filter: blur(4px);
  padding: 3px 10px;
  border-radius: 9999px;
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.status-pill {
  background: #10b981;
  color: white;
  padding: 2px 8px;
  border-radius: 9999px;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.04em;
}

.doc-title {
  font-size: 17pt;
  font-weight: 800;
  margin: 2px 0 4px 0;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

.doc-subtitle {
  font-size: 8.5pt;
  opacity: 0.92;
  font-weight: 500;
}

.meta-bar {
  display: flex;
  gap: 16px;
  margin-top: 8px;
  padding-top: 6px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 7pt;
  opacity: 0.95;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 4px;
}

.page-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
  overflow: hidden;
}

/* Sections */
.section {
  flex-shrink: 0;
}

.section-title {
  font-size: 10pt;
  font-weight: 700;
  color: #0f172a;
  margin: 0 0 6px 0;
  display: flex;
  align-items: center;
  gap: 6px;
  padding-bottom: 3px;
  border-bottom: 1.5px solid #e2e8f0;
}

.section-indicator {
  display: inline-block;
  width: 4px;
  height: 12px;
  border-radius: 2px;
}

/* Grid Layouts */
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

.grid-3 {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 8px;
}

.grid-4 {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 8px;
}

.grid-5 {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  gap: 6px;
}

/* Cards */
.card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 8px 10px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02);
}

.card-header {
  font-size: 8.5pt;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-p {
  font-size: 8pt;
  color: #475569;
  margin: 0;
  line-height: 1.4;
}

/* Tables */
table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 7.5pt;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  overflow: hidden;
}

th {
  background: #1e293b;
  color: white;
  padding: 5px 8px;
  text-align: left;
  font-weight: 600;
  font-size: 7pt;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

td {
  padding: 4.5px 8px;
  border-top: 1px solid #e2e8f0;
  color: #334155;
  vertical-align: middle;
}

tr:nth-child(even) td {
  background: #f8fafc;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 1.5px 6px;
  border-radius: 9999px;
  font-size: 6.5pt;
  font-weight: 700;
  text-align: center;
  white-space: nowrap;
}

.badge-green  { background: #d1fae5; color: #065f46; }
.badge-blue   { background: #dbeafe; color: #1e40af; }
.badge-purple { background: #ede9fe; color: #5b21b6; }
.badge-amber  { background: #fef3c7; color: #92400e; }
.badge-red    { background: #fee2e2; color: #991b1b; }
.badge-teal   { background: #ccfbf1; color: #115e59; }
.badge-slate  { background: #f1f5f9; color: #475569; }

/* Stats Counters */
.stat-box {
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 8px;
  text-align: center;
}

.stat-num {
  font-size: 16pt;
  font-weight: 800;
  line-height: 1.1;
}

.stat-label {
  font-size: 6.5pt;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-top: 2px;
}

/* Dark Code Terminal */
.code-box {
  background: #0f172a;
  color: #e2e8f0;
  border-radius: 6px;
  padding: 8px 10px;
  font-family: var(--font-mono);
  font-size: 7pt;
  line-height: 1.45;
  border: 1px solid #1e293b;
  overflow: hidden;
}

.code-title {
  color: #94a3b8;
  font-size: 6.5pt;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 4px;
  padding-bottom: 3px;
  border-bottom: 1px solid #334155;
  display: flex;
  justify-content: space-between;
}

/* Footer */
.footer {
  margin-top: auto;
  padding-top: 8px;
  border-top: 1px solid #e2e8f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 7pt;
  color: #64748b;
  flex-shrink: 0;
}
"""

def render_html_document(title, phase_num, phase_name, gradient_key, pages):
    """
    Renders a multi-page HTML document.
    pages: list of HTML strings for the body of each page.
    """
    g_start, g_mid, g_end = GRADIENTS.get(gradient_key, GRADIENTS["indigo"])

    page_elements = []
    total_pages = len(pages)

    for i, page_content in enumerate(pages):
        page_num = i + 1
        page_html = f"""
        <div class="page">
          <div class="doc-header" style="background: linear-gradient(135deg, {g_start} 0%, {g_mid} 50%, {g_end} 100%);">
            <div class="header-top">
              <span class="phase-badge">Phase {phase_num} &bull; {phase_name}</span>
              <span class="status-pill">&#x2714; VERIFIED SPECIFICATION</span>
            </div>
            <div class="doc-title">{title}</div>
            <div class="doc-subtitle">AI-Powered Travel Planner &bull; Smart Situational Itinerary Engine</div>
            <div class="meta-bar">
              <div class="meta-item"><strong>Live URL:</strong> travel-planner-iota-plum.vercel.app</div>
              <div class="meta-item"><strong>Repo:</strong> github.com/itskian2007/travel-planner</div>
              <div class="meta-item"><strong>Tech:</strong> React + FastAPI + PostgreSQL</div>
              <div class="meta-item"><strong>Team:</strong> itskian2007</div>
            </div>
          </div>

          <div class="page-body">
            {page_content}
          </div>

          <div class="footer">
            <div>AI-Powered Travel Planner &bull; {title}</div>
            <div>AI-ML &amp; GEN-AI Track &bull; Page {page_num} of {total_pages}</div>
          </div>
        </div>
        """
        page_elements.append(page_html)

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
{MASTER_CSS}
:root {{
  --gradient-start: {g_start};
  --gradient-mid: {g_mid};
  --gradient-end: {g_end};
}}
</style>
</head>
<body>
{''.join(page_elements)}
</body>
</html>
"""
    return full_html
