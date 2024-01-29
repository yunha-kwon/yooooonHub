#(학점 x 과목평점)의 합을 학점의 총합으로 나눈 값
grade_lst = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score_lst = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total_credit = 0
total_score = 0

for i in range(20):
    n = list(map(str, input().split()))
    credit = float(n[1])
    if n[2] == 'P':
        continue
    else:
        score = score_lst[grade_lst.index(n[2])]
        total_score += credit * score
        total_credit += credit

avg = float(total_score / total_credit)
print(avg)
