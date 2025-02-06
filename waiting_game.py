import time


def waiting_game():
    wait_time = input("Please enter a second as integer:\t")
    try:
        int(wait_time)
    except ValueError as e:
        print("Please enter integer value: ", e)
    while True:
        if input('Please press enter to start the timer.') == "":
            start_time = time.perf_counter()

        if input() == "":
            stop_time = time.perf_counter()
            break
    elapsed_time = stop_time - start_time
    print(f"Elabsed time {elapsed_time:.3f}")
    fast_or_slow = int(wait_time) - elapsed_time
    if fast_or_slow > 0:
        print(f"({fast_or_slow:.3f} seconds too fast!)")
    else:
        print(f"({fast_or_slow:.3f} seconds too slow!)")
    
    if fast_or_slow == 0.0:
        print('Wow Amazing result!')

waiting_game()
