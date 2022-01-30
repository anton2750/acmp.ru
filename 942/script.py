with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        f.readline()  # overall count, not used, skipping
        tasks = list(map(int, f.readline().split()))

        orders = {1: sorted(tasks), 3: tasks[::-1], 5: tasks}
        timers = {1: 0, 3: 0, 5: 0}

        for student in timers.keys():
            fine = 0
            counter = 0
            for t in orders[student]:
                counter += t
                fine += counter
            timers[student] = fine

        # print(tasks)
        # print(orders)
        # print(timers)

        # evaluation:
        winner = 1
        result = timers[winner]

        for student, time in timers.items():
            if time < result:
                winner = student
                result = time

        # print(winner)
        o.write(f"{winner}")
