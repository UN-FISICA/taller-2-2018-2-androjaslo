#!/usr/bin/python
# -*- coding: utf8 -*-
import turtle as t

t.color("green")

for i in range(4):
	t.penup()
	t.forward(200)
	for i in range(4):
			t.pendown()
			t.forward(40)
			t.right(90)
	t.left(90)
t.done()
t.bye()
