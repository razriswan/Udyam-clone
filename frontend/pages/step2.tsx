import React from "react";
import ProgressBar from "../components/ProgressBar";
import FormRenderer from "../components/FormRenderer";

export default function Step2Page() {
  return (
    <div style={{ maxWidth: 640, margin: "0 auto", padding: 24 }}>
      <h1 style={{ marginBottom: 8 }}>Udyam Registration</h1>
      <ProgressBar step={2} />
      <FormRenderer step={2} />
    </div>
  );
}
