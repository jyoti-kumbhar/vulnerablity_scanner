from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime
import os


def generate_txt_report(
    target,
    ports,
    findings,
    risk_level
):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    with open(
        "reports/report.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "VULNERABILITY SCAN REPORT\n"
        )

        f.write(
            "=" * 50 + "\n\n"
        )

        f.write(
            f"Target: {target}\n"
        )

        f.write(
            f"Date: {datetime.now()}\n\n"
        )

        f.write("OPEN PORTS\n")

        for port in ports:

            f.write(
                f"{port['port']} - {port['service']} - {port['version']}\n"
            )

        f.write(
            "\nFINDINGS\n"
        )

        for item in findings:

            f.write(
                f"- {item}\n"
            )

        f.write(
            f"\nRisk Level: {risk_level}"
        )


def generate_pdf_report(
    target,
    ports,
    findings,
    risk_level
):

    pdf = SimpleDocTemplate(
        "reports/report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Vulnerability Scan Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Target: {target}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Date: {datetime.now()}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Open Ports",
            styles["Heading2"]
        )
    )

    for port in ports:

        content.append(
            Paragraph(
                f"{port['port']} - {port['service']} - {port['version']}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Findings",
            styles["Heading2"]
        )
    )

    for item in findings:

        content.append(
            Paragraph(
                item,
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Risk Level: {risk_level}",
            styles["Heading1"]
        )
    )

    pdf.build(content)