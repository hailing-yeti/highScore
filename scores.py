import random
scores = []

for i in range(11):
    playerScore = random.randint(1,1000)
    print(f"Ooh, {playerScore}, a high score!")
    scores.append(int(playerScore))
print(sorted(scores))

with open('scorecard.txt','w+') as sc:
    sc.write(str(sorted(scores)))
