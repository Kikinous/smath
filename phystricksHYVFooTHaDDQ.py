# -*- coding: utf8 -*-
from phystricks import *
def HYVFooTHaDDQ():
    pspicts,figs = IndependentPictures("HYVFooTHaDDQ",4)
    for psp in pspicts:
        psp.dilatation(1)

    Ap=Point(0,0)
    Bp=Point(3,0)
    Cp=Point(0.5,2)
    trig=Polygon(Ap,Bp,Cp).rotation(25)
    A=trig.vertices[0]
    B=trig.vertices[1]
    C=trig.vertices[2]
    trig.put_mark(0.2,pspict=pspicts)
    M=trig.edges[0].midpoint()
    M.put_mark(0.2,angle=None,added_angle=180,text="\( M\)",automatic_place=(pspicts,""))
    trig.edges[0].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspicts)

    ang=AngleAOB(A,C,B)
    ang.put_mark(0.2,angle=None,added_angle=0,text="\SI{34}{\degree}",automatic_place=(pspicts,""))
    no_symbol(trig.vertices)
    pspicts[0].DrawGraphs(trig,M,ang)


    trig=Polygon(Ap,Bp,Cp).rotation(47)
    trig.put_mark(0.2,pspict=pspicts)
    A=trig.vertices[0]
    B=trig.vertices[1]
    C=trig.vertices[2]
    M=trig.edges[0].midpoint()
    cod1=trig.edges[0].get_code(n=2,d=0.1,l=0.3,pspict=pspicts)
    cod2=trig.edges[2].get_code(n=2,d=0.1,l=0.3,pspict=pspicts)
    CM=Segment(C,M)
    rh=RightAngleAOB(C,M,B)
    pspicts[1].DrawGraphs(trig,M,CM,rh,cod1,cod2)

    trig=Polygon(Ap,Bp,Cp).rotation(47)
    trig.put_mark(0.2,pspict=pspicts)
    A=trig.vertices[0]
    B=trig.vertices[1]
    C=trig.vertices[2]
    M=trig.edges[0].midpoint()
    cod1=trig.edges[0].get_code(n=2,d=0.1,l=0.3,pspict=pspicts)
    cod2=trig.edges[2].get_code(n=2,d=0.1,l=0.3,pspict=pspicts)
    CM=Segment(C,M)
    rh=RightAngleAOB(C,M,B)
    ang=AngleAOB(M,A,C)
    ang.put_mark(0.2,angle=None,added_angle=0,text="\SI{45}{\degree}",automatic_place=(pspicts,""))
    pspicts[2].DrawGraphs(trig,M,CM,rh,cod1,cod2)


    Cp=Circle(  Segment(A,B).midpoint(),1    ).get_point(30)
    trig=Polygon(Ap,Bp,Cp).rotation(0)
    A=trig.vertices[0]
    B=trig.vertices[1]
    C=trig.vertices[2]
    trig.put_mark(0.2,pspict=pspicts)
    M=trig.edges[0].midpoint()
    M.put_mark(0.2,angle=None,added_angle=180,text="\( M\)",automatic_place=(pspicts,""))
    rh=RightAngleAOB(A,C,B)
    trig.edges[0].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspicts)

    no_symbol(trig.vertices)
    pspicts[3].DrawGraphs(trig,M,rh)


    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
