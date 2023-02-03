def c_dict(file_name):

    dct = {}

    with open(file_name) as file:
        for line in file:
            line_list = line.split(': ')
            dct[line_list[0]] = line_list[1][:-1]

    return dct

seasons = {(12, 1, 2): "зима",
             (3, 4, 5): "весна!",
             (6, 7, 8): "літо",
             (9, 10, 11): "осінь"}