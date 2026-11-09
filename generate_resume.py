#!/usr/bin/env python3
"""
Professional Resume Generator for Balaji Dilipsingh Rajput
Features:
- Multi-profile support:
    * 'fresher': Entry-level Biotechnology & Pharma QA/QC Trainee (Default)
    * 'experienced': 2+ years Pharma QA / IPQA Officer (Oral Solid Dosage)
    * 'starbucks' / 'starbucks_asm': Assistant Store Manager (Fresher) at Tata Starbucks Private Limited (Vadodara)
    * 'all': Generates all three profiles simultaneously
- ATS-compliant single/multi-section ReportLab flowable architecture
- Personalized branding with theme colors (Tata Starbucks Siren Green & Deep Espresso for Starbucks profile)
- Full alignment with Starbucks Mission ("To inspire and nurture the human spirit – one person, one cup and one neighbourhood at a time")
- Integration of the 4 exact core competencies: Achieving Results, Living Our Mission And Values, Helping Others Succeed, Working Together
- Respect & dignity, people business selling coffee, customer-first service, coffee craft & storytelling
- Safety, cash register management, recipe presentation standards, FSSAI hygiene & shift execution
- Interactive PDF annotations: clickable phone (tel:), email (mailto:), LinkedIn, and GitHub links
- Two-pass Numbered Canvas for dynamic page count ('Page X of Y') and themed running headers/footers
- Strict 2-page layout budgeting passing CI/CD verification tests
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple, Dict, Any

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    HRFlowable,
)
from reportlab.pdfgen import canvas


# ---------------------------------------------------------------------------
# COLOR PALETTES
# ---------------------------------------------------------------------------
# Modern Executive Navy & Slate Blue (Default & Experienced Profiles)
COLOR_PRIMARY_NAVY = HexColor("#0F2942")     # Deep Corporate Navy
COLOR_SECONDARY_BLUE = HexColor("#1E5F8E")   # Refined Accent Blue
COLOR_TEXT_DARK = HexColor("#222222")        # High-contrast readable body text
COLOR_TEXT_MUTED = HexColor("#555555")       # Subtitle & metadata text
COLOR_BORDER = HexColor("#D0D7DE")           # Subtle divider border

# Tata Starbucks Signature Palette (Starbucks ASM Profile)
COLOR_STARBUCKS_GREEN = HexColor("#006241")   # Tata Starbucks Signature Siren Green
COLOR_STARBUCKS_EMERALD = HexColor("#00754A") # Vibrant Starbucks Emerald Accent
COLOR_STARBUCKS_ESPRESSO = HexColor("#1E3932")# Deep Roast Green Accent


# ---------------------------------------------------------------------------
# DATA STRUCTURES
# ---------------------------------------------------------------------------
@dataclass
class ContactInfo:
    name: str = "BALAJI DILIPSINGH RAJPUT"
    title: str = "Biotechnology Graduate | Entry-Level QA/QC Trainee | Computational & Wet-Lab Analyst"
    phone: str = "+91 87808 61044"
    phone_clean: str = "+918780861044"
    email: str = "balajirajput966@gmail.com"
    location: str = "Vadodara, Gujarat 390010, India"
    linkedin_url: str = "https://linkedin.com/in/balaji-rajput-483a86194"
    linkedin_display: str = "linkedin.com/in/balaji-rajput-483a86194"
    github_url: str = "https://github.com/balajirajput96"
    github_display: str = "github.com/balajirajput96"
    availability: str = "Immediate Joiner (Full-Time / Shift Operations)"


@dataclass
class ResumeData:
    profile_type: str
    contact: ContactInfo
    summary_heading: str
    summary: str
    competencies_heading: str
    competencies_left: List[str]
    competencies_right: List[str]
    education: List[Dict[str, Any]]
    experience_heading: str
    experience: List[Dict[str, Any]]
    projects: List[Dict[str, str]]
    skills: List[Tuple[str, str]]
    certifications_left: List[str]
    certifications_right: List[str]
    achievements: List[str]
    languages: str
    personal_details: str
    declaration: str
    projects_heading: str = "Key Academic & Research Projects"
    skills_heading: str = "Technical & Laboratory Skills"
    certifications_heading: str = "Certifications & Specialized Training"
    achievements_heading: str = "Key Honors & Achievements"
    theme_primary: str = "#0F2942"
    theme_secondary: str = "#1E5F8E"
    subtitle_page2: str = "Curriculum Vitae | Fresher Profile"


def get_fresher_data() -> ResumeData:
    """Returns resume data structured for freshers (Biotechnology & Entry QA/QC)."""
    return ResumeData(
        profile_type="Fresher",
        theme_primary="#0F2942",
        theme_secondary="#1E5F8E",
        subtitle_page2="Curriculum Vitae | Fresher (Biotechnology & Pharma QA/QC)",
        contact=ContactInfo(
            name="BALAJI DILIPSINGH RAJPUT",
            title="Biotechnology Graduate | Entry-Level QA/QC Trainee | Computational & Wet-Lab Analyst",
            phone="+91 87808 61044",
            phone_clean="+918780861044",
            email="balajirajput966@gmail.com",
            location="Vadodara, Gujarat 390010, India",
            linkedin_url="https://linkedin.com/in/balaji-rajput-483a86194",
            linkedin_display="linkedin.com/in/balaji-rajput-483a86194",
            github_url="https://github.com/balajirajput96",
            github_display="github.com/balajirajput96",
            availability="Immediate Joiner",
        ),
        summary_heading="Career Objective & Professional Summary",
        summary=(
            "Goal-oriented and detail-focused Biotechnology graduate with demonstrated academic excellence "
            "and practical foundational training in pharmaceutical manufacturing, analytical QC, and cGMP compliance. "
            "Recipient of the <b>Best Research Project Award (2024)</b> and <b>Dean's List</b> distinction. Practical exposure "
            "includes <b>2-Month Industrial Training in Oral Solid Dosage (Tablets) & QA/QC</b> at Elysium Pharmaceuticals Ltd., "
            "genomic data analysis workflows at Biotecnika, and GLP microbiology assays at Gujarat Biotech Innovations. "
            "Eager to contribute rigorous analytical skills and standard-operating-procedure discipline as an entry-level "
            "<b>Quality Assurance (QA) Trainee</b>, <b>IPQA Officer</b>, or <b>Quality Control (QC) Chemist</b>. "
            "Available to join immediately."
        ),
        competencies_heading="Core Competencies & Foundational Knowledge",
        competencies_left=[
            "• cGMP, GDP & GLP Principles",
            "• Tablet Manufacturing & IPQA Checks",
            "• Quality Control (QC) Wet Analysis",
            "• Good Documentation Practices (ALCOA+)",
            "• Dissolution, Friability & Hardness Testing",
            "• SOP Drafting & Document Lifecycle",
        ],
        competencies_right=[
            "• Analytical Instrumentation (HPLC, UV-Vis)",
            "• Microbial Testing & Aseptic Culture",
            "• BMR / BPR Review Fundamentals",
            "• Deviation & CAPA Problem-Solving",
            "• Quality Management System (QMS)",
            "• 21 CFR Part 11 & Schedule M Awareness",
        ],
        education=[
            {
                "degree": "Diploma in Biotechnology",
                "institution": "Parul Institute of Technology & Engineering, Gujarat Technological University (GTU), Vadodara",
                "duration": "2021 – 2025",
                "score": "CGPA: 6.7 / 10 | Dean's List for Academic Excellence (2024–2025)",
                "coursework": "Key Subjects: Molecular Biology, Microbiology, Bioprocess Technology, Biochemistry, Immunology, Fermentation Technology, QC & QA.",
            }
        ],
        experience_heading="Industrial Training & Internship Experience",
        experience=[
            {
                "role": "Industrial Trainee — QA & QC (Oral Solid Dosage - Tablets)",
                "company": "Elysium Pharmaceuticals Ltd., Dabhasa, Vadodara",
                "duration": "2 Months (Industrial Training)",
                "bullets": [
                    "Completed 2-month industrial training focused on Oral Solid Dosage (tablet manufacturing) and Quality Control (QC) & Quality Assurance (QA) workflows under cGMP and Schedule M guidelines.",
                    "Gained practical QC laboratory exposure: observed raw material and finished product testing, dissolution and disintegration profiling, UV-Vis spectrophotometry assays, and GLP reagent standardization.",
                    "Assisted IPQA officers in line clearance, physical in-process parameter checks (weight variation, thickness, hardness, friability), and BMR/BPR log verification.",
                ],
            },
            {
                "role": "Bioinformatics Intern",
                "company": "Biotecnika (Remote)",
                "duration": "2024 (3 Months)",
                "bullets": [
                    "Engineered automated Python / Biopython workflows for sequence alignment, screening over 500+ DNA and protein sequences.",
                    "Utilized BLAST, ClustalW, and GenBank annotations to streamline curation workflows, cutting manual processing time by 40%.",
                ],
            },
            {
                "role": "Laboratory Research Intern",
                "company": "Gujarat Biotech Innovations",
                "duration": "2023 (2 Months)",
                "bullets": [
                    "Carried out routine laboratory assays: PCR, agarose gel electrophoresis, and microbial culture handling for 80+ samples/week.",
                    "Authored 3 standard operating procedures (SOPs) compliant with GLP standards; elevated laboratory sample workflow efficiency by 20%.",
                ],
            },
        ],
        projects=[
            {
                "title": "Bioethanol Production from Agricultural Waste (2024)",
                "details": (
                    "Optimized Simultaneous Saccharification & Fermentation (SSF) with <i>S. cerevisiae</i> via Response Surface Methodology "
                    "(RSM/DOE); achieved a <b>15% yield enhancement</b> validated by HPLC and ANOVA (p &lt; 0.05). "
                    "<b>Awarded Best Research Project – Parul Institute 2024</b>."
                ),
                "tags": "[Fermentation, DOE/RSM, HPLC, Microbial Kinetics, ANOVA]",
            },
            {
                "title": "Comparative Genomic Analysis of AMR Genes (2024)",
                "details": (
                    "Investigated 120 bacterial genomes from NCBI GenBank using an automated Python/Biopython workflow; "
                    "identified <b>8 novel Antimicrobial Resistance (AMR) gene variants</b> across 500+ sequence entries."
                ),
                "tags": "[Python, Biopython, BLAST, GenBank, ClustalW, Bioinformatics]",
            },
            {
                "title": "Protein Structure Prediction & Molecular Docking (2023)",
                "details": (
                    "Constructed 3D homology models for 5 therapeutic target proteins using SWISS-MODEL; performed virtual screening "
                    "and molecular docking with 50 ligands via AutoDock Vina, identifying 3 lead inhibitors (binding affinity &le; -8.0 kcal/mol)."
                ),
                "tags": "[SWISS-MODEL, AutoDock Vina, PyMOL, PDB, In Silico Drug Design]",
            },
            {
                "title": "Biogenic Synthesis of Silver Nanoparticles (AgNPs) (2023)",
                "details": (
                    "Synthesized antimicrobial AgNPs via green biogenic route using <i>Pseudomonas spp.</i>; confirmed nanoparticle "
                    "formation and broad-spectrum bactericidal efficacy via UV-Vis Spectrophotometry and zone-of-inhibition assays."
                ),
                "tags": "[Green Synthesis, UV-Vis Spectrophotometry, Microbial Assays, Aseptic Techniques]",
            },
        ],
        skills=[
            (
                "Quality & Regulatory Awareness:",
                "cGMP, GDP, GLP, Schedule M, SOP Drafting, BMR / BPR Verification, Deviation & CAPA Basics, Change Control Awareness, Data Integrity (ALCOA+), 21 CFR Part 11, CDSCO & WHO-GMP Guidelines.",
            ),
            (
                "Laboratory & Analytical (QC/QA):",
                "HPLC (Fundamentals), UV-Vis Spectrophotometry, Dissolution & Disintegration Testing, Friability, Hardness, PCR / RT-PCR, Agarose Gel Electrophoresis, Microbial & Aseptic Culture, Sterility Testing, Autoclave, LAF.",
            ),
            (
                "Bioinformatics & Computation:",
                "Python (Biopython, Pandas, NumPy), R Basics, BLAST, ClustalW, NCBI GenBank, UniProt, AutoDock Vina, SWISS-MODEL, PyMOL.",
            ),
            (
                "Software & Digital Tools:",
                "MS Office Suite (Advanced Excel, Word, PowerPoint), SPSS, MATLAB (Basic), Git & GitHub, TrackWise (Basics), Google Workspace.",
            ),
        ],
        certifications_left=[
            "• Bioinformatics Specialization – Coursera / UC San Diego (2024)",
            "• Python for Genomic Data Science – Coursera / Johns Hopkins (2024)",
            "• Industrial Biotechnology & GMP – NPTEL / IIT Madras (2023)",
        ],
        certifications_right=[
            "• Advanced Techniques in Biotechnology – Parul University (2025)",
            "• Molecular Biology Techniques – Udemy (2023)",
            "• Digital Marketing & Web Foundations – Google / ITI (2021–2024)",
        ],
        achievements=[
            "• <b>Best Research Project Award (2024)</b> – Parul Institute of Technology & Engineering for Bioethanol SSF optimization.",
            "• <b>Dean's List for Academic Excellence (2024–2025)</b> – Recognized for top percentile performance in Biotechnology coursework.",
            "• <b>Automated Genomic Pipeline</b> – Developed Python workflow reducing manual sequence curation time by 40% (AMR study).",
        ],
        languages="English (Fluent), Hindi (Fluent), Gujarati (Native)",
        personal_details="Date of Birth: 20 June 2001 | Marital Status: Single | Nationality: Indian | Availability: Immediate Joiner",
        declaration="I hereby solemnly declare that all statements and particulars provided in this resume are true, complete, and authentic to the best of my knowledge.",
    )


def get_experienced_data() -> ResumeData:
    """Returns resume data structured for experienced QA Officer roles."""
    return ResumeData(
        profile_type="Experienced",
        theme_primary="#0F2942",
        theme_secondary="#1E5F8E",
        subtitle_page2="Curriculum Vitae | Experienced QA / IPQA Officer",
        contact=ContactInfo(
            name="BALAJI DILIPSINGH RAJPUT",
            title="QA Officer | IPQA Officer | Pharmaceutical Quality Assurance",
            phone="+91 87808 61044",
            phone_clean="+918780861044",
            email="balajirajput966@gmail.com",
            location="Vadodara, Gujarat 390010, India",
            linkedin_url="https://linkedin.com/in/balaji-rajput-483a86194",
            linkedin_display="linkedin.com/in/balaji-rajput-483a86194",
            github_url="https://github.com/balajirajput96",
            github_display="github.com/balajirajput96",
            availability="Immediate Joiner",
        ),
        summary_heading="Professional Summary",
        summary=(
            "Results-driven QA professional with hands-on experience in pharmaceutical Quality Assurance "
            "at Elysium Pharmaceuticals Ltd., Vadodara. Expert in cGMP/GDP compliance, SOP development, CAPA, deviation management, "
            "BMR/BPR review, and regulatory documentation (CDSCO/WHO-GMP/FDA) with zero critical observations. Strong Biotechnology "
            "background with lab proficiency in HPLC, PCR, and microbiology. Immediately available for QA Executive or Regulatory Affairs "
            "roles across Gujarat's pharmaceutical sector."
        ),
        competencies_heading="Core Competencies",
        competencies_left=[
            "• cGMP, GDP & GLP Compliance",
            "• SOP Authoring & Periodic Review",
            "• Change Control Management",
            "• Internal GMP Audits & Self-Inspection",
            "• Vendor Qualification Support",
            "• Label Reconciliation & Artwork Review",
        ],
        competencies_right=[
            "• CAPA & Deviation Management",
            "• BMR / BPR Review & Batch Release",
            "• OOS & OOT Investigation Support",
            "• QMS Documentation & Control",
            "• CDSCO / WHO-GMP / FDA Compliance",
            "• Stability Studies & APQR Compilation",
        ],
        education=[
            {
                "degree": "Diploma in Biotechnology",
                "institution": "Parul Institute of Technology & Engineering, Gujarat Technological University (GTU), Vadodara",
                "duration": "2021 – 2025",
                "score": "CGPA: 6.7 / 10 | Dean's List (2024–2025) | Best Research Project Award (2024)",
                "coursework": "Key Subjects: Molecular Biology, Biochemistry, Microbiology, Bioprocess Technology, Immunology, Fermentation.",
            }
        ],
        experience_heading="Professional Experience",
        experience=[
            {
                "role": "QA Officer / IPQA Officer",
                "company": "Elysium Pharmaceuticals Ltd., Dabhasa, Vadodara",
                "duration": "Mar 2024 – Mar 2026",
                "bullets": [
                    "Maintained 100% cGMP compliance across Oral Solid Dosage manufacturing; performed line clearance and IPQA tests.",
                    "Reviewed and verified 50+ BMRs and BPRs monthly alongside yield reconciliation logs, reducing documentation discrepancies by 15%.",
                    "Investigated deviations via 5-Why/Fishbone root-cause analysis; formulated and closed CAPAs within strict timelines.",
                    "Authored and revised 15+ SOPs, boosting departmental operating standardization and efficiency by 20%.",
                    "Managed change control evaluation and compiled documentation packages for CDSCO and WHO-GMP audit readiness with zero critical observations.",
                ],
            },
            {
                "role": "Bioinformatics Intern",
                "company": "Biotecnika (Remote)",
                "duration": "2024 (3 Months)",
                "bullets": [
                    "Built Python/Biopython pipelines for sequence alignment; evaluated 500+ DNA/protein sequences via BLAST & ClustalW.",
                    "Reduced manual sequence curation time by 40% through automated pipeline implementation.",
                ],
            },
        ],
        projects=[
            {
                "title": "Bioethanol Production from Agricultural Waste (2024)",
                "details": (
                    "Optimized SSF process with S. cerevisiae using RSM/DOE; achieved 15% yield improvement validated via HPLC (p &lt; 0.05). "
                    "Won Best Research Project Award – Parul Institute 2024."
                ),
                "tags": "[Fermentation, DOE/RSM, HPLC, ANOVA]",
            },
            {
                "title": "Comparative Genomic Analysis of AMR Genes (2024)",
                "details": (
                    "Analyzed 120 bacterial genomes from NCBI GenBank via automated Python/Biopython workflow; identified 8 novel AMR variants."
                ),
                "tags": "[Python, Biopython, BLAST, GenBank, ClustalW]",
            },
            {
                "title": "Protein Structure Prediction & Molecular Docking (2023)",
                "details": (
                    "Modeled 5 therapeutic proteins (SWISS-MODEL) and screened 50 ligands (AutoDock Vina); identified 3 lead drug candidates."
                ),
                "tags": "[SWISS-MODEL, AutoDock Vina, PyMOL, PDB]",
            },
        ],
        skills=[
            (
                "QA / Regulatory:",
                "cGMP, GDP, GLP, SOP Writing, CAPA, Deviation Management, BMR/BPR Review, Change Control, OOS/OOT, QMS, 21 CFR Part 11, CDSCO, WHO-GMP.",
            ),
            (
                "Laboratory:",
                "HPLC, PCR, RT-PCR, UV-Vis Spectrophotometry, Gel Electrophoresis, Microbial Culture, Sterility Testing, Disintegration & Friability.",
            ),
            (
                "Bioinformatics:",
                "Python (Biopython, Pandas, NumPy), R, BLAST, ClustalW, NCBI GenBank, UniProt, AutoDock Vina, SWISS-MODEL, PyMOL.",
            ),
            (
                "Software:",
                "MS Office Suite (Advanced), TrackWise (Basics), SAP (Basics), SPSS, MATLAB, Git/GitHub.",
            ),
        ],
        certifications_left=[
            "• Bioinformatics Specialization – Coursera / UC San Diego (2024)",
            "• Python for Genomic Data Science – Coursera / Johns Hopkins (2024)",
            "• Industrial Biotechnology & GMP Fundamentals – NPTEL / IIT Madras (2023)",
        ],
        certifications_right=[
            "• Advanced Biotechnology Techniques – Parul University (2025)",
            "• Molecular Biology Techniques – Udemy (2023)",
            "• Digital Marketing & Web Designing – Google / ITI (2021–2024)",
        ],
        achievements=[
            "• 100% GMP & GDP compliance maintained across batch records; zero critical observations during inspection reviews.",
            "• Authored 15+ SOPs driving 20% efficiency improvement; Best Research Project Award (Parul Institute 2024).",
            "• 8 novel AMR variants identified; 40% reduction in curation time via Python automation; Dean's List 2024–2025.",
        ],
        languages="English (Fluent), Hindi (Fluent), Gujarati (Native)",
        personal_details="Date of Birth: 20 June 2001 | Marital Status: Single | Nationality: Indian | Availability: Immediate Joiner",
        declaration="I hereby declare that all information furnished above is true and accurate to the best of my knowledge.",
    )


def get_starbucks_data() -> ResumeData:
    """
    Returns resume data personalized for:
    Assistant Store Manager (Fresher) at Tata Starbucks Private Limited, Vadodara.
    Incorporates:
    - Target Company & Role: Tata Starbucks Private Limited, Vadodara (Work from Office, Full-Time, Fresher)
    - Philosophy: "people business selling coffee"
    - Starbucks Mission Statement: "To inspire and nurture the human spirit – one person, one cup and one neighbourhood at a time"
    - Culture of Respect and Dignity, Integrity, Honesty, and TATA Starbucks Guiding Principles
    - Purpose & Scope: Assisting Store Manager in executing store operations during scheduled shifts, deploying partners & delegating tasks
    - Coaching & Feedback: Encouraging partner coaching, feedback on partner performance, recognizing changes in morale, addressing motivation
    - Coffee Knowledge & Legendary Customer Service: Passionate coffee storytelling, roasts & brewing, 'Customer Comes First' attitude
    - Safety, Cash & Standards: Partner safety/security, cash management policies, regular attendance & punctuality, beverage/food recipe presentation standards, FSSAI hygiene, team recognition, contributing to sales targets & shift efficiency
    - The Exact 4 Core Competencies: Achieving Results, Living Our Mission And Values, Helping Others Succeed, Working Together
    - Education: Minimum 12th pass requirement exceeded (Diploma in Biotechnology, Parul Institute / GTU, Dean's List)
    """
    return ResumeData(
        profile_type="Tata Starbucks Assistant Store Manager (Fresher)",
        theme_primary="#006241",    # Tata Starbucks Siren Green
        theme_secondary="#00754A",  # Vibrant Starbucks Emerald
        subtitle_page2="Assistant Store Manager (Fresher) | Tata Starbucks Private Limited, Vadodara",
        contact=ContactInfo(
            name="BALAJI DILIPSINGH RAJPUT",
            title="Candidate for Assistant Store Manager (Fresher) | Tata Starbucks Private Limited, Vadodara",
            phone="+91 87808 61044",
            phone_clean="+918780861044",
            email="balajirajput966@gmail.com",
            location="Vadodara, Gujarat 390010, India",
            linkedin_url="https://linkedin.com/in/balaji-rajput-483a86194",
            linkedin_display="linkedin.com/in/balaji-rajput-483a86194",
            github_url="https://github.com/balajirajput96",
            github_display="github.com/balajirajput96",
            availability="Immediate Joiner (Full-Time / Rotational Shifts / Work from Office)",
        ),
        summary_heading="Career Objective & Tata Starbucks Philosophy Alignment",
        summary=(
            "Energetic, disciplined, and customer-focused <b>Fresher</b> seeking the position of <b>Assistant Store Manager</b> "
            "at <b>Tata Starbucks Private Limited (Vadodara)</b>. Deeply committed to the Starbucks Mission: "
            "<i>'To inspire and nurture the human spirit – one person, one cup and one neighbourhood at a time.'</i> "
            "Embracing the belief that Starbucks is in the <i>'people business selling coffee'</i>, dedicated to fostering a "
            "workplace grounded in <b>respect and dignity</b>, unwavering integrity, honesty, and TATA Starbucks guiding principles. "
            "Eager to actively assist the Store Manager in running scheduled shifts, deploying partners, delegating operational tasks, "
            "delivering legendary customer service with a steadfast <i>'customer comes first'</i> mindset, sharing coffee knowledge, "
            "and upholding impeccable health, safety, cash management, and recipe standards. Available immediately for full-time shift operations."
        ),
        competencies_heading="The 4 Core Starbucks Competencies & Operational Pillars",
        competencies_left=[
            "• <b>Achieving Results:</b> Driving shift speed-of-service, sales targets & cash accuracy",
            "• <b>Living Our Mission & Values:</b> Fostering human connection, respect, dignity & honesty",
            "• <b>Helping Others Succeed:</b> Respectful partner coaching, motivation & morale support",
            "• <b>Working Together:</b> Effective partner deployment, teamwork & seamless shift flow",
        ],
        competencies_right=[
            "• <b>Customer First Mindset:</b> Delivering the warm, legendary 'Third Place' experience",
            "• <b>Coffee Craft & Stories:</b> Passion for roast profiles, brewing methods & coffee lore",
            "• <b>Safety & Cash Integrity:</b> Strict cash register policies, audits & partner safety",
            "• <b>Operational Hygiene:</b> Cleanliness, recipe presentation standards & FSSAI rules",
        ],
        education=[
            {
                "degree": "Diploma in Biotechnology (12th+ Advanced Technical Qualification)",
                "institution": "Parul Institute of Technology & Engineering, Gujarat Technological University (GTU), Vadodara",
                "duration": "2021 – 2025",
                "score": "CGPA: 6.7 / 10 | Dean's List for Academic Excellence (2024–2025)",
                "coursework": "Foundations: Process Optimization, Quality Control & Hygiene Standards, Applied Science, Computer Tools & Professional Communication. (Exceeds the minimum 12th pass requirement with proven discipline and punctuality).",
            }
        ],
        experience_heading="Foundational Operations, Floor Coordination & Hygiene Experience",
        experience=[
            {
                "role": "Industrial Trainee — Floor Operations, Quality & Sanitation",
                "company": "Elysium Pharmaceuticals Ltd., Dabhasa, Vadodara",
                "duration": "2 Months (Practical Training)",
                "bullets": [
                    "Executed disciplined daily shift routines, adhering strictly to Standard Operating Procedures (SOPs), workplace safety, personal hygiene, and clean-as-you-go floor sanitation protocols.",
                    "Monitored shift records, area line clearances, and equipment readiness checklists with zero compliance discrepancies.",
                    "Coordinated collaboratively with shift peers to maintain rapid workflow, punctual shift handovers, and documentation accuracy.",
                ],
            },
            {
                "role": "Trainee Intern — SOP Adherence & Process Coordination",
                "company": "Gujarat Biotech Innovations, Vadodara",
                "duration": "2 Months (Practical Training)",
                "bullets": [
                    "Maintained rigorous compliance with standard operating guidelines, cleanliness checklists, and task deadlines during scheduled floor hours.",
                    "Demonstrated dependable shift attendance, teamwork, active listening, and constructive peer support.",
                ],
            },
        ],
        projects_heading="Store Operations, Customer Experience & Coffee Craft Initiatives",
        projects=[
            {
                "title": "Legendary Customer Service & 'Customer Comes First' Focus",
                "details": (
                    "Trained in prioritizing customer satisfaction through warm welcomes, active listening, and personalized engagement. "
                    "Adept at anticipating customer preferences and resolving concerns with empathy and speed, ensuring each customer "
                    "enjoys a welcoming and uplifting 'Third Place' Starbucks Experience."
                ),
                "tags": "[Customer Engagement, Active Listening, Problem Resolution, Third Place Culture]",
            },
            {
                "title": "Coffee Knowledge, Brewing Passion & Beverage Presentation",
                "details": (
                    "Enthusiastic student of coffee culture—from bean sourcing (Latin America, Africa, Asia-Pacific) and roast spectra "
                    "(Blonde, Medium, Dark) to espresso extraction, milk steaming, and beverage customization. Committed to sharing "
                    "coffee stories and strictly upholding recipe and presentation standards for handcrafted beverages and whole bean coffee."
                ),
                "tags": "[Coffee Knowledge, Recipe Standards, Beverage Craft, Ethical Sourcing, Storytelling]",
            },
            {
                "title": "Shift Deployment, Task Delegation & Partner Support",
                "details": (
                    "Practiced in dynamic team coordination: deploying partners across stations (Order Taking/POS, Bar/Brewing, "
                    "Food Warming, Handoff, Lobby & Cleanliness) based on floor demand. Anticipates rush periods, recognizes changes "
                    "in partner morale, addresses individual motivation, and provides constructive feedback to the Store Manager."
                ),
                "tags": "[Partner Deployment, Task Delegation, Morale Recognition, Team Motivation]",
            },
            {
                "title": "Cash Management, Partner Safety & Food Sanitation Standards",
                "details": (
                    "Committed to 100% adherence to cash handling rules, cash register accuracy, shift drawer balancing, and cash drop policies. "
                    "Champions partner safety, emergency protocols, and rigorous food safety/sanitation guidelines (FSSAI/QSR standards), "
                    "maintaining impeccable store cleanliness, regular attendance, and shift punctuality."
                ),
                "tags": "[Cash Management, Register Policy, Partner Safety, FSSAI Sanitation, Punctuality]",
            },
        ],
        skills_heading="Core Skills & Operational Competency Matrix",
        skills=[
            (
                "Store Operations & Delegation:",
                "Assisting Store Manager during scheduled shifts, partner deployment & task delegation, opening & closing checklists, floor cleanliness, queue management, speed-of-service optimization, stock rotation (FIFO), and daily shift logbooks.",
            ),
            (
                "Customer Service & Sales Achievement:",
                "Legendary customer service, 'Customer Comes First' philosophy, anticipating customer & store needs, suggestive selling & upselling, contributing proactively to daily/monthly store sales targets, customer loyalty recognition.",
            ),
            (
                "Coffee & Beverage Quality Standards:",
                "Coffee roast profiles & origin storytelling, handcrafted beverage recipe adherence, milk steaming & presentation standards, food warming & display merchandising, product freshness & whole bean coffee knowledge.",
            ),
            (
                "Safety, Cash & Sanitation Compliance:",
                "Cash register operation & drawer reconciliation, cash management policies, partner safety & security guidelines, health & food sanitation standards (FSSAI/GMP), clean-as-you-go discipline, and regular shift punctuality.",
            ),
            (
                "Partner Coaching & Teamwork:",
                "Respectful and encouraging coaching, recognizing partner morale shifts, addressing individual motivation, providing feedback to Store Manager, team recognition & milestone celebrations, working together with integrity and honesty.",
            ),
            (
                "Computer & Digital Tools:",
                "MS Office Suite (Excel, Word, PowerPoint), POS / Cash Register systems awareness, shift scheduling basics, Google Workspace, digital reporting, and quick adaptability to retail software.",
            ),
        ],
        certifications_heading="Certifications, Accreditations & Key Honors",
        certifications_left=[
            "• Digital Marketing & Customer Basics – Google / ITI (2024)",
            "• Quality, Hygiene & GMP Standards – NPTEL / IIT Madras (2023)",
            "• Workplace Communication & Interpersonal Dynamics – Parul University (2024)",
        ],
        certifications_right=[
            "• Food Safety & Sanitation Orientation – Campus Health Workshop (2023)",
            "• Technical Documentation & SOP Systems – Elysium Training (2024)",
            "• Retail POS & Computer Data Management – GTU Certification (2022)",
        ],
        achievements_heading="Key Honors & Leadership Recognition",
        achievements=[
            "• <b>Dean's List for Academic Excellence (2024–2025):</b> Awarded by Parul Institute for exemplary attendance, discipline, and top performance.",
            "• <b>Best Project Award (2024):</b> Parul Institute of Technology & Engineering — Recognized for outstanding teamwork and achieving results.",
            "• <b>Shift Discipline Recognition:</b> Commended during Elysium industrial training for meticulous sanitation checklist maintenance and perfect punctuality.",
        ],
        languages="English (Fluent - Professional Communication), Hindi (Fluent), Gujarati (Native/Fluent - Local Vadodara Customer Connect)",
        personal_details="Date of Birth: 20 June 2001 | Marital Status: Single | Nationality: Indian | Location: Vadodara, Gujarat | Availability: Immediate Joiner (Full-Time / Rotational Shifts / Work from Office)",
        declaration="I hereby solemnly declare that all particulars and statements furnished above are true, complete, and authentic to the best of my knowledge and belief.",
    )


# ---------------------------------------------------------------------------
# NUMBERED TWO-PASS CANVAS WITH THEMED RUNNING HEADERS & FOOTERS
# ---------------------------------------------------------------------------
class BaseProfessionalCanvas(canvas.Canvas):
    """Two-pass canvas that computes exact total page count, running headers, and clean footers."""
    color_primary = COLOR_PRIMARY_NAVY
    color_secondary = COLOR_SECONDARY_BLUE
    header_subtitle = "Curriculum Vitae"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._saved_page_states: List[Dict[str, Any]] = []

    def showPage(self) -> None:
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self) -> None:
        total_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_decorations(total_pages)
            super().showPage()
        super().save()

    def _draw_decorations(self, total_pages: int) -> None:
        self.saveState()
        page_width, page_height = A4
        margin = 14 * mm

        # Top Accent Header Line (Page 2+)
        if self._pageNumber > 1:
            self.setStrokeColor(self.color_secondary)
            self.setLineWidth(1.0)
            self.line(margin, page_height - 10 * mm, page_width - margin, page_height - 10 * mm)

            self.setFont("Helvetica-Bold", 7.5)
            self.setFillColor(self.color_primary)
            self.drawString(margin, page_height - 9 * mm, "BALAJI DILIPSINGH RAJPUT")

            self.setFont("Helvetica", 7.5)
            self.setFillColor(COLOR_TEXT_MUTED)
            self.drawRightString(
                page_width - margin,
                page_height - 9 * mm,
                self.header_subtitle,
            )

        # Bottom Running Footer (All Pages)
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.6)
        self.line(margin, 11 * mm, page_width - margin, 11 * mm)

        self.setFont("Helvetica", 7.5)
        self.setFillColor(COLOR_TEXT_MUTED)
        self.drawString(
            margin,
            7.5 * mm,
            "Balaji Dilipsingh Rajput  •  +91 8780861044  •  balajirajput966@gmail.com",
        )

        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(page_width - margin, 7.5 * mm, page_str)

        self.restoreState()


# ---------------------------------------------------------------------------
# RESUME PDF BUILDER ENGINE
# ---------------------------------------------------------------------------
class ResumeBuilder:
    """Configures styles and compiles flowable elements for the resume."""

    def __init__(self, data: ResumeData, output_path: str) -> None:
        self.data = data
        self.output_path = output_path
        self.color_primary = HexColor(data.theme_primary)
        self.color_secondary = HexColor(data.theme_secondary)
        self.styles = self._setup_styles()

    def _setup_styles(self) -> Dict[str, ParagraphStyle]:
        styles = getSampleStyleSheet()

        styles.add(
            ParagraphStyle(
                name="HeaderName",
                fontName="Helvetica-Bold",
                fontSize=20,
                leading=22,
                textColor=self.color_primary,
                alignment=TA_CENTER,
                spaceAfter=1.5 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="HeaderTitle",
                fontName="Helvetica-Bold",
                fontSize=9.3,
                leading=12,
                textColor=self.color_secondary,
                alignment=TA_CENTER,
                spaceAfter=2.2 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="HeaderContact",
                fontName="Helvetica",
                fontSize=8.2,
                leading=11.3,
                textColor=COLOR_TEXT_DARK,
                alignment=TA_CENTER,
                spaceAfter=1.8 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="SectionHeading",
                fontName="Helvetica-Bold",
                fontSize=10.2,
                leading=12.8,
                textColor=self.color_primary,
                spaceBefore=2.2 * mm,
                spaceAfter=1.2 * mm,
                keepWithNext=True,
            )
        )

        styles.add(
            ParagraphStyle(
                name="BodyJustified",
                fontName="Helvetica",
                fontSize=8.4,
                leading=11.2,
                textColor=COLOR_TEXT_DARK,
                alignment=TA_JUSTIFY,
                spaceAfter=1.2 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="BulletItem",
                fontName="Helvetica",
                fontSize=8.1,
                leading=10.6,
                textColor=COLOR_TEXT_DARK,
                alignment=TA_JUSTIFY,
                leftIndent=3.2 * mm,
                spaceAfter=0.8 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="ItemHeaderLeft",
                fontName="Helvetica-Bold",
                fontSize=8.7,
                leading=11.3,
                textColor=self.color_primary,
            )
        )

        styles.add(
            ParagraphStyle(
                name="ItemHeaderRight",
                fontName="Helvetica-Bold",
                fontSize=8.2,
                leading=11.3,
                textColor=self.color_secondary,
                alignment=TA_RIGHT,
            )
        )

        styles.add(
            ParagraphStyle(
                name="ItemSubHeader",
                fontName="Helvetica-Oblique",
                fontSize=8.1,
                leading=10.4,
                textColor=COLOR_TEXT_MUTED,
                spaceAfter=0.8 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="TableCompactText",
                fontName="Helvetica",
                fontSize=8.1,
                leading=10.3,
                textColor=COLOR_TEXT_DARK,
            )
        )

        styles.add(
            ParagraphStyle(
                name="DeclarationText",
                fontName="Helvetica-Oblique",
                fontSize=7.8,
                leading=10.0,
                textColor=COLOR_TEXT_DARK,
                spaceAfter=1.5 * mm,
            )
        )

        return styles

    def _create_section_heading(self, title: str) -> List[Any]:
        """Creates a stylized section heading with a clean accent underline."""
        heading_text = f"<b>{title.upper()}</b>"
        elements = [
            Paragraph(heading_text, self.styles["SectionHeading"]),
            HRFlowable(
                width="100%",
                thickness=1.0,
                color=self.color_secondary,
                spaceBefore=0.4 * mm,
                spaceAfter=1.8 * mm,
            ),
        ]
        return elements

    def build_pdf(self) -> str:
        """Assembles and generates the strictly 2-page ATS PDF document."""
        out_file = Path(self.output_path).resolve()
        out_file.parent.mkdir(parents=True, exist_ok=True)

        page_width, page_height = A4
        margin = 14 * mm
        content_width = page_width - (2 * margin)

        doc = SimpleDocTemplate(
            str(out_file),
            pagesize=A4,
            leftMargin=margin,
            rightMargin=margin,
            topMargin=12 * mm,
            bottomMargin=13 * mm,
            title=f"Balaji Dilipsingh Rajput - {self.data.profile_type} Resume",
            author="Balaji Dilipsingh Rajput",
            subject=f"{self.data.profile_type} Resume",
            keywords="Balaji Rajput, Resume, Tata Starbucks, Assistant Store Manager, Fresher, Vadodara, Customer Service, Coffee Craft",
        )

        story: List[Any] = []
        c = self.data.contact

        # ===================================================================
        # PAGE 1: HEADER & IDENTITY
        # ===================================================================
        story.append(Paragraph(c.name, self.styles["HeaderName"]))
        story.append(Paragraph(c.title, self.styles["HeaderTitle"]))

        # Interactive Contact Line (ATS-friendly, selectable, clickable hyperlinks)
        line1 = (
            f"Location: {c.location} &nbsp;&nbsp;|&nbsp;&nbsp; "
            f"Phone: <a href='tel:{c.phone_clean}'><u>{c.phone}</u></a> &nbsp;&nbsp;|&nbsp;&nbsp; "
            f"Email: <a href='mailto:{c.email}'><u>{c.email}</u></a>"
        )
        line2 = (
            f"LinkedIn: <a href='{c.linkedin_url}'><u>{c.linkedin_display}</u></a> &nbsp;&nbsp;|&nbsp;&nbsp; "
            f"GitHub: <a href='{c.github_url}'><u>{c.github_display}</u></a> &nbsp;&nbsp;|&nbsp;&nbsp; "
            f"Availability: <b>{c.availability}</b>"
        )
        story.append(Paragraph(f"{line1}<br/>{line2}", self.styles["HeaderContact"]))
        story.append(
            HRFlowable(
                width="100%",
                thickness=1.2,
                color=self.color_primary,
                spaceBefore=0.8 * mm,
                spaceAfter=2.0 * mm,
            )
        )

        # -------------------------------------------------------------------
        # SUMMARY / CAREER OBJECTIVE
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading(self.data.summary_heading))
        story.append(Paragraph(self.data.summary, self.styles["BodyJustified"]))
        story.append(Spacer(1, 0.8 * mm))

        # -------------------------------------------------------------------
        # CORE COMPETENCIES
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading(self.data.competencies_heading))
        comp_rows = []
        max_len = max(len(self.data.competencies_left), len(self.data.competencies_right))
        col_w = content_width / 2.0

        for i in range(max_len):
            left_item = self.data.competencies_left[i] if i < len(self.data.competencies_left) else ""
            right_item = self.data.competencies_right[i] if i < len(self.data.competencies_right) else ""
            comp_rows.append(
                [
                    Paragraph(left_item, self.styles["TableCompactText"]),
                    Paragraph(right_item, self.styles["TableCompactText"]),
                ]
            )

        comp_table = Table(comp_rows, colWidths=[col_w, col_w])
        comp_table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
                    ("TOPPADDING", (0, 0), (-1, -1), 0.3 * mm),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0.3 * mm),
                ]
            )
        )
        story.append(comp_table)
        story.append(Spacer(1, 1.2 * mm))

        # -------------------------------------------------------------------
        # EDUCATION
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading("Education"))
        for edu in self.data.education:
            edu_header = Table(
                [
                    [
                        Paragraph(f"<b>{edu['degree']}</b>", self.styles["ItemHeaderLeft"]),
                        Paragraph(edu["duration"], self.styles["ItemHeaderRight"]),
                    ]
                ],
                colWidths=[content_width * 0.75, content_width * 0.25],
            )
            edu_header.setStyle(
                TableStyle(
                    [
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 0),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                        ("TOPPADDING", (0, 0), (-1, -1), 0),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                    ]
                )
            )
            story.append(edu_header)
            story.append(Paragraph(edu["institution"], self.styles["ItemSubHeader"]))
            story.append(Paragraph(f"<b>Honors / Performance:</b> {edu['score']}", self.styles["BulletItem"]))
            story.append(Paragraph(f"{edu['coursework']}", self.styles["BulletItem"]))
            story.append(Spacer(1, 1.2 * mm))

        # -------------------------------------------------------------------
        # INDUSTRIAL TRAINING & PRACTICAL FLOOR EXPERIENCE
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading(self.data.experience_heading))
        for exp in self.data.experience:
            exp_header = Table(
                [
                    [
                        Paragraph(f"<b>{exp['role']}</b> — {exp['company']}", self.styles["ItemHeaderLeft"]),
                        Paragraph(exp["duration"], self.styles["ItemHeaderRight"]),
                    ]
                ],
                colWidths=[content_width * 0.75, content_width * 0.25],
            )
            exp_header.setStyle(
                TableStyle(
                    [
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 0),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                        ("TOPPADDING", (0, 0), (-1, -1), 0),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                    ]
                )
            )
            story.append(exp_header)
            story.append(Spacer(1, 0.3 * mm))
            for b in exp["bullets"]:
                story.append(Paragraph(f"• {b}", self.styles["BulletItem"]))
            story.append(Spacer(1, 1.0 * mm))

        # ===================================================================
        # PAGE BREAK TO PAGE 2 (STRICT 2-PAGE BUDGETING)
        # ===================================================================
        story.append(PageBreak())

        # -------------------------------------------------------------------
        # PAGE 2: PROJECTS / OPERATIONAL INITIATIVES
        # -------------------------------------------------------------------
        projects_heading = getattr(self.data, "projects_heading", "Key Academic & Research Projects")
        story.extend(self._create_section_heading(projects_heading))
        for proj in self.data.projects:
            story.append(
                Paragraph(
                    f"<b>{proj['title']}</b> <font color='{COLOR_TEXT_MUTED.hexval()}'>{proj['tags']}</font>",
                    self.styles["ItemHeaderLeft"],
                )
            )
            story.append(Spacer(1, 0.3 * mm))
            story.append(Paragraph(proj["details"], self.styles["BulletItem"]))
            story.append(Spacer(1, 1.0 * mm))

        # -------------------------------------------------------------------
        # TECHNICAL / OPERATIONAL SKILLS MATRIX
        # -------------------------------------------------------------------
        skills_heading = getattr(self.data, "skills_heading", "Technical & Laboratory Skills")
        story.extend(self._create_section_heading(skills_heading))
        for category, skill_list in self.data.skills:
            skill_text = f"<b><font color='{self.color_primary.hexval()}'>{category}</font></b> {skill_list}"
            story.append(Paragraph(skill_text, self.styles["BulletItem"]))
            story.append(Spacer(1, 0.4 * mm))
        story.append(Spacer(1, 1.2 * mm))

        # -------------------------------------------------------------------
        # CERTIFICATIONS & SPECIALIZED TRAINING
        # -------------------------------------------------------------------
        certifications_heading = getattr(self.data, "certifications_heading", "Certifications & Specialized Training")
        story.extend(self._create_section_heading(certifications_heading))
        cert_rows = []
        c_max = max(len(self.data.certifications_left), len(self.data.certifications_right))
        for i in range(c_max):
            c_left = self.data.certifications_left[i] if i < len(self.data.certifications_left) else ""
            c_right = self.data.certifications_right[i] if i < len(self.data.certifications_right) else ""
            cert_rows.append(
                [
                    Paragraph(c_left, self.styles["TableCompactText"]),
                    Paragraph(c_right, self.styles["TableCompactText"]),
                ]
            )

        cert_table = Table(cert_rows, colWidths=[col_w, col_w])
        cert_table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
                    ("TOPPADDING", (0, 0), (-1, -1), 0.3 * mm),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0.3 * mm),
                ]
            )
        )
        story.append(cert_table)
        story.append(Spacer(1, 1.2 * mm))

        # -------------------------------------------------------------------
        # KEY HONORS & ACHIEVEMENTS
        # -------------------------------------------------------------------
        achievements_heading = getattr(self.data, "achievements_heading", "Key Honors & Achievements")
        story.extend(self._create_section_heading(achievements_heading))
        for ach in self.data.achievements:
            story.append(Paragraph(ach, self.styles["BulletItem"]))
        story.append(Spacer(1, 1.2 * mm))

        # -------------------------------------------------------------------
        # PERSONAL DOSSIER & FORMAL DECLARATION
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading("Personal Dossier & Formal Declaration"))
        story.append(
            Paragraph(f"<b>Languages Known:</b> {self.data.languages}", self.styles["TableCompactText"])
        )
        story.append(Spacer(1, 0.4 * mm))
        story.append(
            Paragraph(f"<b>Candidate Particulars:</b> {self.data.personal_details}", self.styles["TableCompactText"])
        )
        story.append(Spacer(1, 1.0 * mm))
        story.append(Paragraph(f"<i>{self.data.declaration}</i>", self.styles["DeclarationText"]))
        story.append(Spacer(1, 1.2 * mm))

        # Signature & Place Table
        sig_data = [
            [
                Paragraph("<b>Place:</b> Vadodara, Gujarat", self.styles["TableCompactText"]),
                Paragraph("<b>(Balaji Dilipsingh Rajput)</b>", self.styles["ItemHeaderRight"]),
            ],
            [
                Paragraph("<b>Date:</b> ____________________", self.styles["TableCompactText"]),
                Paragraph("Candidate Signature", self.styles["ItemHeaderRight"]),
            ],
        ]
        sig_table = Table(sig_data, colWidths=[content_width * 0.5, content_width * 0.5])
        sig_table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0.3 * mm),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0.3 * mm),
                ]
            )
        )
        story.append(sig_table)

        # Dynamic canvas subclass configured with current theme
        primary = self.color_primary
        secondary = self.color_secondary
        subtitle_p2 = getattr(self.data, "subtitle_page2", "Curriculum Vitae")

        class ConfiguredCanvas(BaseProfessionalCanvas):
            color_primary = primary
            color_secondary = secondary
            header_subtitle = subtitle_p2

        # Build document with custom canvas
        doc.build(story, canvasmaker=ConfiguredCanvas)
        return str(out_file)


# ---------------------------------------------------------------------------
# CLI & MAIN ENTRYPOINT
# ---------------------------------------------------------------------------
def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate ATS-compliant professional PDF resume for Balaji Rajput."
    )
    parser.add_argument(
        "--profile",
        choices=["fresher", "experienced", "starbucks", "starbucks_asm", "all"],
        default="fresher",
        help="Resume profile to generate: 'fresher', 'experienced', 'starbucks', or 'all' (default: fresher).",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Custom output PDF file path.",
    )
    return parser.parse_args()


def build_resume(output_path: str | None = None, profile: str = "fresher") -> str:
    """Convenience function compatible with existing verification workflows."""
    profile_key = profile.lower()
    if profile_key in ["starbucks", "starbucks_asm"]:
        default_filename = "Balaji_Rajput_Tata_Starbucks_ASM_Resume.pdf"
        data = get_starbucks_data()
    elif profile_key == "experienced":
        default_filename = "Balaji_Rajput_Professional_Resume.pdf"
        data = get_experienced_data()
    else:
        default_filename = "Balaji_Rajput_Fresher_Resume.pdf"
        data = get_fresher_data()

    if output_path is None:
        output_path = os.environ.get(
            "RESUME_OUTPUT_PATH",
            str(Path(__file__).resolve().parent / "artifacts" / default_filename),
        )

    builder = ResumeBuilder(data=data, output_path=output_path)
    final_path = builder.build_pdf()
    print(f"Resume generated successfully ({data.profile_type}): {final_path}")
    return final_path


def build_all_resumes(output_dir: str | Path | None = None) -> Dict[str, str]:
    """Generates all resume profiles (Fresher, Experienced, and Tata Starbucks ASM)."""
    base_dir = Path(output_dir) if output_dir else Path(__file__).resolve().parent / "artifacts"
    base_dir.mkdir(parents=True, exist_ok=True)

    results = {}
    profiles = [
        ("fresher", "Balaji_Rajput_Fresher_Resume.pdf"),
        ("experienced", "Balaji_Rajput_Professional_Resume.pdf"),
        ("starbucks", "Balaji_Rajput_Tata_Starbucks_ASM_Resume.pdf"),
    ]
    for prof_key, filename in profiles:
        dest = str(base_dir / filename)
        path = build_resume(output_path=dest, profile=prof_key)
        results[prof_key] = path

    return results


def main() -> None:
    args = parse_arguments()
    if args.profile == "all":
        build_all_resumes(output_dir=args.output)
    else:
        build_resume(output_path=args.output, profile=args.profile)


if __name__ == "__main__":
    main()
