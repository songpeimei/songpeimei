### 点球大战 ###
import random
import os
attack = '请输入进攻方向1：东，2：南，3：西，4：北'
defend = '请输入防守方向1：东，2：南，3：西，4：北'
score_player = 0
score_computer = 0
while True:
    if_begin = input('输入1 开始游戏,输入2 查看规则,输入3退出 \n')
    if if_begin == '2':
        os.system('cls')
        print('游戏规则：玩家首先输入进攻方向，电脑随机防守，方向一致则为进攻失败，反之则为进攻成功，玩家输入防守方向，电脑随机进攻，每方各五次机会。按任意键继续')
        input()
        continue
    elif if_begin == '1':
        os.system('cls')
        for times in range(1,12):
            if times == 11:
                print('游戏结束 \n：玩家得分 %d,电脑得分 %d \n 按任意键结束' % (score_player,score_computer))
                input()
                break
            if times in(1,3,5,7,9):
                b = random.randint(1,5)
                attack_player = int(input('玩家第%s 次进攻, %s \n ' % (((times+1)/2),attack)))
                print("玩家进攻方向 %s,电脑防守方向 %s"  % (attack_player,b))
                if b != attack_player:
                    score_player += 1
                    print("进攻成功，玩家得分+1\n\n")
                else:
                    print('进攻失败，玩家不得分\n\n')
            else:
                a = random.randint(1,5)
                defend_player = int(input('电脑第%s 次进攻, %s \n ' % (((times) / 2), defend)))
                print('玩家防守方向%s ,电脑进攻方向 %s' %(defend_player,a))
                if a != defend_player:
                    score_computer += 1
                    print("防守失败，电脑得分+1\n\n")
                else:
                    print('防守成功，电脑不得分\n\n')
    elif if_begin == '3':
        break
    else:
        print('输入错误，即将退出')
        break
