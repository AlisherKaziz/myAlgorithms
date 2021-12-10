print("Hello, here I will give a few algorithms I have written:")
while(1):
    with open("Text.txt", "r") as file:
        line_counter = 0
        for line in file:
            print(line, end="")
            line_counter += 1
            if line_counter == 14:
                break
    user_select1 = int(input())
    link_to_repo = {
        1: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/linearSearch.py',
        2: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/binarySearch.py',
        3: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/bubbleSort.py',
        4: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/insertionSort.py',
        5: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/mergeSort.py',
        6: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/quickSOrt.py',
        7: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/heapSort.py',
        8: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/BIS.py'
    }
    try:
        printed_data = link_to_repo[user_select1]
    except KeyError as e:
        raise ValueError('Undefined unit: {}'.format(e.args[0]))
    print(printed_data)
    print("Do you want choose another one? Y/N")
    user_select2 = input()
    if user_select2 == 'Y':
        continue
    else:
        break
