# -*- coding: utf8 -*-
from phystricks import *
def figureAEcZqpP():
    pspict,fig = SinglePicture("figureAEcZqpP")
    pspict.dilatation(0.7)

    A=Point(0,0)
    B=Point(1,3)
    C=Point(-2,4)
    D=Point(-3,-1)
    E=Point(3,-2)

    A.put_mark(0.2,45,"\( A\)",pspict=pspict)
    B.put_mark(0.2,45,"\( B\)",pspict=pspict)
    C.put_mark(0.2,45,"\( C\)",pspict=pspict)
    D.put_mark(0.2,45,"\( D\)",pspict=pspict)
    E.put_mark(0.2,45,"\( E\)",pspict=pspict)

    pspict.DrawGraphs(A,B,C,D,E)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
