from web_scanner import scan_website
from database import save_scan
from risk_engine import calculate_risk
from report_generator import (
    generate_txt_report,
    generate_pdf_report
)

print("=" * 50)
print("WEB APPLICATION VULNERABILITY SCANNER")
print("=" * 50)

target_url = input(
    "\nEnter Website URL: "
)

findings = scan_website(
    target_url
)

risk_data = calculate_risk(
    findings
)

risk = risk_data["risk_level"]

generate_txt_report(
    target_url,
    findings,
    risk
)

generate_pdf_report(
    target_url,
    findings,
    risk
)

save_scan(
    target_url,
    risk
)

print("\n✅ Scan Completed!")
print(f"Risk Level: {risk}")
print("Reports saved in reports folder.")