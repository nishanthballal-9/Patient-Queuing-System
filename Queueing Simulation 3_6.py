__metaclass__=type
import random
import csv
import numpy as np

Patients = []
Patients1 = []

class Patient:
    def __init__(self,j,arrival_time,service_start_time,service_time,relapse1,relapse2,relapse3,relapse4,relapse5,relapse6,relapse7,relapse8,relapse9,relapse10):
        self.j = j
        self.arrival_time = arrival_time
        self.service_start_time = service_start_time
        self.service_time = service_time
        self.service_end_time = self.service_start_time + self.service_time
        self.wait = self.service_start_time - self.arrival_time
        self.relapse1 = relapse1
        self.relapse2 = relapse2
        self.relapse3 = relapse3
        self.relapse4 = relapse4
        self.relapse5 = relapse5
        self.relapse6 = relapse6
        self.relapse7 = relapse7
        self.relapse8 = relapse8
        self.relapse9 = relapse9
        self.relapse10 = relapse10
        self.queue_length = 0
        if self.wait > 0:
            self.queue_length += 1
        else:
            self.queue_length = 0

def handle_relapse(j):
    arrT = 0 
    serST = 0 
    serET = 0 
    wt = 0
    serT = 3
    patAdd = []
    global Patients
    global Patients1
    
    if Patients[j].relapse1 == 1:
        if len(Patients1) != 1:
            temp = []
            k = 1
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1
        arrT = Patients1[len(Patients1)-1][5]    
        wt = 0
        serST = arrT + wt
        serET = serST + serT
        qLength = 0
        patAdd = [j+1,arrT,wt,serST,serT,serET,qLength]
        Patients1.append(patAdd)
    
    if Patients[j].relapse2 == 1:
        if len(Patients1) != 1:
            temp = []
            k = 1
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1
        arrT = Patients1[len(Patients1)-1][5]    
        wt = 0
        serST = arrT + wt
        serET = serST + serT
        qLength = 0
        patAdd = [j+1,arrT,wt,serST,serT,serET,qLength]
        Patients1.append(patAdd)
    
    if Patients[j].relapse3 == 1:
        if len(Patients1) != 1:
            temp = []
            k = 1
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1
        arrT = Patients1[len(Patients1)-1][5]    
        wt = 0
        serST = arrT + wt
        serET = serST + serT
        qLength = 0
        patAdd = [j+1,arrT,wt,serST,serT,serET,qLength]
        Patients1.append(patAdd)
        
    if Patients[j].relapse4 == 1:
        if len(Patients1) != 1:
            temp = []
            k = 1
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1
        arrT = Patients1[len(Patients1)-1][5]    
        wt = 0
        serST = arrT + wt
        serET = serST + serT
        qLength = 0
        patAdd = [j+1,arrT,wt,serST,serT,serET,qLength]
        Patients1.append(patAdd)
        
    if Patients[j].relapse5 == 1:
        if len(Patients1) != 1:
            temp = []
            k = 1
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1
        arrT = Patients1[len(Patients1)-1][5]    
        wt = 0
        serST = arrT + wt
        serET = serST + serT
        qLength = 0
        patAdd = [j+1,arrT,wt,serST,serT,serET,qLength]
        Patients1.append(patAdd)
        
    if Patients[j].relapse6 == 1:
        if len(Patients1) != 1:
            temp = []
            k = 1
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] // Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1
        arrT = Patients1[len(Patients1)-1][5]    
        wt = 0
        serST = arrT + wt
        serET = serST + serT
        qLength = 0
        patAdd = [j+1,arrT,wt,serST,serT,serET,qLength]
        Patients1.append(patAdd)
        
    if Patients[j].relapse7 == 1:
        if len(Patients1) != 1:
            temp = []
            k = 1
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1
        arrT = Patients1[len(Patients1)-1][5]    
        wt = 0
        serST = arrT + wt
        serET = serST + serT
        qLength = 0
        patAdd = [j+1,arrT,wt,serST,serT,serET,qLength]
        Patients1.append(patAdd)
        
    if Patients[j].relapse8 == 1:
        if len(Patients1) != 1:
            temp = []
            k = 1
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1
        arrT = Patients1[len(Patients1)-1][5]    
        wt = 0
        serST = arrT + wt
        serET = serST + serT
        qLength = 0
        patAdd = [j+1,arrT,wt,serST,serT,serET,qLength]
        Patients1.append(patAdd)
    
    if Patients[j].relapse9 == 1:
        if len(Patients1) != 1:
            temp = []
            k = 1
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1
        arrT = Patients1[len(Patients1)-1][5]    
        wt = 0
        serST = arrT + wt
        serET = serST + serT
        qLength = 0
        patAdd = [j+1,arrT,wt,serST,serT,serET,qLength]
        Patients1.append(patAdd)
    
    if Patients[j].relapse10 == 1:
        if len(Patients1) != 1:
            temp = []
            k = 1
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1
        arrT = Patients1[len(Patients1)-1][5]    
        wt = 0
        serST = arrT + wt
        serET = serST + serT
        qLength = 0
        patAdd = [j+1,arrT,wt,serST,serT,serET,qLength]
        Patients1.append(patAdd)
        
    else:
        if len(Patients1) != 1:
            temp = []
            for k in range(1,j):
                if Patients1[len(Patients1)-k][1] < Patients1[len(Patients1)-1-k][1]:
                    temp = Patients1[len(Patients1)-1-k]
                    Patients1[len(Patients1)-1-k] = Patients1[len(Patients1)-k]                    
                    Patients1[len(Patients1)-1-k][2] = Patients1[len(Patients1)-2-k][5] - Patients1[len(Patients1)-1-k][1]
                    Patients1[len(Patients1)-1-k][3] = Patients1[len(Patients1)-1-k][1] + Patients1[len(Patients1)-1-k][2]
                    Patients1[len(Patients1)-1-k][5] = Patients1[len(Patients1)-1-k][3] + Patients1[len(Patients1)-1-k][4]
                    if Patients1[len(Patients1)-1-k][2] % Patients1[len(Patients1)-1-k][4] == 0:
                        Patients1[len(Patients1)-1-k][6] = Patients1[len(Patients1)-1-k][2] // Patients1[len(Patients1)-1-k][4]
                    else:
                        Patients1[len(Patients1)-1-k][6] = (Patients1[len(Patients1)-1-k][2] //  Patients1[len(Patients1)-1-k][4]) + 1
                    Patients1[len(Patients1)-k] = temp
                    Patients1[len(Patients1)-k][2] = Patients1[len(Patients1)-1-k][5] - Patients1[len(Patients1)-k][1]
                    Patients1[len(Patients1)-k][3] = Patients1[len(Patients1)-k][1] + Patients1[len(Patients1)-k][2]
                    Patients1[len(Patients1)-k][5] = Patients1[len(Patients1)-k][3] + Patients1[len(Patients1)-k][4]
                    if Patients1[len(Patients1)-k][2] % Patients1[len(Patients1)-k][4] == 0:
                        Patients1[len(Patients1)-k][6] = Patients1[len(Patients1)-k][2] // Patients1[len(Patients1)-k][4]
                    else:
                        Patients1[len(Patients1)-k][6] = (Patients1[len(Patients1)-k][2] //  Patients1[len(Patients1)-k][4]) + 1
                else:
                    break
            arrT = Patients1[len(Patients1)-1][1]
            if Patients1[len(Patients1)-2][5] >= arrT:
                Patients1[len(Patients1)-1][2] = Patients1[len(Patients1)-2][5]-arrT
                Patients1[len(Patients1)-1][3] = Patients1[len(Patients1)-1][1]+Patients1[len(Patients1)-1][2]
                Patients1[len(Patients1)-1][5] = Patients1[len(Patients1)-1][3]+Patients1[len(Patients1)-1][4]
                if Patients1[len(Patients1)-1][2] %  Patients1[len(Patients1)-1][4] == 0:
                    Patients1[len(Patients1)-1][6]= Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]
                else:
                    Patients1[len(Patients1)-1][6] = (Patients1[len(Patients1)-1][2] //  Patients1[len(Patients1)-1][4]) + 1

def QSim(lambd=False,mu=False,simulation_time=False):
    if not lambd:
        lambd=input('Inter arrival rate:')
    if not mu:
        mu=input('Service rate:')
    if not simulation_time:
        simulation_time=input('Total simulation time:')
    
    t = 0
    j = 0
    global Patients
    
    np.random.seed(700)
    
    while t<simulation_time:
        j = j + 1
        if len(Patients)==0:
            arrival_time=np.random.poisson(lambd)
            service_start_time=arrival_time
        else:
            arrival_time+=np.random.poisson(lambd)
            service_start_time=max(arrival_time,Patients[-1].service_end_time)
        t = arrival_time
        """
        if t>simulation_time:
            break
        """
        service_time = 3
        relapse1 = np.random.binomial(1,0.3)
        if relapse1 == 0:
            relapse2 = 0
        else:
            relapse2 = np.random.binomial(1,0.3)
        if relapse2 == 0:
            relapse3 = 0
        else:
            relapse3 = np.random.binomial(1,0.3)
        if relapse3 == 0:
            relapse4 = 0
        else:
            relapse4 = np.random.binomial(1,0.3)
        if relapse4 == 0:
            relapse5 = 0
        else:
            relapse5 = np.random.binomial(1,0.3)
        if relapse5 == 0:
            relapse6 = 0
        else:
            relapse6 = np.random.binomial(1,0.3)
        if relapse6 == 0:
            relapse7 = 0
        else:
            relapse7 = np.random.binomial(1,0.3)
        if relapse7 == 0:
            relapse8 = 0
        else:
            relapse8 = np.random.binomial(1,0.3)
        if relapse8 == 0:
            relapse9 = 0
        else:
            relapse9 = np.random.binomial(1,0.3)
        if relapse9 == 0:
            relapse10 = 0
        else:
            relapse10 = np.random.binomial(1,0.3)                
            
        Patients.append(Patient(j,arrival_time,service_start_time,service_time,relapse1,relapse2,relapse3,relapse4,relapse5,relapse6,relapse7,relapse8,relapse9,relapse10))
        patAdd = [Patients[j-1].j,Patients[j-1].arrival_time,Patients[j-1].wait,Patients[j-1].service_start_time,Patients[j-1].service_time,Patients[j-1].service_end_time,Patients[j-1].queue_length]
        Patients1.append(patAdd)
        handle_relapse(j-1)
        t = arrival_time
        
    print(len(Patients1))
    
    i = 0
    sumWaits = 0
    for i in range(len(Patients1)-1):
        sumWaits = sumWaits + Patients1[i][2]
    Mean_Wait=sumWaits/(len(Patients))
        
    i = 0
    sumTotalTime = 0
    for i in range(len(Patients1)-1):
        sumTotalTime = sumTotalTime + Patients1[i][2] + Patients1[i][4]
        
    Mean_Time=sumTotalTime/(len(Patients))
    
    i = 0
    Service_Times = 0
    for i in range(len(Patients1)-1):
        Service_Times= Service_Times + Patients1[i][4]
    
    """
    Mean_Service_Time=sum(Service_Times)/len(Service_Times)
    """
    i = 0
    SumQLengths = 0
    for i in range(len(Patients1)-1):
        SumQLengths= SumQLengths + Patients1[i][6]
    Mean_Queue_Lengths = SumQLengths/len(Patients1)
    
    Utilisation=(Service_Times/Patients1[len(Patients1)-1][5])*100

    Free_Time = Patients1[len(Patients1)-1][5] - Service_Times
    PercentageFreeTime = (Free_Time / Patients1[len(Patients1)-1][5])*100

    print("")
    print("Summary results :")
    print("")
    print("Number of patients: ",len(Patients))
    print("Total number of services: ",len(Patients1))
    print("Average Queue Length: ",Mean_Queue_Lengths)
    print("Average Waiting Time: ",Mean_Wait)
    print("Mean Time in System: ",Mean_Time)
    print("Utilisation: ",Utilisation)
    print("Free Time for Doctor:",Free_Time)
    print("Percentage Free Time for Doctor:",PercentageFreeTime)
    print("")
        
    outfile=open('MM1Q-output-(%s,%s,%s) 6.csv' %(lambd,mu,simulation_time),'w+',newline='')
    output=csv.writer(outfile)
    output.writerow(['Patient','Arrival_Time','Wait_Time','Service_Start_Time','Service_Time','Service_End_Time','Relapse1','Relapse2','Relapse3','Relapse4','Relapse5','Relapse6','Relapse7','Relapse8','Relapse9','Relapse10'])
    i=0
    for patient in Patients:
        i = i+1
        outrow=[]
        outrow.append(i)
        outrow.append(patient.arrival_time)
        outrow.append(patient.wait)
        outrow.append(patient.service_start_time)
        outrow.append(patient.service_time)
        outrow.append(patient.service_end_time)
        outrow.append(patient.relapse1)
        outrow.append(patient.relapse2)
        outrow.append(patient.relapse3)
        outrow.append(patient.relapse4)
        outrow.append(patient.relapse5)
        outrow.append(patient.relapse6)
        outrow.append(patient.relapse7)
        outrow.append(patient.relapse8)
        outrow.append(patient.relapse9)
        outrow.append(patient.relapse10)
        output.writerow(outrow)
    outfile.close()
    
    outfile=open('MM1Q-output-(%s,%s,%s) 6_1.csv' %(lambd,mu,simulation_time),'w+',newline='')
    output=csv.writer(outfile)
    output.writerow(['Patient','Arrival_Time','Wait_Time','Service_Start_Time','Service_Time','Service_End_Time','Queue_Length'])
    i=0
    j=0
    for i in range(len(Patients1)):
        outrow=[]
        for j in range(7):
            outrow.append(Patients1[i][j])
        output.writerow(outrow)
    outfile.close()
        
    print("")
    return