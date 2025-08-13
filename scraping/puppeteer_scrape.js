const fs = require('fs');
const puppeteer = require('puppeteer');

(async () => {
  const url = 'https://udyamregistration.gov.in/UdyamRegistration.aspx';
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'networkidle2' });

  const fields = await page.evaluate(() => {
    const out = [];
    const elems = Array.from(document.querySelectorAll('input, select, textarea'));
    elems.forEach(el => {
      out.push({
        name: el.name || el.id || null,
        label: (function() {
        
          const id = el.id;
          if (id) {
            const lab = document.querySelector(`label[for="${id}"]`);
            if (lab) return lab.innerText.trim();
          }
          
          if (el.placeholder) return el.placeholder;
          return el.getAttribute('aria-label') || el.name || el.type;
        })(),
        type: el.tagName.toLowerCase() === 'select' ? 'select' : (el.type || 'text')
      });
    });
    return out;
  });

  fs.writeFileSync('schema.json', JSON.stringify(fields, null, 2));
  await browser.close();
  console.log('Saved schema.json');
})();