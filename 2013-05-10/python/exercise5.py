#from pyplasm import *

Dom1D = INTERVALS(1)(24)

#sezione dall'alto
points1=[[0,-3.5,0],[5.8,-3.9,0],[1,0,0],[8,1,0]]
#C1 = BEZIER(S1)(points1)
c1 = CUBICHERMITE(S1)(points1)
polyline1= POLYLINE(points1)
p1 = MAP(c1)(Dom1D)
#VIEW(STRUCT([polyline1,p1]))

points2=[[5.8,-3.9,0],[8.2,-2.8,0],[1,0,0],[1,1,0]]

polyline2= POLYLINE(points2)
c2 = CUBICHERMITE(S1)(points2)
p2 = MAP(c2)(Dom1D)
#VIEW(STRUCT([p1,p2]))

points3=[[8.2,-2.8,0],[9,0,0],[1,1,0],[0,1,0]]

c3 = CUBICHERMITE(S1)(points3)
p3 = MAP(c3)(Dom1D)
#VIEW(STRUCT([p1,p2,p3]))

points4=[[0,-3.5,0],[-8.5,-3,0],[-1,0,0],[-1,3,0]]

c4 = CUBICHERMITE(S1)(points4)
p4 = MAP(c4)(Dom1D)
#VIEW(STRUCT([p1,p2,p3,p4]))

points5=[[-8.5,-3,0],[-9,0,0],[-1,3,0],[0,1,0]]

c5 = CUBICHERMITE(S1)(points5)
p5 = MAP(c5)(Dom1D)
metaalta=STRUCT([p1,p2,p3,p4,p5])
metaalta2=S([2])([-1])(metaalta)
#VIEW(STRUCT([metaalta,metaalta2]))

#sezione dietro

points6=[[0,0,2.1],[0,2.2,1.9],[0,1,0],[0,1,-1]]
c6 = CUBICHERMITE(S1)(points6)
p6 = MAP(c6)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,p6]))

points7=[[0,2.2,1.9],[0,2.8,1],[0,1,-1],[0,1,-1.5]]
c7 = CUBICHERMITE(S1)(points7)
p7 = MAP(c7)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,p6,p7]))

points8=[[0,2.8,1],[0,3.7,0.5],[0,1,0],[0,0,-1]]
c8 = CUBICHERMITE(S1)(points8)
p8 = MAP(c8)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,p6,p7,p8]))

points9=[[0,3.7,0.5],[0,2.8,-1.7],[0,-1,-2],[0,-2,-1]]
c9 = CUBICHERMITE(S1)(points9)
p9 = MAP(c9)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,p6,p7,p8,p9]))

points10=[[0,2.8,-1.7],[0,0,-2,1],[0,-2,-1],[0,-1,0]]
c10 = CUBICHERMITE(S1)(points10)
p10 = MAP(c10)(Dom1D)
metadietro=STRUCT([p6,p7,p8,p9,p10])
metadietro2=S([2])([-1])(metadietro)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2]))

#sezione laterale

points11=[[0,0,2.1],[2.5,0,0.5],[2,0,-1],[1,0,-1]]
c11 = CUBICHERMITE(S1)(points11)
p11 = MAP(c11)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11]))

points12=[[2.5,0,0.5],[5,0,0.65],[1,0,0.2],[1,0,0]]
c12 = CUBICHERMITE(S1)(points12)
p12 = MAP(c12)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12]))

points13=[[5,0,0.65],[8.5,0,-0.6],[3,0,0],[1,0,-1]]
c13 = CUBICHERMITE(S1)(points13)
p13 = MAP(c13)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12,p13]))

points14=[[8.5,0,-0.6],[9,0,-0.65],[0.5,0,-0.5],[0.5,0,0]]
c14 = CUBICHERMITE(S1)(points14)
p14 = MAP(c14)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12,p13,p14]))

points15=[[9,0,-0.65],[7.7,0,-2.1],[0,0,-1],[-1,0,-1]]
c15 = CUBICHERMITE(S1)(points15)
p15 = MAP(c15)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12,p13,p14,p15]))

points16=[[7.7,0,-2.1],[-4,0,-2.1]]
p16=POLYLINE(points16)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12,p13,p14,p15,p16]))

points17=[[-4,0,-2.1],[-7.3,0,-1.8],[-1,0,0],[-1,0,1]]
c17 = CUBICHERMITE(S1)(points17)
p17 = MAP(c17)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12,p13,p14,p15,p16,p17]))

points18=[[-7.3,0,-1.8],[-8.3,0,-1.2],[-1.2,0,1],[-1,0,0.2]]
c18 = CUBICHERMITE(S1)(points18)
p18 = MAP(c18)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12,p13,p14,p15,p16,p17,p18]))

points19=[[-8.3,0,-1.2],[-9,0,0.2],[-1,0,2],[-1,0,2]]
c19 = CUBICHERMITE(S1)(points19)
p19 = MAP(c19)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12,p13,p14,p15,p16,p17,p18,p19]))

points20=[[-9,0,0.2],[-8.7,0,0.2],[-0.2,0,0.6],[0.2,0,0.3]]
c20 = CUBICHERMITE(S1)(points20)
p20 = MAP(c20)(Dom1D)
#VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20]))

points21=[[-8.7,0,0.2],[0,0,2.1],[0.2,0,0.3],[2,0,-1]]
c21 = CUBICHERMITE(S1)(points21)
p21 = MAP(c21)(Dom1D)

#from pyplasm import *

import sys
sys.path.append("/home/roberto/Scrivania/larpy")

from lar import *
from scipy import *

"""Funzione per generare una griglia di complessi simpliciali"""
def GRID(args):
	model = ([[]],[[0]])
	for k,steps in enumerate(args):
		model = larExtrude(model,steps*[1])
	V,cells = model
	verts = AA(list)(scipy.array(V)/AA(float)(args))
	return MKPOL([verts,AA(AA(lambda h:h+1))(cells),None])
	
domain = S([1])(2*PI)(GRID([25,25]))
domain2 = GRID([25,25])
dominio2D = S([1])(2*PI)(MAP([S2,S1])(GRID([25,25])))
dominio2D2 = MAP([S2,S1])(GRID([25,25]))
Dom1D = INTERVALS(1)(24)



points1=[[0,0,0],[4.6,0,0],[1,0.5,0],[1,-0.5,0]]
curva1 = CUBICHERMITE(S1)(points1)
p1 = MAP(curva1)(Dom1D)

points2=[[0.1,0.7,0.1],[4.5,0.7,0.1],[1,0.5,0],[1,-0.5,0]]
curva2 = CUBICHERMITE(S1)(points2)
pt2 = MAP(curva2)(Dom1D)

#alette=STRUCT([p1,p2])
#VIEW(alette)

superficie1=MAP(BEZIER(S2)([curva1,curva2]))(domain2)
sup=T([1])(-2.3)(superficie1)
#VIEW(sup)
sup2=T([2,3])([-0.5,-0.18])(S([1,2,3])([0.95,0.95,0.95])(sup))
sup3=T([2,3])([-0.5,-0.18])(S([1,2,3])([0.95,0.95,0.95])(sup2))
sup4=T([2,3])([-0.5,-0.18])(S([1,2,3])([0.95,0.95,0.95])(sup3))
sup5=T([2,3])([-0.5,-0.18])(S([1,2,3])([0.95,0.95,0.95])(sup4))
sup6=T([2,3])([-0.5,-0.18])(S([1,2,3])([0.95,0.95,0.95])(sup5))

points2=[[-2.2,0.7,0.15],[2.3,0.7,0.15],[1,0.5,0],[1,-0.5,0]]
curva2 = CUBICHERMITE(S1)(points2)
pt2 = MAP(curva2)(Dom1D)

points3=[[-2.2,2.5,0.5],[2.3,2.5,0.5],[1,0.5,0],[1,-0.5,0]]
curva3 = CUBICHERMITE(S1)(points3)
pt3 = MAP(curva3)(Dom1D)
points4=[[-2.2,3.8,0.15],[2.3,3.8,0.15],[1,0.5,0],[1,-0.5,0]]
curva4 = CUBICHERMITE(S1)(points4)
pt4 = MAP(curva4)(Dom1D)
points5=[[-2,-2.3,-0.8],[2.1,-2.3,-0.8],[1,0.5,0],[1,-0.5,0]]
curva5 = CUBICHERMITE(S1)(points5)
pt5 = MAP(curva5)(Dom1D)
points6=[[-2,-3.9,-1],[2.1,-3.9,-1],[1,0.5,0],[1,-0.5,0]]
curva6 = CUBICHERMITE(S1)(points6)
pt6 = MAP(curva6)(Dom1D)
#VIEW(p3)
sup7=COLOR(YELLOW)(MAP(BEZIER(S2)([curva2,curva3,curva4]))(domain2))
sup8=COLOR(YELLOW)(MAP(BEZIER(S2)([curva5,curva6]))(dominio2D2))
alette=STRUCT([sup,sup2,sup3,sup4,sup5,sup6,sup7,sup8])
aletteruotate=R([1,2])(-PI/2)(alette)
alettetraslate=T([1,3])([-4.5,1.7])(aletteruotate)
#VIEW(alette)

#DIETRO

points1=[[0,0,0],[3,0,-0.5],[1,0,0],[0,0,-2]]
curva1 = CUBICHERMITE(S1)(points1)
p1 = MAP(curva1)(Dom1D)
#VIEW(p1)

points2=[[3,0,-0.5],[2.5,0,-1.7],[0,0,-2],[-1,0,0]]
curva2 = CUBICHERMITE(S1)(points2)
p2 = MAP(curva2)(Dom1D)

points3=[[2.5,0,-1.7],[0,0,-1.7],[-1,0,0],[-1,0,0]]
curva3 = CUBICHERMITE(S1)(points3)
p3 = MAP(curva3)(Dom1D)

points4=[[0,0,-0.5],[3,0,-0.5]]
curva4 = BEZIER(S1)(points4)
p4 = MAP(curva4)(Dom1D)

points5=[[2.5,0,-0.5],[2.5,0,-1.7]]
curva5 = BEZIER(S1)(points5)
p5 = MAP(curva5)(Dom1D)

points6=[[2.5,0,-0.5],[0,0,-0.5]]
curva6 = BEZIER(S1)(points6)
p6 = MAP(curva6)(Dom1D)

superficie1=COLOR(YELLOW)(MAP(BEZIER(S2)([curva1,curva4]))(dominio2D2))
superficie2=COLOR(YELLOW)(MAP(BEZIER(S2)([curva2,curva5]))(dominio2D2))
superficie3=COLOR(YELLOW)(MAP(BEZIER(S2)([curva3,curva6]))(dominio2D2))

points7=[[2.5,-0.01,-0.2],[2.9,-0.01,-0.4],[0.25,0,0],[0,0,-0.5]]
curva7 = CUBICHERMITE(S1)(points7)
p7 = MAP(curva7)(Dom1D)

points8=[[2.3,-0.01,-0.4],[2.9,-0.01,-0.4]]
curva8 = BEZIER(S1)(points8)
p8 = MAP(curva8)(Dom1D)
superficie4=COLOR(RED)(MAP(BEZIER(S2)([curva7,curva8]))(dominio2D2))

#VIEW(STRUCT([p1,p2,p3,superficie1,superficie2,superficie3,superficie4]))

#ribaltiaamo

points11=[[0,0,0],[-3,0,-0.5],[-1,0,0],[0,0,-2]]
curva11 = CUBICHERMITE(S1)(points11)
p11 = MAP(curva11)(Dom1D)
#VIEW(p1)

points22=[[-3,0,-0.5],[-2.5,0,-1.7],[0,0,-2],[1,0,0]]
curva22 = CUBICHERMITE(S1)(points22)
p22 = MAP(curva22)(Dom1D)

points33=[[-2.5,0,-1.7],[-0,0,-1.7],[1,0,0],[1,0,0]]
curva33 = CUBICHERMITE(S1)(points33)
p33 = MAP(curva33)(Dom1D)

points44=[[-0,0,-0.5],[-3,0,-0.5]]
curva44 = BEZIER(S1)(points44)
p44 = MAP(curva44)(Dom1D)

points55=[[-2.5,0,-0.5],[-2.5,0,-1.7]]
curva55 = BEZIER(S1)(points55)
p55 = MAP(curva55)(Dom1D)

points66=[[-2.5,0,-0.5],[0,0,-0.5]]
curva66 = BEZIER(S1)(points66)
p66 = MAP(curva66)(Dom1D)

superficie11=COLOR(YELLOW)(MAP(BEZIER(S2)([curva11,curva44]))(domain2))
superficie22=COLOR(YELLOW)(MAP(BEZIER(S2)([curva22,curva55]))(domain2))
superficie33=COLOR(YELLOW)(MAP(BEZIER(S2)([curva33,curva66]))(domain2))

points77=[[-2.5,-0.01,-0.2],[-2.9,-0.01,-0.4],[0.25,0,0],[0,0,-0.5]]
curva77 = CUBICHERMITE(S1)(points77)
p77 = MAP(curva77)(Dom1D)

points88=[[-2.3,-0.01,-0.4],[-2.9,-0.01,-0.4]]
curva88 = BEZIER(S1)(points88)
p88 = MAP(curva88)(Dom1D)
superficie44=COLOR(RED)(MAP(BEZIER(S2)([curva77,curva88]))(domain2))
dietro=STRUCT([p1,p2,p3,superficie1,superficie2,superficie3,superficie4,superficie11,superficie22,superficie33,superficie44])
dietroruotato=R([1,2])(-PI/2)(dietro)
dietroruotato2=R([1,3])(PI/7)(dietroruotato)
dietrotraslato=T([1,3])([-9,0.3])(dietroruotato2)
#VIEW(dietro)

VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,alettetraslate,dietrotraslato]))

