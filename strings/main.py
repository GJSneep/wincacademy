# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1
scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = f'{scorer_0} {goal_0}, {scorer_1} {goal_1}'
report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'

# Part 2
player = 'Marco van Basten'  # 1
first_name = player[0:player.find(' ')]  # 2
last_name_len = len(player[player.find(' '):]) - 1  # 3
name_short = f"{player[0:1]}.{player[player.find(' '):]}"  # 4
chant = ((len(first_name) - 1) * f'{first_name}! ') + f'{first_name}!'  # 5
good_chant = chant[-1] != ' '  # 6
