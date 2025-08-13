import React, { useEffect, useMemo, useState } from "react";
import axios from "axios";
import { validate } from "../utils/validation";

type Field = {
  name: string;
  label: string;
  type: string;
  validation?: { pattern?: string; example?: string };
};


async function fetchSchema(): Promise<Field[]> {
  try {
    const { data } = await axios.get("http://localhost:8000/schema");
    return data;
  } catch {
    
    return [
      { name: "aadhaar", label: "Aadhaar Number", type: "text", validation: { pattern: "^\\d{12}$", example: "123412341234" } },
      { name: "otp", label: "OTP", type: "text", validation: { pattern: "^\\d{4,6}$", example: "123456" } },
      { name: "pan", label: "PAN", type: "text", validation: { pattern: "^[A-Z]{5}[0-9]{4}[A-Z]{1}$", example: "ABCDE1234F" } },
      { name: "name", label: "Name", type: "text" },
      { name: "email", label: "Email", type: "email", validation: { pattern: "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$" } }
    ];
  }
}

export default function FormRenderer({ step, onNext }: { step: number; onNext?: () => void }) {
  const [schema, setSchema] = useState<Field[]>([]);
  const [data, setData] = useState<Record<string, string>>({});
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchSchema().then((s) => {
      setSchema(s);
      const init: Record<string, string> = {};
      s.forEach((f) => (init[f.name] = ""));
      setData(init);
      setLoading(false);
    });
  }, []);

  const fields = useMemo(() => (step === 1 ? schema.filter(f => ["aadhaar", "otp"].includes(f.name)) : schema), [schema, step]);

  const onChange = (name: string, value: string) => {
    setData((d) => ({ ...d, [name]: value }));
    const err = validate(name, value);
    setErrors((e) => ({ ...e, [name]: err || "" }));
  };

  
  const submit = async (e: React.FormEvent) => {
    e.preventDefault();

    
    let ok = true;
    const nextErrors: Record<string, string> = {};
    fields.forEach((f) => {
      const err = validate(f.name, data[f.name] || "");
      if (err) {
        ok = false;
        nextErrors[f.name] = err;
      }
    });
    setErrors(nextErrors);
    if (!ok) return;

    if (step === 1) {
      onNext?.();
      return;
    }

    
    try {
      await axios.post("http://localhost:8000/submit", data);
      alert("Submitted successfully");
    } catch (err: any) {
      alert(err?.response?.data?.detail || "Submission failed");
    }
  };

  if (loading) return <div>Loading…</div>;

return (
    <form onSubmit={submit}>
      {fields.map((f) => (
        <div key={f.name} style={{ marginBottom: 12 }}>
          <label style={{ display: "block", fontWeight: 600, marginBottom: 6 }}>{f.label}</label>
          <input
            type={f.type === "email" ? "email" : "text"}
            value={data[f.name] || ""}
            onChange={(e) => onChange(f.name, e.target.value)}
            placeholder={f.validation?.example || ""}
            style={{ padding: 10, width: "100%", borderRadius: 6, border: "1px solid #ddd", boxSizing: "border-box" }}
          />
          {!!errors[f.name] && <div style={{ color: "crimson", marginTop: 4 }}>{errors[f.name]}</div>}
        </div>
      ))}
      <button type="submit" style={{ padding: "10px 14px", borderRadius: 8, background: "#111827", color: "white" }}>
        {step === 1 ? "Next" : "Submit"}
      </button>
    </form>
  );
}