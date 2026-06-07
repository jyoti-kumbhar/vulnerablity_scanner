from flask import Flask, render_template, request, send_file

from database import save_scan, init_db
from web_scanner import scan_website
from risk_engine import calculate_risk
from report_generator import (
    generate_pdf_report,
    generate_txt_report
)

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

    url = request.form["url"]

    findings = scan_website(url)

    risk_data = calculate_risk(findings)

    risk = risk_data["risk_level"]

    generate_txt_report(
        url,
        findings,
        risk
    )

    generate_pdf_report(
        url,
        findings,
        risk
    )

    save_scan(
        url,
        risk
    )

    return render_template(
        "index.html",
        findings=findings,
        risk=risk,
        scan_complete=True
    )


if __name__ == "__main__":
    app.run(debug=True)