score=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
t=int(input())
for i in range(t):
    n,K=map(int,input().split())
    same_grade=int(n/10)
    students={}
    for j in range(n):
        mid_exam,final_exam,homework=map(int,input().split())
        total=mid_exam*35+final_exam*45+homework*20
        students[j+1]=total/100
    
    new_students=sorted(students.items(),key=lambda x:x[1], reverse=True)
    
    
    for m in range(len(score)):
        start=same_grade*m
        finish=same_grade*(m+1)
        for k in range(start,finish):
            students[new_students[k][0]]=[new_students[k][1],score[m]]
    #print(students)
    print(f"#{i+1} {students[K][1]}")
