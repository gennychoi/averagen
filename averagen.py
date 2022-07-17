N = int(input('please input the total amount of numbers: '))
sum = 0
count = 0
print('please input {} numbers:'.format(N))
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1
average = sum / N
print('N = {}, Sum = {}'.format(N, sum))
print('Average = {:.2f}'.format(average))