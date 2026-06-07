import matplotlib.pyplot as plt


def generate_chart(
    high,
    medium,
    low
):

    labels = [
        "High",
        "Medium",
        "Low"
    ]

    values = [
        high,
        medium,
        low
    ]

    plt.figure()

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title(
        "Vulnerability Distribution"
    )

    plt.savefig(
        "reports/chart.png"
    )