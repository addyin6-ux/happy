import { useState, useEffect } from "react";
import Layout from "../../components/Layout";
import API from "../../utils/api";

export default function Leads() {
  const [leads, setLeads] = useState([]);

  useEffect(() => {
    API.get("/nbfc/leads/list").then(res => setLeads(res.data));
  }, []);

  return (
    <Layout>
      <h2>NBFC Leads</h2>
      <pre>{JSON.stringify(leads, null, 2)}</pre>
    </Layout>
  );
}
