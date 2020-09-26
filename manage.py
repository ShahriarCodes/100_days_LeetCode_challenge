import shutil
import os
import time

def main():
    print('---creating directories---')
    parent_dir = '.'
    directory = 'week-'
    Day = 100
    for i in range(1,16):
        path = os.path.join(parent_dir, directory+ f'{i}')
        os.mkdir(path)
    
    print('---done creating dirs----')
    print(os.listdir('.'))
    time.sleep(5)

    print('---moving files-----')
    directory = 'week-1'
    j = 0
    folder_name = 'Day_'
    week = 1
    for i in range(1,76):
        folder_name = f'Day_{i}'
        shutil.move(folder_name, directory)
        j += 1 
        if j % 7 == 0:
            week += 1
            directory ='week-' + str(week)
            j = 0
    print('---done moving files---')

if __name__ == '__main__':
    main()
