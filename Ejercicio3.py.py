#!/usr/bin/python
# -*- coding: utf8 -*-
import turtle as t
b=eval(input('Ingrese número de lados del  poligono que no verá : '))
a=eval(input('Ingrese número de lados del segundo poligono : '))
t.color("blue")
c=0
d=0
def pol(c):
	for i in range(c):
		t.down()
		t.left(360/c)
		t.forward(20)
		
def fig(c,d):
	for i in range(d):
		t.penup()
		t.forward(100)
		t.pendown
		t.setheading(360)
		pol(c)	
		t.setheading(360)
		t.left(360/d+(i*360/d))
		
fig(a,b)
t.done()

