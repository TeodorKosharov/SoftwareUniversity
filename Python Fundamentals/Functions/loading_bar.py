def loading_bar(value):
    if int(value) == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        percent_counter = int(value[:1])
        dot_counter = 10 - percent_counter
        result = '%' * percent_counter + '.' * dot_counter

        print(f'{value}% [{result}]')
        print('Still loading...')


number_inp = input()
loading_bar(number_inp)
