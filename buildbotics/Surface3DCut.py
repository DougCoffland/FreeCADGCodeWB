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
from PySide import QtGui, QtCore, QtWebKit
from pivy import coin
import os
from Cut import Cut, ViewCut
import validator as VAL
import math

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
		
	def reverseWire(self,wire):
		reversedWire = list()
		while len(wire) > 0: reversedWire.append(wire.pop())
		return reversedWire
		
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
		self.setBitWidth(obj)
		out("(Starting " + obj.CutName + ')')
		self.setUserUnits()
		self.setOffset(self.parent.XOriginValue.Value, self.parent.YOriginValue.Value, self.parent.ZOriginValue.Value)
		self.updateActionLabel("Setting feeds and speeds for " + obj.CutName)
		
		rapid(z=obj.ZToolChangeLocation.Value)
		rapid(obj.XToolChangeLocation.Value,obj.YToolChangeLocation.Value)
		out('T' + tool + 'M6')
		out('S' + str(obj.SpindleSpeed).split()[0])
		
		fc = FreeCAD.ActiveDocument
		offsetName = self.getUniqueName("Offset")
		fc.addObject("Part::Offset",offsetName)
		offsetObject = fc.getObjectsByLabel(offsetName)[0]
		objectToScan = fc.getObjectsByLabel(obj.ObjectToCut)[0]
		offsetObject.Source = objectToScan
		offsetObject.Value = obj.Offset.Value
		offsetObject.Mode = 0
		offsetObject.Join = 0
		offsetObject.Intersection = False
		offsetObject.SelfIntersection = False
		fc.recompute()
		
		self.updateActionLabel("getting slice wires")
		
		i = 0.
		xmin = offsetObject.Shape.BoundBox.XMin
		xmax = offsetObject.Shape.BoundBox.XMax
		ymin = offsetObject.Shape.BoundBox.YMin
		ymax = offsetObject.Shape.BoundBox.YMax
		if obj.Direction == 'AlongX':
			position = ymin
			maxPosition = ymax
		elif obj.Direction == 'AlongY':
			position = xmin
			maxPosition = xmax
		elif obj.Direction == 'Diagonal':
			position = xmin
			maxPosition = xmax + (ymax - ymin) * math.sqrt(2.)
		wire = list()
		while position <= maxPosition:
			if i % 2 == 0:
				temp = self.getWire(offsetObject,obj.Direction,self.parent.ZOriginValue.Value - obj.MaximumDepth.Value,position)
				if temp != None: wire = wire + temp
			else:
				temp = self.getWire(offsetObject,obj.Direction,self.parent.ZOriginValue.Value - obj.MaximumDepth.Value,position)
				if temp != None: 
					temp.reverse()
					wire = wire + temp
					
			if obj.Direction == 'Diagonal': position = position + obj.StepOver.Value * math.sqrt(2.)
			else: position = position + obj.StepOver.Value
			i = i + 1

		self.cutWire(wire)
		fc.removeObject(offsetName)
		fc.recompute()


