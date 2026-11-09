#!/usr/bin/env python3
"""
Dedicated Standalone Generator for:
Balaji Dilipsingh Rajput — Tata Starbucks Assistant Store Manager (Fresher) ATS Resume

Generates a pixel-perfect, ATS-compliant, strictly 2-page PDF resume tailored
specifically for Tata Starbucks Private Limited (Vadodara) using ReportLab.
"""

from pathlib import Path
from generate_resume import build_resume

def main() -> None:
    output_pdf = Path(__file__).resolve().parent / "artifacts" / "Balaji_Rajput_Tata_Starbucks_ASM_Resume.pdf"
    res_path = build_resume(output_path=str(output_pdf), profile="starbucks")
    print(f"Successfully generated Tata Starbucks ASM Resume: {res_path}")

if __name__ == "__main__":
    main()
