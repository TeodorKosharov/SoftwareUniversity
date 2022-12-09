def perfect_number(number):
    suma = 0

    for i in range(1, number):

        if number % i == 0:
            suma += i

    if suma == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number_inp = int(input())
perfect_number(number_inp)
