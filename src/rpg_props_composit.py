from abc import ABC, abstractmethod


class Health:
    def __init__(self, value: int):
        self.value = value

    def decrease(self, amount: int):
        self.value -= amount

    def increase(self, amount: int):
        self.value += amount

    def is_positive(self):
        return self.value > 0


class AttackPower:
    def __init__(self, value: int):
        self.value = value


class Potions:
    def __init__(self, stock: int):
        self.stock = stock

    def use(self):
        if self.stock > 0:
            self.stock -= 1
            return True
        else:
            return False


class Character(ABC):
    def __init__(self, name: str, health: Health, attack_power: AttackPower):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, other):
        pass

    def is_alive(self):
        return self.health.is_positive()


class Player(Character):
    def __init__(
        self,
        name: str,
        health: Health,
        attack_power: AttackPower,
        potions: Potions,
    ):
        super().__init__(name, health, attack_power)

    def attack(self, other: Character):
        other.health.decrease(self.attack_power.value)
        print(
            f"{self.name}の攻撃: {other.name} へ",
            f"{self.attack_power.value} のダメージ!",
        )

    def drink_potion(self):
        if self.drink_potion.use():
            self.health.increase(10)
            print(f"{self.name}はポーションを使用した!HPが10回復した")
        else:
            print(f"{self.name}はもうポーションを持っていない")
