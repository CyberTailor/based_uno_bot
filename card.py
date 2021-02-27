#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


# Colors
RED = 'r'
TRANS = 'b'
ENBY = 'g'
YELLOW = 'y'
COMMUNIST = 'x'

COLORS = (RED, TRANS, ENBY, YELLOW)

COLOR_ICONS = {
    RED: '❤️',
    TRANS: '💙',
    ENBY: '💜',
    YELLOW: '💛',
    COMMUNIST: '⬛️'
}

# Values
ZERO = '0'
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
DRAW_TWO = 'draw'
REVERSE = 'reverse'
SKIP = 'skip'

VALUES = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, DRAW_TWO,
          REVERSE, SKIP)
WILD_VALUES = (ONE, TWO, THREE, FOUR, FIVE, DRAW_TWO, REVERSE, SKIP)

# Special cards
CHOOSE = 'colorchooser'
DRAW_FOUR = 'draw_four'

SPECIALS = (CHOOSE, DRAW_FOUR)

STICKERS = {
    'b_0': 'CAACAgIAAxkBAAMVYDkekaCD8KIp2RWArGRj2paIuKMAApYLAAKS4chJm2m9OHjazw0eBA',
    'b_1': 'CAACAgIAAxkBAAMWYDkerfIkAAFqqPnKYVY1IvMlMwiuAAJHCgACGczISXR9cChkzCLCHgQ',
    'b_2': 'CAACAgIAAxkBAAMXYDkex8AxnQInLLn35eXc5_QtqKoAApwMAALWO8hJYK_34AnhFFweBA',
    'b_3': 'CAACAgIAAxkBAAMYYDke17PlgSGHrYKBSdD5cHxVvk8AAj0MAAKF3dBJfJWk2iRfsbweBA',
    'b_4': 'CAACAgIAAxkBAAMZYDke9V2wC5VMGAOUKiyvTC_-vXoAAkQMAAKgy8hJToRRUQkjuJ0eBA',
    'b_5': 'CAACAgIAAxkBAAMaYDkfF27eLJTRl6AnXjB1j1FTDHgAAkYNAAI-A8lJaWCmeTnVFdIeBA',
    'b_6': 'CAACAgIAAxkBAAMbYDkfKh_qTKc64d49LXISC0D78egAAvsLAAL-wshJh124fOXt7kgeBA',
    'b_7': 'CAACAgIAAxkBAAMcYDkfOvUUU8tPfT9JLSJK8a0CkX8AAg8MAALyUMhJ3--udHId91geBA',
    'b_8': 'CAACAgIAAxkBAAMdYDkfSPscdWWWW61JZN0lk9A8pl0AAusKAAKkkslJBa96empMWDgeBA',
    'b_9': 'CAACAgIAAxkBAAMeYDkfYxPQj4COGOrz8AvhwsABHpAAAlUKAALifchJREs5cZHODvoeBA',
    'b_draw': 'CAACAgIAAxkBAAMfYDkfmXcmfBbBIE0E6oVTzbu_AnYAAk0MAAJn_shJBrw1YJh8YwgeBA',
    'b_skip': 'CAACAgIAAxkBAAMgYDkfrEcGDHNYbTr7UWhqFSuKAAGxAAILCwACVwTJSc6F4SkYn5s1HgQ',
    'b_reverse': 'CAACAgIAAxkBAAMhYDkf8mw0oet0ytGCl6MqWkJR08kAAlAPAAJ82slJzRiNnFwgpJ4eBA',
    'g_0': 'CAACAgIAAxkBAAMxYDkrmPXVO2lw_22_SP4IoY3N9SEAAqkNAAKoVclJXJeCgftQbz4eBA',
    'g_1': 'CAACAgIAAxkBAAMyYDkrsFF2pTTHObnc7sQAAbzUfo-TAAKlCwACRLjJST7JDplrdKpuHgQ',
    'g_2': 'CAACAgIAAxkBAAMzYDkrxOeBnqGfghGfyOBCBIymG6UAArEKAAL2RslJ5VuQeXNmAzQeBA',
    'g_3': 'CAACAgIAAxkBAAM0YDkr1ovFA9bPspWbZoZ246OvUjkAApkLAAJv4chJE6RnJKEZgUYeBA',
    'g_4': 'CAACAgIAAxkBAAM1YDkr5No3g8i3d2e4dVvnwLdqhFYAAowKAAIy7chJmFto1DAd_TkeBA',
    'g_5': 'CAACAgIAAxkBAAM2YDkr85J-hWzvvjj-gGfQA6K6VjMAAqkLAAJVnchJunlAE3Qi2rMeBA',
    'g_6': 'CAACAgIAAxkBAAM3YDksAbLLwSf9dMfdUqX9YKTfYVAAAg8MAAJ-d8hJNUea_Z5nFdAeBA',
    'g_7': 'CAACAgIAAxkBAAM4YDksEFWMOquK43Tnmg21bZuYYGsAAuYLAALnH8hJB7WX7ovOo6AeBA',
    'g_8': 'CAACAgIAAxkBAAM5YDksJ9XsqZknWmHqyazseQhPgYYAAr4JAAIm5chJxigcp3rw9O8eBA',
    'g_9': 'CAACAgIAAxkBAAM6YDksM9UoAAFo5H9feY8BWpv_21PrAALLDAAC2pzISe7UzgABfyPWux4E',
    'g_draw': 'CAACAgIAAxkBAAM7YDksQmGFyFPTYKeBtAVKkOpLvPIAAikMAAKUxMlJO5crP0NXO4YeBA',
    'g_skip': 'CAACAgIAAxkBAAM8YDksXHRFMHvvdFol-yQY97t5Yj4AAroQAAJSG8lJ_7kpOOtxwYoeBA',
    'g_reverse': 'CAACAgIAAxkBAAM9YDksaiiHuP6dZltgPRRM0NApzdUAAjwLAALliMhJiUeOVc20OrgeBA',
    'r_0': 'BQADBAADEQIAAl9XmQABiUfr1hz-zT8C',
    'r_1': 'BQADBAADEwIAAl9XmQAB5bWfwJGs6Q0C',
    'r_2': 'BQADBAADFQIAAl9XmQABHR4mg9Ifjw0C',
    'r_3': 'BQADBAADFwIAAl9XmQABYBx5O_PG2QIC',
    'r_4': 'BQADBAADGQIAAl9XmQABTQpGrlvet3cC',
    'r_5': 'BQADBAADGwIAAl9XmQABbdLt4gdntBQC',
    'r_6': 'BQADBAADHQIAAl9XmQABqEI274p3lSoC',
    'r_7': 'BQADBAADHwIAAl9XmQABCw8u67Q4EK4C',
    'r_8': 'BQADBAADIQIAAl9XmQAB8iDJmLxp8ogC',
    'r_9': 'BQADBAADIwIAAl9XmQAB_HCAww1kNGYC',
    'r_draw': 'BQADBAADJQIAAl9XmQABuz0OZ4l3k6MC',
    'r_skip': 'BQADBAADKQIAAl9XmQAC2AL5Ok_ULwI',
    'r_reverse': 'BQADBAADJwIAAl9XmQABu2tIeQTpDvUC',
    'y_0': 'BQADBAADKwIAAl9XmQAB_nWoNKe8DOQC',
    'y_1': 'BQADBAADLQIAAl9XmQABVprAGUDKgOQC',
    'y_2': 'BQADBAADLwIAAl9XmQABqyT4_YTm54EC',
    'y_3': 'BQADBAADMQIAAl9XmQABGC-Xxg_N6fIC',
    'y_4': 'BQADBAADMwIAAl9XmQABbc-ZGL8kApAC',
    'y_5': 'BQADBAADNQIAAl9XmQAB67QJZIF6XAcC',
    'y_6': 'BQADBAADNwIAAl9XmQABJg_7XXoITsoC',
    'y_7': 'BQADBAADOQIAAl9XmQABVrd7OcS2k34C',
    'y_8': 'BQADBAADOwIAAl9XmQABRpJSahBWk3EC',
    'y_9': 'BQADBAADPQIAAl9XmQAB9MwJWKLJogYC',
    'y_draw': 'BQADBAADPwIAAl9XmQABaPYK8oYg84cC',
    'y_skip': 'BQADBAADQwIAAl9XmQABO_AZKtxY6IMC',
    'y_reverse': 'BQADBAADQQIAAl9XmQABZdQFahGG6UQC',
    'draw_four': 'CAACAgIAAxkBAAMTYDkd3nU21e1Z-FMCYi81pnZZiGEAAvEKAALM_slJxv9H6mnvCcceBA',
    'colorchooser': 'CAACAgIAAxkBAAMUYDkd8Z8f49f6ArFe3jVmN882ELAAAigNAAIOsshJv4gsBlPTLjseBA',
    'option_draw': 'BQADBAAD-AIAAl9XmQABxEjEcFM-VHIC',
    'option_pass': 'BQADBAAD-gIAAl9XmQABcEkAAbaZ4SicAg',
    'option_bluff': 'CAACAgIAAxkBAAMQYDkbOfkyfO-sO1TWM5rY0kiWMbMAAjMMAAJl_clJDP2VAAEVElHQHgQ',
    'option_info': 'CAACAgIAAxkBAAMPYDkbE5ZLoC2_INgeMgABuSBoMjrgAAJgCgACdsTJSSX8O0SQkraOHgQ'
}

STICKERS_GREY = {
    'b_0': 'CAACAgIAAxkBAAMiYDkgH4lV2kxwkp3jsk6313b8CckAAtUKAAIkH8lJeqzjpaQM16QeBA',
    'b_1': 'CAACAgIAAxkBAAMjYDkgLIyVjFpdvF_DzckzHRlbFr0AAoQKAAL3wslJUyZ4T9tKpHIeBA',
    'b_2': 'CAACAgIAAxkBAAMkYDkgOk6g3UE0_LTJEWBTelo-0DAAAjsOAAJH5clJe9Pq5-nS9CceBA',
    'b_3': 'CAACAgIAAxkBAAMlYDkgUNgufhNBvON_R-aD7a2m22MAAgkMAALVRNFJQwFxSxpwYZUeBA',
    'b_4': 'CAACAgIAAxkBAAMmYDkgXPMcHsQ1FJNaOX9D58HyiTQAArQOAAJGtslJqT-D8V1-G18eBA',
    'b_5': 'CAACAgIAAxkBAAMnYDkgaUQflPoL9pVbtt4nCnIwVy0AAkAMAAJdRclJUEZUeRcnmn8eBA',
    'b_6': 'CAACAgIAAxkBAAMoYDkgdDZapGhAwohsv2tsPMHTFSQAAvkJAALigdBJfVk_RoQ-vHweBA',
    'b_7': 'CAACAgIAAxkBAAMpYDkggE06aoZMg-9Oh_qWbaJJKPcAAgMLAAJ5x8lJc6FSOv3xlY4eBA',
    'b_8': 'CAACAgIAAxkBAAMqYDkgjYZiobh9d0IoRqKkzr8Cky0AAqQLAALMmMlJRyZL0bHKcs8eBA',
    'b_9': 'CAACAgIAAxkBAAMrYDkgn_bm6cS3h244tP0dCeBVCFIAAioLAALVl8lJ51r8CIn898MeBA',
    'b_draw': 'CAACAgIAAxkBAAMsYDkgsGunA8R-fGZnB5Fqq4tOBRAAAmsKAAPSyEnY9LF5X-aL0h4E',
    'b_skip': 'CAACAgIAAxkBAAMtYDkgwt_5KPojJTnpM97eCRq_qu0AAjIMAALixshJAsTD_zEgy7MeBA',
    'b_reverse': 'CAACAgIAAxkBAAMuYDkg0LYDTgOz6usjff1bpK7Kt-8AAr8LAAIikslJq0jwrUxzr88eBA',
    'g_0': 'CAACAgIAAxkBAAM-YDksopF59zzLl8C6nkXRl4Q26fgAAkkMAAKJYMlJgZ3mJDHoNRoeBA',
    'g_1': 'CAACAgIAAxkBAAM_YDkstKtJ6DTW-KsHCNgHLxqiMioAAjcMAAKzyMhJT8lHTH6NZfYeBA',
    'g_2': 'CAACAgIAAxkBAANAYDkswRqmyYU8qdP_zygSOxEZf4wAAkcMAAJXD8lJdFbgQwaeleQeBA',
    'g_3': 'CAACAgIAAxkBAANBYDks0OSYxPs0fRCBxYyP4SLGXMwAAoYKAAJkt8lJK6taAQMEjhAeBA',
    'g_4': 'CAACAgIAAxkBAANCYDks3Q1nhK4OL32QcGFh2IYpkjgAAr0LAAIX-clJA40l3QKayuQeBA',
    'g_5': 'CAACAgIAAxkBAANDYDks6gfwYrSqPSDxm4G40W3TlAoAArMOAAJVdMhJ_nqCAmzKKtQeBA',
    'g_6': 'CAACAgIAAxkBAANEYDks9xpV1KFqf6fixSZEsCvFQucAAkMKAAI_W8hJ5DRpQTCDRFweBA',
    'g_7': 'CAACAgIAAxkBAANFYDktAvsw78H3-QvQhj0MpwmNfrYAAvsMAAKD0clJ69tFKrE92YMeBA',
    'g_8': 'CAACAgIAAxkBAANGYDktENwMseFnT4a4Zqo2P1xJc7gAAoEKAALHk8lJWYAjS8iCKvMeBA',
    'g_9': 'CAACAgIAAxkBAANHYDktLhgSEAg3CyWINJX9z6_yb1MAAo4KAAI8r8hJF7xkdMqRj_YeBA',
    'g_draw': 'CAACAgIAAxkBAANIYDktQ7IP-VIb0ug_F14jIzMR494AAgcMAAIsTMhJl6OwNQ7lE2ceBA',
    'g_skip': 'CAACAgIAAxkBAANJYDktU9wr32AkVowj6_tZ_8T-zNIAAlUJAAL1KslJ5thDwDBN69seBA',
    'g_reverse': 'CAACAgIAAxkBAANKYDktX-yL8ZtKc2YaWRDroUMM0CoAAk4LAAJYG8hJ7BLlcbON0CweBA',
    'r_0': 'BQADBAADfQIAAl9XmQABWrxoiXcsg0EC',
    'r_1': 'BQADBAADfwIAAl9XmQABlav-bkgSgRcC',
    'r_2': 'BQADBAADgQIAAl9XmQABDjZkqfJ4AdAC',
    'r_3': 'BQADBAADgwIAAl9XmQABT7lH7VVcy3MC',
    'r_4': 'BQADBAADhQIAAl9XmQAB1arPC5x0LrwC',
    'r_5': 'BQADBAADhwIAAl9XmQABWvs7xkCDldkC',
    'r_6': 'BQADBAADiQIAAl9XmQABjwABH5ZonWn8Ag',
    'r_7': 'BQADBAADiwIAAl9XmQABjekJfm4fBDIC',
    'r_8': 'BQADBAADjQIAAl9XmQABqFjchpsJeEkC',
    'r_9': 'BQADBAADjwIAAl9XmQAB-sKdcgABdNKDAg',
    'r_draw': 'BQADBAADkQIAAl9XmQABtw9RPVDHZOQC',
    'r_skip': 'BQADBAADlQIAAl9XmQABtG2GixCxtX4C',
    'r_reverse': 'BQADBAADkwIAAl9XmQABz2qyEbabnVsC',
    'y_0': 'BQADBAADlwIAAl9XmQABAb3ZwTGS1lMC',
    'y_1': 'BQADBAADmQIAAl9XmQAB9v5qJk9R0x8C',
    'y_2': 'BQADBAADmwIAAl9XmQABCsgpRHC2g-cC',
    'y_3': 'BQADBAADnQIAAl9XmQAB3kLLXCv-qY0C',
    'y_4': 'BQADBAADnwIAAl9XmQAB7R_y-NexNLIC',
    'y_5': 'BQADBAADoQIAAl9XmQABl-7mwsjD-cMC',
    'y_6': 'BQADBAADowIAAl9XmQABwbVsyv2MfPkC',
    'y_7': 'BQADBAADpQIAAl9XmQABoBqC0JsemVwC',
    'y_8': 'BQADBAADpwIAAl9XmQABpkwAAeh9ldlHAg',
    'y_9': 'BQADBAADqQIAAl9XmQABpSBEUfd4IM8C',
    'y_draw': 'BQADBAADqwIAAl9XmQABMt-2zW0VYb4C',
    'y_skip': 'BQADBAADrwIAAl9XmQABIDf-_TuuxtEC',
    'y_reverse': 'BQADBAADrQIAAl9XmQABm9M0Zh-_UwkC',
    'draw_four': 'CAACAgIAAxkBAAMRYDkdgQmuhHhmUC_kuMcv7CdMiaMAApgKAAIQDshJYaBPy9C4MWIeBA',
    'colorchooser': 'CAACAgIAAxkBAAMSYDkdp7KEYjf17u9XLS_0YH6Ldt8AAmULAAKxxMhJFJdyeSDwWyQeBA'
}


class Card(object):
    """This class represents an UNO card"""

    def __init__(self, color, value, special=None):
        self.color = color
        self.value = value
        self.special = special

    def __str__(self):
        if self.special:
            return self.special
        else:
            return '%s_%s' % (self.color, self.value)

    def __repr__(self):
        if self.special:
            return '%s%s%s' % (COLOR_ICONS.get(self.color, ''),
                               COLOR_ICONS[COMMUNIST],
                               ' '.join([s.capitalize()
                                         for s in self.special.split('_')]))
        else:
            return '%s%s' % (COLOR_ICONS[self.color], self.value.capitalize())

    def __eq__(self, other):
        """Needed for sorting the cards"""
        return str(self) == str(other)

    def __lt__(self, other):
        """Needed for sorting the cards"""
        return str(self) < str(other)


def from_str(string):
    """Decodes a Card object from a string"""
    if string not in SPECIALS:
        color, value = string.split('_')
        return Card(color, value)
    else:
        return Card(None, None, string)
