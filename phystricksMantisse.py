from phystricks import *
def Mantisse():
    pspict,fig = SinglePicture("Mantisse")

    x=var('x')
    f=phyFunction(x-floor(x)).graph(0,5)
    f.plotpoints=1000
    eps=0.01
    surf=SurfaceUnderFunction(f,1,2-eps)
    surf.parameters.color="green"
    surf.Fsegment.parameters.style="none"

    pspict.DrawGraphs(surf,f)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
