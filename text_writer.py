import time
import random
import sys
import datetime
x = input("What would you like to write a number of times: ")
y = int(input("How many times should you write it?: "))

executing_list = ['.', '..', '...']
print(f'Executing{random.choice(executing_list)}\n')

if x and y:
    time.sleep(random.randint(0, 5))
elif y == 0:
    print('\n(Error) 0 will not work')
elif x == '':
    print('\n(Error) I don\'t have anything to write!')
elif x == '' and y == 0:
    print('\n(Error) 0 will not works, and I don\' have anything to write')
else:
    print('\n(Error) Please try again')


for i in range(y):
    print(x)
else:
    time.sleep(0.1)
    print(f'\nFinished writing: ' + str(x) + ', ' + str(y) + f' times. \n')
    print('tasks done, now sleeping in 60 seconds')
    time.sleep(10)
    print(f'Sleeping in{random.choice(executing_list)} ')
    for i in range(10, 0, -1):
        sys.stdout.write(str(i) + ' ')
        sys.stdout.flush()
        time.sleep(1)
    print("\nNow displaying time: ")
    while True:
        now = datetime.datetime.now()
        date_time = now.strftime("\nTHE DATE IS: %Y/%m/%d \nTHE TIME IS: %I:%M:%S")
        print(date_time)
        time.sleep(1)
