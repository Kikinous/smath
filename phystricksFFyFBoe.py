# -*- coding: utf8 -*-
from phystricks import *
def FFyFBoe():
    pspict,fig = SinglePicture("FFyFBoe")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    f=phyFunction( sin(x)+x ).graph(-5,5)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
