import random
import sys

# 定数
DEFAULT_MAX_ATTEMPTS = 10
SEPARATOR = "-----------------------------"

def write_output(message, stream=sys.stdout):
    stream.write(message + "\n")
    stream.flush()

def input_number(prompt, error_message):
    while True:
        write_output(prompt)

        try:
            return int(sys.stdin.readline().strip())
        except ValueError:
            write_output(error_message)

def input_two_number():
    while True:
        n = input_number("- 最小数を入力してください: ", "数字を入力してください.終了するには、Ctl + cを押してください")
        m = input_number("- 最大数を入力してください: ", "数字を入力してください.終了するには、Ctl + cを押してください")

        if n <= m:
            return n, m
        write_output("最小数 > 最大数のため再度数字を入力してください\n", sys.stderr)

def generate_random_int(n, m):
    return random.randint(n, m)

def get_max_attempts():
    try:
        write_output("ゲームの試行回数を決定してください (default: 10回): ")
        return int(sys.stdin.readline().strip())
    except ValueError:
        write_output(f"数字が入力されなかったため、defaultの{DEFAULT_MAX_ATTEMPTS}回で行います", sys.stderr)
        return DEFAULT_MAX_ATTEMPTS

def play_guess_game():
    write_output("これから乱数あてゲームを開始します")
    write_output("乱数の生成範囲を決定してください")
    write_output(SEPARATOR)

    n, m = input_two_number()
    write_output(f"{n} <= 乱数 <= {m} の範囲で生成します")

    random_int = generate_random_int(n, m)
    write_output(SEPARATOR)

    max_attempts = get_max_attempts()
    write_output(SEPARATOR)
    write_output(f"{max_attempts}回以内に、{n} <= 乱数 <= {m}となる乱数を当ててください")

    for attempt in range(max_attempts):
        write_output(f"- 残り{max_attempts - attempt}回")

        guess = input_number("生成された乱数は?: ", "数字を入力してください *先ほどの入力は試行回数はカウントしません*")

        if guess == random_int:
            write_output("正解です! おめでとうございます888888")
            return
        write_output("もっと大きい数字です" if guess < random_int else "もっと小さい数字です")
    write_output("残念! 正解できず。また挑戦してください")

if __name__ == "__main__":
    try:
        play_guess_game()
    except KeyboardInterrupt:
        write_output("\nゲームが中断されました。また遊んでください", sys.stderr)
        sys.exit(1)