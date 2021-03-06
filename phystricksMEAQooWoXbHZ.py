# -*- coding: utf8 -*-
from phystricks import *
def MEAQooWoXbHZ():
    pspict,fig = SinglePicture("MEAQooWoXbHZ")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(2,0)
    C=Point(0,4)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.3,pspict=pspict)

    c1=triangle.edges[0]
    c2=triangle.edges[1]
    c3=triangle.edges[2]
    rh=RightAngle(  c1,c3,1,0   )

    mes1=c1.get_measure(0.2,0.1,text="\( 2\)",pspict=pspict,position="N")
    mes2=c3.get_measure(0.2,0.1,text="\( 6\)",pspict=pspict,position="E")

    pspict.DrawGraphs(triangle,rh,mes1,mes2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
