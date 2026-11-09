# Professional & Fresher Resume Generator — Balaji Dilipsingh Rajput

An automated, ATS-compliant Python resume generator built with **ReportLab**. Generates pixel-perfect, strictly two-page executive PDF resumes tailored for:
1. **Tata Starbucks Assistant Store Manager (Fresher):** Tailored specifically for **Tata Starbucks Private Limited (Vadodara)**.
2. **Fresher QA/QC & Biotechnology Trainee (Default):** Tailored for entry-level Pharmaceutical QA/QC, Junior Biotechnologist, and Lab Analyst roles.
3. **Experienced QA Officer / IPQA Officer:** Tailored for Oral Solid Dosage (OSD) manufacturing and pharmaceutical compliance roles.

---

## ☕ Tata Starbucks Assistant Store Manager (Fresher) Profile Highlights

Tailored meticulously to align with **Tata Starbucks Private Limited** operational values and store leadership requirements:
- **Starbucks Mission Alignment:** *"To inspire and nurture the human spirit – one person, one cup and one neighbourhood at a time."*
- **Brand Philosophy:** Operating as a *"people business selling coffee"*, fostering an environment of **respect and dignity**, honesty, integrity, and TATA Starbucks guiding principles.
- **The 4 Exact Core Competencies:**
  1. **Achieving Results:** Shift operational efficiency, meeting & exceeding store sales targets, waste reduction, beverage speed-of-service, inventory logging, and strict cash management & register accountability.
  2. **Living Our Mission And Values:** Inspiring authentic human connection, embracing diversity, treating partners and customers with respect and dignity, and exemplifying company guiding principles.
  3. **Helping Others Succeed:** Respectful and encouraging coaching to partners, recognizing changes in partner morale, addressing individual motivation, offering constructive feedback to Store Manager, and celebrating team recognition.
  4. **Working Together:** Seamless partner deployment, collaborative floor teamwork, swift conflict resolution, assisting stations during peak rushes, and maintaining a welcoming Third Place shift culture.
- **Store Operations & Delegation:** Assisting Store Manager in executing store operations during scheduled shifts, deploying partners across stations (POS, Bar/Brewing, Food Warming, Handoff, Lobby), anticipating customer & store needs, and shift handovers.
- **Coffee Craft & Legendary Customer Service:** Passion for roast profiles (Blonde, Medium, Dark), brewing methods, origin stories, ethical sourcing (C.A.F.E. Practices), and delivering legendary customer service with a steadfast *"customer comes first"* mindset.
- **Safety, Cash & Compliance:** 100% adherence to cash register policies, shift cash drawer audits, partner safety & security protocols, regular attendance & punctuality, beverage/food recipe presentation standards, and FSSAI/QSR sanitation guidelines.
- **Education:** Exceeds the minimum 12th pass requirement with a **Diploma in Biotechnology** (GTU / Parul Institute of Technology & Engineering, Vadodara, 2021–2025, CGPA 6.7/10, Dean's List distinction).
- **Candidate Particulars:** Balaji Dilipsingh Rajput, Vadodara, Gujarat 390010 | Immediate Joiner (Full-Time / Rotational Shifts / Work from Office).

---

## Technical Highlights
- **Strict 2-Page Budgeting:** Balanced layout strictly adhering to the 2-page constraint and verified by automated CI/CD tests.
- **ATS Compliant:** Pure selectable text, semantic flowables, clean typography (Helvetica), zero missing-glyph/emoji encoding bugs.
- **Interactive Links:** Clickable links for Phone (`tel:`), Email (`mailto:`), LinkedIn, and GitHub.
- **Dynamic Two-Pass Canvas:** Two-pass numbered canvas rendering branded running headers and footers with `Page X of Y` pagination.
- **Custom Branding:** Signature Tata Starbucks Siren Green (`#006241`) & Emerald (`#00754A`) styling for Starbucks profile; Corporate Navy (`#0F2942`) & Slate Blue (`#1E5F8E`) for Pharma profiles.

---

## Usage

### 1. Install Dependencies
```bash
pip install reportlab pypdf
```

### 2. Generate Tata Starbucks Assistant Store Manager Resume
```bash
# Using the dedicated standalone script:
python generate_starbucks_resume.py

# Or using the main CLI:
python generate_resume.py --profile starbucks
# Outputs: artifacts/Balaji_Rajput_Tata_Starbucks_ASM_Resume.pdf
```

### 3. Generate Fresher Resume (Default - Pharma QA/QC)
```bash
python generate_resume.py
# Outputs: artifacts/Balaji_Rajput_Fresher_Resume.pdf
```

### 4. Generate Experienced Resume (Pharma QA Officer)
```bash
python generate_resume.py --profile experienced
# Outputs: artifacts/Balaji_Rajput_Professional_Resume.pdf
```

### 5. Generate All Resumes at Once
```bash
python generate_resume.py --profile all
```

### 6. Custom Output Path or Environment Variable
```bash
python generate_resume.py --profile starbucks --output /path/to/custom_name.pdf

# Or via environment variable:
RESUME_OUTPUT_PATH=artifacts/resume.pdf python generate_resume.py --profile starbucks
```

---

## Automated Validation
Run the local validation check to assert that all generated PDFs exist and contain **strictly 2 pages**:
```bash
python -c "
from pathlib import Path
from pypdf import PdfReader

for f in Path('artifacts').glob('*.pdf'):
    pages = len(PdfReader(str(f)).pages)
    print(f'{f.name}: {pages} pages')
    assert pages == 2
print('All resumes verified: strictly 2 pages!')
"
```
