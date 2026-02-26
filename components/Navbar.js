import Link from "next/link";
export default function Navbar() {
  return (
    <nav style={{ padding: "1rem", background: "#f0f0f0" }}>
      <Link href="/">Home</Link> |{" "}
      <Link href="/customer/kyc">Customer KYC</Link> |{" "}
      <Link href="/customer/offers">Offers</Link> |{" "}
      <Link href="/customer/repayment">Repayment</Link> |{" "}
      <Link href="/nbfc/config">NBFC Config</Link> |{" "}
      <Link href="/nbfc/leads">Leads</Link> |{" "}
      <Link href="/nbfc/repayments">Repayments</Link>
    </nav>
  );
}
