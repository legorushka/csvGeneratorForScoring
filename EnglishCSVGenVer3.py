'''
Возраст;
Семейное положение;
Количество иждевенцов;
Образование;
Отрасль экономики (место работы);
Престиж организации (место работы);
Доходы;
Недвижимость;
Автотранспорт;
Общий трудовой стаж;
Стаж на последнем месте работы;
Кредитная история.
'''
#Checking account status,Duration in months,Credit history,Purpose,Credit amount,Savings,Present employment time,Installment rate in percentage of disposable income,Personal status and sex,Other debtors / guarantors,Present residence time,Property,Age in years,Other installment plans,Housing,Number of existing credits at this bank,Job,Number of dependents,Telephone,ForeignWorker,CreditStatus

__age__ = [
    '18-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
    '50-54', '55-59', '60-64', '65-69', '70+'
    ]
__ageWeights__ = [
    3.53570, 11.17892, 11.00680, 10.08634, 9.34448, 8.48855, 9.80292, 10.54793,
    9.20603, 7.19484, 3.67602, 5.93147
    ]
__ageEdge__= [19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 80]
# Выберем именно эти промежутки, т.к. они указаны во Всероссийской переписи
# населения 2010 года, на статистику которой мы и будем ориентироваться.
__maritalStatus__ = [
    "Not married", "Divorced",
    "Married", "Consists in civil marriage"
    ]
__maritalStatusWeights__ = [
    [90.57177, 0.28609, 1.36627, 7.77586],
    [68.05133, 3.43488, 7.95328, 20.56051],
    [37.49765, 13.33537, 19.84118, 29.32579],
    [20.63503, 23.43010, 24.55118, 31.38369],
    [12.93385, 30.31658, 25.69767, 31.05190],
    [8.75474, 34.63845, 27.35432, 29.25250],
    [7.00225, 36.10307, 30.00143, 26.89325],
    [5.96844, 36.40819, 32.78787, 24.83550],
    [5.63157, 36.99719, 34.92342, 22.44782],
    [5.48415, 36.37710, 38.06756, 20.07119],
    [5.63103, 35.62638, 39.89079, 18.85180],
    [9.11257, 32.48721, 41.23747, 17.16275],
    ]
# Будем считать семейное положение "Состоит в гражданском браке" как
# рассматриваемое банком.
__dependents__ = [0, 1, 2, 3, 4]
__dependentsWeights__ = [
    [97, 3, 0.001, 0, 0],
    [67, 20, 12, 1, 0.001],
    [45, 27, 20, 7, 1],
    [20, 35, 35, 9, 1],
    [20, 35, 35, 9, 1],
    [30, 30, 30, 9, 1],
    [40, 30, 23, 6.5, 0.5],
    [45, 30, 20, 4.5, 0.5],
    [40, 30, 23, 6.5, 0.5],
    [30, 30, 30, 9, 1],
    [20, 35, 35, 9, 1],
    [10, 44, 44, 1.9, 0.1]
    ]
# Будем считать, что в семьях нет более 4 иждевенцев.
# Веса были придуманы лично.
__education__ = [
    "Prechool", "Primary General", "Basic General", "Secondary general",
    "Primary professonal", "Secondary professional",
    "Higher prssional", "Postgraduate professional"
    ]
__educationWeights__ = [
    [0.54235, 1.40244, 15.53859, 54.59769, 9.18213, 18.73679, 0, 0],
    [0.56410, 1.27184, 8.57638, 22.85189, 8.19344, 34.09359, 23.87630, 0.57246],
    [0.45268, 1.06782, 6.85855, 15.79860, 6.0810, 29.92355, 38.38727, 1.42545],
    [0.40207, 1.05469, 7.70378, 16.78073, 6.09916, 32.31027, 34.41160, 1.23770],
    [0.34374, 0.86228, 6.36068, 17.16538, 6.58571, 37.68128, 30.06295, 0.93799],
    [0.31966, 0.72839, 4.58373, 17.19521, 7.09448, 41.91672, 27.50616, 0.65564],
    [0.28008, 0.74291, 4.61111, 19.51812, 7.09655, 41.81784, 25.42660, 0.50679],
    [0.24836, 1.04899, 6.05851, 21.65030, 6.86011, 40.83021, 22.88392, 0.41960],
    [0.23616, 1.86369, 9.232665, 21.67533, 5.90235, 38.75926, 21.93172, 0.39883],
    [0.25586, 3.53578, 12.20627, 19.51164, 4.92056, 36.57823, 22.56534, 0.42632],
    [0.51437, 10.99660, 18.00348, 16.55233, 3.77926, 28.93888, 20.79116, 0.42391],
    [2.54766, 30.00106, 19.80999, 10.54254, 2.68208, 20.22316, 13.90239, 0.29112],
    ]
# Типы образований по порядку: дошкольное, начальное общее, основное общее,
# среднее общее, начальное профессиональное, среднее профессиональное,
# высшее профессиональное, послевузовское профессиональное.
# Типы образований даны в соответствии с Законом РФ "Об образовании".
__prestige__ = ["High", "Medium", "Low"]
# Классификация престижа подлежит дальнейшему изучению и развитию
__income__ = [i for i in range(10000,250001,5000)]
__realEstate__ = [i for i in range(500000,20000001,250000)]
__transport__ = [i for i in range(100000,5000000,100000)]
__totalWorkExperience__ = [i for i in range(0,80)]
__lastWorkExperience__ = [i for i in range(0,80)]
# Общий трудовой стаж и стаж на последнем месте работы не могут быть указаны
# ранее, чем будут обозначенф возраст кредитозаемщика и общий трудовой стаж
# соответственно
__creditHistory__ = ["Positive", "Average", "Negative", "Zero"]
__loanSize__ = [i for i in range(10000, 1000000, 10000)]
__period__ = [i for i in range(1, 24)]


import csv
import random


# Зададим случайные параметры для результирующей переменной
RNG1 = [1/12, 3/12, 5/12, 7/12, 9/12, 11/12, 11/12, 9/12, 7/12, 5/12, 3/12, 1/12]#Возраст(1-12)
RNG2 = [3/4, 0/4, 2/4, 2/4]#Семейное положение(1-4)
RNG3 = [1, 3/5, 2/5, 1/5, 0/5]#Иждивенцы(1-5)
RNG4 = [0, 0, 0, 1/8, 3/8, 5/8, 7/8, 1]#Образование(1-8)
RNG5 = [1, 1/2, 0]#Престиж(1-3)
RNG6 = [i/49 for i in range(1,50)]#Доход(1-49)
RNG7 = [i/79 for i in range(1,80)]#Недвижимость(1-79)
RNG8 = [i/49 for i in range(1,50)]#Автотранспорт(1-49)
RNG9 = [i/80 for i in range(1,80)]#Общий стаж(1-80)
RNG10 = [i/80 for i in range(1,80)]#Последний стаж(1-80)
RNG11 = [1,1/2,1/6,1/3]#Кредитная история(1-4)
RNG12 = [1/2 for i in range(99,0,-1)]#Размер займа(1-99)
RNG13 = [1/2 for i in range(23,0,-1)]#Срок(1-23)



#счетчики для проверки, не важны для работоспособности
counter1=0
counter2=0


class Client():
    def __init__(
        self, number, age, maritalStatus, dependents, education, prestige,
        income, realEstate, transport,totalWorkExperience, lastWorkExperience,
        creditHistory, loanSize, period, repaid
        ):
        self.number = number
        self.age = age
        self.maritalStatus = maritalStatus
        self.dependents = dependents
        self.education = education
        self.prestige = prestige
        self.income = income
        self.realEstate = realEstate
        self.transport = transport
        self.totalWorkExperience = totalWorkExperience
        self.lastWorkExperience = lastWorkExperience
        self.creditHistory = creditHistory
        self.loanSize = loanSize
        self.period = period
        self.repaid = repaid
        

def generateClient(number):
    global counter1
    global counter2
    
    age = random.choices(__age__, weights=__ageWeights__, k=1)[0]

    # Вычислим возраст, который был случайно задан
    i = __age__.index(age)
    ageEdge = __ageEdge__[i]
    
    maritalStatus = random.choices(
        __maritalStatus__, weights=__maritalStatusWeights__[i], k=1
        )[0]
    dependents = random.choices(
        __dependents__, __dependentsWeights__[i], k=1
        )[0]
    education = random.choices(
        __education__, __educationWeights__[i], k=1
        )[0]
    
    prestige = random.choice(__prestige__)
    income = random.choice(__income__)
    realEstate = random.choice(__realEstate__)
    transport = random.choice(__transport__)
    totalWorkExperience = random.randint(0, int(ageEdge) - 16)
    lastWorkExperience = random.randint(0, totalWorkExperience)
    creditHistory = random.choice(__creditHistory__)
    loanSize = random.choice(__loanSize__)
    period = random.choice(__period__)



    # Необходима зависимость результат
    i1 = RNG1[i]
    i2 = RNG2[__maritalStatus__.index(maritalStatus)]
    i3 = RNG3[__dependents__.index(dependents)]
    i4 = RNG4[__education__.index(education)]
    if lastWorkExperience == 0:
        prestige = ("empty")
        income = 0
        i5 = random.random()
        i6 = random.random()
    else:
        i5 = RNG5[__prestige__.index(prestige)]
        i6 = RNG6[__income__.index(income)]
    i7 = RNG7[__realEstate__.index(realEstate)]
    i8 = RNG8[__transport__.index(transport)]
    i9 = RNG9[__totalWorkExperience__.index(totalWorkExperience)]
    i10 = RNG10[__lastWorkExperience__.index(lastWorkExperience)]
    i11 = RNG11[__creditHistory__.index(creditHistory)]
    i12 = RNG12[__loanSize__.index(loanSize)]
    i13 = RNG13[__period__.index(period)]
    # Определяющее значение для клиентов и два счетчика по двум возможным
    # значениям.
    rng = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12 + i13
    if rng > 6:
        repaid = 'Yes'
        counter1+=1
    else:
        repaid = 'No'
        counter2+=1
    
    client = Client(
        number, age, maritalStatus, dependents, education, prestige, income,
        realEstate, transport, totalWorkExperience, lastWorkExperience,
        creditHistory, loanSize, period, repaid
        )
    return(client)


def generateDB(path, number):
    gen = open(path, 'w', newline='')
    with gen:
        writer = csv.writer(gen)#, dialect=";")
        writer.writerow([
            "Number", "Age", "Marital Status", "Dependents", "Education",
            "Company Prestige", "Income", "Real Estate", "Motor Transport",
            "Total Length of Service", "Seniority at the last place of work",
            "Credit History", "Loan Size", "Term", "Status"
            ])
                        
            
        for i in range(1, number+1):      
            
            client = generateClient(i)
            csvOfClient = (
                client.number, client.age, client.maritalStatus,
                client.dependents, client.education, client.prestige,
                client.income, client.realEstate, client.transport,
                client.totalWorkExperience, client.lastWorkExperience,
                client.creditHistory, client.loanSize, client.period,
                client.repaid
                )
                
            writer.writerow(csvOfClient)

def outputData(path, counters, RNGs):
    output = open(path, 'w')#, newline='')
    with output:
        writer = csv.writer(output, dialect=';')
        writer.writerow(['Paid', 'Delayed', 'Not paid'])
        writer.writerow(counters)
        writer.writerow(['Weights'])
        writer.writerows(RNGs)


csv.register_dialect(";", delimiter=";")
path = ('Test3BankClientsDataBase.csv')
generateDB(path, 2000)


path2 = ('Test3BankClientsRNGs&counters.csv')
counters = [counter1, counter2]
RNGs = [RNG1, RNG2, RNG3, RNG4, RNG5, RNG6, RNG7, RNG8, RNG9, RNG10, RNG11, RNG12, RNG13]
outputData(path2, counters, RNGs)
print(counter1, counter2)
