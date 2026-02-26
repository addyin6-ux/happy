import { useState } from "react";
import Layout from "../../components/Layout";
import API from "../../utils/api";

export default function Offers() {
  const [amount, setAmount] = useState("");
  const [offers, setOffers] = useState([]);

  const searchOffers = async () => {
    const res = await API.post("/offers/search", { loan_amount: amount });
    setOffers(res.data);
  };

  return (
    <Layout>
      <h2>Search Loan Offers</h2>
      <input placeholder="Loan Amount" onChange={e => setAmount(e.target.value)} />
      <button onClick={searchOffers}>Search</button>
      <pre>{JSON.stringify(offers, null, 2)}</pre>
    </Layout>
  );
}
