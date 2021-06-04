link_to_repo = {
    1: print("https://github.com/AlisherKaziz/myAlgorithms/blob/ff43b8129a935fd044ffa1a50b2a89c889767c6b/linearSearch.py")
}
with open("Text.txt", "r") as file:
    line_counter=0
    for line in file:
        print(line, end="")
        line_counter+=1
        if line_counter==14:
            break
user_select = int(input())
