#!/usr/bin/python
# -*- coding: utf8 -*-
import turtle as t
a=eval(input('Ingrese el número de lados del poligono : '))
t.color("blue")
c=0
def pol(c):
	for i in range(c):
		t.down()
		t.left(360/c)
		t.forward(20)
		
def fig(c):
	for i in range(4):
		t.penup()
		t.forward(100)
		t.pendown
		t.setheading(360)
		pol(c)	
		t.setheading(360)
		t.left(90+90*i)
		
fig(a)
t.done()

