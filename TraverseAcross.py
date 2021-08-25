import os


def ExplorePath(path, deli=False):
    if not deli:
        if 'status.txt' in os.listdir(path):
            if open(path + '\\' + 'status.txt').read() == '100':
                ExplorePath(path, True)
            else:
                return
        else:
            for i in os.listdir(path):
                if os.path.isdir(path + '\\' + i):
                    ExplorePath(path + '\\' + i)
    else:
        for i in os.listdir(path):
            if os.path.isdir(path + '\\' + i):
                ExplorePath(path + '\\' + i, True)
            else:
                if i != 'status.txt':
                    print("Deleting the file - " + path + '\\' + i)
                    #os.remove(path + '\\' + i)

def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    return ans


def factorial2(n):
    if n < 2:
        return 1
    return n * factorial2(n - 1)


# print(factorial2(int(input("Enter the number:"))))

ExplorePath(r"C:\Users\vigne\Desktop\MUREX\Folder")
