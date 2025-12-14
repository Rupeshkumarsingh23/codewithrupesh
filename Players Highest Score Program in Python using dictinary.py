players={}
for i in range(5):
    Name=input("Enter player names:")
    runs=int(input("Enter score:"))
    players[Name]=runs
print(players)
print("highest score is",max(players.values()))


