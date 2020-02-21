# -*- encoding: utf-8 -*-

#Импортируем нужные библиотеки
import turtle, random
from turtle import*

#Даём название окну с программой
turtle.title("Треугольник Серпинского")

#Даём размеры окна с программой
window = turtle.Screen()
window.bgcolor("white")
window.setup(900, 800)

#Задаём скорость рисования.
turtle.speed(0)

#Переменная для бесконченого цикла
cycle = True

#Случайные координаты точки "1"
x1 = random.randint(-350, 350)
y1 = random.randint(100, 300)

#Случайные координаты точки "2"
x2 = random.randint(-350, -100)
y2 = random.randint(-350, -100)

#Случайные координты точки "3"
x3 = random.randint(100, 350)
y3 = random.randint(-350, 0)

#Рисуем точку "A"
turtle.color("gold")
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.dot(9)
turtle.color("black")
turtle.write("1")

#Рисуем точку "B"
turtle.color("gold")
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.dot(9)
turtle.color("black")
turtle.write("2")

#Рисуем точку "C"
turtle.color("gold")
turtle.penup()
turtle.goto(x3, y3)
turtle.pendown()
turtle.dot(9)
turtle.color("black")
turtle.write("3")

#Рандомно ставим стартовую точку
xStartPoint = random.randint(-150, 150)
yStartPoint = random.randint(-150, 150)
turtle.color("blue")
turtle.penup()
turtle.goto(xStartPoint, yStartPoint)
turtle.pendown()
turtle.dot(5)
turtle.write("First starting point")

#Бесконечный цикл для рисования точек
while cycle:
	center = random.randint(1, 3)
	print("Выбранная точка:", center)

	#Находим центр между точкой "1" и новой стартовой точкой
	if center == 1:
		turtle.color("black")
		turtle.penup()
		xStartPoint = (x1+xStartPoint)/2
		yStartPoint = (y1+yStartPoint)/2
		turtle.goto(xStartPoint, yStartPoint)
		turtle.pendown()
		turtle.dot(3)

#Находим центр между точкой "2" и новой стартовой точкой
	if center == 2:
		turtle.color("black")
		turtle.penup()
		xStartPoint = (x2+xStartPoint)/2
		yStartPoint = (y2+yStartPoint)/2
		turtle.goto(xStartPoint, yStartPoint)
		turtle.pendown()
		turtle.dot(3)

#Находим центр между точкой "3" и новой стартовой точкой
	if center == 3:
		turtle.color("black")
		turtle.penup()
		xStartPoint = (x3+xStartPoint)/2
		yStartPoint = (y3+yStartPoint)/2
		turtle.goto(xStartPoint, yStartPoint)
		turtle.pendown()
		turtle.dot(3)

#The Project Is Made By AndrSad
