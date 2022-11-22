# import turtle
# from turtle import *

# def init():
#     color("white", "white")

#     forward(100)
#     left(90)
#     forward(100)
#     left(90)

#     color("black","white")

# init()

# def draw_inner_square():
#     for i in range(4):
#         forward(200)
#         left(90)

# draw_inner_square()

# # begin_fill()
# # for i in range(4):
# #     forward(100)
# #     left(90)
# #     print(turtle.pos())
# # end_fill()
# done()

import tkinter

window = tkinter.Tk()
window.title("5호관 지도")
window.geometry("640x400+100+100")
window.resizable(False,False)

canvas = tkinter.Canvas(window,relief="solid",bd=2)

canvas.create_line(0,0,100,100)

canvas.pack()

window.mainloop()