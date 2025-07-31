num_employees = 6

def main():
    hours = [0] * num_employees

    for index in range(num_employees):
        print('Enter yhe hours work by em ',index + 1, ': ', sep='', end='')
        hours[index]= float(input())

        pay_rate = float(input('Enter yhe hourly pay rate: '))
        
        for index in range(num_employees):
            gross_pay = hours[index] * pay_rate
            print('gross pay', index + 1, ':$', \
                   format(gross_pay, ',.2f'), sep='' )

    