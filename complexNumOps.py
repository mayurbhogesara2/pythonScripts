def getrealNum(rel1, img1):
    resRel = rel1 
    print('real Num is ' +  str(resRel))
    
def getimmaginaryNum(rel1, img1):
    resImg = img1
    print('immaginary Num is ' +  str(resImg) + ' i')
    
def getconjugatexNum(rel1, img1):
    resRel = rel1
    resImg = img1 * -1
    if img1 < 0:
        print('conjugatex Num is ' +  str(resRel) + ' + ' + str(resImg) + ' i')
    else:
        print('conjugatex Num is ' +  str(resRel) + str(resImg) + ' i')
    
    
def getabsoluteorModulusNum(rel1, img1):
    sqRel = rel1 * rel1
    sqImg = img1 * img1
    sqAdd = sqRel + sqImg
    finalMod= sqAdd ** 0.5
    print('absolute or Modulus of Num is ' +  str(finalMod))
    
def  getargumentNum(rel1, img1):
    resArg = img1 / rel1
    import math as math
    resRad = math.atan(resArg)
    print('argument Num is ' +  str(resRad))
    
def addTwoComplexNum(rel1, img1, rel2, img2):
    resRel = rel1 + rel2
    resImg = img1 + img2
    print('Addition is ' +  str(resRel) + ' + ' + str(resImg) + ' i')
    

def subtractTwoComplexNum(rel1, img1, rel2, img2):
    resRel = rel1 - rel2
    resImg = img1 - img2
    print('Subtraction is ' +  str(resRel) + ' + ' + str(resImg) + ' i') 

def multiplyTwoComplexNum(rel1, img1, rel2, img2):
    resRel = rel1 * rel2
    resImg = img1 * img2
    print('Multiplication is ' +  str(resRel) + ' + ' + str(resImg) + ' i')  
    
def divideTwoComplexNum(rel1, img1, rel2, img2):
    resRel = rel1 / rel2
    resImg = img1 / img2
    print('Division is ' +  str(resRel) + ' + ' + str(resImg) + ' i')  

def getSecondComplexNum(opsNum, rel1, img1):
    print('take 2nd complex no')
    rel2 = float(input('enter real part of complex no.'))
    img2 = float(input('enter imaginary part of complex no.'))
    print('Your complex no is ' + str(rel2) + ' + ' + str(img2) + 'i' )
    opsNum=int(opsNum)
    if opsNum == 1:
        addTwoComplexNum(rel1, img1, rel2, img2)
    elif opsNum == 2:
        subtractTwoComplexNum(rel1, img1, rel2, img2)
    elif opsNum == 3:
        multiplyTwoComplexNum(rel1, img1, rel2, img2)
    elif opsNum == 4:
        divideTwoComplexNum(rel1, img1, rel2, img2)
        
        
def doSingleComplexNumberOps(opsNum, rel1, img1):
    opsNum=int(opsNum)
    if opsNum == 5:
        getrealNum(rel1, img1 )
    elif opsNum == 6:
        getimmaginaryNum(rel1, img1)
    elif opsNum == 7:
        getconjugatexNum(rel1, img1)
    elif opsNum == 8:
        getabsoluteorModulusNum(rel1, img1)
    elif opsNum == 9:
        getargumentNum(rel1, img1)
    
    

#take input for real and imaginary no
rel1 = float(input('enter real part of complex no.'))
img1 = float(input('enter imaginary part of complex no.'))

#show the 1st complex no
print('Your complex no is ' + str(rel1) + ' + ' + str(img1) + 'i' )

#show list of operations which you can perofrm and ask for input for the operations
#peration=int(input('Please enter operation number\n1.Addition\n2.Subtraction\n3.Multi\n4.Div\n5.Get Real part of Complexnumber\n6Get Immaginary of complex number
#operation=int(operation)
operation=int(input('Please enter operation number\n1.Addition\n2.Subtraction\n3.Multi\n4.Div\n5.Find Real part of Complexnumber\n6.Find Immaginary of complex number\n7.Find Conjugate of Complex number\n8.Find Absolute/Modulus of complex number\n9.Find Argument of complex number\n'))
if ((operation == 1)  or (operation == 2) or (operation == 3) or (operation == 4)):
    getSecondComplexNum(operation, rel1, img1)
elif ((operation == 5)  or (operation == 6) or (operation == 7) or (operation == 8) or (operation == 9)):
    doSingleComplexNumberOps(operation, rel1, img1)
else :
    print('Kindly provide proper input')

    
