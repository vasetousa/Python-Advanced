def green_light_cycle(gr_light, window):
    for el in cars:
        ll = len(el)
        if ll <= gr_light:
            dif = gr_light - ll
            dif += window


from collections import deque

green_light = 9
free_window = 3
cars = deque()
time_left_from_green_light = []
time_left_and_window_time = []
car_counter = 0
car_passed = False
time_left = 0

command = input()

while not command == "END":  # end the program
    if command == "green":
        green_light_cycle(green_light, free_window)

    else:   # cars coming before the command "green"

        cars.append(command)
        car_len = len(command)
        if car_len < green_light:
            car_passed = True
            time_left = green_light - car_len
        elif car_len == green_light:
            car_passed = True
            time_left = 0
        if time_left > 0:

            pass

        # else:
        #     print("A crash happened!")
        #     break


    command = input()

print()