import { useState, useEffect } from "react";
import Layout from "../../components/Layout";
import API from "../../utils/api";

export default function Repayments() {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    API.get("/nbfc/repayments/summary").then(res => setSummary(res.data));
  }, []);

  return (
    <Layout>
      <h2>Repayment Summary</h2>
      {summary && <pre>{JSON.stringify(summary, null, 2)}</pre>}
    </Layout>
  );
}
