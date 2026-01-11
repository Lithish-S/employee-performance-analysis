import csv

FILE_NAME = "employee_data.csv"

def load_employee_data():
    data = []
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def average_score(data):
    total = sum(float(row["Score"]) for row in data)
    return total / len(data)

def performance_summary(data):
    summary = {"High": 0, "Medium": 0, "Low": 0}
    for row in data:
        score = float(row["Score"])
        if score >= 80:
            summary["High"] += 1
        elif score >= 50:
            summary["Medium"] += 1
        else:
            summary["Low"] += 1
    return summary

def main():
    data = load_employee_data()

    print("Average Performance Score:", round(average_score(data), 2))

    summary = performance_summary(data)
    print("\nPerformance Distribution:")
    for level, count in summary.items():
        print(level, ":", count)

main()
