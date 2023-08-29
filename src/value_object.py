from abc import ABC, abstractmethod
from dataclasses import dataclass, replace
from typing import Self


# 「Healthクラスのvalueを直接変更する」ことをした場合,
# 結果として,バグが発生する可能性がある
# dataclassで作成したHealthクラスは不変なのでエラーが発生する
@dataclass(frozen=True, slots=True)
class Health:
    value: int

    def decrease(self, amount: int) -> Self:
        return replace(self, value=self.value - amount)
        # return Health(self.value - amount)

    def increase(self, amount: int) -> Self:
        return replace(self, value=self.value + amount)
        # return Health(self.value + amount)

    def is_positive(self) -> bool:
        return self.value > 0


@dataclass(frozen=True, slots=True)
class AttackPower:
    value: int


@dataclass(frozen=True, slots=True)
class Potions:
    stack: int

    def use(self) -> tuple[Self, bool]:
        if self.stock > 0:
            return (replace(self, stock=self.stock - 1), True)
        else:
            return replace(self, False)


class Character(ABC):
    def __init__(self, name: str, health: Health, attack_power: AttackPower):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, other):
        pass

    def is_alive(self) -> bool:
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
        self.potions = potions

    def attack(self, other: Character) -> None:
        other.health = other.health.decrease(self.attack_power.value)
        print(
            f"{self.name} の攻撃: {other.name} へ" f"{self.attack_power.value} のダメージ!",
        )

    def drink_potion(self) -> None:
        self.potions, used = self.potions.use()
        if used:
            self.health = self.health.increase(10)
            print(f"{self.name} はポーションを使用した! HPが10回復した!")
        else:
            print(f"{self.name} はもうポーションを持っていない")
