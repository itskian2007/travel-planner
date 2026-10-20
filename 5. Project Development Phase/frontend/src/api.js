const API_BASE_URL = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

async function request(endpoint, options = {}) {
  const url = `${API_BASE_URL}${endpoint}`;
  const config = {
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
    ...options,
  };

  try {
    const response = await fetch(url, config);
    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
      const errorMsg = data.detail || data.error || `HTTP error! Status: ${response.status}`;
      throw new Error(errorMsg);
    }
    return data;
  } catch (error) {
    if (error.name === "TypeError" && error.message.includes("fetch")) {
      throw new Error("Cannot connect to backend server. Ensure FastAPI is running on port 8000.");
    }
    throw error;
  }
}

export const api = {
  // Health
  checkHealth: () => request("/health"),

  // Authentication
  register: (email, password, date_of_birth) =>
    request("/register", {
      method: "POST",
      body: JSON.stringify({ email, password, date_of_birth }),
    }),

  login: (email, password) =>
    request("/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    }),

  forgotPassword: (email, date_of_birth, new_password) =>
    request("/forgot-password", {
      method: "POST",
      body: JSON.stringify({ email, date_of_birth, new_password }),
    }),

  // Preferences
  savePreferences: (preferences) =>
    request("/save-preferences", {
      method: "POST",
      body: JSON.stringify(preferences),
    }),

  getUserPreferences: (userId) =>
    request(`/preferences/${userId}`),

  // Itineraries
  generateItinerary: (itineraryRequest) =>
    request("/generate-itinerary", {
      method: "POST",
      body: JSON.stringify(itineraryRequest),
    }),

  getUserItineraries: (userId) =>
    request(`/itineraries/user/${userId}`),

  deleteItinerary: (itineraryId) =>
    request(`/itineraries/${itineraryId}`, {
      method: "DELETE",
    }),
};
