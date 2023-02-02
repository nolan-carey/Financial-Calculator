#Nolan Carey
#Septmeber 12, 2022
#This python program is focused on computing mundane financial computations
#libarys for calucations and

import math
import time
import re
import matplotlib.pyplot as p





#Main Data variables


selectionDirectory =["0 - Payment Calculator","1 -  Holding Period Returns","2 -  Bond Price","3 -  Present Value","4 -  Future Value","5 -  CAPM","6 -  Maturity Value",
                     "7 -  Interest", "8 -  FV of 1$","9 -  Contract Positions","10 - Life Expectancy",
                     "11 - Price of Annuity based on Age","12 - Life Annuity Classic Methods","13 - Wealth needed for Retirment", "14 - Years before funds are exhausted",
                     "15 - Mortgage Savings","16 - Binomal Model","17 - Stock Evaluation","18 - Black Scholas","19 - Macaulays Duration of Life Annuity",("-"*5), "Quit"]

startStop = True


#file structure for life annuity and life expectancy
file = open("2010 life expectancy.csv")
header = file.readline()



#functions for oganization of user functions
def testing():
    print("testing"*5)

def clearPage():
    for i in range(10):
        print("\n")
    time.sleep(1.8)

def clearPageQuick():
    for i in range(10):
        print("\n")

def errorStatement():
    print("\n")
    print("Please Enter VALID argument! ")
    clearPage()

def thankYou():
    print("\n")
    print("Thank You")
    print("\n")

def selection(x):

    print("\n")
    print(x)
    print("\n")

def posiionSelection(x):
    print("\n")
    print(f'{x}')
    print("-"*10)

###list of math calculations



#functions to calculate different finacial needs

def PV():

    clearPageQuick()
    print("\n")
    print("PV")
    print("\n")
    fv = float(input("Enter FV: "))
    n = int(input("Enter N periods: "))
    i= float(input("Enter Interest: "))/100
    pmtInput = float(input("Enter PMT: "))
    pmt = pmtInput*((1-(1/(1+i)**n)/i))
    answer = str((fv/(1+i)**n)+pmt)
    print(answer)
    clearPage()

def paymentCalculator():
    clearPageQuick()
    print("Payment")
    print("\n")

    p = float(input("Principle Amount: "))
    r = float(input("Interest % : "))/100
    n = float(input("Number of Years: "))
    print("\n")

    payment = p*((r*((1+r)**n))/(((1+r)**n)-1))
    print("formula: p*((r*((1+r)^n))/(((1+r)^n)-1))")

    print(f"Annual Payment  = {payment} ")
    print(f"Semi-annual Payment  = {payment/2} ")

def bondPrice():
    clearPageQuick()
    print("Bond Price")
    print("\n")

    C = float(input("Enter Annual Coupon Payment: "))
    F = float(input("Enter PAR VALUE: "))
    r = float(input("Enter YTM: "))/100
    n = float(input("Enter the NUMBER of coupon payments in a Year: "))
    t = float(input(("Enter the Number of years until Maturity: ")))

    bond_price = (C*((1-(1+(r/n)**(-1*(n*t))))/(r/n)))+((F)/(1+(r/n)**(n*t)))


    print("\n")
    print(bond_price)
    clearPage()

def FV():
    clearPageQuick()
    FVloopVaribale = True
    while FVloopVaribale == True:
        print("\n")
        print("FV")
        print("\n")

        pv = float(input("Enter PV: "))
        n = int(input("Enter N periods: "))
        i= float(input("Enter Interest: "))/100
        pmt = int(input("Enter PMT per period: "))

        for i in range(n):
            pv = pv + pmt
            fv = (pv * ((1 + i) ** n))
            # print(pv)
            # print(fv)

        print(pv)
        print(fv)



        fv = (pv*((1+i)**n))
        fv = round(fv,2)
        print(fv)
        print("\n")
        con = input("Do you want to continue with FV: Y/N... ")
        print("\n")

        if con.upper() == "Y":
            clearPageQuick()
            continue

        else:
            FVloopVaribale = False

    clearPage()
####

#complete

def holdingPeriodReturns():
    clearPageQuick()
    HPRLoopVariable = True
    while HPRLoopVariable == True:
        print("Holding Period Returns")
        print("\n")
        a= float(input("Enter CURRENT Value: "))
        b = float(input("Enter PREVIOUS Value: "))
        answer = str(round(((a-b)/b)*100,4))
        print(answer + " %" + " return")
        print("\n")
        con = input("Do you want to continue with HPR: Y/N... ")
        print("\n")

        if con.upper() == "Y":
            clearPageQuick()
            continue

        else:
            HPRLoopVariable = False

    clearPage()

def CAPM():
    clearPageQuick()
    rf = float(input("Enter Risk free Rate of market (RF): "))
    b = float(input("Enter company BETA (B): "))
    erm = float(input("Enter Expected Return Market (ERM): "))

    capm = rf + (b*(erm-rf))
    print(capm)


    x = [0,1]
    y = [rf,erm]

    p.xlabel("Risk -(B)")
    p.ylabel("Expected Return - (ER)")
    p.title("CAPM - Market")

    p.plot(x, y)
    p.show()

    clearPage()

def interest():


    clearPageQuick()
    selection("Enter the Following Information: ")
    fv = float(input("Matruity Value: "))
    pv = float(input("PV: "))
    t = float(input("Enter number of days: "))

    print("\n")
    d =365


    siAnswer365 = round(((fv/pv)-1)*(365/t),6)
    siAnswer360  = round(((fv/pv)-1)*(360/t), 6)
    x = math.log((fv / pv))
    ccAnswer = round((x / t) * d, 6)
    dcAnswer = r = round((((fv/pv)**(1/t)-1)*365),6)
    eaAnswer = round((((fv/pv)**(d/t))-1),6)


    selection("Answers")
    print('-'*10)
    print(f'{siAnswer360} - R: simple Interest (360)')
    print(f'{siAnswer365} - R: simple Interest (365)')
    print(f'{dcAnswer} - R: Daily Compunded (365)')
    print(f'{ccAnswer} - R: Continuosly Compounded (365)')
    print(f'{eaAnswer} - R: Effective Annual (365)')


    time.sleep(3)
    clearPage()

def maturityValue():

    clearPageQuick()
    selection("Enter the Following Information: ")
    p = float(input("Princple Amount: "))
    r = float(input("Enter (R)%: "))/100
    t = float(input("Enter period of Time: "))
    e = 2.71828

    print("\n")



    siAnswer365 = (p*(1+((r)*(t/365))))
    siAnswer360 =(p*(1+((r)*(t/360))))
    ccAnswer = p * (e ** (r * (t / 365)))
    dcAnswer = (p*(((1+(r/365))**t)))
    rNew = ((1+(r/365))**365)-1
    eaAnswer = ((p)*((1+(rNew/365))**t))


    selection("Answers")
    print('-'*10)
    print(f'{round(siAnswer360,6)} - MV: simple Interest (360)')
    print(f'{round(siAnswer365,6)} - MV: simple Interest (365)')
    print(f'{round(dcAnswer,6)} - MV: Daily Compunded (365)')
    print(f'{round(ccAnswer,6)} - MV: Continuosly Compounded (365)')
    print(f'{round(eaAnswer,6)} - MV: Effective Annual (365)')
    time.sleep(1.5)
    clearPage()

def FVof1Dollar():

    clearPageQuick()
    selection("Enter the Following Information: ")
    rSi360 = float(input("R for simple Interest (360): "))
    rSi365 = float(input("R for simple Interest (365): "))
    rDC = float(input("R for Daily Compounded: "))
    rCC = float(input("R for Continusly Compounded: "))
    rEA = float(input("R for Effective Anuual Rate: "))
    t = float(input("Enter Number of Days "))
    fv = float(input("Matruity Value: "))
    pv = float(input("PV: "))
    print("\n")



    siAnswer360 = 1+ (rSi360*(t/360))
    siAnswer365 = 1+ (rSi365*(t/365))
    dcAnswer = (1+(rDC/365))**t
    ccAnswer = math.exp((rCC*(t/365)))

    eaAnswer = ((1+rEA)**(t/365))


    selection("Answers")
    print('-'*10)
    print(f'{round(siAnswer360,6)} - MV: simple Interest (360)')
    print(f'{round(siAnswer365,6)} - MV: simple Interest (365)')
    print(f'{round(dcAnswer,6)} - MV: Daily Compunded (365)')
    print(f'{round(ccAnswer,6)} - MV: Continuosly Compounded (365)')
    print(f'{round(eaAnswer,6)} - MV: Effective Annual (365)')
    time.sleep(1.5)
    clearPage()

def contractPostions():

    posiionSelection("Contract Position")
    numberOfSecurities = int(input("Enter the Number of Securites in Position: "))

    pTvariables = list(range(0, 105, 5))



    forward = {"f1":{"Strike":0, "pricePerUnit":0, "Position":0,"time(0)Value": 0}}
    call = {"c1": {"Strike": 0, "pricePerUnit": 0, "Position": 0, "time(0)Value": 0}}
    put = {"p1": {"Strike": 0, "pricePerUnit": 0, "Position": 0, "time(0)Value": 0}}

    forwardCounter = 0
    callCounter =0
    putCounter =0

    for i in range(numberOfSecurities):
        security = input("Type of Secuirty: ")

        if security.upper() == "FORWARD":
            if forwardCounter < 1:

                posiionSelection("Forward")
                strike = float(input("Enter STRIKE price: "))
                forward[f"f1"]["Strike"] = strike
                pPerUnit = float(input("Enter price per unit: "))
                forward[f'f1']["pricePerUnit"] = pPerUnit
                position = float(input("Enter Units: "))
                forward[f"f1"]["Position"] = position
                t0Value = position * pPerUnit
                forward["f1"]["time(0)Value"] = t0Value
                forwardCounter+=1
                clearPageQuick()

            else:
                posiionSelection("ADD aditional Forward")
                forwardCounter+=1
                forward[f"f{forwardCounter}"]= {"Strike":0, "pricePerUnit":0, "Position":0,"time(0)Value": 0}

                posiionSelection("Forward")
                strike = float(input("Enter STRIKE price: "))
                forward[f"f{forwardCounter}"]["Strike"] = strike
                pPerUnit = float(input("Enter price per unit: "))
                forward[f"f{forwardCounter}"]["pricePerUnit"] = pPerUnit
                position = float(input("Enter Units: "))
                forward[f"f{forwardCounter}"]["Position"] = position
                t0Value = position * pPerUnit
                forward[f"f{forwardCounter}"]["time(0)Value"] = t0Value
                clearPageQuick()

        elif security.upper() == "CALL":
            if callCounter < 1:

                posiionSelection("Call")
                strike = float(input("Enter STRIKE price: "))
                call[f"c1"]["Strike"] = strike
                pPerUnit = float(input("Enter price per unit: "))
                call[f'c1']["pricePerUnit"] = pPerUnit
                position = float(input("Enter Units: "))
                call[f"c1"]["Position"] = position
                t0Value = position * pPerUnit
                call["c1"]["time(0)Value"] = t0Value
                callCounter+=1
                clearPageQuick()

            else:
                posiionSelection("ADD aditional Call")
                callCounter+=1
                call[f"c{callCounter}"]= {"Strike":0, "pricePerUnit":0, "Position":0,"time(0)Value": 0}

                posiionSelection("Call")
                strike = float(input("Enter STRIKE price: "))
                call[f"c{callCounter}"]["Strike"] = strike
                pPerUnit = float(input("Enter price per unit: "))
                call[f"c{callCounter}"]["pricePerUnit"] = pPerUnit
                position = float(input("Enter Units: "))
                call[f"c{callCounter}"]["Position"] = position
                t0Value = position * pPerUnit
                call[f"c{callCounter}"]["time(0)Value"] = t0Value
                clearPageQuick()

        elif security.upper() == "PUT":
            if putCounter < 1:

                posiionSelection("Put")
                strike = float(input("Enter STRIKE price: "))
                put[f"p1"]["Strike"] = strike
                pPerUnit = float(input("Enter price per unit: "))
                put[f'p1']["pricePerUnit"] = pPerUnit
                position = float(input("Enter Units: "))
                put[f"p1"]["Position"] = position
                t0Value = position * pPerUnit
                put["p1"]["time(0)Value"] = t0Value
                putCounter+=1
                clearPageQuick()

            else:
                posiionSelection("ADD aditional put")
                putCounter+=1
                put[f"p{putCounter}"]= {"Strike":0, "pricePerUnit":0, "Position":0,"time(0)Value": 0}

                posiionSelection("Put")
                strike = float(input("Enter STRIKE price: "))
                put[f"p{putCounter}"]["Strike"] = strike
                pPerUnit = float(input("Enter price per unit: "))
                put[f"p{putCounter}"]["pricePerUnit"] = pPerUnit
                position = float(input("Enter Units: "))
                put[f"p{putCounter}"]["Position"] = position
                t0Value = position * pPerUnit
                put[f"p{putCounter}"]["time(0)Value"] = t0Value
                clearPageQuick()

    payoffForwardReal = []
    payoffPutReal = []
    payoffCallReal = []


    for key,value in forward.items():
        payoffForward = []
        for i in pTvariables:
            payoffForward.append(i- value["Strike"])

        payoffForwardReal.append(payoffForward)

    for key,value in put.items():
        payoffPut = []
        for i in pTvariables:

            strike = value["Strike"]
            if i <= strike:
                pOff = strike -i
                payoffPut.append(pOff)

            elif i > strike:
                payoffPut.append(0)

        payoffPutReal.append(payoffPut)

    for key,value in call.items():
        payoffCall = []
        for i in pTvariables:
            strike = value["Strike"]

            if i >= strike:
                pOff = strike-i
                payoffCall.append(pOff)

            elif i < strike:
                payoffCall.append(0)
        payoffCallReal.append(payoffCall)



    print()


    print(payoffForwardReal)
    print(payoffCallReal)
    print(payoffPutReal)

def lifeExpectncy():
    clearPageQuick()
    posiionSelection("Life Expectancy")
    gender = input("Male or Female: ")
    n = int(input("Enter current age: "))

    maleAgesList = []
    numberOfMalesAlive =[]
    numberOfFemalesAlive = []

    for line in file:

        dataLine = line.split(",")
        maleAges = dataLine[0]
        maleAgesList.append(maleAges)
        numberOfM = dataLine[2]
        numberOfMales=float(numberOfM.replace('"',""))
        numberOfMalesAlive.append(numberOfMales)
        numberOfF = dataLine[5]
        numberOfFemales = float(numberOfF.replace('"', ""))
        numberOfFemalesAlive.append(numberOfFemales)


    calCount = .5

    x = (len(maleAgesList) - 10) - n
    firstPointMale = calCount * ((numberOfMalesAlive[n] - numberOfMalesAlive[n + 1]) / numberOfMalesAlive[n])
    maleCalulation = [firstPointMale]
    print("\n")
    # print("1: ",firstPointMale)

    # y = (len(maleAgesList) -7) - n
    # firstPoint = counter * ((numberOfFemalesAlive[n + 1] - numberOfFemalesAlive[n + 2]) / numberOfMalesAlive[n])
    # femaleCalcualtion = [firstPoint]


    if gender.upper() == "MALE":

        for i in range(1,x):
            calCount +=1

            val = (calCount) * ((numberOfMalesAlive[n+i]- numberOfMalesAlive[n+i+1])/numberOfMalesAlive[n])
            # ((1 / r) - (1 / (r * (1 + r) ** i)))
            maleCalulation.append(val)
            # print(f"{calCount}: ", val)

        lastPointMale = (calCount+1)* (1 / numberOfMalesAlive[n])
        maleCalulation.append(lastPointMale)
        # print(f"{calCount+1}",lastPointMale)
        # print("\n")



        posiionSelection("Answer")
        print("Sum: ",sum(maleCalulation))
        print("\n")
        clearPage()

        return sum(maleCalulation)

def annuityPriceBasedOnLifeExpectancy():
    clearPageQuick()
    r = float(input("Enter Interest: "))/100
    lifeExp = float(input("Enter life Expectancy: "))
    ans = ((1/r)-(1/(r*((1+r)**lifeExp))))

    posiionSelection("Answer")
    print("Ans: ",ans)
    clearPage()

def lifeAnnuity():
    clearPageQuick()
    posiionSelection("Life Annuity Selection")
    print("Halley Method")
    print("de Witt's")
    print("de Moivres")
    method =input("Who's Method (h) or (w) or (m): ")

    if method.lower() =="h":

        posiionSelection("Annuity Halley Method")
        gender = input("Male or Female: ")
        n = int(input("Enter current age: "))
        r = float(input("Enter Interest: "))/100


        maleAgesList = []
        numberOfMalesAlive = []
        numberOfFemalesAlive = []

        for line in file:
            dataLine = line.split(",")
            maleAges = dataLine[0]
            maleAgesList.append(maleAges)
            numberOfM = dataLine[2]
            numberOfMales = float(numberOfM.replace('"', ""))
            numberOfMalesAlive.append(numberOfMales)
            numberOfF = dataLine[5]
            numberOfFemales = float(numberOfF.replace('"', ""))
            numberOfFemalesAlive.append(numberOfFemales)

        rReal = (1 / (1 + r))


        x = (len(maleAgesList) - 10) - n


        firstPointMale = rReal * ((numberOfMalesAlive[n+1]) / numberOfMalesAlive[n])
        maleCalulation = [firstPointMale]
        print("\n")
        # print("1: ", firstPointMale)
        calCount = 1



        if gender.upper() == "MALE":

            for i in range(2, x+1):
                calCount +=1
                # print(i)
                val = (rReal**i)* ((numberOfMalesAlive[n + i] / numberOfMalesAlive[n]))
                maleCalulation.append(val)
                # print(f"{calCount}: ", val)

            lastPointMale = (rReal**(calCount+1)) * (1 / numberOfMalesAlive[n])
            maleCalulation.append(lastPointMale)
            # print(f"{calCount+1}", lastPointMale)
            print("\n")

            posiionSelection("Answer")
            print("Sum: ", sum(maleCalulation))
            clearPage()
            numberOfMalesAlive[n]
            return sum(maleCalulation)

    elif method.lower() == "w":

        posiionSelection("Annuity de Witt Method")
        gender = input("Male or Female: ")
        n = int(input("Enter current age: "))
        r = float(input("Enter Interest: ")) / 100

        maleAgesList = []
        numberOfMalesAlive = []
        numberOfFemalesAlive = []

        for line in file:
            dataLine = line.split(",")
            maleAges = dataLine[0]
            maleAgesList.append(maleAges)
            numberOfM = dataLine[2]
            numberOfMales = float(numberOfM.replace('"', ""))
            numberOfMalesAlive.append(numberOfMales)
            numberOfF = dataLine[5]
            numberOfFemales = float(numberOfF.replace('"', ""))
            numberOfFemalesAlive.append(numberOfFemales)


        x = (len(maleAgesList) - 10) - n
        firstPointMale = ((1 /(1+r))  * ((numberOfMalesAlive[n+1] - numberOfMalesAlive[n + 2]) / numberOfMalesAlive[n]))
        maleCalulation = [firstPointMale]
        print("\n")
        # print("1: ", firstPointMale)
        calCount = 1


        if gender.upper() == "MALE":

            for i in range(2, x):
                calCount += 1

                val = ((1 / r) - (1 / (r * (1 + r) ** i))) * ((numberOfMalesAlive[n + i] - numberOfMalesAlive[n + i + 1]) / numberOfMalesAlive[n])

                maleCalulation.append(val)
                # print(f"{calCount}: ",val)

            lastPointMale = (((1 / r) - (1 / (r * (1 + r) ** (calCount+1)))) * (1 / numberOfMalesAlive[n]))
            maleCalulation.append(lastPointMale)
            # print(f"{calCount+1}: ", lastPointMale)

            posiionSelection("Answer")
            print("Sum: ", round(sum(maleCalulation),10))
            clearPage()


    elif method.lower() =="m":
        posiionSelection("Price of Life Annuity Under de Moivre")
        h = int(input("Enter possible life age: "))
        v = int((input("Enter current age:  ")))
        k = h - v
        y = float(input("Enter interest %: ")) / 100

        answer = (1 / y) * (1 - (((1 + y) / k) * ((1 / y) - (1 / (y * ((1 + y) ** k))))))
        print("\n")
        print("Answer: ", answer)
        print("\n")

        print("y: ", y)
        print("k: ", k)
        print("This is using the simple equation")
        print("equation: (1 / y) * (1 - (((1 + y) / k) * ((1 / y) - (1 /( y * ((1 + y) ** k))))))")
        clearPage()

def wealthForRetirment():
    clearPageQuick()
    selection("Wealth for Retirment")
    r=  float(input("Implied Return: ")  )/100
    y = float(input("Income per Year required: ") )
    ageMax = int(input("Maxium Age: ")  )
    ageCurr = int(input("Current Age: ")     )
    t = ageMax-ageCurr

    W = (y/r)*(1-(1/((1+r)**t)))
    print("You need "+str(round(W,4)) +" to retire")
    clearPage()

def yearsUntilExhastion():
    clearPageQuick()

    selection("Years Until Exhaustation")
    r=  float(input("Implied Return: ")  )/100
    w = float(input("Wealth: "))
    y = float(input("Enter funds needed per year: "))
    try:

        T = round((1/math.log(1+r))*math.log(y/(y-(r*w))),2)
        print("You have " + str(T) + " years until you run our of money")

    except:
        print(f"With {r*100} % you will not exhaust your finds")

    clearPage()

def mortgageSavings():
    clearPageQuick()
    selection("Mortgage Savings")
    p = float(input("Enter Takeback price: "))
    t = float(input("Enter Time Period: "))
    a = float(input("Enter ammortization period: "))
    i = float(input("Enter lower interest rate: "))/100
    I = float(input("Enter Higher interest rate: "))/100


    x = p/((1/I)-(1/(I*((1+I)**t))))
    y = p/((1/i)-(1/(i*((1+i)**t))))
    ms = (x-y)*((1/I)-(1/(I*((1+I)**a))))
    ms =round(ms, 2)

    xi = x*((1/I)-(1/(I*((1+I)**(t-a)))))
    yi = y*((1/i)-(1/(i*((1+i)**(t-a)))))
    rs = (xi-yi)/((1+I)**a)
    rs = round(rs,2)


    print("\n")
    print("-"*30)
    print(f"Annual Mortgage Payment at {round(I*100,2)}% : {round(x,2)}")
    print(f"Annual Mortgage Payment at {round(i* 100,2)}% : {round(y,2)}")
    print("-"*30)
    print(f"Mortgage Savings: {ms}")
    print(f"Refinancing Savings: {rs}")
    print(f'Total Savings: {rs + ms}')




    clearPage()

def binomModel365():


    clearPageQuick()
    posiionSelection("Binomial Model")
    t = float(input("days: "))/365
    days = t*365
    r = float(input("CC rate: "))
    vol = float(input("Volatility parameter: "))
    m = float(input("Drift paramter: "))
    n =int(input("Number of sub periods: "))
    # kCall = float(input("K- call: "))
    # kPut = float(input("K -put: "))

    h = (t/n)
    u = math.exp(m*h+vol*math.sqrt(h))
    d = math.exp(m*h-vol*math.sqrt(h))
    R = math.exp(r*h)
    risk = ((R-d)/(u-d))

    testing()    
    print("\n")
    print("H: ", round(h,6))
    print("UP - Factor", round(u,6))
    print("Down - Factor",round(d,6))
    print("R", round(R,6),r,h)
    print("Risk-Nuetralized probability", round(risk,6))
    print("\n")

    # print(f'S0 -  {S0}')
    # for i in (range(n)):
    #     i +=1

    #     upStock = (S0 *(u)**i)
    #     downStock = (S0 * (d) ** i)

    #     upStock = round(upStock,3)
    #     downStock = round(downStock,3)

    #     print(upStock,downStock)
    #     # print('S'+('u'*i)+': '+ str(upStock))
    #     # print('S' + ('d' * i) + ': ' + str(downStock))
    #     for i in reversed(range(n)):
    #         upStockNew = (upStock * (u))
    #         downStockNew = (upStock * d)
    #         print(upStockNew,downStockNew)

    #     for i in reversed(range(n)):
    #         upStockNew = (downStock * (u))
    #         downStockNew = (downStock * d)
    #         print(upStockNew, downStockNew)







    clearPage()

def blackScholas():
    clearPageQuick()
    posiionSelection("Black Scholas")
    s = float(input("Enter S0: "))
    r = float(input("Enter Rate: "))
    vol = float(input("Enter Vol: "))
    k = float(input("Enter K: "))
    l = float(input("360 or 365: "))
    d = float(input("Number of Days: "))
    print("\n")
    t =(d/l)
    b = round(math.exp(-r*t),6)
    d1 = round((math.log(s/k)+((r+(.5*(vol**2)))*t))/(vol*math.sqrt(t)),4)
    d2 = round(d1 - (vol*math.sqrt(t)),4)



    if d1 >0:
        # DataFrame of Ztable
        zTable = open("Ztable.csv")

        index1 = str(d1*10000)
        if len(index1)<6:
            lsit = index1.split()
            lsit.insert(0,0)
            index1 = ''
            for i in lsit:
                index1 = str(index1) +str(i)

        oldIndex1 = index1
        index1 = str(d1 * 1000)
        index1 = int(index1[0])
        index1 = index1 + 1
        index2 = str(d1 * 1000)
        index2 = int(index2[1])
        index2 = index2 + 1
        index2i = str(d1 * 1000)
        index2i = int(index2i[1])
        index2i = index2i + 1 + 1

        index3 = str(oldIndex1)
        index3i = index3[2]
        index4 = index3[3]
        index3 = float(index3i + index4)


        index3 = index3 / 100

        for i in zTable:
            index1 -= 1
            if index1 == 0:
                col = i.split(",")
                for ii in col:
                    index2 -= 1
                    index2i -= 1
                    if index2 == 0:
                        n1 = float(ii)

                    if index2i == 0:
                        n2 = float(ii)

        N1 = round(n1 + (index3 * (n2 - n1)), 4)
        print(f"{n1}-{index3}({n1}-{n2})")

    if d1 <0:
        zTable = open("negZtable.csv")
        # DataFrame of Ztable
        d1 = d1*-1

        index1 = str(d1*10000)
        if len(index1)<6:
            lsit = index1.split()
            lsit.insert(0,0)
            index1 = ''
            for i in lsit:
                index1 = str(index1) +str(i)


        print(index1)
        oldIndex1 = index1
        index1 = int(index1[0])
        print(index1,type(index1))
        index1 = index1 + 1
        index2 = str(d1 * 1000)
        index2 = int(index2[1])
        index2 = index2 + 1
        index2i = str(d1 * 1000)
        index2i = int(index2i[1])
        index2i = index2i + 1 + 1

        index3 = str(oldIndex1)
        index3i = index3[2]
        index4 = index3[3]
        index3 = float(index3i + index4)
        index3 = index3 / 100

        for i in zTable:
            index1 -= 1
            if index1 == 0:
                col = i.split(",")
                for ii in col:
                    index2 -= 1
                    index2i -= 1
                    if index2 == 1:
                        n1 = float(ii)

                    if index2i == 2:
                        n2 = float(ii)

        d1 = d1*-1
        print(index3, n1, n2)
        N1 = round(n1 - (index3 * (n1 - n2)), 4)
        print(f"{n1}-{index3}({n1}-{n2})")

    if d2 >0:
        zTable = open("Ztable.csv")
        index1x = str(d2 * 1000)
        print(index1x)
        index1x= int(index1x[0])
        index1x = index1x+1
        index2x = str(d2 *1000)
        index2x = int(index2x[1])
        index2x = index2x +1
        index2ix = str(d2 *1000)
        index2ix = int(index2ix[1])
        index2ix = index2ix +1
        index3x = str(d2*10000)
        index3ix = index3x[2]
        index4x = index3x[3]
        index3x = int(index3ix +index4x)
        index3x = index3x/100

        for ix in zTable:
            index1x -=1
            if index1x ==0:
              col = ix.split(",")
              for iix in col:
                   index2x-= 1
                   index2ix -=1
                   if index2x ==0:
                       n1x =float(iix)

                   if index2ix ==0:
                       n2x = float(iix)

        N2 = round(n1x + (index3x*(n2x-n1x)),4)

    if d2 < 0:
        zTable = open("negZtable.csv")
        d2 = d2 * -1

        index1x = str(d2 * 1000)
        index1x = int(index1x[0])
        index1x = index1x + 1
        index2x = str(d2 * 1000)
        index2x = int(index2x[1])
        index2x = index2x + 1

        index2ix = str(d2 * 1000)
        index2ix = int(index2ix[1])
        index2ix = index2ix + 1
        index3x = str(d2 * 10000)
        index3ix = index3x[2]
        index4x = index3x[3]
        index3x = int(index3ix + index4x)
        index3x = index3x / 100

        for ix in zTable:
            index1x -= 1
            if index1x == 0:
                col = ix.split(",")
                for iix in col:
                    index2x -= 1
                    index2ix -= 1
                    if index2x == 1:
                        n1x = float(iix)

                    if index2ix == 2:
                        n2x = float(iix)

        d2 = d2*-1
        N2 = round(n1x - (index3x * (n1x - n2x)), 4)


    print(f"B      =  {b}")
    print(f"D1    = {d1}")
    print(f'N(d1) = {N1}')
    print(f"D2    =  {d2}")
    print(f'N(d2) = {N2}')

    posiionSelection("Call")
    u = round(s*N1,4)
    i = round(k*b*N2,4)
    print(f'C(1A) = {u}')
    print(f'C(1) ={i}')
    print(f'BS call Price ={round(u-i,4)}')

    posiionSelection("Put")
    o = round(-s*(1-N1),4)
    p = round(k*b*(1-N2),4)
    print(f'P(1A) = {o}')
    print(f'P(1) = {p}')
    print(f'BS put Price = {round(o+p,4)}')

    posiionSelection("Call-Put Parity")
    print(f'{round(u-i,4)} - {s} + {round(k*b,4)} = {round(round(u-i,4) - s +(k*b),4) }')

def MacaulayDurationLifeAnnuity():
    clearPageQuick()
    posiionSelection("Macaulay Duration of Life Annuity")
    r = float(input("Enter Interest: "))
    cA = int(input("Enter CURRENT Age: "))
    fA = int(input("Enter EXPECTED Age: "))
    k = fA- cA

    x = 0.001
    r2 = (r+ x)

    p0 = ((1 / r) - ((1 + r) / (r ** 2 *k)) + ((1) / (r **2 *k *((1 + r) **(k - 1)))))
    p1 = ((1 / r2) - ((1 + r2) / (r2 ** 2 * k)) + ((1) / (r2 ** 2 * k * ((1 + r2) ** (k - 1)))))

    changeInP = p1-p0
    z = (changeInP/x)
    final = ((1+r)/(p0))*(abs(z))
    print("-"*20)
    print(f"k = {k}")
    print(f'r = {r}')
    print(f'r + .001  = {r2}')
    print(f"P[{r}] = {p0}")
    print(f"P[{r2}] = {p1}")
    print(f"{round(changeInP,4)} = p[{round(r2,4)}]-p[{round(r,4)}]")
    print(f"answer = ({round(1+r,4)}/{round(p0,4)}) * ({round(changeInP,4)}/{r2}-{r})")
    print("\n")
    print("Answer: "+str(round(final,2)))
    clearPage()



# main loop to run all functions in program or to quit
while startStop == True:


    print("\n")
    print("Directory : SELECT ONE")
    print("-" * 30)
    print("\n")

    for x in selectionDirectory:
        print(x)
    print("-" * 30)
    print("\n")
    response = str(input("Please Make a SELECTION from above: "))

    if response == "0":
       paymentCalculator()

    elif response =="1":
        holdingPeriodReturns()

    elif response  =="2":
        bondPrice()

    elif response == "3":
        PV()

    elif response == "4":
        FV()

    elif response == "5":
        CAPM()

    elif response == "6":
        maturityValue()

    elif response == "7":
        interest()

    elif response == "8":
        FVof1Dollar()

    elif response == "9":
        contractPostions()

    elif response == "10":
        lifeExpectncy()

    elif response =="11":
        annuityPriceBasedOnLifeExpectancy()

    elif response == "12":
        lifeAnnuity()

    elif response == "13":
        wealthForRetirment()

    elif response == "14":
        yearsUntilExhastion()

    elif response == "15":
        mortgageSavings()

    elif response == "16":
        binomModel365()

    elif response == "18":
        blackScholas()

    elif response == "19":
        MacaulayDurationLifeAnnuity()

    elif response.upper() == "QUIT":

        clearPage()
        print("Thank You")
        startStop == False




    else:
        errorStatement()


