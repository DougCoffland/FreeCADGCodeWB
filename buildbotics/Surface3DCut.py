# FreeCAD init script of buildbotics workbench  

#***************************************************************************
#*   Copyright (c) 2019 Buildbotics LLC                              *   
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/
import FreeCAD,FreeCADGui
from PySide import QtGui, QtCore
from pivy import coin
import os
from Cut import Cut, ViewCut
import validator as VAL
import math
import pyclipper

class ViewSurface3DCut(ViewCut):
	def getIcon(self):
		return """
/* XPM */
static char * surface3D_xpm[] = {
"50 43 296 2",
"  	c None",
". 	c #000000",
"+ 	c #002F00",
"@ 	c #006800",
"# 	c #005C00",
"$ 	c #005100",
"% 	c #006000",
"& 	c #004200",
"* 	c #005D00",
"= 	c #002E00",
"- 	c #004B00",
"; 	c #004E00",
"> 	c #006900",
", 	c #006A00",
"' 	c #004800",
") 	c #000C00",
"! 	c #006E00",
"~ 	c #007200",
"{ 	c #004F00",
"] 	c #006200",
"^ 	c #00D400",
"/ 	c #00D800",
"( 	c #006F00",
"_ 	c #006C00",
": 	c #005200",
"< 	c #00CD00",
"[ 	c #008900",
"} 	c #007900",
"| 	c #00D300",
"1 	c #007A00",
"2 	c #007000",
"3 	c #00CE00",
"4 	c #00B000",
"5 	c #00D200",
"6 	c #008E00",
"7 	c #00D000",
"8 	c #007F00",
"9 	c #003600",
"0 	c #008D00",
"a 	c #009A00",
"b 	c #00D100",
"c 	c #009900",
"d 	c #006B00",
"e 	c #00D700",
"f 	c #002D00",
"g 	c #008500",
"h 	c #00BF00",
"i 	c #007700",
"j 	c #00A900",
"k 	c #005800",
"l 	c #00CF00",
"m 	c #00C900",
"n 	c #008C00",
"o 	c #009000",
"p 	c #005600",
"q 	c #00CA00",
"r 	c #00A300",
"s 	c #00AD00",
"t 	c #008F00",
"u 	c #00A200",
"v 	c #009C00",
"w 	c #483600",
"x 	c #00CC00",
"y 	c #009200",
"z 	c #000700",
"A 	c #009600",
"B 	c #00BD00",
"C 	c #00AC00",
"D 	c #004400",
"E 	c #00AB00",
"F 	c #009100",
"G 	c #006500",
"H 	c #00C600",
"I 	c #005300",
"J 	c #014800",
"K 	c #977300",
"L 	c #00B700",
"M 	c #002100",
"N 	c #00BB00",
"O 	c #004A00",
"P 	c #009800",
"Q 	c #003700",
"R 	c #00AE00",
"S 	c #005000",
"T 	c #005A00",
"U 	c #008400",
"V 	c #00D500",
"W 	c #00B800",
"X 	c #765900",
"Y 	c #987400",
"Z 	c #007B00",
"` 	c #004600",
" .	c #004000",
"..	c #005900",
"+.	c #00A600",
"@.	c #00C100",
"#.	c #00A400",
"$.	c #007400",
"%.	c #007100",
"&.	c #B18700",
"*.	c #8D6B00",
"=.	c #003B00",
"-.	c #004500",
";.	c #00C700",
">.	c #00BC00",
",.	c #003A00",
"'.	c #00BE00",
").	c #00CB00",
"!.	c #007C00",
"~.	c #009B00",
"{.	c #00D600",
"].	c #3A3300",
"^.	c #D2A100",
"/.	c #594200",
"(.	c #00C000",
"_.	c #00A500",
":.	c #004300",
"<.	c #00B100",
"[.	c #001500",
"}.	c #003300",
"|.	c #00C300",
"1.	c #00A800",
"2.	c #8F6C00",
"3.	c #BD9100",
"4.	c #004100",
"5.	c #007800",
"6.	c #00B600",
"7.	c #003F00",
"8.	c #003400",
"9.	c #C09300",
"0.	c #8B6A00",
"a.	c #004900",
"b.	c #00C800",
"c.	c #007300",
"d.	c #009400",
"e.	c #004D00",
"f.	c #003C00",
"g.	c #634A00",
"h.	c #D1A000",
"i.	c #342600",
"j.	c #00AF00",
"k.	c #006300",
"l.	c #009700",
"m.	c #00B900",
"n.	c #003500",
"o.	c #A67E00",
"p.	c #AB8200",
"q.	c #003D00",
"r.	c #005400",
"s.	c #005500",
"t.	c #007500",
"u.	c #1F4000",
"v.	c #CE9D00",
"w.	c #6B5000",
"x.	c #00C400",
"y.	c #009300",
"z.	c #008100",
"A.	c #008000",
"B.	c #00A700",
"C.	c #008200",
"D.	c #00B300",
"E.	c #806100",
"F.	c #C49600",
"G.	c #00A000",
"H.	c #007600",
"I.	c #B78B00",
"J.	c #957100",
"K.	c #001E00",
"L.	c #009500",
"M.	c #004700",
"N.	c #493600",
"O.	c #D4A200",
"P.	c #433100",
"Q.	c #008300",
"R.	c #004C00",
"S.	c #008800",
"T.	c #9B7600",
"U.	c #B48A00",
"V.	c #008A00",
"W.	c #008600",
"X.	c #00C500",
"Y.	c #00BA00",
"Z.	c #C99900",
"`.	c #7B5D00",
" +	c #00C200",
".+	c #003100",
"++	c #005B00",
"@+	c #001400",
"#+	c #00AA00",
"$+	c #715500",
"%+	c #CB9C00",
"&+	c #020100",
"*+	c #003900",
"=+	c #005700",
"-+	c #AD8400",
";+	c #9D7800",
">+	c #008B00",
",+	c #00B500",
"'+	c #009E00",
")+	c #006400",
"!+	c #372800",
"~+	c #523D00",
"{+	c #000900",
"]+	c #006D00",
"^+	c #002500",
"/+	c #8E6C00",
"(+	c #BB8F00",
"_+	c #002000",
":+	c #006100",
"<+	c #008700",
"[+	c #00B400",
"}+	c #006700",
"|+	c #BF9200",
"1+	c #876700",
"2+	c #009F00",
"3+	c #5C4400",
"4+	c #CF9F00",
"5+	c #302200",
"6+	c #003E00",
"7+	c #00A100",
"8+	c #A27B00",
"9+	c #A88000",
"0+	c #005E00",
"a+	c #007E00",
"b+	c #006600",
"c+	c #184100",
"d+	c #CD9D00",
"e+	c #654C00",
"f+	c #005F00",
"g+	c #7F6000",
"h+	c #C29400",
"i+	c #001D00",
"j+	c #B68B00",
"k+	c #926F00",
"l+	c #003800",
"m+	c #001800",
"n+	c #453300",
"o+	c #402F00",
"p+	c #00B200",
"q+	c #009D00",
"r+	c #967200",
"s+	c #B28800",
"t+	c #002A00",
"u+	c #003200",
"v+	c #C69700",
"w+	c #775900",
"x+	c #007D00",
"y+	c #6F5300",
"z+	c #C99A00",
"A+	c #AC8300",
"B+	c #002200",
"C+	c #002700",
"D+	c #303C00",
"E+	c #D09F00",
"F+	c #4C3800",
"G+	c #8B6900",
"H+	c #836300",
"I+	c #7C5E00",
"J+	c #775A00",
"K+	c #735600",
"L+	c #705400",
"M+	c #6D5200",
"N+	c #694F00",
"O+	c #684E00",
"P+	c #674D00",
"Q+	c #664D00",
"R+	c #604800",
"S+	c #5D4500",
"T+	c #594300",
"U+	c #574100",
"V+	c #564000",
"W+	c #553F00",
"X+	c #4A3700",
"Y+	c #3D2D00",
"Z+	c #281D00",
"`+	c #B98D00",
" @	c #D5A300",
".@	c #B38800",
"+@	c #846400",
"@@	c #816100",
"#@	c #261B00",
"$@	c #281C00",
"%@	c #B28700",
"&@	c #C19300",
"*@	c #BD9000",
"=@	c #B08700",
"-@	c #AF8500",
";@	c #AA8200",
">@	c #AA8100",
",@	c #A98100",
"'@	c #A47D00",
")@	c #A47C00",
"!@	c #9F7900",
"~@	c #906E00",
"{@	c #8E6B00",
"]@	c #755800",
"                                                                                    .               ",
"                                                                .         . . .   . . . .           ",
"                                    + @ @ @ @ @ # . $ @ @ @ % . & . * @ $ = @ - . ; > , ' ) ! ~ { . ",
"                                  . ] ^ / / / ^ ( _ : < / / [ } | 1 2 3 % 4 / 5 6 5 / / 7 ( 8 ^ ~ . ",
"                                  . 9 2 | / ^ ( 0 / a # b c d ^ / e 6 f g / / / / h / / / ^ i j . . ",
"                                . k l 0 ] m 2 n / / / o p $ q / / / / r } s / / t . u / / / e v w . ",
"                                ' x / / y z n q / / / / A 4 & B / / / C # D E F G H I o / / / J K   ",
"                              . C / / / / L C M N / / / x O P Q R / m & m m S T l / l d U V W X Y   ",
"                              . Z V / / / C ` s  .h / 5 ..+./ @.D #.G C / / x < 5 / / ^ $.%.} &.*.  ",
"                            . =.$.%.^ / C -.;./ >.,.'.%.F / / / ).: !.~.V / / c : x / / {.F ].^./.  ",
"                            = (.{.[ d _.:.H / / / <.[.!.j 4 / / / 3 y }.~ ^ #.I v ' |./ / 1.2.3..   ",
"                          . L / / / t 4.@.5.@./ / / 6.4 ` 7.1./ / B ' < U ..$ x / s 8.'./ ] 9.0.    ",
"                          a.N / / / / b.2 c.7.b./ / (.4.(.q $ d.b e.N / e a )./ / / N f.P g.h.i.    ",
"                        . . Q j./ / ^ 2 6 / C { x ).& L / / < k.-.l./ / / V m./ / / / (.n.o.p..     ",
"                        . r (.q.C ^ %.6 / / / 1.: r.+.^ / / / | [ s.>./ ^ t.) ~./ / / V u.v.w.      ",
"                      . F / / b.{ ..0 x.^ / / / a y.z.% x / / / } A.9 B.~ Z b.% C.^ / D.E.F..       ",
"                      z.| / / / x a '.= %.^ / / / 0 %.~.D h / G.( {.|.e.U {./ ^ } d < H.I.J.        ",
"                    K.F S ;./ / / W & m.z.%.^ / F d ^ / 4  .L.M.< / / l q 5 / / / d.{ N.O.P.        ",
"                    + $ G.9 './ R 9 h / {.Q.%.c ..x / / / (.R.y S.V / H M.p q / / / S.T.U..         ",
"                  . S x / W ,.V.4.@.m / / {.W.$ N a.s / / / X.& , %.Y.q.C u Q './ / { Z.`.          ",
"                . : q / / /  +_ ;.n .+(./ / e  +e.c ; L.e ^ ++C {.6 @+R / / L Q #+>.$+%+&+          ",
"                *+X.=+C / / / ^ !.%.R *+h / x $ #+/ < > } Q.[ / / / x./ / / / x.S :.-+;+.           ",
"              . o I >+{ l./ ^ %.H.^ / 6.=.,+=+'+/ / / ^ U )+@./ / / @.F V / / / H !+h.~+            ",
"              {+& A / x )+Q.]+V.{./ / / W ^+y 6.^ / / / / u {+E / h n.] 2 l / / 1./+(+.             ",
"            . =+A / / / ^ i t ).j / / / / H R _+:+x / / |. .,+$ <+=.[+{.o : H / }+|+1+              ",
"            : b (./ / / / e |.' & 2+/ / / L Q x.a M.(.b : ,+/ < ! Y./ / / j }.+.3+4+5+              ",
"          . j.c . y./ / / h Q C x : v / '.6+(./ / <.=.k.C.m / / / l.7+/ / / >..+8+9+.               ",
"          0+c I @.> 8 ^ N 7.,+/ / x I S.4.,+B./ / / @.a+b+8.B / t ....Q.^ / V c+d+e+                ",
"        . # I < / ^ !.f+*+B L.h / / < T 4 }+q.A.^ / / >+C.W 9 ( ]+b | Z k.x D.g+h+.                 ",
"        > L.<.|./ / / P >.!.k.q.h / / 7 ]+t ^ 8 0+).j i+b./ X.S.L.V.^ / ~.& f+j+k+                  ",
"      . B h =.=.,+/ / 5 2 1 ^ >. .Y.^ 2 = ;./ / '+l+i+m+M.'.{.0 T i ] q / #+n+^.o+                  ",
"      ~ '.4.N '.f.G.x * . [+/ / h ,.] . -.8.<./ / j.. E p+*+k.%.5 / q+}.L 7+r+s+.                   ",
"    . 1.t+L / / )...= . , 9 C / / (.z ..< h - t 5 ~ y / / x.y ^ / / / N 6+u+v+w+                    ",
"    } x+:.s.;./ / X.. 0 {.X.e.G./ t 0+3 / / l $.6+5.e / / / / / / / / / 6.y+z+.                     ",
"  . & H.^ #.8.[+h f.r / / / x s.f+@ 7 / / / / e +.^ / / / / / / / / / / S.A+T..                     ",
"  . B+>+t t ] . C+T P '++.1.1.v Q #.C C C C C C C C s 4 D.[+[+,+L N  + +D+E+F+                      ",
". 3+*.*.*.*.G+H+I+J+K+L+y+M+w.N+O+P+Q+Q+Q+Q+Q+Q+Q+Q+e+R+S+T+U+V+W+X+Y+Z+H+`+.                       ",
"  *. @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @.@*.+@                        ",
"  *. @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @s+@@#@                        ",
"  *. @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @s+$@.                         ",
"  *. @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @%@.                           ",
"  g+&@&@&@&@&@&@*@j+s+=@-@A+;@>@,@,@,@,@9+o.'@)@!@r+~@{@*.*.*.*.*.*.*.]@.                           ",
"  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             "};
"""

class Surface3DCut(Cut):	
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName
		ViewSurface3DCut(obj.ViewObject)
		for prop in obj.PropertiesList:
			obj.setEditorMode(prop,("ReadOnly",))
		FreeCAD.ActiveDocument.recompute()
	
	def joinPolys(self,clip,subj):
		pc = pyclipper.Pyclipper()
		pc.AddPath(pyclipper.scale_to_clipper(clip), pyclipper.PT_CLIP, True)
		pc.AddPath(pyclipper.scale_to_clipper(subj), pyclipper.PT_SUBJECT, True)
		solution = pyclipper.scale_from_clipper(pc.Execute(pyclipper.CT_UNION, pyclipper.PFT_EVENODD, pyclipper.PFT_EVENODD))
		return solution
		
	def makeTrapazoid(self,seg,depth,direction):
		if direction == 'AlongX': return[(seg[0][0],seg[0][2]),(seg[1][0],seg[1][2]),(seg[1][0],depth),(seg[0][0],depth),(seg[0][0],seg[0][2])]
		return[(seg[0][1],seg[0][2]),(seg[1][1],seg[1][2]),(seg[1][1],depth),(seg[0][1],depth),(seg[0][1],seg[0][2])]
		
	def loopToTopContour(self,loop,depth):
		if loop[0] == loop[-1] and len(loop) > 1: loop.pop()
		# find the point farthest to the right and lowest
		maxPointIndex = 0
		maxPoint = loop[0]
		i = 1
		while i < len(loop):
			if loop[i][0] > maxPoint[0] or (loop[i][0] == maxPoint[0] and loop[i][1] < maxPoint[1]):
				maxPoint = loop[i]
				maxPointIndex = i
			i = i + 1
		loop = loop[maxPointIndex:] + loop[:maxPointIndex]
		loop.reverse()
		i = 0
		while i < len(loop) - 1:
			if loop[i][1] >= depth and loop[i + 1][1] >= depth:
				i = i + 1
				continue
			if loop[i][1] < depth and loop[i + 1][1] < depth:
				loop.pop(i)
				continue
			if loop[i][1] < depth and loop[i + 1][1] >= depth:
				if loop[i + 1][0] == loop[i][0]:
					loop[i] = (loop[i][0],depth)
					i = i + 1
					continue
				m = (loop[i+1][1] - loop[i][1]) / (loop[i][0 + 1] - loop[i][0])
				loop[i] = (loop[i][0] + (depth - loop[i][1])/m,depth)
				i = i + 1
				continue
			if loop[i][1] >= depth and loop[i + 1][1] < depth:
				if loop[i][0] == loop[i + 1][0]:
					loop[i + 1] = (loop[i + 1][0],depth)
					i = i + 1
					continue
				m = (loop[i+1][1] - loop[i][1]) / (loop[i + 1][0] - loop[i][0])
				loop[i] = (loop[i][0] + (depth - loop[i][1])/m,depth)
				i = i + 1
		if loop[-1][1] < depth: loop.pop()
		return loop

	def heightAt(self,x,path, default):
		if len(path) == 0: return default
		if x < path[0][0] or x > path[len(path) - 1][0]: return default
		i = 0
		while i < len(path) and x >= path[i][0]: i = i + 1
		if i == 0: return path[0][1]
		if i == len(path): return path[len(path) - 1][1]
		if x == path[i]: return path[i][1]
		m = (path[i][1] - path[i-1][1])/(path[i][0] - path[i-1][0])
		return path[i-1][1] + m * (x - path[i-1][0])
		
	def getToolProfile(self):
		step = self.obj.StepOver.Value
		bitProfile = [[0.,0.]]
		if self.toolParams['type'] == 'Ball':
			r = self.toolParams['ballDiameter'] / 2
			pos = step
			while pos <= r:
				theta = math.atan(pos/r)
				cosTheta = math.cos(theta)
				h = r - r * cosTheta
				bitProfile.insert(0,[-round(pos,3),round(h,3)])
				bitProfile.append([round(pos,3),round(h,3)])
				pos = pos + step
			if pos > r:
				bitProfile.insert(0,[round(-r,3),round(r,3)])
				bitProfile.append([round(r,3),round(r,3)])
		return bitProfile
		
	def getPixMap(self,obj,axis):
		fc = FreeCAD.ActiveDocument
		objectToCut = fc.getObjectsByLabel(obj.ObjectToCut)[0]		
		bb = objectToCut.Shape.BoundBox
		off = obj.Offset.Value
		if axis == 'AlongX':
			colMin, colMax, rowMin, rowMax = bb.XMin, bb.XMax, bb.YMin, bb.YMax
			a = 0
		else:
			colMin, colMax, rowMin, rowMax = bb.YMin, bb.YMax, bb.XMin, bb.XMax
			a = 1

		zmin, zmax = bb.ZMin, bb.ZMax
		depth = self.parent.ZOriginValue.Value - obj.MaximumDepth.Value
		self.updateActionLabel("Getting " + axis + ' contours')
		contours = list()
		step = obj.StepOver.Value
		offset = rowMin + step
		maximum = rowMax - step
		while offset <= maximum:
			# get next slice
			ds = self.getSlice(objectToCut,axis,offset)
			# form trapazoids below each segment and union each trapazoid with
			# the others and a base block that is defined with the maximum depth
			# and the bounds of the unit. This will return a single polygon
			traps = list()
			base = [(colMin,zmin-1),(colMax,zmin-1),(colMax,depth),(colMin,depth),(colMin,zmin-1)]
			traps.append(base)

			for seg in ds:
				if round(seg[0][a],6) == round(seg[1][a],6): continue
				trap = self.makeTrapazoid(seg,zmin - 1.,axis)
				polys = self.joinPolys(base,trap)
				base = polys[0]
			# get an outer offset from the single polygon that is offset by the value
			# specified by the user
			loop = self.getOffset([base],obj.Offset.Value)[0]
			i = 0
			while i < len(loop):
				loop[i] = (round(loop[i][0],3),round(loop[i][1],3))
				i = i + 1
			# throw away everything but the top contour of the object being cut
			# topContour = self.loopToTopContour(loop,depth + obj.Offset.Value)
			topContour = self.loopToTopContour(loop,depth + obj.Offset.Value)
			contours.append(topContour)
			offset = offset + step
		height = len(contours)
		width = int(math.ceil((colMax - colMin) / step))

		# make pixel map of size height by width an initialize to zmin - 1
		pixMap =  [ [ round(zmin - 1.,3) for y in range (width)] for x in range (height)]
		y = 0
		while y < height:
			x = 0
			while x < width:
				pixMap[y][x] = self.heightAt(colMin + step * x, contours[y], depth + obj.Offset.Value)
				x = x + 1			
			y = y + 1
		return pixMap

	def getHeightNearPoint(self,y,x,profile,hMap):
		center = profile.index([0.0,0.0])
		h = hMap[y][x]
		i = y - center
		while i < y + center:
			if i >= 0 and i < len(hMap):
				h = max(hMap[i][x] - profile[i - (y - center)][1],h)
			i = i + 1
		return h
		
	def interpolate(self,p1,p2,x):
		if p1[0] == p2[0]: return (p1[0],max(p1[1],p2[1]))
		m = (p2[1] - p1[1])/(p2[0] - p1[0])
		return (x,p1[1] + m * (x - p1[0]))
	
	def getTopContours(self,axis):
		obj = self.obj
		objectToCut = FreeCAD.ActiveDocument.getObjectsByLabel(obj.ObjectToCut)[0]		
		bb = objectToCut.Shape.BoundBox
		if axis == 'AlongX':
			colMin, colMax, rowMin, rowMax = bb.XMin, bb.XMax, bb.YMin, bb.YMax
			a = 0
		else:
			colMin, colMax, rowMin, rowMax = bb.YMin, bb.YMax, bb.XMin, bb.XMax
			a = 1
		contours = list()
		zmin, zmax = bb.ZMin, bb.ZMax
		depth = self.parent.ZOriginValue.Value - obj.MaximumDepth.Value
		step = self.obj.StepOver.Value
		offset = rowMin + step
		maximum = rowMax - step
		while offset <= maximum:
			self.updateActionLabel("Getting " + axis + "contour at offset = " + str(offset))
			ds = self.getSlice(objectToCut,axis,offset)
			# form trapazoids below each segment and union each trapazoid with
			# the others and a base block that is defined with the maximum depth
			# and the bounds of the unit. This will return a single polygon
			traps = list()
			base = [(colMin,zmin-1),(colMax,zmin-1),(colMax,depth),(colMin,depth),(colMin,zmin-1)]
			traps.append(base)

			for seg in ds:
				if round(seg[0][a],6) == round(seg[1][a],6): continue
				trap = self.makeTrapazoid(seg,zmin - 1.,axis)
				polys = self.joinPolys(base,trap)
				base = polys[0]
			# get an outer offset from the single polygon that is offset by the value
			# specified by the user
			loop = self.getOffset([base],obj.Offset.Value)[0]
			i = 0
			while i < len(loop):
				loop[i] = (round(loop[i][0],3),round(loop[i][1],3))
				i = i + 1
			# throw away everything but the top contour of the object being cut
			# topContour = self.loopToTopContour(loop,depth + obj.Offset.Value)
			topContour = self.loopToTopContour(loop,depth + obj.Offset.Value)
			
			lastPoint = topContour[0]
			while len(topContour) > 0:
				if  topContour[0][0] < colMin:
					lastPoint = topContour.pop(0)
				else:
					if topContour[0] != lastPoint:
						topContour.insert(0,self.interpolate(lastPoint,topContour[0],colMin)) 
					break
			while len(topContour) > 0:
				if topContour[-1][0] > colMax:
					lastPoint = topContour.pop()
				else:
					if topContour[-1] != lastPoint:
						topContour.append(self.interpolate(lastPoint,topContour[-1],colMax)) 
					break
					
			contours.append(topContour)
			offset = offset + step
		return contours
		
	def getCrossTopContour(self, yTops, x):
		obj = self.obj
		objectToCut = FreeCAD.ActiveDocument.getObjectsByLabel(obj.ObjectToCut)[0]		
		bb = objectToCut.Shape.BoundBox
		step = self.obj.StepOver.Value
		xVal = bb.YMin + x * step
		default = self.parent.ZOriginValue.Value - self.obj.MaximumDepth.Value + self.obj.Offset.Value
		topContour = list()
		i = 0
		while i < len(yTops):
			height = self.heightAt(xVal,yTops[i],default)
			topContour.append((bb.XMin + i * step,height))
			i = i + 1
		return topContour
		
	def insertPoint(self,p,path):
		x = p[0]
		i = 0
		while i < len(path):
			if path[i][0] >= x: break
			i = i + 1
		if i == len(path):
			path.append(p)
			return
		if path[i][0] == path[i - 1][0]:
			p = (path[i][0],max(path[i][1],path[i - 1][1]))
		else:
			m = (path[i][1] - path[i-1][1])/(path[i][0] - path[i-1][0])
			p = (x,path[i-1][1] + m * (x - path[i-1][0]))
		path.insert(i,p)
		return
		
	def getDelta(self,p1,p2,m):
		if m == "UP" or m == "DOWN":
			return abs(p2[0] - p1[0])
		else:
			return abs(p1[1] + m * (p2[0] - p1[0]) - p2[1])
		
	def reducePath(self,p):
		e = self.obj.MaximumError.Value
		l = p[0]
		r = [l]
		i = 1
		while i < len(p):
			if p[i] == r[-1]:
				i = i + 1
				continue
			if p[i][0] == r[-1][0]:
				if p[i][1] >= r[-1][1]: m = "UP"
				else: m = "DOWN"
			else:
				m = (p[i][1] - r[-1][1])/(p[i][0] - r[-1][0])
			i = i + 1
			while i < len(p) and self.getDelta(r[-1],p[i],m) < e:
				l = p[i]
				i = i + 1
			r.append(l)
			if i < len(p): l = p[i]		
		if p[-1] != r[-1]: r.append(p[-1])
		return r		
		
	def getCombinedPath(self,p1,p2):
		''' create new paths with from p1 and p2. Both paths will have
		every x point in either path, then check for segments crossing
		and create the return top path from there. Where crossings
		occur, calculate the crossing point and create another point there.
		Finally, reduce the paths by eliminating colinear line segments.'''
		newP1 = p1[:]
		i = 0
		while i < len(p2):
			self.insertPoint(p2[i],newP1)
			i = i + 1
		i = 0
		newP2 = p2[:]
		while i < len(p1):
			self.insertPoint(p1[i],newP2)
			i = i + 1
		if p1[0][1] >= p2[0][1]: newPath = [p1[0]]
		else: newPath = [p2[0]]
		i = 1
		while i < len(newP1):
			if newP1[i][1] >= newP2[i][1] and newP1[i-1][1] >= newP2[i-1][1]:
				newPath.append(newP1[i])
				i = i + 1
				continue
			elif newP1[i][1] <= newP2[i][1] and newP1[i-1][1] <= newP2[i-1][1]:
				newPath.append(newP2[i])
				i = i + 1
				continue
			else:
				xLen = newP1[i][0] - newP1[i-1][0]
				if xLen == 0.:
					newPath.append((newP1[i][0],max(newP1[i][1],newP2[i][1])))
				else:
					m1 = (newP1[i][1] - newP1[i-1][1])/xLen
					m2 = (newP2[i][1] - newP2[i-1][1])/xLen
					xf = newP1[i-1][0] + (newP2[i][1] - newP1[i][1])/(m1 - m2)
					yf = newP1[i-1][1] + m1 * (xf - newP1[i-1][0])
					newPath.append((xf,yf))
					newPath.append((newP1[i][0],max(newP1[i][1],newP2[i][1])))
			i = i + 1
		reducedPath = self.reducePath(newPath)
		return reducedPath
		
	def shiftLoop(self,loop,delta):
		shiftedLoop = loop[:]
		for p in shiftedLoop:
			p = (p[0],p[1] + delta)
		return shiftedLoop
		
	def joinManyPolys(self,polys):
		pc = pyclipper.Pyclipper()
		pc.AddPath(pyclipper.scale_to_clipper(polys[0]), pyclipper.PT_CLIP, True)
		pc.AddPaths(pyclipper.scale_to_clipper(polys[1:]), pyclipper.PT_SUBJECT, True)
		solution = pyclipper.scale_from_clipper(pc.Execute(pyclipper.CT_UNION, pyclipper.PFT_NONZERO, pyclipper.PFT_NONZERO))
		return solution
	
	def getContours(self):
		obj = self.obj
		objectToCut = FreeCAD.ActiveDocument.getObjectsByLabel(obj.ObjectToCut)[0]		
		bb = objectToCut.Shape.BoundBox
		if obj.Direction == 'AlongX':
			colMin, colMax, rowMin, rowMax = bb.XMin, bb.XMax, bb.YMin, bb.YMax
			a = 0
		else:
			colMin, colMax, rowMin, rowMax = bb.YMin, bb.YMax, bb.XMin, bb.XMax
			a = 1
		toolProfile = self.getToolProfile()

		slices = list()
		zmin, zmax = bb.ZMin, bb.ZMax
		depth = self.parent.ZOriginValue.Value - obj.MaximumDepth.Value
		step = self.obj.StepOver.Value
		direction = obj.Direction
		offset = rowMin + step
		maximum = rowMax - step
		while offset <= maximum:
			self.updateActionLabel("Getting " + direction + " slice at offset = " + str(offset))
			ds = self.getSlice(objectToCut,direction,offset)
			# form trapazoids below each segment and union each trapazoid with
			# the others and a base block that is defined with the maximum depth
			# and the bounds of the unit. This will return a single polygon
			traps = list()
			base = [(colMin,zmin-1),(colMax,zmin-1),(colMax,depth),(colMin,depth),(colMin,zmin-1)]
			traps.append(base)

			for seg in ds:
				if round(seg[0][a],6) == round(seg[1][a],6): continue
				trap = self.makeTrapazoid(seg,zmin - 1.,direction)
				polys = self.joinPolys(base,trap)
				base = polys[0]
			# get an outer offset from the single polygon that is offset by the value
			# specified by the user
			slices.append(self.getOffset([base],obj.Offset.Value)[0])
			offset = offset + step
		topContours = list()
		j = 0
		while j < len(slices):
			loopsToCombine = list()
			offset = 0
			i = -int(len(toolProfile) / 2)
			while i <= int(len(toolProfile) / 2):
				if j + i >= 0 and j + i < len(slices):
					loopsToCombine.append(self.shiftLoop(slices[j + i],toolProfile[int(len(toolProfile) / 2) + i][1]))
				i = i + 1			
			if len(loopsToCombine) > 1:
				solution = self.joinManyPolys(loopsToCombine)[0]
			elif len(loopsToCombine) == 1:
				solution = loopsToCombine[0]
			else:
				solution = []

			if solution != []: topContour = self.loopToTopContour(solution,depth + obj.Offset.Value)
			lastPoint = topContour[0]
			while len(topContour) > 0:
				if  topContour[0][0] < colMin:
					lastPoint = topContour.pop(0)
				else:
					if topContour[0] != lastPoint:
						topContour.insert(0,self.interpolate(lastPoint,topContour[0],colMin)) 
					break
			while len(topContour) > 0:
				if topContour[-1][0] > colMax:
					lastPoint = topContour.pop()
				else:
					if topContour[-1] != lastPoint:
						topContour.append(self.interpolate(lastPoint,topContour[-1],colMax)) 
					break
			topContours.append(topContour)
			j = j + 1
		return topContours
				
	def run(self, ui, obj, outputUnits,fp):
		self.obj = obj
		self.parent = obj.getParentGroup()
		self.fp = fp
		self.ui = ui
		self.outputUnits = outputUnits
		self.cuttingDirection = None

		out = self.writeGCodeLine
		self.updateActionLabel("Running " + obj.CutName)
		self.safeHeight = obj.SafeHeight.Value
		tool = str(obj.ToolNumber)
		rapid = self.rapid
		cut = self.cut
		self.setToolParams(obj)
		out("(Starting " + obj.CutName + ')')
		self.setUserUnits()
		self.setOffset(self.parent.XOriginValue.Value, self.parent.YOriginValue.Value, self.parent.ZOriginValue.Value)
		self.updateActionLabel("Setting feeds and speeds for " + obj.CutName)
		
		rapid(z=obj.ZToolChangeLocation.Value)
		rapid(obj.XToolChangeLocation.Value,obj.YToolChangeLocation.Value)
		out('T' + tool + 'M6')
		out('S' + str(obj.SpindleSpeed).split()[0])
		
		#xTopContours = self.getTopContours('AlongX')

		combinedPaths = self.getContours()
		'''
		
		yTopContours = self.getTopContours('AlongY')
		self.updateActionLabel("Getting cross top contours")
		crossTopContours = list()
		i = 0
		while i < len(xTopContours):
			crossTopContours.append(self.getCrossTopContour(yTopContours,i))
			i = i + 1
		self.updateActionLabel('Combining X contours with crosstop contours')
		
		combinedPaths = list()
		i = 0
		while i < len(xTopContours):
			combinedPaths.append(self.getCombinedPath(xTopContours[i],crossTopContours[i]))
			i = i + 1
		'''
		fc = FreeCAD.ActiveDocument
		objectToCut = fc.getObjectsByLabel(obj.ObjectToCut)[0]		
		bb = objectToCut.Shape.BoundBox
		offset = obj.Offset.Value
		step = obj.StepOver.Value
		
		if obj.Direction == 'AlongX':
			rowShift = bb.YMin
			i = 0
			while i < len(combinedPaths):
				self.rapid(z = self.safeHeight)
				self.rapid(combinedPaths[i][0][0], rowShift + i * step)
				j = 0
				while j < len(combinedPaths[i]):
					self.cut(combinedPaths[i][j][0],rowShift + i * step,combinedPaths[i][j][1] - self.parent.ZOriginValue.Value - obj.Offset.Value)
					j = j + 1
				i = i + 1
		else:
			colShift = bb.XMin
			i = 0
			while i < len(combinedPaths):
				self.rapid(z = self.safeHeight)
				self.rapid(colShift + i * step,combinedPaths[i][0][0])
				j = 0
				while j < len(combinedPaths[i]):
					self.cut(colShift + i * step,combinedPaths[i][j][0],combinedPaths[i][j][1] - self.parent.ZOriginValue.Value - obj.Offset.Value)
					j = j + 1
				i = i + 1
					
		self.rapid(z = self.safeHeight)
		return
		'''
		self.updateActionLabel("Making X oriented pixel map")
		xMap = self.getPixMap(obj,obj.Direction)
		# adjust height if bit conflicts with adjacent contours
		pixMap = list()
		profile = self.getToolProfile()

		y = 0
		while y < len(xMap):
			row = list()
			x = 0
			while x < len(xMap[y]):
				row.append(self.getHeightNearPoint(y,x,profile,xMap))
				#row.append(xMap[y][x])
				x = x + 1
			pixMap.append(row)
			y = y + 1
		
		fc = FreeCAD.ActiveDocument
		objectToCut = fc.getObjectsByLabel(obj.ObjectToCut)[0]		
		bb = objectToCut.Shape.BoundBox
		offset = obj.Offset.Value
		step = obj.StepOver.Value
		rowShift = bb.YMin
		colShift = bb.XMin
		r = 0
		while r < len(pixMap):
			self.rapid(z = self.safeHeight)
			self.rapid(colShift, rowShift + r * step)
			c = 0
			while c < len(pixMap[0]):
				self.cut(colShift + c * step,rowShift + r * step,pixMap[r][c] - self.parent.ZOriginValue.Value - obj.Offset.Value)
				c = c + 1
			r = r + 1
		
		return		
		'''
