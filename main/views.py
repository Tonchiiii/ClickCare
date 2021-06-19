from django.shortcuts import render, redirect
from .models import Record


def home(request):
    return render(request, 'main/home.html')

def index(request):
    return render(request, 'main/index -clickcare.html')

def checkup(request):
    return render(request, 'main/checkup.html')

def MSDs(request):
    return render(request, 'main/MSDs.html')

def elbow(request):
    return render(request, 'main/elbow/elbow.html')

def elbow_results(request):
    return render(request, 'main/elbow/elbow_results.html')

def back_results(request):
    return render(request, 'main/back/back_results.html')

def hipthigh_results(request):
    return render(request, 'main/hipthigh/hipthigh_results.html')

def kneelowerleg_results(request):
    return render(request, 'main/kneelowerleg/kneelowerleg_results.html')

def wristhand_results(request):
    return render(request, 'main/wristhand/wristhand_results.html')

#Neck_Questionnaire --------------------------------------------------------------------
def neck_A_list(neck_questions):
    neck_indices_to_access_A = [0, 1, 2]
    neck_accessed_mapping_A = map(neck_questions.__getitem__, neck_indices_to_access_A)
    neck_accessed_list_A = list(neck_accessed_mapping_A)
    return neck_accessed_list_A

def neck_B_list(neck_questions):
    neck_indices_to_access_B = [0, 2, 4]
    neck_accessed_mapping_B = map(neck_questions.__getitem__, neck_indices_to_access_B)
    neck_accessed_list_B = list(neck_accessed_mapping_B)
    return neck_accessed_list_B

def neck_C_list(neck_questions):
    neck_indices_to_access_C = [0, 1, 3, 5, 6]
    neck_accessed_mapping_C = map(neck_questions.__getitem__, neck_indices_to_access_C)
    neck_accessed_list_C = list(neck_accessed_mapping_C)
    return neck_accessed_list_C

def neck_D_list(neck_questions):
    neck_indices_to_access_D = [1, 3]
    neck_accessed_mapping_D = map(neck_questions.__getitem__, neck_indices_to_access_D)
    neck_accessed_list_D = list(neck_accessed_mapping_D)
    return neck_accessed_list_D

def neck_E_list(neck_questions):
    neck_indices_to_access_E = [1, 3, 7, 8, 9]
    neck_accessed_mapping_E = map(neck_questions.__getitem__, neck_indices_to_access_E)
    neck_accessed_list_E = list(neck_accessed_mapping_E)
    return neck_accessed_list_E


def painscale_neck_A_list(painscale):
    painscale_neck_indices_to_access_A = [0, 1, 2]
    painscale_neck_accessed_mapping_A = map(painscale.__getitem__, painscale_neck_indices_to_access_A)
    painscale_neck_accessed_list_A = list(painscale_neck_accessed_mapping_A)
    return painscale_neck_accessed_list_A

def painscale_neck_B_list(painscale):
    painscale_neck_indices_to_access_B = [0, 2, 4]
    painscale_neck_accessed_mapping_B = map(painscale.__getitem__, painscale_neck_indices_to_access_B)
    painscale_neck_accessed_list_B = list(painscale_neck_accessed_mapping_B)
    return painscale_neck_accessed_list_B

def painscale_neck_C_list(painscale):
    painscale_neck_indices_to_access_C = [0, 1, 3, 5, 6]
    painscale_neck_accessed_mapping_C = map(painscale.__getitem__, painscale_neck_indices_to_access_C)
    painscale_neck_accessed_list_C = list(painscale_neck_accessed_mapping_C)
    return painscale_neck_accessed_list_C

def painscale_neck_D_list(painscale):
    painscale_neck_indices_to_access_D = [1, 3]
    painscale_neck_accessed_mapping_D = map(painscale.__getitem__, painscale_neck_indices_to_access_D)
    painscale_neck_accessed_list_D = list(painscale_neck_accessed_mapping_D)
    return painscale_neck_accessed_list_D

def painscale_neck_E_list(painscale):
    painscale_neck_indices_to_access_E = [1, 3, 7, 8, 9]
    painscale_neck_accessed_mapping_E = map(painscale.__getitem__, painscale_neck_indices_to_access_E)
    painscale_neck_accessed_list_E = list(painscale_neck_accessed_mapping_E)
    return painscale_neck_accessed_list_E


def check_neck_diagA(neck_questions):
    checker = "1"
    if checker in neck_questions:
        return 'Neck Strain'
    else:
        return "0"

def check_neck_diagB(neck_questions):
    checker = "1"
    if checker in neck_questions:
        return 'Torticollis'
    else:
        return "0"

def check_neck_diagC(neck_questions):
    checker = "1"
    if checker in neck_questions:
        return 'Cervical (Neck) Spondylosis'
    else:
        return "0"

def check_neck_diagD(neck_questions):
    checker = "1"
    if checker in neck_questions:
        return 'Cervical (Neck) Herniated Disc'
    else:
        return "0"

def check_neck_diagE(neck_questions):
    checker = "1"
    if checker in neck_questions:
        return 'Broken Neck'
    else:
        return "0"

def neck_questionnaire(request):
    if request.method == "POST":
        neck_questions = []
        diagnosis = []
        painscale = []
        severity = 0
        n = 0
        neck_scoreA = 0
        neck_scoreB = 0
        neck_scoreC = 0
        neck_scoreD = 0
        neck_scoreE = 0
        neck_scores = []
        for i in range(1,11):
            request.POST.get("neck_questions"+ str(i))
            current_question = request.POST.get("neck_questions"+ str(i))
            current_painscale = request.POST.get("painscale"+ str(i))
            neck_questions.append(current_question)
            if current_question == "1":
                painscale.append(current_painscale)
            else:
                painscale.append("0")

        var_neck_A_list = neck_A_list(neck_questions)
        var_neck_B_list = neck_B_list(neck_questions)
        var_neck_C_list = neck_C_list(neck_questions)
        var_neck_D_list = neck_D_list(neck_questions)
        var_neck_E_list = neck_E_list(neck_questions)

        var_painscale_neck_A_list = painscale_neck_A_list(painscale)
        var_painscale_neck_B_list = painscale_neck_B_list(painscale)
        var_painscale_neck_C_list = painscale_neck_C_list(painscale)
        var_painscale_neck_D_list = painscale_neck_D_list(painscale)
        var_painscale_neck_E_list = painscale_neck_E_list(painscale)

        diagnosis.append(check_neck_diagA(var_neck_A_list))
        diagnosis.append(check_neck_diagB(var_neck_B_list))
        diagnosis.append(check_neck_diagC(var_neck_C_list)) 
        diagnosis.append(check_neck_diagD(var_neck_D_list)) 
        diagnosis.append(check_neck_diagD(var_neck_E_list)) 
        
        print("THIS IS neck QUESTION")
        print(neck_questions)
        print(painscale) 
        print(diagnosis) 
        print("THIS var_neck_alist")
        print(var_neck_A_list)
        print(var_neck_B_list)
        print(var_neck_C_list)
        print(var_neck_D_list)
        print(var_neck_E_list)
        print("THIS IS PAINSCALE")
        print(var_painscale_neck_A_list)
        print(var_painscale_neck_B_list)
        print(var_painscale_neck_C_list)
        print(var_painscale_neck_D_list)
        print(var_painscale_neck_E_list)


        for choice_1 in var_neck_A_list:
            if choice_1 == "1":
                severity = severity + int(var_painscale_neck_A_list[n])
                n = n + 1
                neck_scoreA = severity / n
                print("THIS IS neckSCOREA")
                print(neck_scoreA)
            else:
                pass
                
        neck_scores.append(neck_scoreA)
        print(neck_scoreA)
        
        n = 0
        severity = 0
        for choice_2 in var_neck_B_list:
            if choice_2 == "1":
                severity = severity + int(var_painscale_neck_B_list[n])
                n += 1
                neck_scoreB = severity / n
            else:
                pass
                
        neck_scores.append(neck_scoreB)
        print(neck_scoreB)

        n = 0
        severity = 0
        for choice_3 in var_neck_C_list:
            if choice_3 == "1":
                severity = severity + int(var_painscale_neck_C_list[n])
                n += 1
                neck_scoreC = severity / n
            else:
                pass
                
        neck_scores.append(neck_scoreC)
        print(neck_scoreC)

        n = 0
        severity = 0
        for choice_4 in var_neck_D_list:
            if choice_4 == "1":
                severity = severity + int(var_painscale_neck_D_list[n])
                n += 1
                neck_scoreD = severity / n
            else:
                pass
                
        neck_scores.append(neck_scoreD)
        print(neck_scoreD)

        n = 0
        severity = 0
        for choice_5 in var_neck_E_list:
            if choice_5 == "1":
                severity = severity + int(var_painscale_neck_E_list[n])
                n += 1
                neck_scoreE = severity / n
            else:
                pass
                
        neck_scores.append(neck_scoreE)
        print(neck_scoreE)

        context = {
            "first": diagnosis[0], "second": diagnosis[1], "third": diagnosis[2], "fourth": diagnosis[3], "fifth": diagnosis[4],
            'neck_scoreA' : neck_scores[0], 'neck_scoreB' : neck_scores[1], 'neck_scoreC' : neck_scores[2], 'neck_scoreD' : neck_scores[3], 'neck_scoreE' : neck_scores[4],
            }
        return render(request, 'main/neck/neck_results.html', context)
    else:
        return render(request, 'main/neck/neck_questionnaire.html')

#End of Neck Questionnaire ---------------------------------------------------------------

#Shoulder_Questionnaire --------------------------------------------------------------------
def shoulder_A_list(shoulder_questions):
    shoulder_indices_to_access_A = [0, 1, 2, 3, 4, 5, 6]
    shoulder_accessed_mapping_A = map(shoulder_questions.__getitem__, shoulder_indices_to_access_A)
    shoulder_accessed_list_A = list(shoulder_accessed_mapping_A)
    return shoulder_accessed_list_A

def shoulder_B_list(shoulder_questions):
    shoulder_indices_to_access_B = [0, 1, 3, 4]
    shoulder_accessed_mapping_B = map(shoulder_questions.__getitem__, shoulder_indices_to_access_B)
    shoulder_accessed_list_B = list(shoulder_accessed_mapping_B)
    return shoulder_accessed_list_B

def shoulder_C_list(shoulder_questions):
    shoulder_indices_to_access_C = [0, 1, 2, 3, 5, 6, 7]
    shoulder_accessed_mapping_C = map(shoulder_questions.__getitem__, shoulder_indices_to_access_C)
    shoulder_accessed_list_C = list(shoulder_accessed_mapping_C)
    return shoulder_accessed_list_C

def shoulder_D_list(shoulder_questions):
    shoulder_indices_to_access_D = [8, 9, 10]
    shoulder_accessed_mapping_D = map(shoulder_questions.__getitem__, shoulder_indices_to_access_D)
    shoulder_accessed_list_D = list(shoulder_accessed_mapping_D)
    return shoulder_accessed_list_D

def shoulder_E_list(shoulder_questions):
    shoulder_indices_to_access_E = [2, 8, 9, 10]
    shoulder_accessed_mapping_E = map(shoulder_questions.__getitem__, shoulder_indices_to_access_E)
    shoulder_accessed_list_E = list(shoulder_accessed_mapping_E)
    return shoulder_accessed_list_E


def painscale_shoulder_A_list(painscale):
    painscale_shoulder_indices_to_access_A = [0, 1, 2, 3, 4, 5, 6]
    painscale_shoulder_accessed_mapping_A = map(painscale.__getitem__, painscale_shoulder_indices_to_access_A)
    painscale_shoulder_accessed_list_A = list(painscale_shoulder_accessed_mapping_A)
    return painscale_shoulder_accessed_list_A

def painscale_shoulder_B_list(painscale):
    painscale_shoulder_indices_to_access_B = [0, 1, 3, 4]
    painscale_shoulder_accessed_mapping_B = map(painscale.__getitem__, painscale_shoulder_indices_to_access_B)
    painscale_shoulder_accessed_list_B = list(painscale_shoulder_accessed_mapping_B)
    return painscale_shoulder_accessed_list_B

def painscale_shoulder_C_list(painscale):
    painscale_shoulder_indices_to_access_C = [0, 1, 2, 3, 5, 6, 7]
    painscale_shoulder_accessed_mapping_C = map(painscale.__getitem__, painscale_shoulder_indices_to_access_C)
    painscale_shoulder_accessed_list_C = list(painscale_shoulder_accessed_mapping_C)
    return painscale_shoulder_accessed_list_C

def painscale_shoulder_D_list(painscale):
    painscale_shoulder_indices_to_access_D = [8, 9, 10]
    painscale_shoulder_accessed_mapping_D = map(painscale.__getitem__, painscale_shoulder_indices_to_access_D)
    painscale_shoulder_accessed_list_D = list(painscale_shoulder_accessed_mapping_D)
    return painscale_shoulder_accessed_list_D

def painscale_shoulder_E_list(painscale):
    painscale_shoulder_indices_to_access_E = [2, 8, 9, 10]
    painscale_shoulder_accessed_mapping_E = map(painscale.__getitem__, painscale_shoulder_indices_to_access_E)
    painscale_shoulder_accessed_list_E = list(painscale_shoulder_accessed_mapping_E)
    return painscale_shoulder_accessed_list_E


def check_shoulder_diagA(shoulder_questions):
    checker = "1"
    if checker in shoulder_questions:
        return 'Rotator Cuff Tendinitis'
    else:
        return "0"

def check_shoulder_diagB(shoulder_questions):
    checker = "1"
    if checker in shoulder_questions:
        return 'Frozen Shoulder'
    else:
        return "0"

def check_shoulder_diagC(shoulder_questions):
    checker = "1"
    if checker in shoulder_questions:
        return 'Labrum Tear'
    else:
        return "0"

def check_shoulder_diagD(shoulder_questions):
    checker = "1"
    if checker in shoulder_questions:
        return 'Dislocated Shoulder'
    else:
        return "0"

def check_shoulder_diagE(shoulder_questions):
    checker = "1"
    if checker in shoulder_questions:
        return 'Separated Shoulder'
    else:
        return "0"

def shoulder_questionnaire(request):
    if request.method == "POST":
        shoulder_questions = []
        diagnosis = []
        painscale = []
        severity = 0
        n = 0
        shoulder_scoreA = 0
        shoulder_scoreB = 0
        shoulder_scoreC = 0
        shoulder_scoreD = 0
        shoulder_scoreE = 0
        shoulder_scores = []
        for i in range(1,12):
            request.POST.get("shoulder_questions"+ str(i))
            current_question = request.POST.get("shoulder_questions"+ str(i))
            current_painscale = request.POST.get("painscale"+ str(i))
            shoulder_questions.append(current_question)
            if current_question == "1":
                painscale.append(current_painscale)
            else:
                painscale.append("0")

        var_shoulder_A_list = shoulder_A_list(shoulder_questions)
        var_shoulder_B_list = shoulder_B_list(shoulder_questions)
        var_shoulder_C_list = shoulder_C_list(shoulder_questions)
        var_shoulder_D_list = shoulder_D_list(shoulder_questions)
        var_shoulder_E_list = shoulder_E_list(shoulder_questions)

        var_painscale_shoulder_A_list = painscale_shoulder_A_list(painscale)
        var_painscale_shoulder_B_list = painscale_shoulder_B_list(painscale)
        var_painscale_shoulder_C_list = painscale_shoulder_C_list(painscale)
        var_painscale_shoulder_D_list = painscale_shoulder_D_list(painscale)
        var_painscale_shoulder_E_list = painscale_shoulder_E_list(painscale)

        diagnosis.append(check_shoulder_diagA(var_shoulder_A_list))
        diagnosis.append(check_shoulder_diagB(var_shoulder_B_list))
        diagnosis.append(check_shoulder_diagC(var_shoulder_C_list)) 
        diagnosis.append(check_shoulder_diagD(var_shoulder_D_list)) 
        diagnosis.append(check_shoulder_diagD(var_shoulder_E_list)) 
        
        print("THIS IS shoulder QUESTION")
        print(shoulder_questions)
        print(painscale) 
        print(diagnosis) 
        print("THIS var_shoulder_alist")
        print(var_shoulder_A_list)
        print(var_shoulder_B_list)
        print(var_shoulder_C_list)
        print(var_shoulder_D_list)
        print(var_shoulder_E_list)
        print("THIS IS PAINSCALE")
        print(var_painscale_shoulder_A_list)
        print(var_painscale_shoulder_B_list)
        print(var_painscale_shoulder_C_list)
        print(var_painscale_shoulder_D_list)
        print(var_painscale_shoulder_E_list)


        for choice_1 in var_shoulder_A_list:
            if choice_1 == "1":
                severity = severity + int(var_painscale_shoulder_A_list[n])
                n = n + 1
                shoulder_scoreA = severity / n
                print("THIS IS shoulderSCOREA")
                print(shoulder_scoreA)
            else:
                pass
                
        shoulder_scores.append(shoulder_scoreA)
        print(shoulder_scoreA)
        
        n = 0
        severity = 0
        for choice_2 in var_shoulder_B_list:
            if choice_2 == "1":
                severity = severity + int(var_painscale_shoulder_B_list[n])
                n += 1
                shoulder_scoreB = severity / n
            else:
                pass
                
        shoulder_scores.append(shoulder_scoreB)
        print(shoulder_scoreB)

        n = 0
        severity = 0
        for choice_3 in var_shoulder_C_list:
            if choice_3 == "1":
                severity = severity + int(var_painscale_shoulder_C_list[n])
                n += 1
                shoulder_scoreC = severity / n
            else:
                pass
                
        shoulder_scores.append(shoulder_scoreC)
        print(shoulder_scoreC)

        n = 0
        severity = 0
        for choice_4 in var_shoulder_D_list:
            if choice_4 == "1":
                severity = severity + int(var_painscale_shoulder_D_list[n])
                n += 1
                shoulder_scoreD = severity / n
            else:
                pass
                
        shoulder_scores.append(shoulder_scoreD)
        print(shoulder_scoreD)

        n = 0
        severity = 0
        for choice_5 in var_shoulder_E_list:
            if choice_5 == "1":
                severity = severity + int(var_painscale_shoulder_E_list[n])
                n += 1
                shoulder_scoreE = severity / n
            else:
                pass
                
        shoulder_scores.append(shoulder_scoreE)
        print(shoulder_scoreE)

        context = {
            "first": diagnosis[0], "second": diagnosis[1], "third": diagnosis[2], "fourth": diagnosis[3], "fifth": diagnosis[4],
            'shoulder_scoreA' : shoulder_scores[0], 'shoulder_scoreB' : shoulder_scores[1], 'shoulder_scoreC' : shoulder_scores[2], 'shoulder_scoreD' : shoulder_scores[3], 'shoulder_scoreE' : shoulder_scores[4],
            }
        return render(request, 'main/shoulder/shoulder_results.html', context)
    else:
        return render(request, 'main/shoulder/shoulder_questionnaire.html')

#End of Shoulder Questionnaire ---------------------------------------------------------------


#Elbow_Questionnaire --------------------------------------------------------------------
def check_elbow_diagA(elbow_questions):
    checker = "1"
    if checker in elbow_questions:
        return 'Rotator Cuff Tendinitis'
    else:
        return "0"

def check_elbow_diagB(elbow_questions):
    checker = "1"
    if checker in elbow_questions:
        return 'Frozen Shoulder'
    else:
        return "0"

def check_elbow_diagC(elbow_questions):
    checker = "1"
    if checker in elbow_questions:
        return 'Labrum Tear'
    else:
        return "0"

def check_elbow_diagD(elbow_questions):
    checker = "1"
    if checker in elbow_questions:
        return 'Dislocated Shoulder'
    else:
        return "0"

def check_elbow_diagE(elbow_questions):
    checker = "1"
    if checker in elbow_questions:
        return 'Separated Shoulder'
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
        return render(request, 'main/elbow/elbow_results.html', context)
    else:
        return render(request, 'main/elbow/elbow_questionnaire.html')
       

#End of Elbow Questionnaire ---------------------------------------------------------------



#Back_Questionnaire --------------------------------------------------------------------
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
        
        print("THIS IS BACK QUESTION")
        print(back_questions)
        print(painscale) 
        print(diagnosis) 
        print("THIS var_back_alist")
        print(var_back_A_list)
        print(var_back_B_list)
        print(var_back_C_list)
        print(var_back_D_list)
        print("THIS IS PAINSCALE")
        print(var_painscale_back_A_list)
        print(var_painscale_back_B_list)
        print(var_painscale_back_C_list)
        print(var_painscale_back_D_list)


        for choice_1 in var_back_A_list:
            if choice_1 == "1":
                severity = severity + int(var_painscale_back_A_list[n])
                n = n + 1
                back_scoreA = severity / n
                print("THIS IS BACKSCOREA")
                print(back_scoreA)
            else:
                pass
                
        back_scores.append(back_scoreA)
        print(back_scoreA)
        
        n = 0
        severity = 0
        for choice_2 in var_back_B_list:
            if choice_2 == "1":
                severity = severity + int(var_painscale_back_B_list[n])
                n += 1
                back_scoreB = severity / n
            else:
                pass
                
        back_scores.append(back_scoreB)
        print(back_scoreB)

        n = 0
        severity = 0
        for choice_3 in var_back_C_list:
            if choice_3 == "1":
                severity = severity + int(var_painscale_back_C_list[n])
                n += 1
                back_scoreC = severity / n
            else:
                pass
                
        back_scores.append(back_scoreC)
        print(back_scoreC)

        n = 0
        severity = 0
        for choice_4 in var_back_D_list:
            if choice_4 == "1":
                severity = severity + int(var_painscale_back_D_list[n])
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


#Hipthigh Questionnaire ------------------------------------------------------------------
def hipthigh_A_list(hipthigh_questions):
    hipthigh_indices_to_access_A = [0, 1, 2, 3]
    hipthigh_accessed_mapping_A = map(hipthigh_questions.__getitem__, hipthigh_indices_to_access_A)
    hipthigh_accessed_list_A = list(hipthigh_accessed_mapping_A)
    return hipthigh_accessed_list_A

def hipthigh_B_list(hipthigh_questions):
    hipthigh_indices_to_access_B = [0, 1, 4, 7]
    hipthigh_accessed_mapping_B = map(hipthigh_questions.__getitem__, hipthigh_indices_to_access_B)
    hipthigh_accessed_list_B = list(hipthigh_accessed_mapping_B)
    return hipthigh_accessed_list_B

def hipthigh_C_list(hipthigh_questions):
    hipthigh_indices_to_access_C = [0, 1, 8]
    hipthigh_accessed_mapping_C = map(hipthigh_questions.__getitem__, hipthigh_indices_to_access_C)
    hipthigh_accessed_list_C = list(hipthigh_accessed_mapping_C)
    return hipthigh_accessed_list_C

def hipthigh_D_list(hipthigh_questions):
    hipthigh_indices_to_access_D = [3, 5, 6]
    hipthigh_accessed_mapping_D = map(hipthigh_questions.__getitem__, hipthigh_indices_to_access_D)
    hipthigh_accessed_list_D = list(hipthigh_accessed_mapping_D)
    return hipthigh_accessed_list_D

def hipthigh_E_list(hipthigh_questions):
    hipthigh_indices_to_access_E = [0, 2, 3, 4]
    hipthigh_accessed_mapping_E = map(hipthigh_questions.__getitem__, hipthigh_indices_to_access_E)
    hipthigh_accessed_list_E = list(hipthigh_accessed_mapping_E)
    return hipthigh_accessed_list_E


def painscale_hipthigh_A_list(painscale):
    painscale_hipthigh_indices_to_access_A = [0, 1, 2, 3]
    painscale_hipthigh_accessed_mapping_A = map(painscale.__getitem__, painscale_hipthigh_indices_to_access_A)
    painscale_hipthigh_accessed_list_A = list(painscale_hipthigh_accessed_mapping_A)
    return painscale_hipthigh_accessed_list_A

def painscale_hipthigh_B_list(painscale):
    painscale_hipthigh_indices_to_access_B = [0, 1, 4, 7]
    painscale_hipthigh_accessed_mapping_B = map(painscale.__getitem__, painscale_hipthigh_indices_to_access_B)
    painscale_hipthigh_accessed_list_B = list(painscale_hipthigh_accessed_mapping_B)
    return painscale_hipthigh_accessed_list_B

def painscale_hipthigh_C_list(painscale):
    painscale_hipthigh_indices_to_access_C = [0, 1, 8]
    painscale_hipthigh_accessed_mapping_C = map(painscale.__getitem__, painscale_hipthigh_indices_to_access_C)
    painscale_hipthigh_accessed_list_C = list(painscale_hipthigh_accessed_mapping_C)
    return painscale_hipthigh_accessed_list_C

def painscale_hipthigh_D_list(painscale):
    painscale_hipthigh_indices_to_access_D = [3, 5, 6]
    painscale_hipthigh_accessed_mapping_D = map(painscale.__getitem__, painscale_hipthigh_indices_to_access_D)
    painscale_hipthigh_accessed_list_D = list(painscale_hipthigh_accessed_mapping_D)
    return painscale_hipthigh_accessed_list_D

def painscale_hipthigh_E_list(painscale):
    painscale_hipthigh_indices_to_access_E = [0, 2, 3, 4]
    painscale_hipthigh_accessed_mapping_E = map(painscale.__getitem__, painscale_hipthigh_indices_to_access_E)
    painscale_hipthigh_accessed_list_E = list(painscale_hipthigh_accessed_mapping_E)
    return painscale_hipthigh_accessed_list_E


def check_hipthigh_diagA(hipthigh_questions):
    checker = "1"
    if checker in hipthigh_questions:
        return 'Hip Strain/Sprain'
    else:
        return "0"

def check_hipthigh_diagB(hipthigh_questions):
    checker = "1"
    if checker in hipthigh_questions:
        return 'Hip Dislocation'
    else:
        return "0"

def check_hipthigh_diagC(hipthigh_questions):
    checker = "1"
    if checker in hipthigh_questions:
        return 'Hamstring Muscle Injury'
    else:
        return "0"

def check_hipthigh_diagD(hipthigh_questions):
    checker = "1"
    if checker in hipthigh_questions:
        return 'Ischial Bursitis'
    else:
        return "0"

def check_hipthigh_diagE(hipthigh_questions):
    checker = "1"
    if checker in hipthigh_questions:
        return 'Hip (Acetabular) Labral Tear'
    else:
        return "0"


def hipthigh_questionnaire(request):
    if request.method == "POST":
        hipthigh_questions = []
        diagnosis = []
        painscale = []
        severity = 0
        n = 0
        hipthigh_scoreA = 0
        hipthigh_scoreB = 0
        hipthigh_scoreC = 0
        hipthigh_scoreD = 0
        hipthigh_scoreE = 0
        hipthigh_scores = []
        for i in range(1,10):
            request.POST.get("hipthigh_questions"+ str(i))
            current_question = request.POST.get("hipthigh_questions"+ str(i))
            current_painscale = request.POST.get("painscale"+ str(i))
            hipthigh_questions.append(current_question)
            if current_question == "1":
                painscale.append(current_painscale)
            else:
                painscale.append("0")

        var_hipthigh_A_list = hipthigh_A_list(hipthigh_questions)
        var_hipthigh_B_list = hipthigh_B_list(hipthigh_questions)
        var_hipthigh_C_list = hipthigh_C_list(hipthigh_questions)
        var_hipthigh_D_list = hipthigh_D_list(hipthigh_questions)
        var_hipthigh_E_list = hipthigh_E_list(hipthigh_questions)

        var_painscale_hipthigh_A_list = painscale_hipthigh_A_list(painscale)
        var_painscale_hipthigh_B_list = painscale_hipthigh_B_list(painscale)
        var_painscale_hipthigh_C_list = painscale_hipthigh_C_list(painscale)
        var_painscale_hipthigh_D_list = painscale_hipthigh_D_list(painscale)
        var_painscale_hipthigh_E_list = painscale_hipthigh_E_list(painscale)

        diagnosis.append(check_hipthigh_diagA(var_hipthigh_A_list))
        diagnosis.append(check_hipthigh_diagB(var_hipthigh_B_list))
        diagnosis.append(check_hipthigh_diagC(var_hipthigh_C_list)) 
        diagnosis.append(check_hipthigh_diagD(var_hipthigh_D_list)) 
        diagnosis.append(check_hipthigh_diagE(var_hipthigh_E_list)) 
        
        print("THIS IS hipthigh QUESTION")
        print(hipthigh_questions)
        print(painscale)
        print(diagnosis) 

        print("THIS var_hipthigh_alist")
        print(var_hipthigh_A_list)
        print(var_hipthigh_B_list)
        print(var_hipthigh_C_list)
        print(var_hipthigh_D_list)
        print(var_hipthigh_E_list)
        
        print("THIS IS PAINSCALE")
        print(var_painscale_hipthigh_A_list)
        print(var_painscale_hipthigh_B_list)
        print(var_painscale_hipthigh_C_list)
        print(var_painscale_hipthigh_D_list)
        print(var_painscale_hipthigh_E_list)


        for choice_1 in var_hipthigh_A_list:
            if choice_1 == "1":
                severity = severity + int(var_painscale_hipthigh_A_list[n])
                n = n + 1
                hipthigh_scoreA = severity / n
                print("THIS IS hipthighSCOREA")
                print(hipthigh_scoreA)
            else:
                pass
                
        hipthigh_scores.append(hipthigh_scoreA)
        print(hipthigh_scoreA)
        
        n = 0
        severity = 0
        for choice_2 in var_hipthigh_B_list:
            if choice_2 == "1":
                severity = severity + int(var_painscale_hipthigh_B_list[n])
                n += 1
                hipthigh_scoreB = severity / n
            else:
                pass
    
        hipthigh_scores.append(hipthigh_scoreB)
        print(hipthigh_scoreB)

        n = 0
        severity = 0
        for choice_3 in var_hipthigh_C_list:
            if choice_3 == "1":
                severity = severity + int(var_painscale_hipthigh_C_list[n])
                n += 1
                hipthigh_scoreC = severity / n
            else:
                pass
                
        hipthigh_scores.append(hipthigh_scoreC)
        print(hipthigh_scoreC)

        n = 0
        severity = 0
        for choice_4 in var_hipthigh_D_list:
            if choice_4 == "1":
                severity = severity + int(var_painscale_hipthigh_D_list[n])
                n += 1
                hipthigh_scoreD = severity / n
            else:
                pass
                
        hipthigh_scores.append(hipthigh_scoreD)
        print(hipthigh_scoreD)

        n = 0
        severity = 0
        for choice_5 in var_hipthigh_E_list:
            if choice_5 == "1":
                severity = severity + int(var_painscale_hipthigh_E_list[n])
                n += 1
                hipthigh_scoreE = severity / n
            else:
                pass
                
        hipthigh_scores.append(hipthigh_scoreE)
        print(hipthigh_scoreE)


        context = {
            "first": diagnosis[0], "second": diagnosis[1], "third": diagnosis[2], "fourth": diagnosis[3], "fifth": diagnosis[4],
            'hipthigh_scoreA' : hipthigh_scores[0], 'hipthigh_scoreB' : hipthigh_scores[1], 'hipthigh_scoreC' : hipthigh_scores[2], 'hipthigh_scoreD' : hipthigh_scores[3], 'hipthigh_scoreE' : hipthigh_scores[4],
            }
        return render(request, 'main/hipthigh/hipthigh_results.html', context)
    else:
        return render(request, 'main/hipthigh/hipthigh_questionnaire.html')

#End of Hipthigh Questionnaire -----------------------------------------------------------




#KneeLowerLeg_Questionnaire --------------------------------------------------------------------
def kneelowerleg_A_list(kneelowerleg_questions):
    kneelowerleg_indices_to_access_A = [0, 1, 2, 6, 7, 9]
    kneelowerleg_accessed_mapping_A = map(kneelowerleg_questions.__getitem__, kneelowerleg_indices_to_access_A)
    kneelowerleg_accessed_list_A = list(kneelowerleg_accessed_mapping_A)
    return kneelowerleg_accessed_list_A

def kneelowerleg_B_list(kneelowerleg_questions):
    kneelowerleg_indices_to_access_B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    kneelowerleg_accessed_mapping_B = map(kneelowerleg_questions.__getitem__, kneelowerleg_indices_to_access_B)
    kneelowerleg_accessed_list_B = list(kneelowerleg_accessed_mapping_B)
    return kneelowerleg_accessed_list_B

def kneelowerleg_C_list(kneelowerleg_questions):
    kneelowerleg_indices_to_access_C = [0, 1, 2, 3 ,4 ,5, 8]
    kneelowerleg_accessed_mapping_C = map(kneelowerleg_questions.__getitem__, kneelowerleg_indices_to_access_C)
    kneelowerleg_accessed_list_C = list(kneelowerleg_accessed_mapping_C)
    return kneelowerleg_accessed_list_C



def painscale_kneelowerleg_A_list(painscale):
    painscale_kneelowerleg_indices_to_access_A = [0, 1, 2, 6, 7, 9]
    painscale_kneelowerleg_accessed_mapping_A = map(painscale.__getitem__, painscale_kneelowerleg_indices_to_access_A)
    painscale_kneelowerleg_accessed_list_A = list(painscale_kneelowerleg_accessed_mapping_A)
    return painscale_kneelowerleg_accessed_list_A

def painscale_kneelowerleg_B_list(painscale):
    painscale_kneelowerleg_indices_to_access_B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    painscale_kneelowerleg_accessed_mapping_B = map(painscale.__getitem__, painscale_kneelowerleg_indices_to_access_B)
    painscale_kneelowerleg_accessed_list_B = list(painscale_kneelowerleg_accessed_mapping_B)
    return painscale_kneelowerleg_accessed_list_B

def painscale_kneelowerleg_C_list(painscale):
    painscale_kneelowerleg_indices_to_access_C = [0, 1, 2, 3 ,4 ,5, 8]
    painscale_kneelowerleg_accessed_mapping_C = map(painscale.__getitem__, painscale_kneelowerleg_indices_to_access_C)
    painscale_kneelowerleg_accessed_list_C = list(painscale_kneelowerleg_accessed_mapping_C)
    return painscale_kneelowerleg_accessed_list_C


def check_kneelowerleg_diagA(kneelowerleg_questions):
    checker = "1"
    if checker in kneelowerleg_questions:
        return 'ACL (Anterior Cruciate Ligament) Tear'
    else:
        return "0"

def check_kneelowerleg_diagB(kneelowerleg_questions):
    checker = "1"
    if checker in kneelowerleg_questions:
        return 'Meniscus Tear'
    else:
        return "0"

def check_kneelowerleg_diagC(kneelowerleg_questions):
    checker = "1"
    if checker in kneelowerleg_questions:
        return 'Arthritis of the Knee'
    else:
        return "0"


def kneelowerleg_questionnaire(request):
    if request.method == "POST":
        kneelowerleg_questions = []
        diagnosis = []
        painscale = []
        severity = 0
        n = 0
        kneelowerleg_scoreA = 0
        kneelowerleg_scoreB = 0
        kneelowerleg_scoreC = 0
        kneelowerleg_scores = []
        for i in range(1,11):
            request.POST.get("kneelowerleg_questions"+ str(i))
            current_question = request.POST.get("kneelowerleg_questions"+ str(i))
            current_painscale = request.POST.get("painscale"+ str(i))
            kneelowerleg_questions.append(current_question)
            if current_question == "1":
                painscale.append(current_painscale)
            else:
                painscale.append("0")

        var_kneelowerleg_A_list = kneelowerleg_A_list(kneelowerleg_questions)
        var_kneelowerleg_B_list = kneelowerleg_B_list(kneelowerleg_questions)
        var_kneelowerleg_C_list = kneelowerleg_C_list(kneelowerleg_questions)

        var_painscale_kneelowerleg_A_list = painscale_kneelowerleg_A_list(painscale)
        var_painscale_kneelowerleg_B_list = painscale_kneelowerleg_B_list(painscale)
        var_painscale_kneelowerleg_C_list = painscale_kneelowerleg_C_list(painscale)

        diagnosis.append(check_kneelowerleg_diagA(var_kneelowerleg_A_list))
        diagnosis.append(check_kneelowerleg_diagB(var_kneelowerleg_B_list))
        diagnosis.append(check_kneelowerleg_diagC(var_kneelowerleg_C_list)) 
        
        print("THIS IS kneelowerleg QUESTION")
        print(kneelowerleg_questions)
        print(painscale) 
        print(diagnosis) 
        print("THIS var_kneelowerleg_alist")
        print(var_kneelowerleg_A_list)
        print(var_kneelowerleg_B_list)
        print(var_kneelowerleg_C_list)
        print("THIS IS PAINSCALE")
        print(var_painscale_kneelowerleg_A_list)
        print(var_painscale_kneelowerleg_B_list)
        print(var_painscale_kneelowerleg_C_list)


        for choice_1 in var_kneelowerleg_A_list:
            if choice_1 == "1":
                severity = severity + int(var_painscale_kneelowerleg_A_list[n])
                n = n + 1
                kneelowerleg_scoreA = severity / n
                print("THIS IS kneelowerlegSCOREA")
                print(kneelowerleg_scoreA)
            else:
                pass
                
        kneelowerleg_scores.append(kneelowerleg_scoreA)
        print(kneelowerleg_scoreA)
        
        n = 0
        severity = 0
        for choice_2 in var_kneelowerleg_B_list:
            if choice_2 == "1":
                severity = severity + int(var_painscale_kneelowerleg_B_list[n])
                n += 1
                kneelowerleg_scoreB = severity / n
            else:
                pass
                
        kneelowerleg_scores.append(kneelowerleg_scoreB)
        print(kneelowerleg_scoreB)

        n = 0
        severity = 0
        for choice_3 in var_kneelowerleg_C_list:
            if choice_3 == "1":
                severity = severity + int(var_painscale_kneelowerleg_C_list[n])
                n += 1
                kneelowerleg_scoreC = severity / n
            else:
                pass
                
        kneelowerleg_scores.append(kneelowerleg_scoreC)
        print(kneelowerleg_scoreC)


        context = {
            "first": diagnosis[0], "second": diagnosis[1], "third": diagnosis[2],
            'kneelowerleg_scoreA' : kneelowerleg_scores[0], 'kneelowerleg_scoreB' : kneelowerleg_scores[1], 'kneelowerleg_scoreC' : kneelowerleg_scores[2],
            }
        return render(request, 'main/kneelowerleg/kneelowerleg_results.html', context)
    else:
        return render(request, 'main/kneelowerleg/kneelowerleg_questionnaire.html')

#End of KneeLowerLeg Questionnaire ---------------------------------------------------------------




#WristHand Questionnaire -----------------------------------------------------------------
def wristhand_A_list(wristhand_questions):
    wristhand_indices_to_access_A = [0, 1, 4, 6]
    wristhand_accessed_mapping_A = map(wristhand_questions.__getitem__, wristhand_indices_to_access_A)
    wristhand_accessed_list_A = list(wristhand_accessed_mapping_A)
    return wristhand_accessed_list_A

def wristhand_B_list(wristhand_questions):
    wristhand_indices_to_access_B = [0, 1, 4]
    wristhand_accessed_mapping_B = map(wristhand_questions.__getitem__, wristhand_indices_to_access_B)
    wristhand_accessed_list_B = list(wristhand_accessed_mapping_B)
    return wristhand_accessed_list_B

def wristhand_C_list(wristhand_questions):
    wristhand_indices_to_access_C = [2, 3, 8]
    wristhand_accessed_mapping_C = map(wristhand_questions.__getitem__, wristhand_indices_to_access_C)
    wristhand_accessed_list_C = list(wristhand_accessed_mapping_C)
    return wristhand_accessed_list_C

def wristhand_D_list(wristhand_questions):
    wristhand_indices_to_access_D = [1, 5, 6, 7]
    wristhand_accessed_mapping_D = map(wristhand_questions.__getitem__, wristhand_indices_to_access_D)
    wristhand_accessed_list_D = list(wristhand_accessed_mapping_D)
    return wristhand_accessed_list_D

def wristhand_E_list(wristhand_questions):
    wristhand_indices_to_access_E = [2, 3, 8]
    wristhand_accessed_mapping_E = map(wristhand_questions.__getitem__, wristhand_indices_to_access_E)
    wristhand_accessed_list_E = list(wristhand_accessed_mapping_E)
    return wristhand_accessed_list_E

def wristhand_F_list(wristhand_questions):
    wristhand_indices_to_access_F = [2, 3, 8]
    wristhand_accessed_mapping_F = map(wristhand_questions.__getitem__, wristhand_indices_to_access_F)
    wristhand_accessed_list_F = list(wristhand_accessed_mapping_F)
    return wristhand_accessed_list_F


def painscale_wristhand_A_list(painscale):
    painscale_wristhand_indices_to_access_A = [0, 1, 4, 6]
    painscale_wristhand_accessed_mapping_A = map(painscale.__getitem__, painscale_wristhand_indices_to_access_A)
    painscale_wristhand_accessed_list_A = list(painscale_wristhand_accessed_mapping_A)
    return painscale_wristhand_accessed_list_A

def painscale_wristhand_B_list(painscale):
    painscale_wristhand_indices_to_access_B = [0, 1, 4]
    painscale_wristhand_accessed_mapping_B = map(painscale.__getitem__, painscale_wristhand_indices_to_access_B)
    painscale_wristhand_accessed_list_B = list(painscale_wristhand_accessed_mapping_B)
    return painscale_wristhand_accessed_list_B

def painscale_wristhand_C_list(painscale):
    painscale_wristhand_indices_to_access_C = [2, 3, 8]
    painscale_wristhand_accessed_mapping_C = map(painscale.__getitem__, painscale_wristhand_indices_to_access_C)
    painscale_wristhand_accessed_list_C = list(painscale_wristhand_accessed_mapping_C)
    return painscale_wristhand_accessed_list_C

def painscale_wristhand_D_list(painscale):
    painscale_wristhand_indices_to_access_D = [1, 5, 6, 7]
    painscale_wristhand_accessed_mapping_D = map(painscale.__getitem__, painscale_wristhand_indices_to_access_D)
    painscale_wristhand_accessed_list_D = list(painscale_wristhand_accessed_mapping_D)
    return painscale_wristhand_accessed_list_D

def painscale_wristhand_E_list(painscale):
    painscale_wristhand_indices_to_access_E = [2, 3, 8]
    painscale_wristhand_accessed_mapping_E = map(painscale.__getitem__, painscale_wristhand_indices_to_access_E)
    painscale_wristhand_accessed_list_E = list(painscale_wristhand_accessed_mapping_E)
    return painscale_wristhand_accessed_list_E

def painscale_wristhand_F_list(painscale):
    painscale_wristhand_indices_to_access_F = [2, 3, 8]
    painscale_wristhand_accessed_mapping_F = map(painscale.__getitem__, painscale_wristhand_indices_to_access_F)
    painscale_wristhand_accessed_list_F = list(painscale_wristhand_accessed_mapping_F)
    return painscale_wristhand_accessed_list_F


def check_wristhand_diagA(wristhand_questions):
    checker = "1"
    if checker in wristhand_questions:
        return 'De Quervain’s Syndrome'
    else:
        return "0"

def check_wristhand_diagB(wristhand_questions):
    checker = "1"
    if checker in wristhand_questions:
        return 'Carpal Tunnel Syndrome'
    else:
        return "0"

def check_wristhand_diagC(wristhand_questions):
    checker = "1"
    if checker in wristhand_questions:
        return 'Colles Fracture (Broken Wrist)'
    else:
        return "0"

def check_wristhand_diagD(wristhand_questions):
    checker = "1"
    if checker in wristhand_questions:
        return 'Trigger Finger (Stenosing Tenosynovitis)'
    else:
        return "0"

def check_wristhand_diagE(wristhand_questions):
    checker = "1"
    if checker in wristhand_questions:
        return 'Dislocated Finger'
    else:
        return "0"

def check_wristhand_diagF(wristhand_questions):
    checker = "1"
    if checker in wristhand_questions:
        return 'Finger Fracture'
    else:
        return "0"

def wristhand_questionnaire(request):
    if request.method == "POST":
        wristhand_questions = []
        diagnosis = []
        painscale = []
        severity = 0
        n = 0
        wristhand_scoreA = 0
        wristhand_scoreB = 0
        wristhand_scoreC = 0
        wristhand_scoreD = 0
        wristhand_scoreE = 0
        wristhand_scoreF = 0
        wristhand_scores = []
        for i in range(1,11):
            request.POST.get("wristhand_questions"+ str(i))
            current_question = request.POST.get("wristhand_questions"+ str(i))
            current_painscale = request.POST.get("painscale"+ str(i))
            wristhand_questions.append(current_question)
            if current_question == "1":
                painscale.append(current_painscale)
            else:
                painscale.append("0")

        var_wristhand_A_list = wristhand_A_list(wristhand_questions)
        var_wristhand_B_list = wristhand_B_list(wristhand_questions)
        var_wristhand_C_list = wristhand_C_list(wristhand_questions)
        var_wristhand_D_list = wristhand_D_list(wristhand_questions)
        var_wristhand_E_list = wristhand_E_list(wristhand_questions)
        var_wristhand_F_list = wristhand_F_list(wristhand_questions)

        var_painscale_wristhand_A_list = painscale_wristhand_A_list(painscale)
        var_painscale_wristhand_B_list = painscale_wristhand_B_list(painscale)
        var_painscale_wristhand_C_list = painscale_wristhand_C_list(painscale)
        var_painscale_wristhand_D_list = painscale_wristhand_D_list(painscale)
        var_painscale_wristhand_E_list = painscale_wristhand_E_list(painscale)
        var_painscale_wristhand_F_list = painscale_wristhand_F_list(painscale)

        diagnosis.append(check_wristhand_diagA(var_wristhand_A_list))
        diagnosis.append(check_wristhand_diagB(var_wristhand_B_list))
        diagnosis.append(check_wristhand_diagC(var_wristhand_C_list)) 
        diagnosis.append(check_wristhand_diagD(var_wristhand_D_list)) 
        diagnosis.append(check_wristhand_diagE(var_wristhand_E_list)) 
        diagnosis.append(check_wristhand_diagF(var_wristhand_F_list)) 
        
        print("THIS IS WRISTHAND QUESTION")
        print(wristhand_questions)
        print(painscale) 
        print(diagnosis) 
        print("THIS var_wristhand_alist")
        print(var_wristhand_A_list)
        print(var_wristhand_B_list)
        print(var_wristhand_C_list)
        print(var_wristhand_D_list)
        print(var_wristhand_E_list)
        print(var_wristhand_F_list)
        print("THIS IS PAINSCALE")
        print(var_painscale_wristhand_A_list)
        print(var_painscale_wristhand_B_list)
        print(var_painscale_wristhand_C_list)
        print(var_painscale_wristhand_D_list)
        print(var_painscale_wristhand_E_list)
        print(var_painscale_wristhand_F_list)


        for choice_1 in var_wristhand_A_list:
            if choice_1 == "1":
                severity = severity + int(var_painscale_wristhand_A_list[n])
                n = n + 1
                wristhand_scoreA = severity / n
                print("THIS IS wristhandSCOREA")
                print(wristhand_scoreA)
            else:
                pass
                
        wristhand_scores.append(wristhand_scoreA)
        print(wristhand_scoreA)
        
        n = 0
        severity = 0
        for choice_2 in var_wristhand_B_list:
            if choice_2 == "1":
                severity = severity + int(var_painscale_wristhand_B_list[n])
                n += 1
                wristhand_scoreB = severity / n
            else:
                pass
                
        wristhand_scores.append(wristhand_scoreB)
        print(wristhand_scoreB)

        n = 0
        severity = 0
        for choice_3 in var_wristhand_C_list:
            if choice_3 == "1":
                severity = severity + int(var_painscale_wristhand_C_list[n])
                n += 1
                wristhand_scoreC = severity / n
            else:
                pass
                
        wristhand_scores.append(wristhand_scoreC)
        print(wristhand_scoreC)

        n = 0
        severity = 0
        for choice_4 in var_wristhand_D_list:
            if choice_4 == "1":
                severity = severity + int(var_painscale_wristhand_D_list[n])
                n += 1
                wristhand_scoreD = severity / n
            else:
                pass
                
        wristhand_scores.append(wristhand_scoreD)
        print(wristhand_scoreD)

        n = 0
        severity = 0
        for choice_5 in var_wristhand_E_list:
            if choice_5 == "1":
                severity = severity + int(var_painscale_wristhand_E_list[n])
                n += 1
                wristhand_scoreE = severity / n
            else:
                pass
                
        wristhand_scores.append(wristhand_scoreE)
        print(wristhand_scoreE)

        n = 0
        severity = 0
        for choice_6 in var_wristhand_F_list:
            if choice_6 == "1":
                severity = severity + int(var_painscale_wristhand_F_list[n])
                n += 1
                wristhand_scoreF = severity / n
            else:
                pass
                
        wristhand_scores.append(wristhand_scoreF)
        print(wristhand_scoreF)

        context = {
            "first": diagnosis[0], "second": diagnosis[1], "third": diagnosis[2], "fourth": diagnosis[3], "fifth": diagnosis[4], "sixth": diagnosis[5],
            'wristhand_scoreA' : wristhand_scores[0], 'wristhand_scoreB' : wristhand_scores[1], 'wristhand_scoreC' : wristhand_scores[2], 'wristhand_scoreD' : wristhand_scores[3], 'wristhand_scoreE' : wristhand_scores[4], 'wristhand_scoreF' : wristhand_scores[5]
            }
        return render(request, 'main/wristhand/wristhand_results.html', context)
    else:
        return render(request, 'main/wristhand/wristhand_questionnaire.html')

# End of WristHand Questionnaire -----------------------------------------------