import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security"
]

COMMON_PATHS = [
    "/admin",
    "/backup",
    "/test",
    "/uploads"
]


def scan_website(url):

    findings = []

    try:

        response = requests.get(
            url,
            timeout=10
        )

        headers = response.headers

        if not url.startswith("https://"):
            findings.append(
                "Website not using HTTPS"
            )

        for header in SECURITY_HEADERS:

            if header not in headers:
                findings.append(
                    f"Missing security header: {header}"
                )

        server = headers.get(
            "Server",
            "Unknown"
        )

        findings.append(
            f"Server: {server}"
        )

        for path in COMMON_PATHS:

            try:

                r = requests.get(
                    url + path,
                    timeout=5
                )

                if r.status_code == 200:

                    findings.append(
                        f"Accessible directory: {path}"
                    )

            except:
                pass

    except Exception as e:

        findings.append(
            f"Website scan error: {e}"
        )

    return findings