#let start
import turtle
heart = turtle.Turtle()
heart.color('black','red')
heart.begin_fill()
heart.pensize(5)
heart.left(50)
heart.forward(133)
heart.circle(50,200)
heart.right(140)
heart.circle(50,200)
heart.forward(133)
heart.end_fill()

heart.color('white')
heart.begin_fill()
heart.left(45)
heart.backward(70)
heart.end_fill()

heart.pensize(4)
heart.color('red')
heart.begin_fill()
heart.left()
heart.forward(245)
heart.end_fill()

turtle.mainloop()