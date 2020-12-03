import turtle
import random

#전역 변수 선언
myTurtle, tX, tY, tColor, tSize, tShape=[None]*6

shapeList = []
playTurtles = [] #거북 2차원 리스트

swidth, sheight = 500,500

#Part of Main code 메인코드 부분
if __name__ == "__main__":
    turtle.title("거북이 리스트 활용 ")
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth, sheight)
    shapeList = turtle.getshapes()
    print("shapeList %s"%shapeList)
    for i in range(0,100):
        random.shuffle(shapeList)
        myTurtle = turtle.Turtle(shapeList[0])
        tX = random.randrange(-swidth/2, swidth/2)
        tY = random.randrange(-sheight/2, sheight/2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1,3)
        playTurtles.append([myTurtle, tX, tY, tSize, r, g, b])
    print("리스트 확인: %s"% playTurtles, end=' ')
    for tList in playTurtles:
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])
    turtle.done()