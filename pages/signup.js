import { useState } from "react";
import API from "../utils/api";

export default function Signup() {
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const [error, setError] = useState(null);

  const handleSignup = async () => {
    try {
      await API.post("/signup", form);
      window.location.href = "/login";
    } catch (err) {
      setError("Signup failed");
    }
  };

  return (
    <div className="flex h-screen items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-96">
        <h2 className="text-2xl font-bold mb-4">Sign Up</h2>
        <input
          className="border p-2 w-full mb-3"
          placeholder="Name"
          onChange={e => setForm({ ...form, name: e.target.value })}
        />
        <input
          className="border p-2 w-full mb-3"
          placeholder="Email"
          onChange={e => setForm({ ...form, email: e.target.value })}
        />
        <input
          type="password"
          className="border p-2 w-full mb-3"
          placeholder="Password"
          onChange={e => setForm({ ...form, password: e.target.value })}
        />
        <button
          onClick={handleSignup}
          className="bg-green-500 text-white p-2 w-full rounded"
        >
          Sign Up
        </button>
        {error && <p className="text-red-500 mt-2">{error}</p>}
        <p className="mt-4 text-sm">
          Already have an account? <a href="/login" className="text-blue-600">Login</a>
        </p>
      </div>
    </div>
  );
}
