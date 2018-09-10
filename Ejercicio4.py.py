#!/usr/bin/python
# -*- coding: utf8 -*-
import turtle as t
b=eval(input('Ingrese número de lados del  poligono  : '))
a=eval(input('Ingrese número de filas de la pirámide : '))
t.color("red")
c=0
d=0
def pol(c):
	for i in range(c):
		t.down()
		t.left(360/c)
		t.forward(30)
def fila(c,d):
	for i in range (d):
		for j in range (i+1):
			pol(c)
			t.up()
			t.forward(10*c)
		t.up
		t.setheading(0)
		t.right(90)
		t.forward(10*c)
		t.setheading(180)
		t.forward((10*c)+((i+1)*(10*c)))
		t.setheading(0)
		
			
	
		
fila(b,a)
t.done()
