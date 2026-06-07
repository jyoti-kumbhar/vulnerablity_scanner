SEVERITY_RULES = {
    "FTP": "Medium",
    "Telnet": "High",
    "SMB": "High",
    "HTTPS": "High",
    "Content-Security-Policy": "Medium",
    "Strict-Transport-Security": "Medium",
    "X-Frame-Options": "Low",
    "X-Content-Type-Options": "Low"
}


def calculate_risk(findings):

    high = 0
    medium = 0
    low = 0

    detailed_findings = []

    for finding in findings:

        severity = "Low"

        for keyword, level in SEVERITY_RULES.items():

            if keyword.lower() in finding.lower():

                severity = level
                break

        if severity == "High":
            high += 1

        elif severity == "Medium":
            medium += 1

        else:
            low += 1

        detailed_findings.append({
            "finding": finding,
            "severity": severity
        })

    score = high * 3 + medium * 2 + low

    if high >= 2:
        score = "High"

    elif high >= 1 or medium >= 4:
        score = "Medium"

    else:
        score = "Low"

    return {
        "risk_level": score,
        "high": high,
        "medium": medium,
        "low": low,
        "findings": detailed_findings
    }