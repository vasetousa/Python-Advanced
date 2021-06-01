def bang():
    print("Bang!")
    return


def ping():
    print("Ping!")
    return


def reloading():
    if bullets:
        print("Reloading!")
    return


def print_results():
    if no_bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
    else:
        bullets_left = total_bullets - len(bullets)
        print(f"{len(bullets)} bullets left. Earned ${intelligence_value - (bullets_left * bullet_price)}")


from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(el) for el in input().split()])
locks = deque([int(el) for el in input().split()])
intelligence_value = int(input())  # remove price of bullets from this value
bullet_counter = gun_barrel_size
total_bullets = len(bullets)
no_bullets = False
no_locks = False

while True:
    if not locks:
        no_locks = True
        break
    elif not bullets:
        no_bullets = True
        break

    current_bullet = bullets.pop()
    current_lock = locks[0]
    if current_bullet <= current_lock:
        bang()
        locks.popleft()
        bullet_counter -= 1
    else:
        ping()
        bullet_counter -= 1
    if bullet_counter == 0:
        reloading()
        bullet_counter = gun_barrel_size

print_results()
