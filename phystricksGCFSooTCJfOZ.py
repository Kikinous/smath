# -*- coding: utf8 -*-
from phystricks import *
def GCFSooTCJfOZ():
    pspicts,figs = IndependentPictures("GCFSooTCJfOZ",4)

    pspicts[0].dilatation(1)
    names_list=["A","B","C"]
    ll=[5,12,13]
    length_list=[   "\( {}\)".format(x) for x in ll   ]
    A=Point(0,0)
    B=Point(2,1)
    l=1
    K=Segment(B,A).orthogonal().F
    v=K-B
    C=B+l*v
    ang=Angle(C,A,B,r=0.3)

    for p in A,B,C:
        p.parameters.symbol=""
    trig=Polygon(A,B,C)
    trig.put_mark(0.2,text_list=[   "\( "+s+"\)" for s in names_list   ],pspict=pspicts)
    rh=RightAngle(Segment(A,B),Segment(B,C),0.2,0,1)

    m1=Segment(A,B).get_mark(0.15,None,length_list[0],automatic_place=(pspicts,""))
    m2=Segment(B,C).get_mark(0.15,None,length_list[1],automatic_place=(pspicts,""))
    m3=Segment(C,A).get_mark(0.15,None,length_list[2],automatic_place=(pspicts,""))
    pspicts[0].DrawGraphs(trig,rh,m1,m2,m3,ang)


    pspicts[1].dilatation(0.4)
    ll=[9,40,41]
    length_list=[   "\( {}\)".format(x) for x in ll   ]
    names_list=["K","L","M"]
    names_list=["A","B","C"]
    A=Point(0,0)
    B=Point(1,3)
    l=-2
    K=Segment(B,A).orthogonal().F
    v=K-B
    C=B+l*v
    ang=Angle(B,A,C,r=0.3)

    for p in A,B,C:
        p.parameters.symbol=""
    trig=Polygon(A,B,C)
    trig.put_mark(0.2,text_list=[   "\( "+s+"\)" for s in names_list   ],pspict=pspicts)
    rh=RightAngle(Segment(A,B),Segment(B,C),0.5,0,1)
    m1=Segment(B,A).get_mark(0.2,None,length_list[0],automatic_place=(pspicts,""))
    m2=Segment(C,B).get_mark(0.2,None,length_list[1],automatic_place=(pspicts,""))
    m3=Segment(A,C).get_mark(0.2,None,length_list[2],automatic_place=(pspicts,""))
    pspicts[1].DrawGraphs(trig,rh,m1,m2,m3,ang)

    pspicts[2].dilatation(0.9)
    ll=[18,80,""]
    length_list=[   "\( {}\)".format(x) for x in ll   ]
    names_list=["S","T","U"]
    names_list=["A","B","C"]
    A=Point(0,0)
    B=Point(0,3)
    l=0.7
    K=Segment(B,A).orthogonal().F
    v=K-B
    C=B+l*v
    ang=Angle(B,C,A,r=0.5)

    for p in A,B,C:
        p.parameters.symbol=""
    trig=Polygon(A,B,C)
    trig.put_mark(0.2,text_list=[   "\( "+s+"\)" for s in names_list   ],pspict=pspicts)
    rh=RightAngle(Segment(A,B),Segment(B,C),0.3,0,1)
    m1=Segment(A,B).get_mark(0.2,None,length_list[0],automatic_place=(pspicts,""))
    m2=Segment(B,C).get_mark(0.2,None,length_list[1],automatic_place=(pspicts,""))
    m3=Segment(C,A).get_mark(0.2,None,length_list[2],automatic_place=(pspicts,""))
    pspicts[2].DrawGraphs(trig,rh,m1,m2,m3,ang)


    pspicts[3].dilatation(0.9)
    ll=["","",""]
    length_list=[   "\( {}\)".format(x) for x in ll   ]
    names_list=["U","V","I"]
    A=Point(-1,0)
    B=Point(0,3)
    l=0.7
    K=Segment(B,A).orthogonal().F
    v=K-B
    C=B+l*v

    for p in A,B,C:
        p.parameters.symbol=""
    trig=Polygon(A,B,C)
    trig.put_mark(0.2,text_list=[   "\( "+s+"\)" for s in names_list   ],pspict=pspicts)
    rh=RightAngle(Segment(A,B),Segment(B,C),0.3,0,1)
    m1=Segment(A,B).get_mark(0.2,None,length_list[0],automatic_place=(pspicts,""))
    m2=Segment(B,C).get_mark(0.2,None,length_list[1],automatic_place=(pspicts,""))
    m3=Segment(C,A).get_mark(0.2,None,length_list[2],automatic_place=(pspicts,""))
    pspicts[3].DrawGraphs(trig,rh,m1,m2,m3)



    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()