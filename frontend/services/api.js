import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add request interceptor for debugging
API.interceptors.request.use(
  (config) => {
    console.log("📤 Sending request to:", config.url);
    console.log("📦 With data:", config.data);
    return config;
  },
  (error) => {
    console.error("Request error:", error);
    return Promise.reject(error);
  }
);

// Add response interceptor for debugging
API.interceptors.response.use(
  (response) => {
    console.log("📥 Received response:", response.status);
    console.log("📋 Response data:", response.data);
    return response;
  },
  (error) => {
    console.error("Response error:", error.response?.status, error.response?.data);
    return Promise.reject(error);
  }
);

export default API;