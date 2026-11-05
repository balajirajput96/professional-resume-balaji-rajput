#!/usr/bin/env python3
"""
Professional Resume Generator for Balaji Dilipsingh Rajput
Features:
- Dual profile support: 'fresher' (default) and 'experienced'
- ATS-compliant single/multi-section ReportLab flowable architecture
- Clean modern typography with zero missing-glyph/emoji fallback bugs
- Interactive PDF annotations: clickable phone, email, LinkedIn, and GitHub links
- Two-pass Numbered Canvas for dynamic page count ('Page X of Y') and headers/footers
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
# COLOR PALETTE (Modern Executive Navy & Slate Blue)
# ---------------------------------------------------------------------------
COLOR_PRIMARY = HexColor("#0F2942")     # Deep Corporate Navy
COLOR_SECONDARY = HexColor("#1E5F8E")   # Refined Accent Blue
COLOR_TEXT_DARK = HexColor("#222222")   # High-contrast readable body text
COLOR_TEXT_MUTED = HexColor("#555555")  # Subtitle & metadata text
COLOR_BORDER = HexColor("#D0D7DE")      # Subtle divider border


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


def get_fresher_data() -> ResumeData:
    """Returns resume data structured for freshers (Biotechnology & Entry QA/QC)."""
    return ResumeData(
        profile_type="Fresher",
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
        ),
        summary_heading="Career Objective & Professional Summary",
        summary=(
            "Goal-oriented and detail-focused Biotechnology graduate with demonstrated academic excellence "
            "and foundational competence in cGMP/GDP compliance, wet-lab analytical techniques, and computational pipelines. "
            "Recipient of the <b>Best Research Project Award (2024)</b> and <b>Dean's List</b> distinction. Practical exposure "
            "encompasses genomic data workflows (Biotecnika), GLP microbiology & PCR testing (Gujarat Biotech Innovations), "
            "and industrial exposure in Oral Solid Dosage manufacturing. Proactive learner seeking an entry-level position as "
            "<b>Quality Assurance (QA) Trainee</b>, <b>IPQA Officer</b>, or <b>Quality Control (QC) Chemist</b> in Gujarat's pharmaceutical sector. "
            "Available to join immediately."
        ),
        competencies_heading="Core Competencies & Foundational Knowledge",
        competencies_left=[
            "• cGMP, GDP & GLP Principles",
            "• SOP Drafting & Document Lifecycle",
            "• In-Process Quality Checks (IPQA)",
            "• Good Documentation Practices (ALCOA+)",
            "• 21 CFR Part 11 & Schedule M Awareness",
            "• Label Reconciliation & Inspection",
        ],
        competencies_right=[
            "• Deviation & CAPA Basics",
            "• BMR / BPR Review Protocols",
            "• HPLC & Spectrophotometry Concepts",
            "• Microbial Testing & Aseptic Culture",
            "• Quality Management System (QMS)",
            "• Root Cause Analysis (5-Why, Fishbone)",
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
                "role": "Industrial QA Trainee / Apprentice",
                "company": "Elysium Pharmaceuticals Ltd., Dabhasa, Vadodara",
                "duration": "Mar 2024 – Mar 2026",
                "bullets": [
                    "Received hands-on industrial training in Oral Solid Dosage (tablets) manufacturing under strict cGMP and Schedule M standards.",
                    "Assisted IPQA officers in line clearance, physical parameter checks (hardness, friability, disintegration time), and BMR/BPR log verification.",
                    "Observed and supported SOP authoring, deviation tracking, and preparation of documentation packages for CDSCO/WHO-GMP audit readiness.",
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
                "Laboratory & Analytical:",
                "HPLC (Fundamentals), PCR / RT-PCR, UV-Vis Spectrophotometry, Agarose Gel Electrophoresis, Microbial & Aseptic Culture, Sterility Testing, Disintegration & Friability Testing, Autoclave, LAF.",
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
        ),
        summary_heading="Professional Summary",
        summary=(
            "Results-driven QA professional with 2+ years of hands-on experience in pharmaceutical Quality Assurance "
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


# ---------------------------------------------------------------------------
# NUMBERED TWO-PASS CANVAS WITH RUNNING HEADERS & FOOTERS
# ---------------------------------------------------------------------------
class ProfessionalCanvas(canvas.Canvas):
    """Two-pass canvas that computes exact total page count, running headers, and clean footers."""

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
            self.setStrokeColor(COLOR_SECONDARY)
            self.setLineWidth(1.0)
            self.line(margin, page_height - 10 * mm, page_width - margin, page_height - 10 * mm)

            self.setFont("Helvetica-Bold", 7.5)
            self.setFillColor(COLOR_PRIMARY)
            self.drawString(margin, page_height - 9 * mm, "BALAJI DILIPSINGH RAJPUT")

            self.setFont("Helvetica", 7.5)
            self.setFillColor(COLOR_TEXT_MUTED)
            self.drawRightString(
                page_width - margin,
                page_height - 9 * mm,
                "Curriculum Vitae | Pharmaceutical QA/QC & Biotechnology",
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
        self.styles = self._setup_styles()

    def _setup_styles(self) -> Dict[str, ParagraphStyle]:
        styles = getSampleStyleSheet()

        styles.add(
            ParagraphStyle(
                name="HeaderName",
                fontName="Helvetica-Bold",
                fontSize=20,
                leading=22,
                textColor=COLOR_PRIMARY,
                alignment=TA_CENTER,
                spaceAfter=1.5 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="HeaderTitle",
                fontName="Helvetica-Bold",
                fontSize=9.5,
                leading=12,
                textColor=COLOR_SECONDARY,
                alignment=TA_CENTER,
                spaceAfter=2.5 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="HeaderContact",
                fontName="Helvetica",
                fontSize=8.3,
                leading=11.5,
                textColor=COLOR_TEXT_DARK,
                alignment=TA_CENTER,
                spaceAfter=2 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="SectionHeading",
                fontName="Helvetica-Bold",
                fontSize=10.5,
                leading=13,
                textColor=COLOR_PRIMARY,
                spaceBefore=2.5 * mm,
                spaceAfter=1.5 * mm,
                keepWithNext=True,
            )
        )

        styles.add(
            ParagraphStyle(
                name="BodyJustified",
                fontName="Helvetica",
                fontSize=8.5,
                leading=11.5,
                textColor=COLOR_TEXT_DARK,
                alignment=TA_JUSTIFY,
                spaceAfter=1.5 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="BulletItem",
                fontName="Helvetica",
                fontSize=8.2,
                leading=10.8,
                textColor=COLOR_TEXT_DARK,
                alignment=TA_JUSTIFY,
                leftIndent=3.5 * mm,
                spaceAfter=1.0 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="ItemHeaderLeft",
                fontName="Helvetica-Bold",
                fontSize=8.8,
                leading=11.5,
                textColor=COLOR_PRIMARY,
            )
        )

        styles.add(
            ParagraphStyle(
                name="ItemHeaderRight",
                fontName="Helvetica-Bold",
                fontSize=8.3,
                leading=11.5,
                textColor=COLOR_SECONDARY,
                alignment=TA_RIGHT,
            )
        )

        styles.add(
            ParagraphStyle(
                name="ItemSubHeader",
                fontName="Helvetica-Oblique",
                fontSize=8.2,
                leading=10.5,
                textColor=COLOR_TEXT_MUTED,
                spaceAfter=1 * mm,
            )
        )

        styles.add(
            ParagraphStyle(
                name="TableCompactText",
                fontName="Helvetica",
                fontSize=8.2,
                leading=10.5,
                textColor=COLOR_TEXT_DARK,
            )
        )

        styles.add(
            ParagraphStyle(
                name="DeclarationText",
                fontName="Helvetica-Oblique",
                fontSize=7.8,
                leading=10.2,
                textColor=COLOR_TEXT_DARK,
                spaceAfter=2 * mm,
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
                color=COLOR_SECONDARY,
                spaceBefore=0.5 * mm,
                spaceAfter=2.0 * mm,
            ),
        ]
        return elements

    def build_pdf(self) -> str:
        """Assembles and generates the PDF document."""
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
            subject=f"{self.data.profile_type} Resume - Biotechnology, Pharmaceutical Quality Assurance & Control",
            keywords="Balaji Rajput, Resume, Biotechnology, QA Officer, QC Chemist, IPQA, cGMP, GDP, GLP, Python, Vadodara",
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
            f"GitHub: <a href='{c.github_url}'><u>{c.github_display}</u></a>"
        )
        story.append(Paragraph(f"{line1}<br/>{line2}", self.styles["HeaderContact"]))
        story.append(
            HRFlowable(
                width="100%",
                thickness=1.2,
                color=COLOR_PRIMARY,
                spaceBefore=1 * mm,
                spaceAfter=2.5 * mm,
            )
        )

        # -------------------------------------------------------------------
        # SUMMARY
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading(self.data.summary_heading))
        story.append(Paragraph(self.data.summary, self.styles["BodyJustified"]))
        story.append(Spacer(1, 1 * mm))

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
                    ("TOPPADDING", (0, 0), (-1, -1), 0.4 * mm),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0.4 * mm),
                ]
            )
        )
        story.append(comp_table)
        story.append(Spacer(1, 1.5 * mm))

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
            story.append(Spacer(1, 1.5 * mm))

        # -------------------------------------------------------------------
        # EXPERIENCE / INTERNSHIPS
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
            story.append(Spacer(1, 0.4 * mm))
            for b in exp["bullets"]:
                story.append(Paragraph(f"• {b}", self.styles["BulletItem"]))
            story.append(Spacer(1, 1.2 * mm))

        # ===================================================================
        # PAGE BREAK TO PAGE 2 (STRICT 2-PAGE BUDGETING)
        # ===================================================================
        story.append(PageBreak())

        # -------------------------------------------------------------------
        # PAGE 2: RESEARCH & ACADEMIC PROJECTS
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading("Key Academic & Research Projects"))
        for proj in self.data.projects:
            story.append(
                Paragraph(
                    f"<b>{proj['title']}</b> <font color='{COLOR_TEXT_MUTED.hexval()}'>{proj['tags']}</font>",
                    self.styles["ItemHeaderLeft"],
                )
            )
            story.append(Spacer(1, 0.3 * mm))
            story.append(Paragraph(proj["details"], self.styles["BulletItem"]))
            story.append(Spacer(1, 1.2 * mm))

        # -------------------------------------------------------------------
        # TECHNICAL & LABORATORY SKILLS
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading("Technical & Laboratory Skills"))
        for category, skill_list in self.data.skills:
            skill_text = f"<b><font color='{COLOR_PRIMARY.hexval()}'>{category}</font></b> {skill_list}"
            story.append(Paragraph(skill_text, self.styles["BulletItem"]))
            story.append(Spacer(1, 0.5 * mm))
        story.append(Spacer(1, 1.5 * mm))

        # -------------------------------------------------------------------
        # PROFESSIONAL CERTIFICATIONS
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading("Certifications & Specialized Training"))
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
                    ("TOPPADDING", (0, 0), (-1, -1), 0.4 * mm),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0.4 * mm),
                ]
            )
        )
        story.append(cert_table)
        story.append(Spacer(1, 1.5 * mm))

        # -------------------------------------------------------------------
        # KEY ACADEMIC ACHIEVEMENTS & AWARDS
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading("Key Honors & Achievements"))
        for ach in self.data.achievements:
            story.append(Paragraph(ach, self.styles["BulletItem"]))
        story.append(Spacer(1, 1.5 * mm))

        # -------------------------------------------------------------------
        # PERSONAL DETAILS & DECLARATION
        # -------------------------------------------------------------------
        story.extend(self._create_section_heading("Personal Dossier & Declaration"))
        story.append(
            Paragraph(f"<b>Languages Known:</b> {self.data.languages}", self.styles["TableCompactText"])
        )
        story.append(Spacer(1, 0.4 * mm))
        story.append(
            Paragraph(f"<b>Details:</b> {self.data.personal_details}", self.styles["TableCompactText"])
        )
        story.append(Spacer(1, 1.2 * mm))
        story.append(Paragraph(f"<i>{self.data.declaration}</i>", self.styles["DeclarationText"]))
        story.append(Spacer(1, 1.5 * mm))

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
                    ("TOPPADDING", (0, 0), (-1, -1), 0.4 * mm),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0.4 * mm),
                ]
            )
        )
        story.append(sig_table)

        # Build document with custom canvas
        doc.build(story, canvasmaker=ProfessionalCanvas)
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
        choices=["fresher", "experienced"],
        default="fresher",
        help="Resume profile to generate (default: fresher).",
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
    if output_path is None:
        filename = (
            "Balaji_Rajput_Fresher_Resume.pdf"
            if profile == "fresher"
            else "Balaji_Rajput_Professional_Resume.pdf"
        )
        output_path = os.environ.get(
            "RESUME_OUTPUT_PATH",
            str(Path(__file__).resolve().parent / "artifacts" / filename),
        )

    data = get_fresher_data() if profile == "fresher" else get_experienced_data()
    builder = ResumeBuilder(data=data, output_path=output_path)
    final_path = builder.build_pdf()
    print(f"Resume generated successfully ({profile} profile): {final_path}")
    return final_path


def main() -> None:
    args = parse_arguments()
    build_resume(output_path=args.output, profile=args.profile)


if __name__ == "__main__":
    main()
