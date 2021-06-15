from django.shortcuts import render, redirect
from .models import Record


def home(request):
    return render(request, 'main/home.html')

def index(request):
    return render(request, 'main/index -clickcare.html')

def checkup(request):
    return render(request, 'main/checkup.html')

def temp(request):
    return render(request, 'main/temp_elbow_questionnaire.html')

def pain_scale(request):
    return render(request, 'main/pain_scale.html')

def neck_questionnaire(request):
    return render(request, 'main/neck_questionnaire.html')

def shoulder_questionnaire(request):
    return render(request, 'main/shoulder_questionnaire.html')

def results(request):
    return render(request, 'main/results.html')

def back_results(request):
    return render(request, 'main/back/back_results.html')


#Elbow_Questionnaire --------------------------------------------------------------------
def check_elbow_diagA(elbow_questions):
    checker = "1"
    if checker in elbow_questions:
        return 'Tennis Elbow (Lateral Epicondylitis)'
    else:
        return "0"

def check_elbow_diagB(elbow_questions):
    checker = "1"
    if checker in elbow_questions:
        return 'Bursitis (Olecranon)'
    else:
        return "0"

def check_elbow_diagC(elbow_questions):
    checker = "1"
    if checker in elbow_questions:
        return 'Broken/Dislocated Elbow'
    else:
        return "0"

def elbow_questionnaire(request):
    if request.method == "POST":
        elbow_questions = []
        diagnosis = []
        PScale = []
        severity = 0
        n = 0
        y = 0
        scoreA = 0
        scoreB = 0
        scoreC = 0
        scores = []
        for i in range(1,10):
            request.POST.get("elbow_questions"+ str(i))
            print(elbow_questions)
            if i == 3:
                diagnosis.append(check_elbow_diagA(elbow_questions[0:2]))
            elif i == 6:
                diagnosis.append(check_elbow_diagB(elbow_questions[3:4]))
            elif i == 9:
                diagnosis.append(check_elbow_diagC(elbow_questions[5:8]))
            current_question = request.POST.get("elbow_questions"+ str(i))
            current_painscale = request.POST.get("painscale"+ str(i))
            elbow_questions.append(current_question)
            if current_question == "1":
                PScale.append(current_painscale)
            else:
                PScale.append("0") 
        print(elbow_questions)
        print(PScale)  
        for x in range (1, 4):
            current_question = request.POST.get("elbow_questions"+ str(x))
            if current_question == "1":
                y = x - 1
                severity = (severity + int(PScale[y]))
                n += 1
                scoreA = severity / n
            else:
                severity += 0
        scores.append(scoreA)
        for x in range (5, 6):
            current_question = request.POST.get("elbow_questions"+ str(x))
            if current_question == "1":
                y = x - 1
                severity = (severity + int(PScale[y]))
                n += 1
                scoreB = severity / n
                
            else:
             severity += 0
        scores.append(scoreB)
        for x in range (7, 10):
            current_question = request.POST.get("elbow_questions"+ str(x))
            if current_question == "1":
                y = x - 1
                severity = (severity + int(PScale[y]))
                n += 1
                scoreC = severity / n
                
            else:
                severity += 0
        scores.append(scoreC)
        context = {
            "first": diagnosis[0], "second": diagnosis[1], "third": diagnosis[2],
            'scoreA' : scores[0], 'scoreB' : scores[1], 'scoreC' : scores[2],
            }
        return render(request, 'main/results.html', context)
    else:
        return render(request, 'main/elbow/elbow_questionnaire.html')
       

#End of Elbow Questionnaire ---------------------------------------------------------------



#back_Questionnaire --------------------------------------------------------------------
def back_A_list(back_questions):
    back_indices_to_access_A = [0, 2, 4]
    back_accessed_mapping_A = map(back_questions.__getitem__, back_indices_to_access_A)
    back_accessed_list_A = list(back_accessed_mapping_A)
    return back_accessed_list_A

def back_B_list(back_questions):
    back_indices_to_access_B = [1, 2, 3, 6]
    back_accessed_mapping_B = map(back_questions.__getitem__, back_indices_to_access_B)
    back_accessed_list_B = list(back_accessed_mapping_B)
    return back_accessed_list_B

def back_C_list(back_questions):
    back_indices_to_access_C = [0, 1, 4, 5, 8, 9]
    back_accessed_mapping_C = map(back_questions.__getitem__, back_indices_to_access_C)
    back_accessed_list_C = list(back_accessed_mapping_C)
    return back_accessed_list_C

def back_D_list(back_questions):
    back_indices_to_access_D = [1, 4, 5, 6, 7]
    back_accessed_mapping_D = map(back_questions.__getitem__, back_indices_to_access_D)
    back_accessed_list_D = list(back_accessed_mapping_D)
    return back_accessed_list_D


def painscale_back_A_list(painscale):
    painscale_back_indices_to_access_A = [0, 2, 4]
    painscale_back_accessed_mapping_A = map(painscale.__getitem__, painscale_back_indices_to_access_A)
    painscale_back_accessed_list_A = list(painscale_back_accessed_mapping_A)
    return painscale_back_accessed_list_A

def painscale_back_B_list(painscale):
    painscale_back_indices_to_access_B = [1, 2, 3, 6]
    painscale_back_accessed_mapping_B = map(painscale.__getitem__, painscale_back_indices_to_access_B)
    painscale_back_accessed_list_B = list(painscale_back_accessed_mapping_B)
    return painscale_back_accessed_list_B

def painscale_back_C_list(painscale):
    painscale_back_indices_to_access_C = [0, 1, 4, 5, 8, 9]
    painscale_back_accessed_mapping_C = map(painscale.__getitem__, painscale_back_indices_to_access_C)
    painscale_back_accessed_list_C = list(painscale_back_accessed_mapping_C)
    return painscale_back_accessed_list_C

def painscale_back_D_list(painscale):
    painscale_back_indices_to_access_D = [1, 4, 5, 6, 7]
    painscale_back_accessed_mapping_D = map(painscale.__getitem__, painscale_back_indices_to_access_D)
    painscale_back_accessed_list_D = list(painscale_back_accessed_mapping_D)
    return painscale_back_accessed_list_D


def check_back_diagA(back_questions):
    checker = "1"
    if checker in back_questions:
        return 'Thoracic (Upper Back) Strain'
    else:
        return "0"

def check_back_diagB(back_questions):
    checker = "1"
    if checker in back_questions:
        return 'Spinal Osteoarthritis'
    else:
        return "0"

def check_back_diagC(back_questions):
    checker = "1"
    if checker in back_questions:
        return 'Scoliosis'
    else:
        return "0"

def check_back_diagD(back_questions):
    checker = "1"
    if checker in back_questions:
        return 'Sciatica'
    else:
        return "0"

def back_questionnaire(request):
    if request.method == "POST":
        back_questions = []
        diagnosis = []
        painscale = []
        severity = 0
        n = 0
        back_scoreA = 0
        back_scoreB = 0
        back_scoreC = 0
        back_scoreD = 0
        back_scores = []
        for i in range(1,11):
            request.POST.get("back_questions"+ str(i))
            current_question = request.POST.get("back_questions"+ str(i))
            current_painscale = request.POST.get("painscale"+ str(i))
            back_questions.append(current_question)
            if current_question == "1":
                painscale.append(current_painscale)
            else:
                painscale.append("0")

        var_back_A_list = back_A_list(back_questions)
        var_back_B_list = back_B_list(back_questions)
        var_back_C_list = back_C_list(back_questions)
        var_back_D_list = back_D_list(back_questions)

        var_painscale_back_A_list = painscale_back_A_list(painscale)
        var_painscale_back_B_list = painscale_back_B_list(painscale)
        var_painscale_back_C_list = painscale_back_C_list(painscale)
        var_painscale_back_D_list = painscale_back_D_list(painscale)

        diagnosis.append(check_back_diagA(var_back_A_list))
        diagnosis.append(check_back_diagB(var_back_B_list))
        diagnosis.append(check_back_diagC(var_back_C_list)) 
        diagnosis.append(check_back_diagD(var_back_D_list)) 
        
        print(back_questions)
        print(painscale) 
        print(diagnosis) 
        print(var_painscale_back_A_list)
        print(var_painscale_back_B_list)
        print(var_painscale_back_C_list)
        print(var_painscale_back_D_list)
        

        for x in range (0, 3):
            if var_back_A_list[x] == 1:
                severity = severity + int(var_painscale_back_A_list[x])
                n += 1
                back_scoreA = severity / n
            else:
                pass
                
        back_scores.append(back_scoreA)
        print(back_scoreA)
        

        for x in range (0, 4):
            if var_back_B_list[x] == 1:
                severity = severity + int(var_painscale_back_B_list[x])
                n += 1
                back_scoreB = severity / n
            else:
                pass
                
        back_scores.append(back_scoreB)
        print(back_scoreB)

        for x in range (0, 5):
            if var_back_C_list[x] == 1:
                severity = severity + int(var_painscale_back_C_list[x])
                n += 1
                back_scoreB = severity / n
            else:
                pass
                
        back_scores.append(back_scoreC)
        print(back_scoreC)

        for x in range (0, 5):
            if var_back_D_list[x] == 1:
                severity = severity + int(var_painscale_back_D_list[x])
                n += 1
                back_scoreD = severity / n
            else:
                pass
                
        back_scores.append(back_scoreD)
        print(back_scoreD)

        context = {
            "first": diagnosis[0], "second": diagnosis[1], "third": diagnosis[2], "fourth": diagnosis[3],
            'back_scoreA' : back_scores[0], 'back_scoreB' : back_scores[1], 'back_scoreC' : back_scores[2], 'back_scoreD' : back_scores[3],
            }
        return render(request, 'main/back/back_results.html', context)
    else:
        return render(request, 'main/back/back_questionnaire.html')

#End of Back Questionnaire ---------------------------------------------------------------


def wrist_questionnaire(request):
    return render(request, 'main/wrist_questionnaire.html')

def hnf_questionnaire(request):
    return render(request, 'main/hnf_questionnaire.html')

