# -*- coding: utf8 -*-
from phystricks import *
def figureCSIQETx():
    pspict,fig = SinglePicture("figureCSIQETx")
    pspict.dilatation(1)

    x=var('x')
    <+Définition des objets+>

    pspict.DrawGraphs(<++>)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

----------------

    pspicts,fig = MultiplePictures("figureCSIQETx",3)
    pspicts[0].mother.caption="<+caption1+>"
    pspicts[1].mother.caption="<+caption2+>"
    pspicts[2].mother.caption="<+caption3+>"

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    <+Définition des objets+>

    for psp in pspicts:
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
