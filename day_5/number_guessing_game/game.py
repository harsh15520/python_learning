import random
def get_settings_for_difficulty(difficulty: str) -> tuple[int, int, int]:
    # returns (min_value, max_value, closeness_threshold)
    difficulty = difficulty.lower().strip()
    if difficulty == 'easy':
        return (0, 50, 10)
    if difficulty == 'medium':
        return (0, 50, 5)
    if difficulty == 'hard':
        return (0, 50, 2)
    raise ValueError('Invalid difficulty')


def play_round(min_value: int, max_value: int, close_threshold: int, attempts_remaining: int) -> tuple[int, bool]:
    # returns (attempts_remaining_after_round, won_this_round)
    target_number = random.randint(min_value, max_value)
    while attempts_remaining > 0:
        raw = input(f'Guess a number between {min_value} and {max_value} (attempts left {attempts_remaining}, or Q to quit round): ').strip()
        if raw.lower() == 'q':
            return attempts_remaining, False
        if not raw.isdigit():
            print('Please enter a valid integer.')
            continue
        guess = int(raw)

        if guess == target_number:
            print('Hurray, you got it!')
            return attempts_remaining, True

        difference = abs(guess - target_number)
        if difference <= close_threshold:
            print('Very close')
        elif guess < target_number:
            print('Very low')
        else:
            print('Very high')

        attempts_remaining -= 1

    print(f'Out of attempts for this round. The number was {target_number}.')
    return attempts_remaining, False


if __name__ == '__main__':
    print('Welcome to Number Guess!')
    total_attempts = 10
    score = 0

    while total_attempts > 0:
        choice = input("Choose difficulty each round (easy, medium, hard) or 'q' to quit: ").strip().lower()
        if choice == 'q':
            break
        try:
            min_value, max_value, close_threshold = get_settings_for_difficulty(choice)
        except ValueError:
            print('Invalid difficulty. Please choose easy, medium, or hard.')
            continue

        total_attempts, won = play_round(min_value, max_value, close_threshold, total_attempts)
        if won:
            score += 1
            print(f'Score: {score} | Attempts left: {total_attempts}')
        else:
            print(f'Score: {score} | Attempts left: {total_attempts}')

    print(f'Game over. Final score: {score}.')
