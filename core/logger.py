import csv
import os
from datetime import datetime


class ActionLogger:
    def __init__(self, log_file: str):
        self.log_file = log_file

        # Ensure file exists with headers
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "timestamp",
                    "prompt",
                    "role",
                    "name",
                    "phone",
                    "status",
                    "details"
                ])

    def log(self, data: dict):
        with open(self.log_file, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                data.get("prompt"),
                data.get("role"),
                data.get("name"),
                data.get("phone"),
                data.get("status"),
                data.get("details")
            ])
