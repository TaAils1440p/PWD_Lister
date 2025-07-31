import random
from config import MIN_LENGTH, MAX_LENGTH, CHARS, SHOW_PROGRESS, PROGRESS_STEP

def generate_passwords(n):
    for i in range(1, n + 1):
        length = random.randint(MIN_LENGTH, MAX_LENGTH)
        password = ''.join(random.choices(CHARS, k=length))
        yield (password, i)

        if SHOW_PROGRESS and i % PROGRESS_STEP == 0:
            print(f"{i} passwords generated...")
