from flask import Flask, render_template, request
from database import save_scan, init_db
from network_scanner import scan_network
from web_scanner import scan_website
from risk_engine import calculate_risk
from report_generator import (
    generate_pdf_report,
    generate_txt_report
)
from flask import send_file

app = Flask(__name__)
init_db()
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/download")
def download():
    return send_file(
        "reports/report.pdf",
        as_attachment=True
    )

@app.route("/scan", methods=["POST"])
def scan():

    ip = request.form["ip"]
    url = request.form["url"]

    ports, network_findings = scan_network(ip)

    web_findings = scan_website(url)

    findings = network_findings + web_findings

    risk_data = calculate_risk(findings)

    risk = risk_data["risk_level"]

    generate_txt_report(
        ip,
        ports,
        findings,
        risk
    )

    generate_pdf_report(
        ip,
        ports,
        findings,
        risk
    )

    save_scan(ip, risk)

    return render_template(
    "index.html",
    findings=findings,
    risk=risk,
    ports=ports,
    scan_complete=True
)


if __name__ == "__main__":
    app.run(debug=True)