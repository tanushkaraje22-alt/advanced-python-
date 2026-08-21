
# Dynamic Report Generator

# Decorator for formatting the report
from pydoc import text


def format_report(func):
    def wrapper(self):
        report = func(self)

        if self.format_type == "uppercase":
            return report.upper()

        elif self.format_type == "lowercase":
            return report.lower()

        elif self.format_type == "title":
            return report.title()

        return report

    return wrapper


class Report:
    # Class variable
    report_count = 0

    def __init__(self, title, content, format_type="normal"):
        self.title = title
        self.content = content
        self.format_type = format_type

        Report.report_count += 1

    # Class method
    @classmethod
    def get_report_count(cls):
        return cls.report_count

    # Magic method
    def __str__(self):
        return f"Report: {self.title}"

    # Magic method
    def __len__(self):
        return len(self.content)

    # Decorator applied to this method
    @format_report
    def generate_report(self):
        return f"{self.title}\n{self.content}"


# Create reports
report1 = Report(
    "Python Report",
    "Python is a powerful programming language.",
    "uppercase"
)

report2 = Report(
    "DSA Report",
    "Data structures and algorithms are important.",
    "title"
)


# Generate reports
print("REPORT 1")
print(report1.generate_report())

print("\nREPORT 2")
print(report2.generate_report())


# Using magic methods
print("\nMagic Method Examples:")
print(report1)
print("Length of report content:", len(report1))


# Using class method
print("\nTotal Reports Created:", Report.get_report_count())


