def init_2D_array(rows, columns):
    temp_row_array = []
    temp_col_array = []

    for i in range(0, COLUMNS):
        temp_col_array.append(0)

    for i in range(0, ROWS):
        temp_row_array.append(temp_col_array)

    return temp_row_array

if __name__ == '__main__':
    # ROWS = 3
    # COLUMNS = 4
    #
    # print(init_2D_array(ROWS, COLUMNS))

    # for i in range(5, 0, -1):
    #     print(i)

    # stack = []
    # list = []
    #
    # test_string = '12345'
    # print(test_string[::-1])
    #
    # for i in test_string:
    #     stack.append(i)
    #
    # for i in range(5):
    #     print(stack.pop())
    #
    # test_string_1 = 'cba'
    # print(sorted(test_string_1))

    test_set = set()
    test_set.add(10)
    test_set.add(20)
    test_set.add(30)

    print(test_set)

    if 10 in test_set:
        print("IT IS")
