import { useState } from "react";
import Layout from "../../components/Layout";
import API from "../../utils/api";

export default function Repayment() {
  const [loanId, setLoanId] = useState("");
  const [result, setResult] = useState(null);

  const payEmi = async () => {
    const res = await API.post("/repayment/pay", { loan_id: loanId });
    setResult(res.data);
  };

  return (
    <Layout>
      <h2>Repayment</h2>
      <input placeholder="Loan ID" onChange={e => setLoanId(e.target.value)} />
      <button onClick={payEmi}>Pay EMI</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </Layout>
  );
}
