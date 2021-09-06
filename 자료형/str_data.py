print('I eat %d aplle. \n' % 3)
print('I eat %s aplles.' % 'five')

num = ['2', '3']
message = 'I eat ' + num[1] + ' aplles.'
print(message)

number = 10
day = 'three'
print('I eat %d aplles, so i was sick for %s days' % (number, day))
print('Error is %d%% \n' % 100)

print('I eat {0} apples'.format(3))
print('I eat {0} apples \n'.format('five'))

print('I eat {0} apples'.format(number))
print('I eat {0} apples, so i was sick for {1} days \n'.format(number, day))

print('I eat {number} apples, so i was sick for {day} days'.format(number=10, day='three'))
print(f'I eat {number} apples, so i was sick for {day} days')
print(f'I eat {number+1} apples, so i was sick for {day} days')
