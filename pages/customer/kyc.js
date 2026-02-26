import { useState } from "react";
import Layout from "../../components/Layout";
import API from "../../utils/api";

export default function KYC() {
  const [form, setForm] = useState({ aadhaar_number: "", pan_number: "", full_name: "" });
  const [result, setResult] = useState(null);

  const submitKYC = async () => {
    const res = await API.post("/kyc/submit", form);
    setResult(res.data);
  };

  return (
    <Layout>
      <h2>KYC Submission</h2>
      <input placeholder="Aadhaar" onChange={e => setForm({ ...form, aadhaar_number: e.target.value })} />
      <input placeholder="PAN" onChange={e => setForm({ ...form, pan_number: e.target.value })} />
      <input placeholder="Full Name" onChange={e => setForm({ ...form, full_name: e.target.value })} />
      <button onClick={submitKYC}>Submit</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </Layout>
  );
}
