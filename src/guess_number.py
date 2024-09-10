import random
import sys

def input_number(prompt, error_message):
    while True:
        sys.stdout.write(prompt)
        sys.stdout.flush()

        try:
            return int(sys.stdin.readline().strip())
        except ValueError:
            sys.stderr.write(error_message + "\n")
            sys.stderr.flush()

def input_two_number():
    while True:
        n = input_number("- 最小数を入力してください: ", "数字を入力してください.終了するには、Ctl + cを押してください")
        m = input_number("- 最大数を入力してください: ", "数字を入力してください.終了するには、Ctl + cを押してください")

        if n <= m:
            return n, m
        else:
            sys.stdout.write("最小数 > 最大数のため再度数字を入力してください\n")
            sys.stdout.flush()

def generate_random_int(n, m):
    return random.randint(n, m)

def get_max_attempts():
    try:
        sys.stdout.write("ゲームの試行回数を決定してください (default: 10回): ")
        sys.stdout.flush()
        return int(sys.stdin.readline().strip())
    except ValueError:
        sys.stderr.write("数字が入力されなかったため、defaultの10回で行います\n")
        return 10

def play_guess_game():
    sys.stdout.write("これから乱数あてゲームを開始します\n")
    sys.stdout.flush()
    sys.stdout.write("乱数の生成範囲を決定してください\n")
    sys.stdout.flush()
    sys.stdout.write("----------------------------------\n")
    sys.stdout.flush()
    n, m = input_two_number()
    sys.stdout.write(f"{n} <= 乱数 <= {m} の範囲で生成します\n")
    sys.stdout.flush()

    random_int = generate_random_int(n, m)
    sys.stdout.write("----------------------------------\n")
    sys.stdout.flush()

    max_attempts = get_max_attempts()
    sys.stdout.write("----------------------------------\n")
    sys.stdout.flush()
    sys.stdout.write(f"{max_attempts}回以内に、{n} <= 乱数 <= {m}となる乱数を当ててください\n")
    sys.stdout.flush()

    for attempt in range(max_attempts):
        sys.stdout.write(f"- 残り{max_attempts - attempt}回\n")
        sys.stdout.flush()

        guess = input_number("生成された乱数は?: ", "数字を入力してください *先ほどの入力は試行回数はカウントしません*")

        if guess == random_int:
            sys.stdout.write("正解です! おめでとうございます888888\n")
            sys.stdout.flush()
            return
        sys.stdout.write("もっと大きい数字です\n" if guess < random_int else "もっと小さい数字です\n")
        sys.stdout.flush()
    sys.stdout.write("残念! 正解できず。また挑戦してください\n")
    sys.stdout.flush()

if __name__ == "__main__":
    play_guess_game()