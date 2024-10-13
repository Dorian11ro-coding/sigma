import webbrowser



num_1 = input("num 1:")

num_2 = input("num 2:")

num_1 = int(num_1)
num_2 = int(num_2)
if num_2!=0:
    print(num_1 / num_2)
elif num_2==0:
    webbrowser.open("https://www.youtube.com/watch?v=lg0-GF6pAsg")