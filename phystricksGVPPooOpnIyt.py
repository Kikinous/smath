# -*- coding: utf8 -*-
from phystricks import *
def GVPPooOpnIyt():
    pspict,fig = SinglePicture("GVPPooOpnIyt")
    pspict.dilatation(1)

    A=Point(3.5,0)
    B=Point(0,0)
    C=Point(-1,-2)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)

    K=Segment(B,A).midpoint()
    L=Segment(A,C).midpoint()
    drm=Segment(L,K)

    trig.edges[1].put_mark(0.1,trig.edges[1].advised_mark_angle+180,"\( 3\)",automatic_place=(pspict,""))
    m=Segment(A,L).get_mark(0.2,None,"\( 5\)",automatic_place=(pspict,""))

    K.put_mark(0.2,None,"\( K\)",automatic_place=(pspict,""))
    L.put_mark(0.2,None,"\( L\)",automatic_place=(pspict,""))

    for x in [A,B,C,K,L]:
        x.parameters.symbol=""

    pspict.comment="The marks of 'K', 'L' and the segment BC are correclty placed."
    pspict.DrawGraphs(trig,drm,K,L,m)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

