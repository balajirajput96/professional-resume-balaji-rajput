# Professional & Fresher Resume Generator — Balaji Dilipsingh Rajput

An automated, ATS-compliant Python resume generator built with **ReportLab**. Generates pixel-perfect, strictly two-page executive PDF resumes tailored for both **Fresher** and **Experienced** roles in **Pharmaceutical Quality Assurance (QA/QC)**, **Quality Control**, and **Biotechnology**.

## Highlights
- **Fresher Profile (Default):** Tailored for entry-level QA/QC Trainee, Junior Biotechnologist, and Lab Analyst roles. Focuses on Biotechnology Diploma (GTU), award-winning academic research projects (Bioethanol SSF optimization, AMR gene curation, molecular docking), internships (Biotecnika, Gujarat Biotech Innovations), and compliance fundamentals (cGMP, GDP, IPQA, ALCOA+).
- **Experienced Profile:** Tailored for QA Officer / IPQA Officer roles in Oral Solid Dosage manufacturing.
- **ATS Compliant:** Pure selectable text, semantic flowables, clean typography (Helvetica), zero missing-glyph/emoji encoding bugs.
- **Interactive Links:** Clickable links for Phone (`tel:`), Email (`mailto:`), LinkedIn, and GitHub.
- **Dynamic Canvas:** Two-pass numbered canvas rendering running headers and footers with `Page X of Y` pagination.
- **Strict 2-Page Budgeting:** Balanced layout strictly adhering to the two-page constraint and CI/CD validation.

## Usage

### 1. Install Dependencies
```bash
pip install reportlab pypdf
```

### 2. Generate Fresher Resume (Default)
```bash
python generate_resume.py
# Outputs: artifacts/Balaji_Rajput_Fresher_Resume.pdf
```

### 3. Generate Experienced Resume
```bash
python generate_resume.py --profile experienced
# Outputs: artifacts/Balaji_Rajput_Professional_Resume.pdf
```

### 4. Specify Custom Output Path or Environment Variable
```bash
python generate_resume.py --output /path/to/resume.pdf
# Or via environment variable:
RESUME_OUTPUT_PATH=artifacts/resume.pdf python generate_resume.py
```
