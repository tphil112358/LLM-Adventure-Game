class Player:
    def __init__(self, name):
        self._name = name
        self._hp = 1000
        self._max_hp = 1000
        self._attack_stat = 100
        self._items = []
        self._statuses = [False, False]  # Burn, Frozen

    def get_name(self):
        return self._name

    def get_health_factor(self):
        return max(0, self._hp // (self._max_hp // 50))

    def is_alive(self):
        return self._hp >= 1

    def receives_damage(self, damage):
        self._hp -= max(1, damage)

    def deals_damage(self):
        return self._attack_stat

    def add_item(self, item):
        self._items.append(item)

# Enemy class
class Enemy:
    def __init__(self, name, max_hp):
        self._name = name
        self._hp = max_hp

    def is_alive(self):
        return self._hp > 0

    def attack(self):
        return random.randint(10, 50)

    def receives_damage(self, damage):
        self._hp -= damage

class Combat:
    def __init__(self, player):
        self._player = player
        self._enemy = None

    def spawn_enemy(self):
        self._enemy = Enemy("Goblin", 300)

    def battle_is_active(self):
        return self._player.is_alive() and self._enemy.is_alive()

    def engage_in_battle(self):
        while self.battle_is_active():
            self.player_turn()
            if self._enemy.is_alive():
                self.enemy_turn()

    def player_turn(self):
        damage = self._player.deals_damage()
        self._enemy.receives_damage(damage)
        print(f"You dealt {damage} damage to the {self._enemy._name}!")
        
        # Ask Ollama for a reaction to the player's action
        player_action_reaction = ollama_chat(
            f"Generate a reaction from the {self._enemy._name} after {self._player.get_name()} dealt {damage} damage."
        )
        print(f"Enemy reacts: {player_action_reaction}")
        time.sleep(1)

    def enemy_turn(self):
        damage = self._enemy.attack()
        self._player.receives_damage(damage)
        print(f"The {self._enemy._name} dealt {damage} damage to you!")
        
        # Ask Ollama for a taunt or threat from the enemy
        enemy_attack_reaction = ollama_chat(
            f"Generate a taunt or threat from {self._enemy._name} after attacking {self._player.get_name()}."
        )
        print(f"Enemy says: {enemy_attack_reaction}")
        time.sleep(1)