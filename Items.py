class Item:
    def __init__(self, name):
        self._name = name
        self._description = ""

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def return_value(self):
        return 0


class NonConsumable(Item):
    def __init__(self, name):
        super().__init__(name)


class Sword(NonConsumable):
    def __init__(self, name, damage_increase_amount):
        super().__init__(name)
        self._damage_increase_amount = damage_increase_amount
        self._description = (
            f"Hold this {name.upper()} in your bag to increase your base damage by {damage_increase_amount}!"
        )

    def return_value(self):
        return self._damage_increase_amount


class Shield(NonConsumable):
    def __init__(self, name, damage_reduction_amount):
        super().__init__(name)
        self._damage_reduction_amount = damage_reduction_amount
        self._description = (
            f"Hold this {name.upper()} in your bag to increase your base defense by {damage_reduction_amount}!"
        )

    def return_value(self):
        return self._damage_reduction_amount
