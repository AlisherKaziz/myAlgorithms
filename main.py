print("Hello there, here I will provide some algorithms:")
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
        8: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/BIS.py',
        9: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/treeSort.py',
        10: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/QSSLL.py',
        11: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/QSDLL.py',
        12: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/MSLL.py',
        13: 'https://github.com/AlisherKaziz/myAlgorithms/blob/master/listOfAlgorithms/MSDL.py'
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
