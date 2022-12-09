from Exercise.Hero.project.hero import Hero
import unittest


class HeroTest(unittest.TestCase):
    def test_constructor(self):
        sample = Hero('test', 10, 100.25, 10.25)
        self.assertEqual('test', sample.username)
        self.assertEqual(10, sample.level)
        self.assertEqual(100.25, sample.health)
        self.assertEqual(10.25, sample.damage)

    def test_battle_method_when_enemy_name_equals_hero_name(self):
        sample = Hero('test', 10, 100.25, 10.25)
        enemy_sample = Hero('test', 10, 100.25, 10.25)
        with self.assertRaises(Exception) as error:
            sample.battle(enemy_sample)
        self.assertEqual('You cannot fight yourself', str(error.exception))

    def test_battle_method_when_hp_is_zero(self):
        sample = Hero('test', 10, 0, 10.25)
        enemy_sample = Hero('test1', 10, 100.25, 10.25)
        with self.assertRaises(ValueError) as error:
            sample.battle(enemy_sample)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(error.exception))

    def test_battle_method_when_hp_is_negative(self):
        sample = Hero('test', 10, -10, 10.25)
        enemy_sample = Hero('test1', 10, 100, 10.25)
        with self.assertRaises(ValueError) as error:
            sample.battle(enemy_sample)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(error.exception))

    def test_battle_method_when_enemy_has_hp_zero(self):
        sample = Hero('test', 10, 10, 10.25)
        enemy_sample = Hero('test1', 10, 0, 10.25)
        with self.assertRaises(ValueError) as error:
            sample.battle(enemy_sample)
        self.assertEqual('You cannot fight test1. He needs to rest', str(error.exception))

    def test_battle_method_when_enemy_has_hp_negative(self):
        sample = Hero('test', 10, 10, 10.25)
        enemy_sample = Hero('test1', 10, -100, 10.25)
        with self.assertRaises(ValueError) as error:
            sample.battle(enemy_sample)
        self.assertEqual('You cannot fight test1. He needs to rest', str(error.exception))

    def test_battle_method_when_both_players_have_zero_hp_left(self):
        sample = Hero('test', 10, 102.5, 10.25)
        enemy_sample = Hero('test1', 10, 102.5, 10.25)
        # player dmg = 102.5
        # enemy dmg = 102.5
        result = sample.battle(enemy_sample)
        self.assertEqual('Draw', result)

    def test_battle_method_when_both_players_have_negative_hp_left(self):
        sample = Hero('test', 10, 102.5, 10.25)
        enemy_sample = Hero('test1', 10, 102.5, 10.25)
        # player dmg = 102.5
        # enemy dmg = 102.5
        result = sample.battle(enemy_sample)
        self.assertEqual('Draw', result)

    def test_battle_method_when_enemy_has_zero_hp_left(self):
        sample = Hero('test', 10, 1000.5, 10.25)
        enemy_sample = Hero('test1', 10, 102.5, 10.25)
        # player dmg = 102.5
        # enemy dmg = 102.5
        result = sample.battle(enemy_sample)
        self.assertEqual('You win', result)
        self.assertEqual(11, sample.level)
        self.assertEqual(903.0, sample.health)
        self.assertEqual(15.25, sample.damage)
        self.assertEqual(0, enemy_sample.health)

    def test_battle_method_when_enemy_has_negative_hp_left(self):
        sample = Hero('test', 10, 1000.5, 10.25)
        enemy_sample = Hero('test1', 10, 10.5, 10.25)
        # player dmg = 102.5
        # enemy dmg = 102.5
        result = sample.battle(enemy_sample)
        self.assertEqual('You win', result)
        self.assertEqual(11, sample.level)
        self.assertEqual(903.0, sample.health)
        self.assertEqual(15.25, sample.damage)
        self.assertEqual(-92.0, enemy_sample.health)

    def test_battle_method_when_enemy_has_positive_hp(self):
        sample = Hero('test', 10, 1000.5, 10.25)
        enemy_sample = Hero('test1', 10, 1000.5, 10.25)
        # player dmg = 102.5
        # enemy dmg = 102.5
        result = sample.battle(enemy_sample)
        self.assertEqual('You lose', result)
        self.assertEqual(11, enemy_sample.level)
        self.assertEqual(903.0, enemy_sample.health)
        self.assertEqual(15.25, enemy_sample.damage)

    def test_str_dunder_method(self):
        sample = Hero('test', 10, 10.5, 10.25)
        expected = f"Hero test: 10 lvl\n" \
                   f"Health: 10.5\n" \
                   f"Damage: 10.25\n"
        actual = str(sample)
        self.assertEqual(expected, actual)
