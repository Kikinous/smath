#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from phystricks import *
import sys

from phystricksTracerUn import TracerUn
from phystricksExerciceGraphes import ExerciceGraphes
from phystricksExerciceGraphesbis import ExerciceGraphesbis
from phystricksGrapheunsurunmoinsx import Grapheunsurunmoinsx
from phystricksExoCUd import ExoCUd
from phystricksUnSurxInt import UnSurxInt
from phystricksAireParabole import AireParabole
from phystricksPartieEntiere import PartieEntiere
from phystricksMantisse import Mantisse
from phystricksDS2010ExoGraph import DS2010ExoGraph
from phystricksDS2010bisExoGraph import DS2010bisExoGraph
from phystricksSolsEqDiffSin import SolsEqDiffSin
from phystricksSolsSinpA import SolsSinpA
from phystricksTrajs import Trajs

from phystricksEvZZys import EvZZys
from phystricksBpCNVm import BpCNVm
from phystricksNotesSVT import NotesSVT
from phystricksHistoAutomobile import HistoAutomobile
from phystricksHistoTdkccB import HistoTdkccB
from phystricksHistoPySeT import HistoPySeT
from phystricksHistoAgeFrance import HistoAgeFrance
from phystricksHistoAgeKenya import HistoAgeKenya
from phystricksSecondDeg import SecondDeg
from phystricksParabolesfTKFw import ParabolesfTKFw
from phystricksEffectifsCumulwfqAhj import EffectifsCumulwfqAhj
from phystricksSurfaceTriangletcNPPE import SurfaceTriangletcNPPE
from phystricksLectureGraphnrkEEM import LectureGraphnrkEEM
from phystricksParaboleMCLCbG import ParaboleMCLCbG
from phystricksbDdpfh import bDdpfh
from phystricksParabolevQzhjq import ParabolevQzhjq
from phystricksParaboleiLbviP import ParaboleiLbviP
from phystricksParaboleHautMLbPQF import ParaboleHautMLbPQF
from phystricksParaboleBasfKtFCN import ParaboleBasfKtFCN
from phystricksParabolezBeHFl import ParabolezBeHFl
from phystricksParabolezmMGdN import ParabolezmMGdN
from phystricksParaboleUneSolPktmCR import ParaboleUneSolPktmCR
from phystricksParaboleHautjOEAzn import ParaboleHautjOEAzn
from phystricksParaboleBasDqAAua import ParaboleBasDqAAua
from phystricksParaboleUniqueHautviflbY import ParaboleUniqueHautviflbY
from phystricksParaboleUniqueBaskGdqda import ParaboleUniqueBaskGdqda

figures_list=[DS2010bisExoGraph, ExoCUd,DS2010ExoGraph,SolsEqDiffSin, Grapheunsurunmoinsx, TracerUn, ExerciceGraphes,SolsSinpA,Trajs, ExerciceGraphesbis, UnSurxInt, AireParabole, PartieEntiere, Mantisse, EvZZys,BpCNVm,NotesSVT,HistoAutomobile,HistoTdkccB,HistoPySeT, HistoAgeFrance,HistoAgeKenya,EffectifsCumulwfqAhj,SurfaceTriangletcNPPE,ParabolevQzhjq,bDdpfh,ParaboleiLbviP,ParaboleMCLCbG,LectureGraphnrkEEM,ParaboleHautMLbPQF,ParaboleBasfKtFCN,ParabolezBeHFl,ParabolezmMGdN,ParaboleUneSolPktmCR,
        ParaboleHautjOEAzn,ParaboleBasDqAAua,ParaboleUniqueHautviflbY,ParaboleUniqueBaskGdqda
        ]

# Ajouter quelque chose dans cette liste n'épargne pas de l'ajouter dans l'autre également.
figures_list=[ParaboleUniqueBaskGdqda]

def AllFigures():
    tests=main.FigureGenerationSuite(figures_list,first=0,title=u"Soupçon de mathématiques")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    if "--all" in sys.argv :
        AllFigures()
    else:
        HistoAutomobile()
