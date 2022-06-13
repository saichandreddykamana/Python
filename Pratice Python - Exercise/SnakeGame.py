board_size = int(input("Enter board Size : "))
snake = 1
steps = -1
while snake <= (board_size*board_size):
    snake = snake * 2
    steps += 1

print("NO OF STEPS : ", steps)
