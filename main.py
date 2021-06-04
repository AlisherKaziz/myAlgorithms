print("Hello there, here I will provide some algorithms:")
with open("Text.txt", "r") as file:
    line_counter = 0
    for line in file:
        print(line, end="")
        line_counter += 1
        if line_counter == 14:
            break
user_select = int(input())
link_to_repo = {
    1: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/linearSearch.py',
    2: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/binarySearch.py',
    3: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/bubbleSort.py',
    4: '',
    5: '',
    6: '',
    7: '',
    8: '',
    9: '',
    10: '',
    11: '',
    12: '',
    13: ''
}
try:
    printed_data = link_to_repo[user_select]
except KeyError as e:
    raise ValueError('Undefined unit: {}'.format(e.args[0]))
print(printed_data)
