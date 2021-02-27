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
RAINBOW = 'r'
TRANS = 'b'
ENBY = 'g'
YELLOW = 'y'
COMMUNIST = 'x'

COLORS = (RAINBOW, TRANS, ENBY, YELLOW)

COLOR_ICONS = {
    RAINBOW: '🏳️‍🌈',
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
    'r_0': 'CAACAgIAAxkBAANLYDn1ziAyhmhO6Hppa3CYfFnOA6YAAokNAAJsGchJb8BeXsjvAAGOHgQ',
    'r_1': 'CAACAgIAAxkBAANMYDn18We4VhimqcE2NJRg1Lt1I-YAAjwLAAKQQ8lJ3mhmwgAB4ubgHgQ',
    'r_2': 'CAACAgIAAxkBAANNYDn2B908jkPpXl24oWMsmxdDoVEAAhAMAAIsxshJw1mqHYeISdYeBA',
    'r_3': 'CAACAgIAAxkBAANOYDn2FNsHCdoa8mipEarucDz3mhwAAn0JAALoV8lJAwABm40fb_1yHgQ',
    'r_4': 'CAACAgIAAxkBAANPYDn2INp-RWk5lrWAI6KFv1LSo-YAAogLAAKa3MlJ34bNGaGU-2EeBA',
    'r_5': 'CAACAgIAAxkBAANQYDn2LB4litctERNbFYsQ2zW9MPAAApoLAAIeQMhJsGUbjP4Ua6YeBA',
    'r_6': 'CAACAgIAAxkBAANRYDn2TERPTo-fEpJDhizDbwtC1SsAAokOAAKkMshJcAwgK-_AZ7UeBA',
    'r_7': 'CAACAgIAAxkBAANSYDn2WKgxbyu_UiT9SORa7YfIzTcAAkwLAALnychJylNcYUKHj8UeBA',
    'r_8': 'CAACAgIAAxkBAANTYDn2aB82UH1o5Tx-Zz39HQUIH2sAApMLAAKrjchJXC9wyNrI4RQeBA',
    'r_9': 'CAACAgIAAxkBAANUYDn2dTVK0Twn5QLOte0niged2VcAAkEMAAIuDshJsuYca07aoV8eBA',
    'r_draw': 'CAACAgIAAxkBAANVYDn2hghS7PTIvtCvj9MQ6anl1ckAAsMLAAJU2clJI4e5uQjztWweBA',
    'r_skip': 'CAACAgIAAxkBAANWYDn2k3dbd_f7eQu_kNDLkgNG1YYAAtsMAAJkW8lJqPbFW68G5WIeBA',
    'r_reverse': 'CAACAgIAAxkBAANXYDn2pSYp6tlI4U_TaLgN7fvJywEAAg4OAALg_clJ1ZLcxrqMXQIeBA',
    'y_0': 'CAACAgIAAxkBAANzYDn9ECz0b8rteXOXgyYLwLaslxkAAooKAAIZw8lJklbkM7H0aKUeBA',
    'y_1': 'CAACAgIAAxkBAAN0YDn9UVY9m-S4cENVjN0rET1L3zcAAhwKAAKbyMhJAo9HXfh-NQUeBA',
    'y_2': 'CAACAgIAAxkBAAN1YDn9XAf47E8CBzkql04oLj6YftsAApgNAAL-9MlJLO-3xdD1PvEeBA',
    'y_3': 'CAACAgIAAxkBAAN2YDn9cR2KZOP2V0G6SHL0Jn2MZu0AAuILAAK0M8hJfVeNXejyLmkeBA',
    'y_4': 'CAACAgIAAxkBAAN3YDn9gp7CkLrGy1-a_AnKQsWoEIsAAr4LAAK5O8hJif38iY2KUOgeBA',
    'y_5': 'CAACAgIAAxkBAAN4YDn9j-Ntj-OEAiMnRAc2icH4f4wAAjYLAAJ-BclJ7E_8NdNwG_UeBA',
    'y_6': 'CAACAgIAAxkBAAN5YDn9maz9a9Mv6hoYKgPmnh1k9AMAAkYKAAJTLtBJ53neKr2PKuseBA',
    'y_7': 'CAACAgIAAxkBAAN6YDn-wQ22I9M84LHdUX09O8wBcSsAApENAAIs0MhJNn8-3siNbGkeBA',
    'y_8': 'CAACAgIAAxkBAAN7YDn-0RMcGV6_jVm8uQwDkPbiIsAAApgKAAIQTMlJWI-Q8HxkpooeBA',
    'y_9': 'CAACAgIAAxkBAAN8YDn-3v69uaUY5nJ8qJYIHAGD8iQAAh8LAAKJzMhJcP9WbiQT5cMeBA',
    'y_draw': 'CAACAgIAAxkBAAN9YDn-_vIwAR8_4RrKCMVOYgW7cvIAApEKAAIvUMhJr8V4jHddBQABHgQ',
    'y_skip': 'CAACAgIAAxkBAAN-YDn_DNyJ5PhxzY6gv3ogqMhtISYAAvcKAAIVV8lJYEh904ekipIeBA',
    'y_reverse': 'CAACAgIAAxkBAAN_YDn_Gfqx4KcbCqCpLsm5B8BbBjcAAv0PAAKP_clJW3wo0kJ_yGgeBA',
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
    'r_0': 'CAACAgIAAxkBAANYYDn2zUorrGj6Ix3bcWlIXAQVoNEAAuALAAIJ7slJmYhZsZcbAWIeBA',
    'r_1': 'CAACAgIAAxkBAANZYDn23o2sqU58svr2xmPBM-awAAGMAALdCgACidXISVs7jVjROtKsHgQ',
    'r_2': 'CAACAgIAAxkBAANaYDn26Y8FWnEeHIYnCPq0zPoBuhQAAuMLAAI_wslJthxUtYl9a_0eBA',
    'r_3': 'CAACAgIAAxkBAANbYDn289Sgs1rt_B91nbR6hPpW55AAAhQJAAKWm8lJwOnvyWZoodUeBA',
    'r_4': 'CAACAgIAAxkBAANcYDn2_mnzSdrE4dUl3UT-4CEsaisAAqEQAAKvQchJCzxH_QHf758eBA',
    'r_5': 'CAACAgIAAxkBAANdYDn3DIALPwwVTKhiXyD1wwsTQ8cAAlMKAAKrZshJduVfpKajZDUeBA',
    'r_6': 'CAACAgIAAxkBAANeYDn3GJwkOTQF-4j81pcwODrhgQ4AAlkNAAKQBslJJ0BnbTE9kpUeBA',
    'r_7': 'CAACAgIAAxkBAANfYDn3JE_BmK_yOsWfcIhzAbay2DEAAsENAALTR8lJlcNreKwRAz8eBA',
    'r_8': 'CAACAgIAAxkBAANgYDn3MXlfinqh-mZDal882tJhKOUAAs4KAALMkslJ_AhjRzeMNmIeBA',
    'r_9': 'CAACAgIAAxkBAANhYDn3QofwcZAPHYg3AVOIc4BAolsAAkULAALM3chJ-TzmXlIOUoMeBA',
    'r_draw': 'CAACAgIAAxkBAANiYDn3TpDqMLBLuwqRy4hvvEl-xJUAAisLAAJkOMlJvu0Nf28r654eBA',
    'r_skip': 'CAACAgIAAxkBAANjYDn3XWpq8Y3atSZIlR7agoQbW2IAAl0MAAIQAchJFPA4BNoAAdMBHgQ',
    'r_reverse': 'CAACAgIAAxkBAANkYDn3a5Qv7pdtxNgPvA0cMc6pr88AAh4KAAKS8chJr7RBi-z6gSQeBA',
    'y_0': 'CAACAgIAAxkBAANlYDn4oUGlr7LW4kh5EA7LF3HnJcoAApUJAAKE-MlJ0uBgCBqmsekeBA',
    'y_1': 'CAACAgIAAxkBAANnYDn4vua3-Bw2En_L1EbC_YSRf58AAtYKAAKFUshJe7oiAAHTsHrOHgQ',
    'y_2': 'CAACAgIAAxkBAANoYDn40H_-BsRz38YVYRg2fKdttkIAAvEJAAKM78lJ6OrmF9P7Td4eBA',
    'y_3': 'CAACAgIAAxkBAANpYDn432EG7idDUINCQ7EgB_q6c58AAjIMAAKuAAHISSAbrf2a7f7XHgQ',
    'y_4': 'CAACAgIAAxkBAANqYDn48ffZmZx5zPfhuPYkZHk9aJcAAiEMAAJPf8hJFoz9JrLn6DIeBA',
    'y_5': 'CAACAgIAAxkBAANrYDn4_7ojliWcUdwDUlLBtZMLE9IAAp8KAALP58hJJ8b7KmXr5tIeBA',
    'y_6': 'CAACAgIAAxkBAANsYDn5LRgX2NvrZOmDwOlDrvIg0g8AApcLAALxnMlJsyzPyD_kfpYeBA',
    'y_7': 'CAACAgIAAxkBAANtYDn5Smd9e9kTwsYs1Y7_ZmO90gUAAnILAAIjKshJnvAEIHK15ooeBA',
    'y_8': 'CAACAgIAAxkBAANuYDn5X5ECUl9r5elI0dmSqvVt5woAAq0LAAJ2DMlJ8qjAafxRbKceBA',
    'y_9': 'CAACAgIAAxkBAANvYDn5cePqnaU5Do0KcIZ6yyj9wOMAAhYMAAJNCslJkE1MZ_X54VkeBA',
    'y_draw': 'CAACAgIAAxkBAANwYDn5f8ZH-hs0tMJ_rTHTYX8-MAkAAmQKAAKfMclJ2kmu2HzQepgeBA',
    'y_skip': 'CAACAgIAAxkBAANxYDn5jS7laB2vYLXxPHPDVyjY200AAi4LAALVl8lJKif7zK90lHIeBA',
    'y_reverse': 'CAACAgIAAxkBAANyYDn5nLZrz1byXzTMsz3P9LKLFo0AAjILAAIr9MlJlzl7gZhid_ceBA',
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
