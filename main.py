from generator.password_generator import generate_passwords
from generator.writer import write_passwords_to_csv
from config import NB_PASSWORDS, CSV_PATH
from utils.timer import measure_time

@measure_time
def main():
    passwords = generate_passwords(NB_PASSWORDS)
    write_passwords_to_csv(passwords, CSV_PATH)

if __name__ == "__main__":
    main()