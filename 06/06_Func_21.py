"""function call"""

def read_answers():
    n=int(input())
    answers=[]
    for k in range(n):
        sid,ans=input().split()
        answers.append([sid,ans])
    return answers

def marking(answer,solution):
    score=0
    l=len(answer)
    for i in range(l):
        if answer[i]==solution[i]:
            score+=1
    return score

def grading(score):
    g=[[80,"A"],[70,"B"],
       [60,"C"],[50,"D"]]
    for a,b in g:
        if score>=a:
            return b
    return "F"

def scoring(answers,solution):
    scores=[]
    for sid,ans in answers:
        score=marking(ans,solution)/len(solution)*100
        grade=grading(score)
        scores.append([sid,score,grade])
    return scores

def report(scores):
    for sid,sc,grade in scores:
        print(sid,sc,grade)
        
def sorting(scores):
    x=[]
    for sid,score,grade in scores:
        x.append([score,sid,grade])
    x.sort(reverse=True)
    l=len(x)
    for i in range(l):
        scores[i]=[x[i][1],x[i][0],x[i][2]]
        
solution_ip=input()
ans1=read_answers() #list [sid,ans]
list_score=scoring(ans1,solution_ip) #list [sid,score,grade]
sorting(list_score)
report(list_score)
