# 可直接在windows终端运行
import random
import os

attack_directions = ['东', '南', '西', '北']
rule_game = '游戏规则: 玩家首先输入进攻方向，电脑随机防守，方向一致则为进攻失败，反之则为进攻成功。玩家输入防守方向，电脑随机进攻，每方各五次机会。按任意键继续'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt, valid_range=None):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            val = int(user_input)
            if not valid_range or val in valid_range:
                return val
        print("输入错误，请输入正确的数字。")

def penalty_shootout():
    score_player, score_computer = 0, 0
    clear_screen()
    print(rule_game)
    input('按任意键开始游戏')

    for i in range(5):
        # Player attack
        b = random.choice(attack_directions)
        attack_player = get_user_input(f'玩家第{i+1}次进攻，1:东, 2:南, 3:西, 4:北\n', valid_range=range(1, 5))
        print(f'玩家进攻方向 {attack_directions[attack_player - 1]}，电脑防守方向 {b}')
        if attack_directions[attack_player - 1] != b:
            score_player += 1
            print('进攻成功，玩家得分+1\n')
        else:
            print('进攻失败，玩家不得分\n')

        # Computer attack
        a = random.choice(attack_directions)
        defend_player = get_user_input(f'电脑第{i+1}次进攻，1:东, 2:南, 3:西, 4:北\n', valid_range=range(1, 5))
        print(f'玩家防守方向 {attack_directions[defend_player - 1]}，电脑进攻方向 {a}')
        if attack_directions[defend_player - 1] != a:
            score_computer += 1
            print('防守失败，电脑得分+1\n')
        else:
            print('防守成功，电脑不得分\n')

    print(f'游戏结束：玩家得分 {score_player}，电脑得分 {score_computer}')
    if score_player > score_computer:
        print('恭喜你获胜！')
    elif score_player < score_computer:
        print('很遗憾，电脑获胜。')
    else:
        print('平局啦！')
    input('按任意键结束')

if __name__ == "__main__":
    while True:
        print("1. 开始游戏\n2. 查看规则\n3. 退出")
        option = get_user_input("请选择：", valid_range=range(1, 4))
        if option == 1:
            penalty_shootout()
        elif option == 2:
            clear_screen()
            print(rule_game)
            input('按任意键返回')
        else:
            print('感谢游玩！')
            break
