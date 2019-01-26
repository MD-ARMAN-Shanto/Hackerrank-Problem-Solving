class Enemy:
    life = 3

    def attack(self):
        print("OUCH")
        self.life -= 1

    while True:
        try:
            def remain_life(self):
                if self.life <= 0:
                    print("I am dead")
                else:
                    print(str(self.life) + " life left ")
            break
        except ZeroDivisionError:
            break


enemy1 = Enemy()
enemy2 = Enemy()
enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy2.attack()
enemy2.attack()
enemy2.attack()
enemy1.remain_life()
enemy2.remain_life()
