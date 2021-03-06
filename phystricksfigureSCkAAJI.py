# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def figureSCkAAJI():
    pspict,fig = SinglePicture("figureSCkAAJI")
    pspict.dilatation(1)

    R = PolynomialRing(QQ,str('x'))
    f=phyFunction(R.lagrange_polynomial( [(2,1),(5,1),(7/2,3)] )).graph(1,6)

    K=Rectangle(mx=1.5,Mx=5,my=1.5,My=3.5)
    K.filled()
    K.fill_parameters.color="black"

    pspict.DrawGraphs(f,K)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
