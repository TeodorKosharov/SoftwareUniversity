from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))  # stack
locks = deque(list(map(int, input().split())))
intelligence = int(input())

spent_money_on_bullets = 0
left_bullets_in_barrel = gun_barrel_size

while locks:

    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        exit(0)

    current_lock = locks[0]
    current_bullet = bullets[-1]

    if current_bullet <= current_lock:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')

    bullets.pop()
    spent_money_on_bullets += bullet_price
    left_bullets_in_barrel -= 1

    if left_bullets_in_barrel == 0 and bullets:
        left_bullets_in_barrel = gun_barrel_size
        print("Reloading!")

print(f"{len(bullets)} bullets left. Earned ${intelligence - spent_money_on_bullets}")
