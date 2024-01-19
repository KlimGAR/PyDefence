if wave:
    while timer <= 2:
        timer -= 2
    print(working_paths)
    for i in working_paths:
        if i.is_pressed:
            print('eck')
else:
    wave = next[-1]
    next.remove(next[-1])