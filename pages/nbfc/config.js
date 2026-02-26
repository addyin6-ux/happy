import { useState } from "react";
import Layout from "../../components/Layout";
import API from "../../utils/api";

export default function Config() {
  const [config, setConfig] = useState({ api_key: "", endpoint: "" });
  const [result, setResult] = useState(null);

  const saveConfig = async () => {
    const res = await API.post("/nbfc/api/save", config);
    setResult(res.data);
  };

  return (
    <Layout>
      <h2>NBFC API Config</h2>
      <input placeholder="API Key" onChange={e => setConfig({ ...config, api_key: e.target.value })} />
      <input placeholder="Endpoint" onChange={e => setConfig({ ...config, endpoint: e.target.value })} />
      <button onClick={saveConfig}>Save</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </Layout>
  );
}
