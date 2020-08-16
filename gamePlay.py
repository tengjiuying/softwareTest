"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""
def fight():
    #定义四个变量，存放你和我的血量以及攻击力
    my_hp = 1000
    my_power = 100
    your_hp = 1000
    your_power = 90
    #一轮对打过后，我的血量和敌人的血量
    while True:
        my_hp_final = my_hp - your_power
        your_hp_final = your_hp - my_power
        if my_hp_final > your_hp_final:
            print("I win!")
        elif my_hp_final < your_hp_final:
            print("You win!")
        else:
            print("no peace,keep fighting for the last time!")

#调用fight函数
fight()
