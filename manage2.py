import shutil
import os
import time

def main():
    with open("test.md" , "w") as test_file:
        test_file.write('| Week | Day | Problem Link | Solution | \n')
        test_file.write('| --- | --- | --- | --- | \n')

        for i in range(1,16):
            parent_dir = '.'
            directory = 'week-' + str(i)
            path = os.path.join(parent_dir, directory)
            print(os.listdir(path))

            for day in os.listdir(path=path):
                path2 = os.path.join(path, day)
                print(day , os.listdir(path2))

                for file in os.listdir(path2):
                    print(file)

                    github = f'https://github.com/shahriar100/100_days_LeetCode_challenge/blob/master/{directory}/{day}/{file}'
                    test_file.write(f'| {directory} | {day} | --- | [{file}]({github}) | \n')

if __name__ == '__main__':
    main()
