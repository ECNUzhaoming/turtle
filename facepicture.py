import turtle as t
t.pensize(4)
t.colormode(255)
t.setup(700,500)
t.speed(0)
t.pu()
t.goto(-100,200)
#t.circle(100)
t.pd()
# t.forward(-83)  # 前行183个单位
# t.left(45)
# t.forward(30)
t.circle(-100,20)
t.circle(-200,140)
t.circle(-100,40)
t.circle(-200,160)
t.pu()#lefteye
t.goto(-190,120)
#t.circle(100)

t.pd()
t.circle(-400,10)
t.pu()#righteye
t.goto(-80,120)
#t.circle(100)
t.pd()
t.circle(-400,10)

t.pu()#nose
t.goto(-120,20)
#t.circle(100)
t.pd()
t.forward(2)

t.pu()#mouse
t.goto(-180,-120)
#t.circle(100)
t.pd()
t.circle(300,10)

t.left(90)
for i in range(1,180):
    t.pu()#hair
    t.goto(-180+i,160)
    #t.circle(100)
    t.pd()
    t.forward(70)
    i+=1

t.hideturtle()
t.done();