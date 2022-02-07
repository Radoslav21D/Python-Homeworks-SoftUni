team_a = "A-1, A-2, A-3, A-4, A-5, A-6, A-7, A-8, A-9, A-10, A-11"
team_b = "B-1, B-2, B-3, B-4, B-5, B-6, B-7, B-8, B-9, B-10, B-11"
team_a_split = team_a.split(", ")
team_b_split = team_b.split(", ")
red_cards = input().split()
count_a = 11
count_b = 11
is_terminated = False
for i in range(len(red_cards)):
    first = red_cards[i]
    if first in team_a_split:
        count_a -= 1
        team_a_split.remove(first)
    elif first in team_b_split:
        count_b -= 1
        team_b_split.remove(first)
    if count_a < 7 or count_b < 7:
        is_terminated = True
print(f"Team A - {count_a}; Team B - {count_b}")
if is_terminated:
    print("Game was terminated")
