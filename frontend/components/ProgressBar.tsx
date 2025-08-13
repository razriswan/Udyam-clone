import React from "react";

export default function ProgressBar({ step }: { step: number }) {
  const pct = step === 1 ? 50 : 100;
  return (
    <div style={{ marginBottom: 16 }}>
      <div style={{ fontWeight: 600, marginBottom: 6 }}>Step {step} of 2</div>
      <div style={{ height: 8, background: "#eee", borderRadius: 6 }}>
        <div style={{ width: `${pct}%`, height: 8, borderRadius: 6, background: "#3b82f6" }} />
      </div>
    </div>
  );
}
