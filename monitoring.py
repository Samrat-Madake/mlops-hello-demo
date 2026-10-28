
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset


def main():
    reference_data = pd.DataFrame({
        "age": [22, 24, 25, 27, 29, 30, 32, 35, 28, 26],
        "income": [25000, 28000, 30000, 32000, 35000,
                   36000, 40000, 45000, 33000, 31000],
    })

    current_data = pd.DataFrame({
        "age": [22, 24, 40, 42, 45, 37, 39, 43, 41, 44],
        "income": [25000, 28000, 50000, 55000, 60000,
                   52000, 49000, 58000, 53000, 57000],
    })

    report = Report([DataDriftPreset()])
    snapshot = report.run(
        reference_data=reference_data,
        current_data=current_data,
    )

    snapshot.save_html("drift_report.html")
    print("Evidently report generated: drift_report.html")


if __name__ == "__main__":
    main()
