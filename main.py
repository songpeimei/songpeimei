import random
import os

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("输入错误，请输入数字。")

def penalty_shootout():
    attack_directions = ['东', '南', '西', '北']
    rule_game = '游戏规则: 玩家首先输入进攻方向，电脑随机防守，方向一致则为进攻失败，反之则为进攻成功。玩家输入防守方向，电脑随机进攻，每方各五次机会。按任意键继续'
    
    score_player = 0
    score_computer = 0

    os.system('cls')
    print(rule_game)
    input('按任意键开始游戏')

    for times in range(1, 11):
        if times % 2 != 0:  # 玩家进攻
            b = random.choice(attack_directions)
            attack_player = get_user_input(f'玩家第{times // 2 + 1}次进攻，1:东, 2:南, 3:西, 4:北\n')
            print(f'玩家进攻方向 {attack_directions[attack_player - 1]}，电脑防守方向 {b}')
            if attack_directions[attack_player - 1] != b:
                score_player += 1
                print('进攻成功，玩家得分+1\n\n')
            else:
                print('进攻失败，玩家不得分\n\n')
        else:  # 电脑进攻
            a = random.choice(attack_directions)
            defend_player = get_user_input(f'电脑第{times // 2}次进攻，1:东, 2:南, 3:西, 4:北\n')
            print(f'玩家防守方向 {attack_directions[defend_player - 1]}，电脑进攻方向 {a}')
            if attack_directions[defend_player - 1] != a:
                score_computer += 1
                print('防守失败，电脑得分+1\n\n')
            else:
                print('防守成功，电脑不得分\n\n')

    print(f'游戏结束：玩家得分 {score_player}，电脑得分 {score_computer}\n按任意键结束')
    input()

if __name__ == "__main__":
    while True:
        init_word = '输入1开始游戏，输入2查看规则，输入3退出\n'
        if_begin = get_user_input(init_word)

        if if_begin == 1:
            penalty_shootout()
        elif if_begin == 2:
            os.system('cls')
            print(rule_game)
            input()
        elif if_begin == 3:
            break
        else:
            print('输入错误，即将退出')
            break
