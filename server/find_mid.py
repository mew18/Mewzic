def mid_exist():
    from os import path,walk
    dir_path = path.dirname(path.realpath(__file__))
    for root, dirs, files in walk(dir_path):
        for file in files:
            if file.endswith('.mid'):
                return True

# print(mid_exist())