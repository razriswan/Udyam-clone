export const PAN_RE = /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/;
export const AADHAAR_RE = /^\d{12}$/;
export const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
export const OTP_RE = /^\d{4,6}$/;

export const validate = (name: string, value: string): string | null => {
  const n = name.toLowerCase();
  if (n.includes("pan") && !PAN_RE.test(value)) return "Invalid PAN format (e.g., ABCDE1234F)";
  if ((n.includes("aadhaar") || n.includes("aadhar")) && !AADHAAR_RE.test(value)) return "Aadhaar must be 12 digits";
  if (n.includes("email") && !EMAIL_RE.test(value)) return "Invalid email address";
  if (n.includes("otp") && !OTP_RE.test(value)) return "OTP must be 4–6 digits";
  return null;
};
