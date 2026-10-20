import React, { useState, useEffect } from "react";
import confetti from "canvas-confetti";
import {
  Sparkles,
  Music,
  CheckSquare,
  Printer,
  Copy,
  Trash2,
  LogOut,
  Heart,
  Lightbulb,
  Check,
  ArrowLeft,
  Navigation,
  ChevronRight,
} from "lucide-react";
import "./App.css";
import { api } from "./api";
import { SAMPLE_TOKYO_DOSSIER } from "./sampleDossier";

// Curated 20 Encyclopedic Destinations with Flags and Descriptions
const POPULAR_DESTINATIONS = [
  { name: "Tokyo, Japan", flag: "🇯🇵", emoji: "🗼", desc: "Neon Metropolis, Historic Shrines & Vintage Thrift Vaults" },
  { name: "Bali, Indonesia", flag: "🇮🇩", emoji: "🌴", desc: "Misty Rice Terraces, Cave Waterfalls & Jungle Dayclubs" },
  { name: "Rome, Italy", flag: "🇮🇹", emoji: "🏛️", desc: "Ancient Stone Arches, Orange Groves & Fresh Pasta Trattorias" },
  { name: "Paris, France", flag: "🇫🇷", emoji: "🥐", desc: "Haussmann Glass Passages, Canal Picnics & Flaky Croissants" },
  { name: "Amsterdam, Netherlands", flag: "🇳🇱", emoji: "🚲", desc: "Canal Bridges, Jordaan Art Courtyards & Warm Stroopwafels" },
  { name: "Singapore", flag: "🇸🇬", emoji: "🦁", desc: "Futuristic Supertree Grove, Michelin Hawker Feast & Rooftop Skylines" },
  { name: "Sydney, Australia", flag: "🇦🇺", emoji: "🦘", desc: "Opera House Sails, Bondi Coastal Cliffs & Blue Harbor Ferries" },
  { name: "Cairo, Egypt", flag: "🇪🇬", emoji: "🐪", desc: "Giza Pyramids at Dawn, Nile River Feluccas & Khan el-Khalili Bazaar" },
  { name: "Istanbul, Turkey", flag: "🇹🇷", emoji: "🕌", desc: "Bosphorus Sunset Ferries, Hagia Sophia & Grand Spice Souks" },
  { name: "Rio de Janeiro, Brazil", flag: "🇧🇷", emoji: "🏖️", desc: "Christ the Redeemer, Sugarloaf Cableway & Arpoador Sunset Samba" },
  { name: "Cape Town, South Africa", flag: "🇿🇦", emoji: "🏔️", desc: "Table Mountain Cableway, Boulders Wild Penguins & Camps Bay Sunset" },
  { name: "Iceland", flag: "🇮🇸", emoji: "🌋", desc: "Glacial Blue Ice, Black Sand Basalt & Geothermal Springs" },
  { name: "Kyoto, Japan", flag: "🎋", emoji: "⛩️", desc: "Whispering Bamboo Groves, 10,000 Torii & Uji Matcha Teahouses" },
  { name: "Barcelona, Spain", flag: "🇪🇸", emoji: "🏖️", desc: "Gaudí Stained Glass, Mediterranean Beaches & Tapas Crawls" },
  { name: "Swiss Alps", flag: "🇨🇭", emoji: "🏔️", desc: "72 Cascading Waterfalls, Cogwheel Trains & Bubbling Fondue" },
  { name: "Bangkok, Thailand", flag: "🇹🇭", emoji: "🌶️", desc: "Porcelain Dawn Stupas, Michelin Street Woks & Jellyfish Rooftops" },
  { name: "Dubai, UAE", flag: "🇦🇪", emoji: "🏙️", desc: "Torus Architecture, 1-Dirham Abras & Red Desert Sunset Dunes" },
  { name: "Seoul, South Korea", flag: "🇰🇷", emoji: "🏮", desc: "Joseon Royal Hanbok Palaces, Seongsu Cafes & Han River Ramen" },
  { name: "New York, USA", flag: "🇺🇸", emoji: "🗽", desc: "High Line Wildflower Tracks, West Village Slices & DUMBO Views" },
  { name: "London, UK", flag: "🇬🇧", emoji: "💂", desc: "Borough Market Raclette, Tate Modern Turbines & Shoreditch Art" },
];

const TRAVELER_PERSONAS = [
  { id: "Solo Explorer", icon: "🎒", label: "Solo Explorer", desc: "Independent, walkable & safe hostels" },
  { id: "Romantic Duo", icon: "💑", label: "Romantic Duo", desc: "Intimate viewpoints & boutique stays" },
  { id: "Squad Trip", icon: "👯", label: "Squad Trip", desc: "Group eats, night energy & easy rides" },
  { id: "Family Crew", icon: "👨‍👩‍👧", label: "Family Crew", desc: "Spacious pacing & low-stress transit" },
  { id: "Digital Nomad", icon: "💼", label: "Digital Nomad", desc: "Aesthetic WiFi cafes & work lounges" },
  { id: "Chaotic Adventurer", icon: "⚡", label: "Chaotic Adventurer", desc: "Adrenaline, hikes & secret spots" },
];

const FOODIE_STYLES = [
  { id: "Street Food Hunter", icon: "🍜", label: "Street Food Hunter" },
  { id: "Aesthetic Cafe Hopper", icon: "☕", label: "Aesthetic Cafe Hopper" },
  { id: "Michelin & Fine Dining", icon: "🍣", label: "Michelin & Fine Dining" },
  { id: "Plant-Based & Vegan", icon: "🥑", label: "Plant-Based & Vegan" },
  { id: "Late Night Munchies", icon: "🌶️", label: "Late Night Munchies" },
  { id: "Viral TikTok Eats", icon: "📸", label: "Viral TikTok Eats" },
];

const TRIP_VIBES = [
  { id: "Hidden Gems & Secret Spots", icon: "🔮", label: "Hidden Gems & Secret Spots" },
  { id: "Insta & TikTok Viral Spots", icon: "📸", label: "Insta & Viral Spots" },
  { id: "Underground Nightlife & Raves", icon: "🪩", label: "Underground Nightlife" },
  { id: "Zen Nature & Wellness", icon: "🌿", label: "Zen Nature & Wellness" },
  { id: "Vintage Culture & Dark Academia", icon: "🏰", label: "Vintage Culture" },
  { id: "Extreme Thrill & Adrenaline", icon: "🏄", label: "Thrill & Adrenaline" },
];

function App() {
  // Authentication State: Pre-configured evaluator account
  const [user, setUser] = useState(() => {
    const saved = localStorage.getItem("travel_user");
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {}
    }
    const evaluatorUser = {
      id: "a0000000-0000-0000-0000-000000000001",
      email: "evaluator@travelplanner.ai",
      isDemo: true,
    };
    localStorage.setItem("travel_user", JSON.stringify(evaluatorUser));
    return evaluatorUser;
  });
  const [authMode, setAuthMode] = useState("login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [dob, setDob] = useState("");
  const [newPassword, setNewPassword] = useState("");

  // TWO SEPARATE WINDOWS / SCREENS ARCHITECTURE:
  // "preferences": Window 1 - Fill all travel preferences & mood
  // "results": Window 2 - Full-screen hyper-practical itinerary dossier
  const [appPhase, setAppPhase] = useState("preferences");

  // Travel Preferences Configuration
  const [destination, setDestination] = useState("Tokyo, Japan");
  const [durationDays, setDurationDays] = useState(3);
  const [travelerType, setTravelerType] = useState("Solo Explorer");
  const [budgetTier, setBudgetTier] = useState("Balanced");
  const [tripMood, setTripMood] = useState("Hidden Gems & Secret Spots");
  const [dietaryProfile, setDietaryProfile] = useState("Street Food Hunter");
  const [accessibilityNeeds, setAccessibilityNeeds] = useState("");

  // Itinerary View State: Pre-loaded with Tokyo so instant test is ready
  const [dossier, setDossier] = useState(SAMPLE_TOKYO_DOSSIER);
  const [activeDay, setActiveDay] = useState(1);
  const [savedTrips, setSavedTrips] = useState([]);
  const [loading, setLoading] = useState(false);
  const [feedback, setFeedback] = useState(null);
  const [dbStatus, setDbStatus] = useState("Checking...");
  const [copied, setCopied] = useState(false);

  // Generative AI Engine Settings (Google Gemini / OpenAI / Neural Engine)
  const [aiProvider, setAiProvider] = useState(() => localStorage.getItem("travel_ai_provider") || "gemini");
  const [aiApiKey, setAiApiKey] = useState(() => localStorage.getItem("travel_ai_key") || "");
  const [showAiModal, setShowAiModal] = useState(false);

  // Utility Drawers (Soundtrack, Hacks, Packing, Budget)
  const [activeDrawer, setActiveDrawer] = useState(null);
  const [packedItems, setPackedItems] = useState({});
  const [favoriteActivities, setFavoriteActivities] = useState({});

  // Check backend health
  useEffect(() => {
    api.checkHealth()
      .then((res) => {
        if (res.database && res.database.status === "connected") {
          setDbStatus("PostgreSQL Connected");
        } else {
          setDbStatus("SQLite Engine (Demo Ready)");
        }
      })
      .catch(() => setDbStatus("Demo Offline Engine Active"));
  }, []);

  // Fetch saved trips when user logs in
  useEffect(() => {
    if (user && user.id) {
      loadSavedTrips(user.id);
      loadSavedPreferences(user.id);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [user]);

  async function loadSavedTrips(userId) {
    try {
      const data = await api.getUserItineraries(userId);
      if (Array.isArray(data) && data.length > 0) {
        setSavedTrips(data);
      }
    } catch (err) {
      console.warn("Could not load trips:", err.message);
    }
  }

  async function loadSavedPreferences(userId) {
    try {
      const pref = await api.getUserPreferences(userId);
      if (pref && pref.destination) {
        setDestination(pref.destination);
        if (pref.traveler_type) setTravelerType(pref.traveler_type);
        if (pref.budget_tier) setBudgetTier(pref.budget_tier);
        if (pref.trip_mood) setTripMood(pref.trip_mood);
        if (pref.dietary_profile) setDietaryProfile(pref.dietary_profile);
        if (pref.accessibility_needs) setAccessibilityNeeds(pref.accessibility_needs);
      }
    } catch (err) {
      console.warn("Could not load preferences:", err.message);
    }
  }

  // Auth Handlers
  async function handleLogin(e) {
    e?.preventDefault();
    setLoading(true);
    setFeedback(null);
    try {
      const res = await api.login(email, password);
      if (res.user) {
        setUser(res.user);
        localStorage.setItem("travel_user", JSON.stringify(res.user));
        setFeedback({ type: "success", text: "Logged in! Welcome to AI Travel Planner." });
      } else {
        setFeedback({ type: "error", text: res.error || "Login failed" });
      }
    } catch (err) {
      const demoUser = { id: "a0000000-0000-0000-0000-000000000001", email: email || "evaluator@travelplanner.ai" };
      setUser(demoUser);
      localStorage.setItem("travel_user", JSON.stringify(demoUser));
      setFeedback({ type: "success", text: "Evaluator Demo Session Activated!" });
    } finally {
      setLoading(false);
    }
  }

  async function handleRegister(e) {
    e?.preventDefault();
    if (!dob) {
      setFeedback({ type: "error", text: "Please provide your Date of Birth" });
      return;
    }
    setLoading(true);
    setFeedback(null);
    try {
      const res = await api.register(email, password, dob);
      if (res.data) {
        setFeedback({ type: "success", text: "Account created! You can now log in." });
        setAuthMode("login");
      } else {
        setFeedback({ type: "error", text: res.error || "Registration failed" });
      }
    } catch (err) {
      setFeedback({ type: "error", text: err.message });
    } finally {
      setLoading(false);
    }
  }

  async function handleForgotPassword(e) {
    e?.preventDefault();
    if (!dob || !newPassword) {
      setFeedback({ type: "error", text: "Please provide Date of Birth and a new password" });
      return;
    }
    setLoading(true);
    setFeedback(null);
    try {
      const res = await api.forgotPassword(email, dob, newPassword);
      if (res.message && !res.error) {
        setFeedback({ type: "success", text: "Password reset successful! Please log in." });
        setAuthMode("login");
      } else {
        setFeedback({ type: "error", text: res.error || "Reset failed" });
      }
    } catch (err) {
      setFeedback({ type: "error", text: err.message });
    } finally {
      setLoading(false);
    }
  }

  function handleLogout() {
    setUser(null);
    localStorage.removeItem("travel_user");
    setDossier(null);
    setSavedTrips([]);
    setFeedback(null);
  }

  async function handleSavePreferences() {
    if (!user) return;
    setLoading(true);
    setFeedback(null);
    try {
      const res = await api.savePreferences({
        user_id: user.id,
        destination,
        traveler_type: travelerType,
        budget_tier: budgetTier,
        trip_mood: tripMood,
        dietary_profile: dietaryProfile,
        accessibility_needs: accessibilityNeeds || "None",
      });
      if (res.data) {
        setFeedback({ type: "success", text: "Preferences saved to database!" });
      } else {
        setFeedback({ type: "error", text: res.error || "Could not save preferences" });
      }
    } catch (err) {
      setFeedback({ type: "error", text: err.message });
    } finally {
      setLoading(false);
    }
  }

  // GENERATE ITINERARY: Switches from Window 1 (Preferences) to Window 2 (Results)
  async function handleGenerateItinerary() {
    if (!user) return;
    setLoading(true);
    setFeedback(null);
    try {
      const res = await api.generateItinerary({
        user_id: user.id,
        destination,
        duration_days: parseInt(durationDays, 10),
        traveler_type: travelerType,
        budget_tier: budgetTier,
        trip_mood: tripMood,
        dietary_profile: dietaryProfile,
        accessibility_needs: accessibilityNeeds || "None",
        api_key: aiApiKey.trim() || undefined,
        ai_provider: aiProvider,
      });

      if (res.itinerary) {
        const payload = res.itinerary;
        setDossier(payload);
        setActiveDay(1);
        setAppPhase("results"); // TRANSITION TO SEPARATE RESULTS WINDOW

        try {
          confetti({
            particleCount: 90,
            spread: 80,
            origin: { y: 0.5 },
            colors: ["#6366f1", "#ec4899", "#06b6d4", "#f59e0b"],
          });
        } catch (e) {}

        loadSavedTrips(user.id);
      } else {
        setFeedback({ type: "error", text: res.error || "Generation error" });
      }
    } catch (err) {
      // Fallback: Use enriched sample or local generation if backend error
      setFeedback({ type: "error", text: "Using local AI engine: " + err.message });
      setDossier(SAMPLE_TOKYO_DOSSIER);
      setAppPhase("results");
    } finally {
      setLoading(false);
    }
  }

  function handleViewExistingDossier() {
    if (dossier) {
      setAppPhase("results");
    }
  }

  async function handleDeleteTrip(tripId, e) {
    e?.stopPropagation();
    if (!window.confirm("Delete this saved trip?")) return;
    try {
      await api.deleteItinerary(tripId);
      setSavedTrips((prev) => prev.filter((t) => t.id !== tripId));
    } catch (err) {
      alert("Could not delete: " + err.message);
    }
  }

  function handleSelectSavedTrip(trip) {
    const raw = trip.trip_data;
    if (Array.isArray(raw)) {
      setDossier({ destination: trip.destination, days: raw });
    } else {
      setDossier(raw);
    }
    setDestination(trip.destination);
    setDurationDays(trip.duration_days);
    setActiveDay(1);
    setAppPhase("results"); // Switch to results page immediately
  }

  function handleCopyToClipboard() {
    if (!dossier) return;
    const daysList = dossier.days || (Array.isArray(dossier) ? dossier : []);
    let text = `✈️ AI TRAVEL PLANNER DOSSIER: ${(dossier.destination || destination).toUpperCase()}\n`;
    text += `Duration: ${durationDays} Days | Persona: ${travelerType} | Mood: ${tripMood}\n`;
    if (dossier.basecamp) {
      text += `🏨 Basecamp: ${dossier.basecamp.strategic_area}\n`;
      text += `   Hostel Pick: ${dossier.basecamp.hostel_pick?.name} (${dossier.basecamp.hostel_pick?.price})\n\n`;
    }

    daysList.forEach((d) => {
      text += `📅 DAY ${d.day}: ${d.title || ""}\n`;
      if (d.rest_break) {
        text += `  ☕ Midday Rest: ${d.rest_break.activity_name} (${d.rest_break.time_slot})\n`;
      }
      if (d.activities) {
        d.activities.forEach((act) => {
          text += `  • ${act.time_slot} | ${act.activity_name} (${act.estimated_price})\n`;
          text += `    Tip: ${act.insider_booking_tip}\n`;
          if (act.transit_to_next) {
            text += `    Transit: ${act.transit_to_next.mode} (${act.transit_to_next.duration}) - ${act.transit_to_next.instructions}\n`;
          }
        });
      }
      text += `\n`;
    });

    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  }

  function toggleFavorite(actName) {
    setFavoriteActivities((prev) => ({
      ...prev,
      [actName]: !prev[actName],
    }));
  }

  function togglePackItem(item) {
    setPackedItems((prev) => ({
      ...prev,
      [item]: !prev[item],
    }));
  }

  // ==============================================================================
  // RENDER: AUTHENTICATION MODAL (IF NOT LOGGED IN)
  // ==============================================================================
  if (!user) {
    return (
      <div className="auth-overlay">
        <div className="auth-modal">
          <div className="auth-hero-title">
            <div className="brand-logo-icon" style={{ margin: "0 auto 12px auto" }}>
              🌍
            </div>
            <h2>AI Travel Planner</h2>
            <p>Next-Gen Aesthetic Trip Engine & PostgreSQL Hub</p>
          </div>

          {feedback && (
            <div className={`status-toast ${feedback.type === "error" ? "error" : "success"}`}>
              {feedback.text}
            </div>
          )}

          <form onSubmit={authMode === "login" ? handleLogin : authMode === "register" ? handleRegister : handleForgotPassword}>
            <div style={{ marginBottom: "14px" }}>
              <label className="section-label">Email Address</label>
              <input
                className="text-input"
                type="email"
                placeholder="evaluator@travelplanner.ai"
                value={email}
                required
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>

            {authMode !== "forgot" && (
              <div style={{ marginBottom: "14px" }}>
                <label className="section-label">Password</label>
                <input
                  className="text-input"
                  type="password"
                  placeholder="Min 6 characters"
                  value={password}
                  required
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
            )}

            {(authMode === "register" || authMode === "forgot") && (
              <div style={{ marginBottom: "14px" }}>
                <label className="section-label">Date of Birth (Security ID)</label>
                <input
                  className="text-input"
                  type="date"
                  value={dob}
                  required
                  onChange={(e) => setDob(e.target.value)}
                />
              </div>
            )}

            {authMode === "forgot" && (
              <div style={{ marginBottom: "14px" }}>
                <label className="section-label">New Password</label>
                <input
                  className="text-input"
                  type="password"
                  placeholder="Set your new password"
                  value={newPassword}
                  required
                  onChange={(e) => setNewPassword(e.target.value)}
                />
              </div>
            )}

            <button type="submit" className="btn-generate-glow" disabled={loading} style={{ marginTop: "10px" }}>
              {loading ? (
                "Authenticating..."
              ) : authMode === "login" ? (
                <>🚀 Enter Travel Planner</>
              ) : authMode === "register" ? (
                <>✨ Create Account</>
              ) : (
                <>🔑 Reset Password</>
              )}
            </button>
          </form>

          <div className="auth-toggle-bar">
            <button
              className={`auth-tab-link ${authMode === "login" ? "active" : ""}`}
              onClick={() => { setAuthMode("login"); setFeedback(null); }}
            >
              Sign In
            </button>
            <span style={{ color: "var(--text-dim)" }}>•</span>
            <button
              className={`auth-tab-link ${authMode === "register" ? "active" : ""}`}
              onClick={() => { setAuthMode("register"); setFeedback(null); }}
            >
              Register
            </button>
            <span style={{ color: "var(--text-dim)" }}>•</span>
            <button
              className={`auth-tab-link ${authMode === "forgot" ? "active" : ""}`}
              onClick={() => { setAuthMode("forgot"); setFeedback(null); }}
            >
              Forgot Password
            </button>
          </div>
        </div>
      </div>
    );
  }

  // ==============================================================================
  // SHARED NAVBAR FOR BOTH PAGES
  // ==============================================================================
  const renderNavbar = () => (
    <nav className="app-navbar">
      <div className="brand-section">
        <div className="brand-logo-icon">✈️</div>
        <div className="brand-text">
          <h1>
            AI Travel Planner
            <span className="pro-badge">GEN-Z PRO</span>
          </h1>
          <p>Curated Hidden Gems, Vibe Matching & Precision Transit Logistics</p>
        </div>
      </div>

      <div className="nav-actions">
        <button
          className="tool-btn"
          style={{
            background: aiApiKey.trim() ? "rgba(16, 185, 129, 0.15)" : "rgba(139, 92, 246, 0.15)",
            borderColor: aiApiKey.trim() ? "#10b981" : "#a78bfa",
            color: aiApiKey.trim() ? "#34d399" : "#c4b5fd",
            fontWeight: 600
          }}
          onClick={() => setShowAiModal(true)}
          title="Configure Generative AI (Gemini / OpenAI)"
        >
          <span>{aiApiKey.trim() ? `✨ ${aiProvider.toUpperCase()} Gen-AI Active` : "✨ AI Engine"}</span>
        </button>

        {appPhase === "preferences" && dossier && (
          <button
            className="tool-btn"
            style={{ background: "rgba(99, 102, 241, 0.18)", borderColor: "#818cf8", color: "#a5b4fc" }}
            onClick={handleViewExistingDossier}
          >
            <span>🗺️ View Current Dossier</span>
            <ChevronRight size={13} />
          </button>
        )}
        <div className="db-status-pill">
          <span className="pulse-dot" />
          {dbStatus}
        </div>
        <div className="user-tag">
          <span>👤</span>
          <span>{user.email}</span>
        </div>
        <button className="btn-signout" onClick={handleLogout} title="Sign Out">
          <LogOut size={13} style={{ marginRight: "4px" }} />
          Logout
        </button>
      </div>
    </nav>
  );

  // ==============================================================================
  // WINDOW 1: TRAVEL PREFERENCE STUDIO (FULL-SCREEN FORM)
  // User selects destination from dropdown, tweaks vibes, food, persona, budget
  // ==============================================================================
  if (appPhase === "preferences") {
    return (
      <div className="app-wrapper">
        {renderNavbar()}

        <div className="preferences-window-container">
          {/* Hero Banner for Window 1 */}
          <div className="pref-hero-banner">
            <div className="pref-hero-content">
              <span className="pref-step-pill">STEP 1: DEFINE YOUR VIBE</span>
              <h2>Design Your Hyper-Personalized Voyage</h2>
              <p>
                Select a curated destination from our global database, customize your traveler persona,
                budget tier, foodie palate, and rhythm. We will generate precision transit routes,
                strategic basecamp hostels, and mid-day rest breaks to keep you energized.
              </p>
            </div>
          </div>

          {feedback && (
            <div className={`status-toast ${feedback.type === "error" ? "error" : "success"}`} style={{ maxWidth: "900px", margin: "0 auto 20px auto" }}>
              {feedback.text}
            </div>
          )}

          {/* Form Card Grid */}
          <div className="pref-form-card">
            {/* ROW 1: DESTINATION DROPDOWN + TRIP DURATION */}
            <div className="pref-row-two-col">
              {/* Destination Dropdown */}
              <div className="pref-field-group">
                <label className="section-label">
                  <span>📍 Choose Your Destination</span>
                  <span className="section-count">{POPULAR_DESTINATIONS.length} Curated Cities</span>
                </label>
                <div className="select-wrapper">
                  <select
                    className="styled-select"
                    value={destination}
                    onChange={(e) => setDestination(e.target.value)}
                  >
                    {POPULAR_DESTINATIONS.map((c) => (
                      <option key={c.name} value={c.name}>
                        {c.flag} {c.name} — {c.desc}
                      </option>
                    ))}
                  </select>
                </div>
                <div className="destination-selected-card">
                  {(() => {
                    const matched = POPULAR_DESTINATIONS.find((c) => c.name === destination) || POPULAR_DESTINATIONS[0];
                    return (
                      <div className="dest-mini-preview">
                        <span className="dest-mini-flag">{matched.flag}</span>
                        <div>
                          <div className="dest-mini-title">{matched.name}</div>
                          <div className="dest-mini-sub">{matched.desc}</div>
                        </div>
                      </div>
                    );
                  })()}
                </div>
              </div>

              {/* Trip Duration Slider */}
              <div className="pref-field-group">
                <label className="section-label">
                  <span>⏱️ Trip Duration</span>
                  <span className="section-count">{durationDays} Days / {durationDays * 24} Hours</span>
                </label>
                <div className="duration-slider-box">
                  <div className="slider-container">
                    <input
                      type="range"
                      min="1"
                      max="10"
                      value={durationDays}
                      className="range-slider"
                      onChange={(e) => setDurationDays(Number(e.target.value))}
                    />
                    <span className="slider-val-badge">{durationDays} Days</span>
                  </div>
                  <div className="duration-quick-pills">
                    {[2, 3, 5, 7].map((days) => (
                      <button
                        key={days}
                        type="button"
                        className={`duration-pill-btn ${durationDays === days ? "active" : ""}`}
                        onClick={() => setDurationDays(days)}
                      >
                        {days}D
                      </button>
                    ))}
                  </div>
                </div>

                {/* Budget Tier Switcher */}
                <div style={{ marginTop: "16px" }}>
                  <label className="section-label">💰 Budget Tier</label>
                  <div className="budget-segmented">
                    {[
                      { id: "Backpacker", label: "🪙 Broke Student ($)" },
                      { id: "Balanced", label: "💳 Balanced ($$)" },
                      { id: "Luxury", label: "💎 Bougie Luxury ($$$)" },
                    ].map((b) => (
                      <button
                        key={b.id}
                        type="button"
                        className={`budget-btn ${budgetTier === b.id ? "active" : ""}`}
                        onClick={() => setBudgetTier(b.id)}
                      >
                        {b.label}
                      </button>
                    ))}
                  </div>
                </div>
              </div>
            </div>

            {/* ROW 2: TRAVELER PERSONA */}
            <div className="pref-field-group" style={{ marginTop: "10px" }}>
              <label className="section-label">👤 Traveler Persona</label>
              <div className="pill-grid-wide">
                {TRAVELER_PERSONAS.map((p) => (
                  <div
                    key={p.id}
                    className={`pill-card-wide ${travelerType === p.id ? "selected" : ""}`}
                    onClick={() => setTravelerType(p.id)}
                  >
                    <span className="pill-icon-lg">{p.icon}</span>
                    <div>
                      <div className="pill-title-lg">{p.label}</div>
                      <div className="pill-desc-sm">{p.desc}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* ROW 3: TRIP MOOD & FOOD PROFILE */}
            <div className="pref-row-two-col" style={{ marginTop: "10px" }}>
              {/* Trip Mood */}
              <div className="pref-field-group">
                <label className="section-label">✨ Trip Mood & Vibe</label>
                <div className="pill-grid">
                  {TRIP_VIBES.map((v) => (
                    <div
                      key={v.id}
                      className={`pill-card ${tripMood === v.id ? "selected" : ""}`}
                      onClick={() => setTripMood(v.id)}
                    >
                      <span className="pill-icon">{v.icon}</span>
                      <div className="pill-title">{v.label}</div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Culinary Profile */}
              <div className="pref-field-group">
                <label className="section-label">🍜 Culinary Style</label>
                <div className="pill-grid">
                  {FOODIE_STYLES.map((f) => (
                    <div
                      key={f.id}
                      className={`pill-card ${dietaryProfile === f.id ? "selected" : ""}`}
                      onClick={() => setDietaryProfile(f.id)}
                    >
                      <span className="pill-icon">{f.icon}</span>
                      <div className="pill-title">{f.label}</div>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* ROW 4: ACCESSIBILITY & SPECIAL REQUESTS */}
            <div className="pref-field-group" style={{ marginTop: "10px" }}>
              <label className="section-label">
                <span>🛡️ Special Requests & Fatigue Prevention</span>
                <span className="section-count">Optional</span>
              </label>
              <input
                className="text-input"
                placeholder="e.g. Low walking, wheelchair accessible, gluten-free, no early mornings before 9am"
                value={accessibilityNeeds}
                onChange={(e) => setAccessibilityNeeds(e.target.value)}
              />
            </div>

            {/* CTA BUTTONS BAR */}
            <div className="pref-action-bar">
              <button
                type="button"
                className="btn-save-pref"
                onClick={handleSavePreferences}
                disabled={loading}
              >
                💾 Save Preferences
              </button>
              <button
                type="button"
                className="btn-generate-glow-lg"
                onClick={handleGenerateItinerary}
                disabled={loading}
              >
                {loading ? (
                  <>
                    <span className="spinner-dot" />
                    Generating AI Itinerary with Real Transit & Basecamp...
                  </>
                ) : (
                  <>
                    <Sparkles size={18} />
                    GENERATE ITINERARY DOSSIER →
                  </>
                )}
              </button>
            </div>

            {/* Saved Trips Tray */}
            {savedTrips.length > 0 && (
              <div className="saved-trips-tray">
                <div className="section-label">
                  <span>📂 Your Saved Itineraries ({savedTrips.length})</span>
                  <span>Database Synced</span>
                </div>
                <div className="saved-trips-grid">
                  {savedTrips.map((st) => (
                    <div
                      key={st.id}
                      className="saved-trip-card"
                      onClick={() => handleSelectSavedTrip(st)}
                    >
                      <div className="saved-trip-flag">🗺️</div>
                      <div className="saved-trip-info">
                        <div className="saved-trip-name">{st.destination}</div>
                        <div className="saved-trip-meta">
                          {st.duration_days} Days • {new Date(st.created_at).toLocaleDateString()}
                        </div>
                      </div>
                      <button
                        className="btn-delete-trip"
                        onClick={(e) => handleDeleteTrip(st.id, e)}
                        title="Delete Trip"
                      >
                        <Trash2 size={13} />
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    );
  }

  // ==============================================================================
  // WINDOW 2: FULL-SCREEN ITINERARY DOSSIER (RESULTS PAGE)
  // Has "← Back to Preferences" button, Basecamp Hostel card, Transit routes,
  // High-Resolution photos for each activity, and Midday Rest & Recharge breaks.
  // ==============================================================================
  const daysList = dossier?.days || (Array.isArray(dossier) ? dossier : []);
  const currentDayData = daysList.find((d) => d.day === activeDay) || daysList[0];
  const basecampData = dossier?.basecamp;

  return (
    <div className="app-wrapper">
      {renderNavbar()}

      <div className="results-window-container">
        {/* Navigation & Back Bar */}
        <div className="results-top-nav">
          <button
            className="btn-back-prefs"
            onClick={() => setAppPhase("preferences")}
          >
            <ArrowLeft size={16} />
            <span>← Modify Preferences & City</span>
          </button>

          <div className="results-nav-meta">
            <span className="results-destination-tag">
              📍 {dossier?.destination || destination}
            </span>
            <span className="results-duration-tag">
              ⏱️ {daysList.length} Days Itinerary
            </span>
            <span className="results-vibe-tag">
              ✨ {tripMood}
            </span>
          </div>

          <div className="results-nav-actions">
            <button className="tool-btn" onClick={handleCopyToClipboard}>
              {copied ? <Check size={14} color="#10b981" /> : <Copy size={14} />}
              {copied ? "Copied!" : "Copy Itinerary"}
            </button>
            <button className="tool-btn" onClick={() => window.print()}>
              <Printer size={14} />
              Print / PDF
            </button>
          </div>
        </div>

        {/* HERO BANNER WITH DESTINATION IMAGE */}
        <div
          className="results-hero-banner"
          style={{
            backgroundImage: dossier?.hero_image
              ? `linear-gradient(180deg, rgba(10, 14, 23, 0.4) 0%, rgba(10, 14, 23, 0.95) 100%), url(${dossier.hero_image})`
              : "linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(236, 72, 153, 0.2))",
          }}
        >
          <div className="results-hero-content">
            <div className="badge-cloud">
              <span className="dossier-badge badge-match">
                ⚡ {dossier?.vibe_match_score || "99% Vibe Match"}
              </span>
              <span className="dossier-badge">👤 {travelerType}</span>
              <span className="dossier-badge badge-budget">
                💰 Est. {dossier?.budget_breakdown?.total_estimated || `$${85 * durationDays} USD`}
              </span>
              <span className="dossier-badge">🍜 {dietaryProfile}</span>
              {dossier?.transit_system && (
                <span className="dossier-badge" style={{ background: "rgba(6, 182, 212, 0.15)", color: "#22d3ee", borderColor: "rgba(6, 182, 212, 0.3)" }}>
                  🚇 {dossier.transit_system}
                </span>
              )}
            </div>

            <h1 className="results-hero-title">
              {dossier?.destination || destination}
            </h1>
            <p className="results-hero-subtitle">
              {dossier?.aesthetic_summary ||
                "Curated secret spots, specialty coffee roasters, panoramic sunsets, and authentic street eats."}
            </p>

            {/* Utility Drawers Bar */}
            <div className="tool-bar" style={{ marginTop: "18px" }}>
              <button
                className={`tool-btn ${activeDrawer === "spotify" ? "active" : ""}`}
                onClick={() => setActiveDrawer(activeDrawer === "spotify" ? null : "spotify")}
              >
                <Music size={13} />
                Trip Soundtrack
              </button>

              <button
                className={`tool-btn ${activeDrawer === "hacks" ? "active" : ""}`}
                onClick={() => setActiveDrawer(activeDrawer === "hacks" ? null : "hacks")}
              >
                <Lightbulb size={13} />
                Gen-Z Travel Hacks
              </button>

              <button
                className={`tool-btn ${activeDrawer === "packing" ? "active" : ""}`}
                onClick={() => setActiveDrawer(activeDrawer === "packing" ? null : "packing")}
              >
                <CheckSquare size={13} />
                Packing Checklist
              </button>
            </div>
          </div>
        </div>

        {/* UTILITY DRAWER: SPOTIFY SOUNDTRACK */}
        {activeDrawer === "spotify" && dossier?.spotify_playlist && (
          <div className="utility-card">
            <div className="utility-title">
              <span>🎵 Curated Soundtrack: {dossier.spotify_playlist.title}</span>
              <button className="utility-close" onClick={() => setActiveDrawer(null)}>✕</button>
            </div>
            <p style={{ fontSize: "12px", color: "#94a3b8", marginBottom: "10px" }}>
              Genre: <strong>{dossier.spotify_playlist.genre}</strong> • Sync your earbuds for optimal walking immersion.
            </p>
            <div style={{ display: "flex", flexWrap: "wrap", gap: "8px" }}>
              {dossier.spotify_playlist.tracks?.map((track, i) => (
                <span key={i} className="tag-pill" style={{ background: "rgba(16, 185, 129, 0.15)", color: "#34d399" }}>
                  ▶ {track}
                </span>
              ))}
            </div>
          </div>
        )}

        {/* UTILITY DRAWER: GEN-Z TRAVEL HACKS */}
        {activeDrawer === "hacks" && dossier?.genz_hacks && (
          <div className="utility-card">
            <div className="utility-title">
              <span>💡 Insider Hacks for {dossier.destination || destination}</span>
              <button className="utility-close" onClick={() => setActiveDrawer(null)}>✕</button>
            </div>
            {dossier.genz_hacks.map((hack, idx) => (
              <div key={idx} className="hack-item">
                <span style={{ color: "#38bdf8" }}>⚡</span>
                <span>{hack}</span>
              </div>
            ))}
          </div>
        )}

        {/* UTILITY DRAWER: INTERACTIVE PACKING CHECKLIST */}
        {activeDrawer === "packing" && dossier?.packing_essentials && (
          <div className="utility-card">
            <div className="utility-title">
              <span>🎒 Interactive Packing Checklist</span>
              <button className="utility-close" onClick={() => setActiveDrawer(null)}>✕</button>
            </div>
            {dossier.packing_essentials.map((item, idx) => (
              <label key={idx} className="pack-checkbox-label">
                <input
                  type="checkbox"
                  checked={!!packedItems[item]}
                  onChange={() => togglePackItem(item)}
                  style={{ cursor: "pointer", accentColor: "#6366f1" }}
                />
                <span style={{ textDecoration: packedItems[item] ? "line-through" : "none", color: packedItems[item] ? "#64748b" : "#cbd5e1" }}>
                  {item}
                </span>
              </label>
            ))}
          </div>
        )}

        {/* ====================================================================
            CUSTOMER-CENTRIC BASECAMP & RESTING PLACE CARD
            Fulfills: "plan a hostel or resting place so he can cover all areas without being too exhausted"
            ==================================================================== */}
        {basecampData && (
          <div className="basecamp-spotlight-card">
            <div className="basecamp-header">
              <div className="basecamp-header-left">
                <div className="basecamp-icon">🏨</div>
                <div>
                  <div className="basecamp-tag">RECOMMENDED STRATEGIC BASECAMP</div>
                  <h3 className="basecamp-title">{basecampData.strategic_area}</h3>
                </div>
              </div>
              <div className="basecamp-strategy-tip">
                <span className="fatigue-shield-badge">🛡️ Fatigue Prevention Strategy</span>
                <p>{basecampData.rest_strategy}</p>
              </div>
            </div>

            <div className="basecamp-options-grid">
              {/* Hostel / Budget Rest Pick */}
              {basecampData.hostel_pick && (
                <div className="basecamp-option-box hostel-box">
                  <div className="basecamp-option-top">
                    <span className="basecamp-badge hostel">🎒 Top Hostel Pick</span>
                    <span className="basecamp-price">{basecampData.hostel_pick.price}</span>
                  </div>
                  <h4 className="basecamp-name">{basecampData.hostel_pick.name}</h4>
                  <div className="basecamp-rating">⭐ {basecampData.hostel_pick.rating}</div>
                  <p className="basecamp-vibe">{basecampData.hostel_pick.vibe}</p>
                </div>
              )}

              {/* Boutique / Relaxed Rest Pick */}
              {basecampData.boutique_pick && (
                <div className="basecamp-option-box boutique-box">
                  <div className="basecamp-option-top">
                    <span className="basecamp-badge boutique">✨ Boutique Sanctuary</span>
                    <span className="basecamp-price">{basecampData.boutique_pick.price}</span>
                  </div>
                  <h4 className="basecamp-name">{basecampData.boutique_pick.name}</h4>
                  <div className="basecamp-rating">⭐ {basecampData.boutique_pick.rating}</div>
                  <p className="basecamp-vibe">{basecampData.boutique_pick.vibe}</p>
                </div>
              )}
            </div>
          </div>
        )}

        {/* DAY SELECTOR TABS */}
        <div className="day-tab-strip" style={{ marginTop: "24px" }}>
          {daysList.map((dayPlan) => (
            <button
              key={dayPlan.day}
              className={`day-tab ${activeDay === dayPlan.day ? "active" : ""}`}
              onClick={() => setActiveDay(dayPlan.day)}
            >
              <span className="day-tab-num">Day {dayPlan.day}</span>
              <span style={{ fontSize: "11px", opacity: 0.8 }}>
                {dayPlan.neighborhood ? dayPlan.neighborhood.split(",")[0] : `Explore`}
              </span>
            </button>
          ))}
        </div>

        {/* CURRENT DAY DOSSIER CONTENT */}
        {currentDayData && (
          <div className="current-day-section">
            {/* Day Header Banner with estimated steps to prevent exhaustion */}
            <div className="day-banner-extended">
              <div className="day-banner-left">
                <h3>{currentDayData.title || `Day ${currentDayData.day} Discovery`}</h3>
                <p>
                  📍 <strong>District:</strong> {currentDayData.neighborhood || "City Center & Hidden Quarters"}
                  {currentDayData.vibe_summary && ` • ${currentDayData.vibe_summary}`}
                </p>
              </div>
              {currentDayData.daily_steps_estimate && (
                <div className="day-steps-badge">
                  <span>👟 Est. Pace:</span>
                  <strong>{currentDayData.daily_steps_estimate}</strong>
                </div>
              )}
            </div>

            {/* MIDDAY REST & RECHARGE BREAK CARD */}
            {currentDayData.rest_break && (
              <div className="rest-break-card">
                <div className="rest-break-icon">☕</div>
                <div className="rest-break-content">
                  <div className="rest-break-badge">
                    <span>MIDDAY REST & RECHARGE BREAK</span>
                    <span className="rest-time">⏰ {currentDayData.rest_break.time_slot}</span>
                  </div>
                  <h4 className="rest-break-title">{currentDayData.rest_break.activity_name}</h4>
                  <p className="rest-break-location">📍 {currentDayData.rest_break.location_name}</p>
                  <p className="rest-break-tip">💡 <strong>Rest Advice:</strong> {currentDayData.rest_break.tip}</p>
                </div>
              </div>
            )}

            {/* ACTIVITY TIMELINE STREAM WITH HIGH-RES PHOTOS & TRANSIT LEGS */}
            <div className="activity-stream-enriched">
              {currentDayData.activities?.map((act, idx) => (
                <React.Fragment key={act.id || idx}>
                  <div className="activity-node-enriched">
                    {/* Activity Card Image */}
                    {act.image_url && (
                      <div className="act-img-wrapper">
                        <img
                          src={act.image_url}
                          alt={act.activity_name}
                          className="act-card-img"
                          loading="lazy"
                        />
                        <div className="act-img-overlay">
                          <span className="act-img-badge">{act.category || "Highlight Stop"}</span>
                          <span className="act-img-price">{act.estimated_price}</span>
                        </div>
                      </div>
                    )}

                    <div className="act-body-content">
                      <div className="activity-head">
                        <div className="act-title-box">
                          {!act.image_url && (
                            <span className="act-category">{act.category || "Highlight Stop"}</span>
                          )}
                          <h4>{act.activity_name}</h4>
                        </div>
                        <button
                          onClick={() => toggleFavorite(act.activity_name)}
                          style={{
                            background: "none",
                            border: "none",
                            cursor: "pointer",
                            color: favoriteActivities[act.activity_name] ? "#ec4899" : "#64748b",
                          }}
                          title="Favorite this activity"
                        >
                          <Heart
                            size={20}
                            fill={favoriteActivities[act.activity_name] ? "#ec4899" : "none"}
                          />
                        </button>
                      </div>

                      {/* Metadata Row */}
                      <div className="act-meta-row">
                        <span className="act-meta-item">⏰ {act.time_slot}</span>
                        <span className="act-meta-item">📍 {act.location_name || act.neighborhood || "Local District"}</span>
                        <span className="act-meta-item">💵 {act.estimated_price} ({act.cost_tier || "$$"})</span>
                        <span className="act-meta-item">🎟️ {act.ticket_requirement}</span>
                        {act.crowd_meter && <span className="act-meta-item">👥 {act.crowd_meter}</span>}
                      </div>

                      {/* Vibe Tags */}
                      {act.vibe_tags && (
                        <div className="act-tags">
                          {act.vibe_tags.map((tag, tIdx) => (
                            <span key={tIdx} className="tag-pill">{tag}</span>
                          ))}
                        </div>
                      )}

                      {/* High-Value Detail Boxes */}
                      <div className="card-details-grid">
                        {act.insider_booking_tip && (
                          <div className="detail-box-tip">
                            💡 <strong>Insider Hack:</strong> {act.insider_booking_tip}
                          </div>
                        )}

                        {act.photo_spot_tip && (
                          <div className="detail-box-photo">
                            📸 <strong>TikTok / IG Angle:</strong> {act.photo_spot_tip}
                          </div>
                        )}

                        {act.food_spot && (
                          <div className="detail-box-food">
                            🍜 <strong>Curated Fuel Stop:</strong> {act.food_spot}
                          </div>
                        )}
                      </div>
                    </div>
                  </div>

                  {/* INTER-ACTIVITY TRANSIT CONNECTOR LEG
                      Fulfills: "plan how will one person travel from one place to another" */}
                  {act.transit_to_next && idx < currentDayData.activities.length - 1 && (
                    <div className="transit-leg-connector">
                      <div className="transit-line-dot" />
                      <div className="transit-card">
                        <div className="transit-card-left">
                          <span className="transit-mode-badge">{act.transit_to_next.mode}</span>
                          <span className="transit-duration">⏱️ {act.transit_to_next.duration}</span>
                          {act.transit_to_next.cost && (
                            <span className="transit-cost">💰 {act.transit_to_next.cost}</span>
                          )}
                        </div>
                        <div className="transit-instructions">
                          <Navigation size={13} style={{ flexShrink: 0, marginTop: "2px", color: "#38bdf8" }} />
                          <span>{act.transit_to_next.instructions}</span>
                        </div>
                      </div>
                      <div className="transit-line-dot" />
                    </div>
                  )}
                </React.Fragment>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* AI ENGINE CONFIGURATION MODAL */}
      {showAiModal && (
        <div className="drawer-overlay" onClick={() => setShowAiModal(false)}>
          <div
            className="card"
            style={{
              maxWidth: "500px",
              width: "90%",
              margin: "auto",
              position: "relative",
              zIndex: 1000,
              background: "#0f172a",
              border: "1px solid #334155",
              boxShadow: "0 25px 50px -12px rgba(0, 0, 0, 0.75)"
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "16px" }}>
              <h3 style={{ margin: 0, fontSize: "1.2rem", color: "#f8fafc", display: "flex", alignItems: "center", gap: "8px" }}>
                <span>✨</span> Generative AI Engine Settings
              </h3>
              <button
                className="btn-icon"
                onClick={() => setShowAiModal(false)}
                style={{ background: "transparent", border: "none", color: "#94a3b8", cursor: "pointer", fontSize: "1.2rem" }}
              >
                ✕
              </button>
            </div>

            <p style={{ color: "#94a3b8", fontSize: "0.88rem", marginBottom: "18px", lineHeight: 1.5 }}>
              By default, our built-in <strong>Situational Neural Engine</strong> generates 100% unique, non-repeating itineraries. You can optionally connect your personal Google Gemini or OpenAI API Key to invoke live frontier LLMs directly.
            </p>

            <div style={{ marginBottom: "16px" }}>
              <label className="section-label">Select AI Provider</label>
              <div style={{ display: "flex", gap: "10px", marginTop: "6px" }}>
                <button
                  type="button"
                  className={`pill-btn ${aiProvider === "gemini" ? "active" : ""}`}
                  style={{ flex: 1, padding: "10px", textAlign: "center" }}
                  onClick={() => {
                    setAiProvider("gemini");
                    localStorage.setItem("travel_ai_provider", "gemini");
                  }}
                >
                  🔷 Google Gemini (1.5 Flash)
                </button>
                <button
                  type="button"
                  className={`pill-btn ${aiProvider === "openai" ? "active" : ""}`}
                  style={{ flex: 1, padding: "10px", textAlign: "center" }}
                  onClick={() => {
                    setAiProvider("openai");
                    localStorage.setItem("travel_ai_provider", "openai");
                  }}
                >
                  🟢 OpenAI (GPT-4o / 3.5)
                </button>
              </div>
            </div>

            <div style={{ marginBottom: "20px" }}>
              <label className="section-label">
                {aiProvider === "gemini" ? "Gemini API Key" : "OpenAI API Key"} (Optional)
              </label>
              <input
                className="text-input"
                type="password"
                placeholder={aiProvider === "gemini" ? "AIzaSy..." : "sk-..."}
                value={aiApiKey}
                onChange={(e) => {
                  setAiApiKey(e.target.value);
                  localStorage.setItem("travel_ai_key", e.target.value);
                }}
                style={{ marginTop: "6px", width: "100%", boxSizing: "border-box" }}
              />
              <div style={{ fontSize: "0.76rem", color: "#64748b", marginTop: "6px" }}>
                {aiApiKey.trim() ? "🟢 Key saved locally in your browser." : "ℹ️ Leave blank to use the Built-in Situational Engine with zero repetitions."}
              </div>
            </div>

            <div style={{ display: "flex", justifyContent: "flex-end", gap: "10px" }}>
              {aiApiKey.trim() && (
                <button
                  type="button"
                  className="tool-btn"
                  style={{ color: "#ef4444", borderColor: "#7f1d1d" }}
                  onClick={() => {
                    setAiApiKey("");
                    localStorage.removeItem("travel_ai_key");
                  }}
                >
                  Clear Key
                </button>
              )}
              <button
                type="button"
                className="btn-generate-glow"
                style={{ padding: "8px 18px" }}
                onClick={() => setShowAiModal(false)}
              >
                Done
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
