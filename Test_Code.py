#14 i 51
current = input("vvedite vase vremya ")
timer_hours = input("vvedite chasov timera ")
timer_off = ((int(current) + int(timer_hours)) % 24)
print("Timer viklychitsa kogda na chasah bydet ", timer_off)


