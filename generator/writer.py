import csv
from os import makedirs
from os.path import dirname

def write_passwords_to_csv(password_generator, filepath):
    makedirs(dirname(filepath), exist_ok=True)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["PASSWORD", "NUM"])
        for password, num in password_generator:
            writer.writerow([password, num])
