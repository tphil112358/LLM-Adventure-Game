class Combat:
    def __init__(self, player):
        self._player = player
        self._enemy = None
        self._dropped_item = None

    def get_enemy(self, score):
        type_selection = random.randint(0, 2)
        if (score + 1) % 5 == 0:
            self._enemy = HeavyBoss(score) if type_selection == 0 else HealerBoss(score)
        else:
            self._enemy = FireEnemy(score) if type_selection == 0 else IceEnemy(score)

    def get_enemy_name(self):
        return self._enemy.get_name()

    def get_dropped_item(self):
        return self._dropped_item.get_name() if self._dropped_item else None

    def battle_is_active(self):
        return self._player.is_alive() and self._enemy.is_alive()

    def engage_in_battle(self):
        while self.battle_is_active():
            self.player_turn()
            if self._enemy.is_alive():
                self.enemy_turn()

        # Handle item drop after battle
        if self._enemy.is_alive() is False:
            self._dropped_item = self._enemy.drop_item()
            if self._dropped_item:
                self._player.get_item(self._dropped_item)

    def player_turn(self):
        damage = self._player.deals_damage()
        self._enemy.receives_damage(damage)

    def enemy_turn(self):
        damage = self._enemy.attack()
        self._player.receives_damage(damage)
