import turtle as t
t.screensize(300,300)
t.pu()
t.goto(0,70)
while True:
    #свитафор
    t.pd()
    t.begin_fill()
    t.circle(20)
    t.fillcolor("red")
    t.end_fill()
    
    #человек
    t.pu()
    t.right(90)
    t.goto(80,-80)
    t.right(45)
    t.pd()
    t.forward(20)
    t.left(180)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(180)
    t.forward(20)
    t.right(45)
    t.forward(30)
    t.pu()
    t.right(90)
    t.forward(1)
    t.pd()
    t.circle(10)
    t.right(90)
    t.forward(10)
    t.left(45)
    t.forward(20)
    t.left(180)
    t.forward(20)
    t.left(135)
    t.right(45)
    t.forward(20)
    t.pu()
    t.goto(0,70)
    t.right(225)

    

