import random


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


class Player:
    def __init__(self, name, max_hp, attack_stat, defense_stat):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        self._attack_stat = attack_stat
        self._defense_stat = defense_stat
        self._items = []  # Store Item objects
        self._cooldowns = {"Power Strike": 0, "Healing Aura": 0, "Crippling Blow": 0}
        self._defend_mode = False

    def get_name(self):
        return self._name

    def get_health(self):
        return self._hp

    def add_item(self, item):
        """Add an Item object to the inventory."""
        self._items.append(item)
        print(f"{item} added to {self._name}'s inventory.")

    def use_item(self, item_name):
        """Use an item from the player's inventory."""
        for item in self._items:
            if item.name.lower() == item_name.lower():
                if item.name.lower() == "healing potion":
                    self._hp = min(self._max_hp, self._hp + 200)
                    self._items.remove(item)
                    print(f"{self._name} used {item}! HP is now {self._hp}.")
                return True
        print(f"{self._name} doesn't have {item_name}!")
        return False

    def attack(self):
        """Basic attack damage."""
        return random.randint(self._attack_stat - 5, self._attack_stat + 5)

    def special_attack(self, ability_name):
        """Perform a special attack if off cooldown."""
        if self._cooldowns[ability_name] == 0:
            if ability_name == "Power Strike":
                self._cooldowns["Power Strike"] = 3
                return self._attack_stat * 2
            elif ability_name == "Healing Aura":
                self._cooldowns["Healing Aura"] = 5
                self._hp = min(self._max_hp, self._hp + 100)
                print(f"{self._name} healed for 100 HP! Current HP: {self._hp}.")
                return None
            elif ability_name == "Crippling Blow":
                self._cooldowns["Crippling Blow"] = 4
                return self._attack_stat * 1.5
        else:
            print(f"{ability_name} is on cooldown for {self._cooldowns[ability_name]} more turns.")
            return None

    def reduce_cooldowns(self):
        """Reduce all cooldowns by 1."""
        for ability in self._cooldowns:
            if self._cooldowns[ability] > 0:
                self._cooldowns[ability] -= 1

    def is_alive(self):
        return self._hp > 0


class Enemy:
    def __init__(self, name, hp, attack_stat):
        self._name = name
        self._hp = hp
        self._attack_stat = attack_stat

    def is_alive(self):
        return self._hp > 0

    def attack(self):
        return random.randint(self._attack_stat - 5, self._attack_stat + 5)

    def receives_damage(self, damage):
        self._hp -= max(1, damage)
        print(f"{self._name} takes {damage} damage! Remaining HP: {self._hp}")


class Combat:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def player_turn(self):
        """Handle the player's turn."""
        if self._player._defend_mode:
            print(f"{self._player.get_name()} is no longer defending.")
        self._player._defend_mode = False

        print(f"\n{self._player.get_name()} - HP: {self._player._hp}/{self._player._max_hp}")
        print(f"{self._enemy._name} - HP: {self._enemy._hp}")

        action = input("Choose an action (Attack, Defend, Special, Item): ").strip().lower()
        if action == "attack":
            damage = self._player.attack()
            print(f"{self._player.get_name()} attacks for {damage} damage!")
            self._enemy.receives_damage(damage)
        elif action == "defend":
            self._player._defend_mode = True
            print(f"{self._player.get_name()} is defending!")
        elif action == "special":
            ability = input("Choose a special ability (Power Strike, Healing Aura, Crippling Blow): ").title()
            damage = self._player.special_attack(ability)
            if damage:
                self._enemy.receives_damage(damage)
        elif action == "item":
            item_name = input("Enter the item name: ").strip()
            self._player.use_item(item_name)

        self._player.reduce_cooldowns()

    def enemy_turn(self):
        """Handle the enemy's turn."""
        if self._enemy.is_alive():
            damage = self._enemy.attack()
            if self._player._defend_mode:
                damage = max(1, damage // 2)  # Halve damage while defending
            self._player._hp -= damage
            print(f"{self._enemy._name} attacks for {damage} damage! Remaining HP: {self._player.get_health()}")

    def engage_in_battle(self):
        """Run the battle until one side wins."""
        while self._player.is_alive() and self._enemy.is_alive():
            self.player_turn()
            if self._enemy.is_alive():
                self.enemy_turn()

        if not self._player.is_alive():
            print(f"{self._player.get_name()} has been defeated.")
        else:
            print(f"The {self._enemy._name} has been defeated!")

            

    def print_turn_summary(player, enemy):
        """Displays the current status of the player, their abilities, and the enemy."""
        print("\n=== Turn Summary ===")
        print(f"{player.get_name()} - HP: {player.get_health()}/{player._max_hp}")
        print("Abilities:")
        for ability_name, cooldown in player._cooldowns.items():
            status = f"Ready" if cooldown == 0 else f"On Cooldown ({cooldown} turns)"
            print(f"  {ability_name}: {status}")
        print("\nEnemy:")
        print(f"{enemy._name} - HP: {enemy._hp}")
        print("====================\n")

# Example Usage
player = Player(name="Hero", max_hp=100, attack_stat=20, defense_stat=10)
player.add_item(Item("Healing Potion", "Restores 200 HP."))
enemy = Enemy(name="Goblin", hp=50, attack_stat=15)
combat = Combat(player, enemy)

combat.engage_in_battle()
