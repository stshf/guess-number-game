import random
def input_number(prompt, error_message):
    try:
        return int(input(prompt))
    except ValueError:
        print(error_message)
def input_two_number():
    while True:
        n = input_number("- 最小数を入力してください: ", "数字を入力してください.終了するには、Ctl + cを押してください")
        m = input_number("- 最大数を入力してください: ", "数字を入力してください.終了するには、Ctl + cを押してください")

        if n <= m:
            return n, m
        else:
            print("最小数 > 最大数のため再度数字を入力してください")

def generate_random_int(n, m):
    return random.randint(n, m)

def get_max_attempts():
    try:
        return int(input("ゲームの試行回数を決定してください (default: 10回): "))
    except ValueError:
        print("数字が入力されなかったため、defaultの10回で行います")
        return 10

def play_guess_game():
    print("これから乱数あてゲームを開始します")
    print("乱数の生成範囲を決定してください")
    print("----------------------------------")
    n, m = input_two_number()
    print(f"{n} <= 乱数 <= {m} の範囲で生成します")

    random_int = generate_random_int(n, m)
    print("----------------------------------")

    max_attempts = get_max_attempts()
    print("----------------------------------")
    print(f"{max_attempts}回以内に、{n} <= 乱数 <= {m}となる乱数を当ててください")

    for attempt in range(max_attempts):
        print(f"- 残り{max_attempts - attempt}回")

        guess = input_number("生成された乱数は?: ", "数字を入力してください *先ほどの入力は試行回数はカウントしません*")

        if guess == random_int:
            print("正解です! おめでとうございます888888")
            return
        print("もっと大きい数字です" if guess < random_int else "もっと小さい数字です")

    print("残念! 正解できず。また挑戦してください")


if __name__ == "__main__":
    play_guess_game()