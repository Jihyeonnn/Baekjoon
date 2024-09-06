num = int(input())
answers = []
for _ in range(num):
    a, b = map(int, input().split())
    answers.append(a + b)

for i in range(num):
    print(answers[i])