import requests
from bs4 import BeautifulSoup
import json
import re

URL = "https://udyamregistration.gov.in/UdyamRegistration.aspx"


PAN_RE = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
AADHAAR_RE = r"^\d{12}$"
EMAIL_RE = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
OTP_RE = r"^\d{4,6}$"

def scrape_form():
    res = requests.get(URL, timeout=15)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')

    fields = []
    for el in soup.find_all(['input', 'select', 'textarea']):
        name = el.get('name') or el.get('id')
        if not name:
            continue
            
        label = el.get('placeholder') or ''
       
        if el.get('id'):
            lab = soup.find('label', attrs={'for': el.get('id')})
            if lab and lab.text.strip():
                label = lab.text.strip()
        field_type = el.get('type') or ('select' if el.name == 'select' else 'text')
        validation = {}
        lname = name .lower()
        if "pan" in lname:
            validation["pattern"] = PAN_RE
            validation["example"] = "ABCDE1234F"
        if "aadhaar" in lname or "aadhar" in lname:
            validation["pattern"] = AADHAAR_RE
            validation["example"] = "123412341234"
        if "email" in lname:
            validation["pattern"] = EMAIL_RE
            validation["example"] = "name@example.com"
        if "otp" in lname:
            validation["pattern"] = OTP_RE
            validation["example"] = "123456"
        fields.append({
            'name': name,
            'label': label ,
            'type': field_type,
            'validation': validation
        })

    if not fields:
        fields = [
            {"name": "aadhaar", "label": "Aadhaar Number", "type": "text", "validation": {"pattern": AADHAAR_RE, "example": "123412341234"}},
            {"name": "otp", "label": "OTP", "type": "text", "validation": {"pattern": OTP_RE, "example": "123456"}},
            {"name": "pan", "label": "PAN", "type": "text", "validation": {"pattern": PAN_RE, "example": "ABCDE1234F"}},
            {"name": "name", "label": "Name", "type": "text", "validation": {}},
            {"name": "email", "label": "Email", "type": "email", "validation": {"pattern": EMAIL_RE, "example": "name@example.com"}}
        ]

    with open('schema.json', 'w') as f:
        json.dump(fields, f, indent=2)
    print('schema.json written with', len(fields), 'fields')

if __name__ == '__main__':
    scrape_form()