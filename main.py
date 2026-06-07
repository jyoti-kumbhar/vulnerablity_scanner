from network_scanner import scan_network
from web_scanner import scan_website
from database import save_scan
from risk_engine import calculate_risk
from report_generator import (
    generate_txt_report,
    generate_pdf_report
)

print("=" * 50)
print("Hybrid Vulnerability Scanner")
print("=" * 50)

target_ip = input(
    "\nEnter IP Address: "
)

target_url = input(
    "Enter Website URL: "
)

ports, network_findings = scan_network(
    target_ip
)

web_findings = scan_website(
    target_url
)

all_findings = (
    network_findings +
    web_findings
)

risk_data = calculate_risk(all_findings)

risk = risk_data["risk_level"]

generate_txt_report(
    target_ip,
    ports,
    all_findings,
    risk
)

generate_pdf_report(
    target_ip,
    ports,
    all_findings,
    risk
)
save_scan(
    target_ip,
    risk
)
print("\nScan Completed!")
print(f"Risk Level: {risk}")
print("Reports saved in reports folder.")