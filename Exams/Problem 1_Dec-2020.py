from collections import deque

males = deque([int(el) for el in input().split()])
females = deque([int(el) for el in input().split()])
matches = []
no_males = False
no_females = False

while True:
    if not males:
        no_males = True
        break
    if not females:
        no_females = True
        break
    current_female = females[0]
    current_male = males[len(males)-1]
    if current_male <= 0:
        males.pop()
        continue
    if current_male % 25 == 0:
        males.pop()
        males.pop()
        continue
    if current_female <= 0:
        females.popleft()
        continue
    if current_female % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if current_male == current_female:
        males.pop()
        females.popleft()
        matches.append((current_female, current_male))
    else:
        if males:
            x = males.pop() - 2
            males.append(x)
            females.popleft()

print(f"Matches: {len(matches)}")
if not males:
    print("Males left: none")
else:
    males.reverse()
    print(f"Males left: {', '.join([str(el) for el in males])}")
if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(el) for el in females])}")