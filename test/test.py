
arrow_head = int(input('Enter arrow head :\n'))
arrow_size = int(input('Enter arrow head size:\n'))
arrow_width = int(input('Enter arrow head width:\n'))




while arrow_size > 0:
    print(arrow_width*'*')
    arrow_size -= 1
    if arrow_size == 0:
        for i in range(arrow_head,0,-1):
            print(i*'*')



