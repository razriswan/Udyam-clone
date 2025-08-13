import React, { useState } from "react";
import ProgressBar from "../components/ProgressBar";
import FormRenderer from "../components/FormRenderer";

export default function IndexPage() {
  const [step, setStep] = useState(1);
  return (
    <div style={{ maxWidth: 640, margin: "0 auto", padding: 24 }}>
      <h1 style={{ marginBottom: 20}}>Udyam Registration</h1>
      <ProgressBar step={step} />
      <FormRenderer step={step} onNext={() => setStep(2)} />
    </div>
  );
}
