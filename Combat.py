import random

def query_ollama(enemy_info):
    data = {
        "query": f"Tell me about this enemy: {enemy_info['name']}, HP: {enemy_info['hp']}, Attack: {enemy_info['attack']}."
    }
    # Add logic to send data to Ollama

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def description(self):
        return self.description


class Player:
    def __init__(self, name, max_hp, attack_stat, defense_stat):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        self._attack_stat = attack_stat
        self._defense_stat = defense_stat
        self._items = []  # This will now store Item objects
        self._cooldowns = {"Power Strike": 0, "Healing Aura": 0, "Crippling Blow": 0}
        self._special_abilities = {"Power Strike": 0, "Healing Aura": 0, "Crippling Blow": 0}
        self._defend_mode = False\
    
    def get_name(self):
        return self._name
    
    def get_health(self):
        return self._hp

    def add_item(self, item):
        """Add an Item object to the inventory."""
        self._items.append(item)
        print(f"{item} added to {self._name}'s inventory.")

    def use_item(self, item_name):
        """Use an item from the player's inventory and apply its effects."""
        if item_name.lower() == "back":
            print("Going back to the previous menu.")
            return False  # Indicate the action was canceled

        if item_name == "Healing Potion":
            if "Healing Potion" in self._items:
                self._hp = min(self._max_hp, self._hp + 200)
                self._items.remove("Healing Potion")
                print(f"{self._name} used a Healing Potion! HP is now {self._hp}.")
                return True  # Indicate the item was successfully used
            else:
                print(f"{self._name} doesn't have a Healing Potion!")
                return False

        print(f"{item_name} is not a valid item or not in your inventory!")
        return False  # Indicate the item was not used



    def is_alive(self):
        """Check if the character is alive."""
        return self._hp > 0


class Enemy:
    def __init__(self, name, hp, attack_stat):
        self._name = name
        self._hp = hp
        self._attack_stat = attack_stat

    def is_alive(self):
        return self._hp > 0

    def attack(self, min_damage=10, max_damage=50):
        return random.randint(min_damage, max_damage)

    def receives_damage(self, damage):
        self._hp -= max(1, int(damage))
        print(f"{self._name} takes {damage} damage! Remaining HP: {self._hp}")


class Combat:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def player_turn(self):
        """Handle the player's turn with input validation and cooldown updates."""
        if self._player._defend_mode:
            print(f"{self._player.get_name()} is no longer defending.")
        self._player._defend_mode = False

        print(f"\n{self._player.get_name()} - HP: {self._player._hp}/{self._player._max_hp}")
        print(f"{self._enemy._name} - HP: {self._enemy._hp}")

        # Display active cooldowns
        print("Active cooldowns:")
        for ability, turns in self._player._cooldowns.items():
            if turns > 0:
                print(f"  {ability}: {turns} turn(s) remaining.")

        valid_actions = {"attack", "defend", "special", "item"}
        action = ""

        while action not in valid_actions:
            action = input("Choose an action (Attack, Defend, Special, Item): ").strip().lower()
            if action not in valid_actions:
                print("Invalid action! Please choose from Attack, Defend, Special, or Item.")

        if action == "attack":
            damage = self._player.attack()
            print(f"{self._player.get_name()} attacks for {damage} damage!")
            self._enemy.receives_damage(damage)

        elif action == "defend":
            self._player._defend_mode = True
            print(f"{self._player.get_name()} is defending!")

        elif action == "special":
            valid_abilities = {"power strike", "healing aura", "crippling blow"}
            ability_name = ""

            while ability_name not in valid_abilities:
                ability_name = input("Choose a special ability (Power Strike, Healing Aura, Crippling Blow): ").strip().lower()
                if ability_name not in valid_abilities:
                    print("Invalid ability! Please choose from Power Strike, Healing Aura, or Crippling Blow.")

            damage = self._player.special_attack(ability_name.title())
            if damage is not None:
                self._enemy.receives_damage(damage)

        elif action == "item":
            while True:
                valid_items = {item.lower() for item in self._player._items}
                if not valid_items:
                    print("No items available!")
                    break

                valid_items.add("back")  # Add a "Back" option

                item_name = input(f"Choose an item to use ({', '.join(valid_items)}): ").strip().lower()

                if item_name == "back":
                    print("Returning to the main menu.")
                    return self.player_turn()  # Restart the player's turn

                if item_name not in valid_items:
                    print("Invalid item! Please choose from your available items or type 'Back' to cancel.")
                else:
                    used = self._player.use_item(item_name.title())
                    if used:
                        break  # Exit item selection after successfully using an item


        self._player.reduce_cooldowns()  # Reduce cooldowns at the end of the turn

    def enemy_turn(self):
        """Handle the enemy's turn."""
        if self._enemy.is_alive():
            damage = self._enemy.attack()
            print(f"The {self._enemy._name} attacks for {damage} damage!")
            self._player.receives_damage(damage)

    def battle_is_active(self):
        """Check if the battle is still ongoing."""
        return self._player.is_alive() and self._enemy.is_alive()

    def engage_in_battle(self):
        """Run the battle until one side wins."""
        while self.battle_is_active():
            self.player_turn()
            if self._enemy.is_alive():
                self.enemy_turn()
            self._player.reduce_cooldowns()

        if not self._player.is_alive():
            print(f"{self._player.get_name()} has been defeated.")
        else:
            print(f"The {self._enemy._name} has been defeated!")

    def enemy_turn(self):
        """Handle the enemy's turn."""
        if self._enemy.is_alive():
            damage = self._enemy.attack()
            print(f"The {self._enemy._name} attacks for {damage} damage!")
            self._player.receives_damage(damage)

    def battle_is_active(self):
        """Check if the battle is still ongoing."""
        return self._player.is_alive() and self._enemy.is_alive()

    def engage_in_battle(self):
        """Run the battle until one side wins."""
        while self.battle_is_active():
            self.player_turn()
            if self._enemy.is_alive():
                self.enemy_turn()
            self._player.reduce_cooldowns()

        if not self._player.is_alive():
            print(f"{self._player.get_name()} has been defeated.")
        else:
            print(f"The {self._enemy._name} has been defeated!")


# Example Usage
#player = Player(name="Hero", max_hp=100, attack_stat=20, defense_stat=10)
#player._items = ["Healing Potion",]
#enemy = Enemy(name="Goblin", hp=50, attack_stat=15)
#combat = Combat(player, enemy)

#combat.engage_in_battle()
