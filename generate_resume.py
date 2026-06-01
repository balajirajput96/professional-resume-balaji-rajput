#!/usr/bin/env python3
"""
Professional 2-Page Resume Generator for Balaji Dilipsingh Rajput
Using ReportLab for modern, clean, professional PDF output.
"""

from reportlab.lib.pagesizes import A4
 from reportlab.lib.units import mm, inch
 from reportlab.lib.colors import HexColor, black, white
 from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
 from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
 from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
 from reportlab.pdfbase import pdfmetrics
 from reportlab.pdfbase.ttfonts import TTFont

import os

# Colors
PRIMARY_COLOR = HexColor('#1a3a5c')  # Dark blue
ACCENT_COLOR = HexColor('#2c5aa0')  # Medium blue
LIGHT_GRAY = HexColor('#f5f5f5')
DARK_GRAY = HexColor('#333333')

# Page setup
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 15 * mm

 def create_styles():
    styles = getSampleStyleSheet()
    
    # Name style
    styles.add(ParagraphStyle(
        name='ResumeName',
        fontName='Helvetica-Bold',
        fontSize=22,
        textColor=PRIMARY_COLOR,
        alignment=TA_CENTER,
        spaceAfter=2*mm
    ))
    
    # Title style
    styles.add(ParagraphStyle(
        name='ResumeTitle',
        fontName='Helvetica',
        fontSize=11,
        textColor=ACCENT_COLOR,
        alignment=TA_CENTER,
        spaceAfter=3*mm
    ))
    
    # Contact style
    styles.add(ParagraphStyle(
        name='Contact',
        fontName='Helvetica',
        fontSize=9,
        textColor=DARK_GRAY,
        alignment=TA_CENTER,
        spaceAfter=4*mm
    ))
    
    # Section header
    styles.add(ParagraphStyle(
        name='SectionHeader',
        fontName='Helvetica-Bold',
        fontSize=12,
        textColor=PRIMARY_COLOR,
        spaceBefore=4*mm,
        spaceAfter=2*mm,
        borderPadding=2*mm
    ))
    
    # Body text
    styles.add(ParagraphStyle(
        name='BodyText',
        fontName='Helvetica',
        fontSize=9,
        textColor=DARK_GRAY,
        alignment=TA_JUSTIFY,
        spaceAfter=2*mm,
        leading=12
    ))
    
    # Bullet style
    styles.add(ParagraphStyle(
        name='Bullet',
        fontName='Helvetica',
        fontSize=9,
        textColor=DARK_GRAY,
        leftIndent=5*mm,
        spaceAfter=1.5*mm,
        leading=11
    ))
    
    # Small text
    styles.add(ParagraphStyle(
        name='Small',
        fontName='Helvetica',
        fontSize=8,
        textColor=DARK_GRAY,
        alignment=TA_LEFT,
        leading=10
    ))
    
    # Project title
    styles.add(ParagraphStyle(
        name='ProjectTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        textColor=PRIMARY_COLOR,
        spaceAfter=1*mm
    ))
    
    return styles

def add_header_footer(canvas, doc):
    canvas.saveState()
    # Top accent line
    canvas.setStrokeColor(ACCENT_COLOR)
    canvas.setLineWidth(2)
    canvas.line(MARGIN, PAGE_HEIGHT - 10*mm, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 10*mm)
    # Bottom line
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 10*mm, PAGE_WIDTH - MARGIN, 10*mm)
    canvas.restoreState()

def build_resume():
    output_path = '/home/workdir/artifacts/Balaji_Rajput_Professional_Resume.pdf'
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=15*mm,
        bottomMargin=15*mm
    )
    
    styles = create_styles()
    story = []
    
    # === HEADER ===
    story.append(Paragraph('Balaji Dilipsingh Rajput', styles['ResumeName']))
    story.append(Paragraph('QA Officer | IPQA Officer | Pharmaceutical Quality Assurance', styles['ResumeTitle']))
    contact = 'Vadodara, Gujarat 390010, India | +91 8780861044 | balajirajput966@gmail.com<br/>LinkedIn: linkedin.com/in/balaji-rajput-483a86194 | GitHub: github.com/balajirajput96'
    story.append(Paragraph(contact, styles['Contact']))
    
    # Accent line
    story.append(HRFlowable(width='100%', thickness=1.5, color=ACCENT_COLOR, spaceAfter=4*mm))
    
    # === PROFESSIONAL SUMMARY ===
    story.append(Paragraph('PROFESSIONAL SUMMARY', styles['SectionHeader']))
    summary = '''Results-driven QA professional with 2+ years of hands-on experience in pharmaceutical Quality Assurance at Elysium Pharmaceuticals Ltd., Vadodara. Proven expertise in GMP &amp; GDP compliance, SOP writing, CAPA implementation, deviation management, BMR/BPR review, change control, OOS investigation, and QMS documentation. Strong academic foundation in Biotechnology (Diploma, GTU) with laboratory proficiency in HPLC, PCR, and microbiology. Achieved zero critical observations during regulatory inspections. Immediately available for QA Executive, Documentation Officer, or Regulatory Affairs roles across the Gujarat pharmaceutical sector.'''
    story.append(Paragraph(summary, styles['BodyText']))
    
    # === CORE COMPETENCIES ===
    story.append(Paragraph('CORE COMPETENCIES', styles['SectionHeader']))
    
    competencies_left = [
        '• GMP, GDP &amp; GLP Compliance',
        '• SOP Writing &amp; Periodic Review',
        '• Change Control Management',
        '• Internal GMP Audits &amp; Self-Inspection',
        '• Vendor Qualification &amp; Supplier Audit',
        '• HPLC, PCR &amp; Spectrophotometry',
    ]
    competencies_right = [
        '• CAPA &amp; Deviation Management',
        '• BMR / BPR Review &amp; Approval',
        '• OOS &amp; OOT Investigation',
        '• QMS Documentation &amp; Control',
        '• CDSCO / WHO-GMP / FDA Compliance',
        '• Stability Studies &amp; APQR',
    ]
    
    comp_data = []
    for i in range(len(competencies_left)):
        comp_data.append([
            Paragraph(competencies_left[i], styles['Small']),
            Paragraph(competencies_right[i], styles['Small'])
        ])
    
    comp_table = Table(comp_data, colWidths=[90*mm, 90*mm])
    comp_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3*mm),
        ('TOPPADDING', (0, 0), (-1, -1), 0.5*mm),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5*mm),
    ]))
    story.append(comp_table)
    story.append(Spacer(1, 3*mm))
    
    # === PROFESSIONAL EXPERIENCE ===
    story.append(Paragraph('PROFESSIONAL EXPERIENCE', styles['SectionHeader']))
    story.append(Paragraph('<b>QA Officer / IPQA Officer</b> | Elysium Pharmaceuticals Ltd., Dabhasa, Vadodara, Gujarat | <i>Mar 2024 – Mar 2026</i>', styles['Small']))
    story.append(Paragraph('Production / Quality Assurance Department | Employee Code: 16836', styles['Small']))
    story.append(Spacer(1, 1*mm))
    
    exp_bullets = [
        'Conducted rigorous in-process quality checks during tablet compression per BMR, SOP, and cGMP requirements, maintaining <b>100% GMP compliance</b> across all production batches.',
        'Reviewed and approved <b>50+ BMRs and BPRs monthly</b> alongside reconciliation records and logbooks, ensuring complete GDP compliance and reducing documentation discrepancies by 15%.',
        'Identified, documented, and escalated deviations; executed root-cause analysis and tracked CAPA closure within stipulated timelines, achieving timely regulatory compliance.',
        'Authored and revised <b>15+ SOPs</b>, contributing to a <b>20% improvement in operational efficiency</b> and process standardisation.',
        'Managed initiation, review, and closure for equipment, process, and documentation changes within the QMS framework per regulatory requirements.',
        'Facilitated GMP audits and self-inspections across production, warehouse, and utility areas; tracked 100% corrective-action closure with zero critical findings.',
        'Compiled documentation packages for CDSCO, WHO-GMP, and FDA inspection reviews, <b>achieving zero critical observations</b>.',
        'Coordinated GMP training schedules and maintained records for floor staff, ensuring <b>100% training compliance</b>. Supported OOS/OOT investigations, APQR data compilation, stability programme documentation, and market complaint reports per strict GDP standards.',
    ]
    for bullet in exp_bullets:
        story.append(Paragraph('• ' + bullet, styles['Bullet']))
    
    # === EDUCATION ===
    story.append(Paragraph('EDUCATION', styles['SectionHeader']))
    story.append(Paragraph('<b>Diploma in Biotechnology</b> | Parul Institute of Technology &amp; Engineering, GTU, Vadodara | 2021 – 2025', styles['Small']))
    story.append(Paragraph('CGPA: 6.7/10 | Dean’s List 2024–25 | Best Research Project Award 2024', styles['Small']))
    story.append(Paragraph('Key Subjects: Molecular Biology, Biochemistry, Microbiology, Bioprocess Technology, Immunology, Fermentation Technology', styles['Small']))
    
    # PAGE BREAK
    story.append(PageBreak())
    
    # === RESEARCH PROJECTS ===
    story.append(Paragraph('RESEARCH PROJECTS', styles['SectionHeader']))
    
    projects = [
        ('<b>2024 | Bioethanol Production from Agricultural Waste</b>', '15% yield improvement via RSM/DOE-optimised SSF with S. cerevisiae; validated by HPLC (p &lt; 0.05). <b>Best Research Project – Parul Institute 2024</b>. [Fermentation, RSM, DOE, HPLC, ANOVA, SPSS]'),
        ('<b>2024 | Comparative Genomic Analysis of AMR Genes</b>', 'Analysed 120 bacterial genomes; identified 8 novel AMR gene variants from 500+ sequences; reduced manual curation time by 40% via Python/Biopython automation. [Python, Biopython, BLAST, R, ClustalW]'),
        ('<b>2023 | Protein Structure Prediction &amp; Molecular Docking</b>', 'Modelled 5 therapeutic proteins; docked 50 ligands; identified 3 lead compounds (binding affinity &lt; –8.0 kcal/mol). [SWISS-MODEL, AutoDock Vina, PyMOL, PDB]'),
        ('<b>2023 | Biogenic Synthesis of Silver Nanoparticles (AgNPs)</b>', 'Synthesised AgNPs using Pseudomonas spp.; confirmed antimicrobial efficacy via spectrophotometry and zone-of-inhibition assays. [Microbiology, UV-Vis Spectrophotometry]'),
    ]
    for title, desc in projects:
        story.append(Paragraph(title, styles['ProjectTitle']))
        story.append(Paragraph(desc, styles['Small']))
        story.append(Spacer(1, 1.5*mm))
    
    # === CERTIFICATIONS ===
    story.append(Paragraph('CERTIFICATIONS', styles['SectionHeader']))
    certs_left = [
        '• Bioinformatics Specialization – Coursera / UC San Diego (2024)',
        '• Python for Genomic Data Science – Coursera / JHU (2024)',
        '• Industrial Biotechnology &amp; GMP Fundamentals – NPTEL / IIT Madras (2023)',
        '• Bioinformatics Internship – Biotecnika (2024)',
    ]
    certs_right = [
        '• Molecular Biology Techniques – Udemy (2023)',
        '• Advanced Biotechnology Techniques – Parul University (2025)',
        '• Digital Marketing – Google Digital Garage (2024)',
        '• Web Designing – ITI Vadodara (2021)',
    ]
    cert_data = []
    for i in range(len(certs_left)):
        cert_data.append([
            Paragraph(certs_left[i], styles['Small']),
            Paragraph(certs_right[i], styles['Small'])
        ])
    cert_table = Table(cert_data, colWidths=[90*mm, 90*mm])
    cert_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0.5*mm),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5*mm),
    ]))
    story.append(cert_table)
    story.append(Spacer(1, 3*mm))
    
    # === KEY ACHIEVEMENTS ===
    story.append(Paragraph('KEY ACHIEVEMENTS', styles['SectionHeader']))
    achievements = [
        '• <b>100% GMP &amp; GDP compliance</b> maintained across all batch records throughout 2-year tenure; <b>zero critical observations</b> during regulatory inspection preparedness.',
        '• Authored <b>15+ SOPs</b> driving <b>20% efficiency improvement</b>; Best Research Project Award – Parul Institute 2024 for RSM-optimised bioethanol production.',
        '• <b>8 novel AMR gene variants</b> identified; <b>40% reduction</b> in bioinformatics curation time; Dean’s List for Academic Excellence 2024–2025.',
    ]
    for ach in achievements:
        story.append(Paragraph(ach, styles['Bullet']))
    
    # === TECHNICAL SKILLS ===
    story.append(Paragraph('TECHNICAL SKILLS', styles['SectionHeader']))
    
    skills = [
        ('<b>QA / Regulatory:</b>', 'GMP, GDP, GLP, SOP, CAPA, BMR/BPR, Change Control, OOS/OOT, QMS, 21 CFR, ICH, CDSCO, WHO-GMP'),
        ('<b>Laboratory:</b>', 'PCR, RT-PCR, HPLC, Spectrophotometry, Gel Electrophoresis, Microbial Culture, Sterility Testing, MLT'),
        ('<b>Bioinformatics:</b>', 'Python (Biopython, Pandas, NumPy), R (Bioconductor), BLAST, ClustalW, AutoDock Vina, SWISS-MODEL, PyMOL'),
        ('<b>Software:</b>', 'MS Office (Advanced), SAP (Basics), TrackWise QMS, SPSS, MATLAB'),
    ]
    for label, content in skills:
        story.append(Paragraph(f'{label} {content}', styles['Small']))
        story.append(Spacer(1, 1*mm))
    
    # === PERSONAL DETAILS ===
    story.append(Paragraph('PERSONAL DETAILS &amp; DECLARATION', styles['SectionHeader']))
    personal = 'D.O.B.: 20 June 2001 | Marital Status: Single | Languages: English, Hindi (Fluent), Gujarati (Native) | Availability: Immediate'
    story.append(Paragraph(personal, styles['Small']))
    story.append(Spacer(1, 2*mm))
    declaration = 'I hereby declare that all information furnished above is true and accurate to the best of my knowledge.'
    story.append(Paragraph(declaration, styles['Small']))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph('<b>Balaji Dilipsingh Rajput</b>', styles['Small']))
    
    # Build PDF
    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f'Resume generated successfully: {output_path}')
    return output_path

if __name__ == '__main__':
    build_resume()
