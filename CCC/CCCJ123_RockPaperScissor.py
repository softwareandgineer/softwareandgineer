N = int(input())
a = input().split()
b = input().split()

aw = 0
bw = 0

for i in range(N):
    if a[i] == "rock" and b[i] == "scissors":
        aw += 1
    elif a[i] == "rock" and b[i] == "paper":
        bw += 1
    elif a[i] == "rock" and b[i] == "rock":
        aw += 0
    elif a[i] == "paper" and b[i] == "scissors":
        bw += 1
    elif a[i] == "paper" and b[i] == "paper":
        aw += 0
    elif a[i] == "paper" and b[i] == "rock":
        aw += 1
    elif a[i] == "scissors" and b[i] == "scissors":
        aw += 0
    elif a[i] == "scissors" and b[i] == "paper":
        aw += 1
    elif a[i] == "scissors" and b[i] == "rock":
        bw += 1

print(aw, bw)




