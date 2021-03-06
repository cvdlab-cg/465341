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
Dom1D = INTERVALS(1)(24)

def cerchio (r,h,dx,dy):
	def cerchio0(p):
		u = p[0]
		return [dx + r*COS(u),dy + r*SIN(u),h]
	return cerchio0
dom = INTERVALS(2*PI)(32);
c1 = cerchio(3,0,0,0);
c2 = cerchio(3,0.6,0,0)
cerchio1 = MAP(c1)(dom);
cerchio2 = MAP(c2)(dom);

superficie1=MAP(BEZIER(S2)([c1,c2]))(domain)

c3 = cerchio(3.2,0.7,0,0)
cerchio3 = MAP(c3)(dom);
superficie2=MAP(BEZIER(S2)([c2,c3]))(domain)

c4 = cerchio(3.2,0.9,0,0)
cerchio4 = MAP(c4)(dom);
superficie3=MAP(BEZIER(S2)([c3,c4]))(domain)

c5 = cerchio(3.4,1,0,0)
cerchio5 = MAP(c5)(dom);
superficie4=MAP(BEZIER(S2)([c4,c5]))(domain)

c6 = cerchio(3.4,1.1,0,0)
cerchio6 = MAP(c6)(dom);
superficie5=MAP(BEZIER(S2)([c5,c6]))(domain)

c7 = cerchio(2.8,0.7,0,0)
cerchio7 = MAP(c7)(dom);
superficie6=MAP(BEZIER(S2)([c6,c7]))(domain)
cerchione=STRUCT([superficie1,superficie2,superficie3,superficie4,superficie5,superficie6])

c8 = cerchio(3,-0.6,0,0)
cerchio8 = MAP(c8)(dom);
superficie7=MAP(BEZIER(S2)([c8,c1]))(domain)

c9 = cerchio(3.2,-0.7,0,0)
cerchio9 = MAP(c9)(dom);
superficie8=MAP(BEZIER(S2)([c9,c8]))(domain)

c10 = cerchio(3.2,-0.9,0,0)
cerchio10 = MAP(c10)(dom);
superficie9=MAP(BEZIER(S2)([c10,c9]))(domain)

c11 = cerchio(3.4,-1,0,0)
cerchio11 = MAP(c11)(dom);
superficie10=MAP(BEZIER(S2)([c11,c10]))(domain)

c12 = cerchio(3.4,-1.1,0,0)
cerchio12 = MAP(c12)(dom);
superficie11=MAP(BEZIER(S2)([c12,c11]))(domain)

c13 = cerchio(2.8,-0.7,0,0)
cerchio13 = MAP(c13)(dom);
superficie12=MAP(BEZIER(S2)([c13,c12]))(domain)
superficie13=MAP(BEZIER(S2)([c7,c13]))(domain)

cerchione2=STRUCT([superficie7,superficie8,superficie9,superficie10,superficie11,superficie12,superficie13])

#pneumatico
cp1 = cerchio(3.6,1.3,0,0)
cerchiop1 = MAP(cp1)(dom)

cp2 = cerchio(4.3,1.3,0,0)
cerchiop2 = MAP(cp2)(dom)

cp3 = cerchio(4,1.5,0,0)
cerchiop3 = MAP(cp2)(dom)
superficiep1=MAP(BEZIER(S2)([c6,cp1,cp3,cp2]))(domain)
cp4 = cerchio(4.5,0,0,0)
cerchiop4 = MAP(cp4)(dom)
cp5 = cerchio(4,-1.5,0,0)
cerchiop5 = MAP(cp5)(dom)


cp6 = cerchio(3.6,-1.3,0,0)
cerchiop6 = MAP(cp6)(dom)

cp7 = cerchio(4.3,-1.3,0,0)
cerchiop7 = MAP(cp7)(dom)
superficiep3=MAP(BEZIER(S2)([c12,cp5,cp6,cp7]))(dominio2D)
superficiep2=MAP(BEZIER(S2)([cp2,cp4,cp7]))(domain)
pneumatico=STRUCT([superficiep1,cerchiop6,cerchiop7,superficiep3,superficiep2])

#cerchione interno
ci1 = cerchio(1.2,0,0,0)
cerchioi1 = MAP(ci1)(dom);

ci2 = cerchio(1.2,0.3,0,0)
cerchioi2 = MAP(ci2)(dom);
superficiei1=MAP(BEZIER(S2)([ci1,ci2]))(domain)
superficiei2=MAP(BEZIER(S2)([ci2,[0,0,0.301]]))(domain)

ci3 = cerchio(0.6,0.3,0,0)
cerchioi3 = MAP(ci3)(dom);

ci4 = cerchio(0.6,0.6,0,0)
cerchioi4 = MAP(ci4)(dom);
ci5 = cerchio(0.4,0.7,0,0)
cerchioi5 = MAP(ci5)(dom);
superficiei3=MAP(BEZIER(S2)([ci3,ci4,ci5,[0,0,0.9]]))(domain)


ci11 = cerchio(1.2,0,0,0)
cerchioi11 = MAP(ci11)(dom);

ci22 = cerchio(1.2,-0.3,0,0)
cerchioi22 = MAP(ci22)(dom);
superficiei11=MAP(BEZIER(S2)([ci11,ci22]))(dominio2D)
superficiei22=MAP(BEZIER(S2)([ci22,[0,0,-0.301]]))(dominio2D)

ci33 = cerchio(0.6,-0.3,0,0)
cerchioi33 = MAP(ci33)(dom);

ci44 = cerchio(0.6,-0.6,0,0)
cerchioi44 = MAP(ci44)(dom);
ci55 = cerchio(0.4,-0.7,0,0)
cerchioi55 = MAP(ci55)(dom);
superficiei33=MAP(BEZIER(S2)([ci33,ci44,ci55,[0,0,-0.9]]))(dominio2D)


#raggio1
points1=[[0.4,0,0.4],[3,0,0.6],[1,0,-0.5],[1,0,1]]
cr1 = CUBICHERMITE(S1)(points1)
pr1 = MAP(cr1)(Dom1D)

points2=[[0.3,-0.4,0],[3,-0.9,0.6],[1,0,-0.5],[1,-3,1]]
cr2 = CUBICHERMITE(S1)(points2)
pr2 = MAP(cr2)(Dom1D)

points3=[[0.3,0.4,0],[3,0.9,0.6],[1,0,-0.5],[1,3,1]]
cr3 = CUBICHERMITE(S1)(points3)
pr3 = MAP(cr3)(Dom1D)
superficier1=MAP(CUBICHERMITE(S2)([cr1,cr3,[1,0,0],[1,0,0]]))(domain2)
superficier2=MAP(CUBICHERMITE(S2)([cr2,cr1,[-1,0,0],[-1,0,0]]))(domain2)
raggi=STRUCT([pr1,pr2,pr3,superficier1,superficier2])
raggi2=R([1,2])(PI)(raggi)
raggi3=R([1,2])(PI/2)(raggi)
raggi4=R([1,3])(PI)(raggi)
raggi5=R([1,3])(PI)(raggi2)
raggi6=R([1,3])(PI)(raggi3)
raggi7=R([1,2])(-PI/2)(raggi)
raggi8=R([1,3])(PI)(raggi7)
#VIEW(STRUCT([raggi,raggi2,raggi3,raggi4,raggi5,raggi6,raggi7,raggi8]))


cerchioneinterno=STRUCT([superficiei1,superficiei2,superficiei3,superficiei11,superficiei22,superficiei33,raggi,raggi2,raggi3,raggi4,raggi5,raggi6,raggi7,raggi8])
#VIEW(STRUCT([cerchione,cerchione2,pneumatico,cerchioneinterno]))


ruota=S([1,2,3])([0.3,0.3,0.3])(STRUCT([cerchione,cerchione2,pneumatico,cerchioneinterno]))
ruotaruotata=R([1,3])(PI/2)(ruota)
ruotaruotata2=R([1,2])(PI/2)(ruotaruotata)
ruotatraslata=T([1,2,3])([5,3.3,-1.7])(ruotaruotata2)

ruotatraslata2=T([1,2,3])([-5.5,3.3,-1.7])(ruotaruotata2)


ruotatraslata22=T([1,2,3])([5,-3.3,-1.7])(ruotaruotata2)

ruotatraslata222=T([1,2,3])([-5.5,-3.3,-1.7])(ruotaruotata2)
dueruote=STRUCT([ruotatraslata,ruotatraslata2])
dueruote2=STRUCT([ruotatraslata222,ruotatraslata22])








VIEW(STRUCT([metaalta,metaalta2,metadietro,metadietro2,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,dueruote,dueruote2]))

