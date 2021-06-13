def print_result(effort_status):
    if not effort_status:
        print("Sorry. You can't make the perfect firework show.")
    else:
        print("Congrats! You made the perfect firework show!")
    if q:
        print(f"Firework Effects left: {', '.join(str(x) for x in q)}")
    if power:
        print(f"Explosive Power left: {', '.join(str(x) for x in power)}")
    print(f"Palm Fireworks: {palm_firework}")
    print(f"Willow Fireworks: {willow_firework}")
    print(f"Crossette Fireworks: {crossette_firework}")
    return


effects = [int(el) for el in input().split(", ")]   # start from the first
power = [int(el) for el in input().split(", ")]     # add with the last
from collections import deque
q = deque(effects)
is_true = False
is_break = False
palm_firework = 0
willow_firework = 0
crossette_firework = 0

while q:
    lenn = len(power)
    if lenn == 0:
        break
    current_power_element = power[lenn - 1]
    if current_power_element <= 0:
        power.pop()
        continue
    current_effect_element = q[0]
    if current_effect_element <= 0:
        q.popleft()
        continue
    current_sum = current_power_element + current_effect_element
    if current_sum % 3 == 0 and not current_sum % 5 == 0:
        palm_firework += 1
        q.popleft()
        power.pop()
    elif current_sum % 5 == 0 and not current_sum % 3 == 0:
        willow_firework += 1
        q.popleft()
        power.pop()
    elif current_sum % 5 == 0 and current_sum % 3 == 0:
        crossette_firework += 1
        q.popleft()
        power.pop()
    else:
        current_effect_element = q.popleft()
        current_effect_element -= 1
        q.append(current_effect_element)

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        is_true = True
        is_break = True
        break

if is_break:
    print_result(is_true)
else:
    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        is_true = True
        print_result(is_true)
    else:
        is_true = False
        print_result(is_true)