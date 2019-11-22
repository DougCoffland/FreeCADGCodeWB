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

class ViewVolume2DCut(ViewCut):
	def getIcon(self):
		return """
/* XPM */
static char * Volume2D_xpm[] = {
"50 50 293 2",
"  	c None",
". 	c #000000",
"+ 	c #201507",
"@ 	c #5A4120",
"# 	c #72532B",
"$ 	c #7F5D30",
"% 	c #836032",
"& 	c #916A38",
"* 	c #8D6837",
"= 	c #7E5D30",
"- 	c #604623",
"; 	c #1F1406",
"> 	c #493419",
", 	c #9E743E",
"' 	c #A0763F",
") 	c #9A713C",
"! 	c #5D4321",
"~ 	c #1F1507",
"{ 	c #674B26",
"] 	c #000200",
"^ 	c #003300",
"/ 	c #006600",
"( 	c #002C00",
"_ 	c #33230F",
": 	c #916B38",
"< 	c #9D743E",
"[ 	c #443016",
"} 	c #007300",
"| 	c #00DB00",
"1 	c #00EB00",
"2 	c #00FD00",
"3 	c #00FF00",
"4 	c #003900",
"5 	c #004B00",
"6 	c #00F600",
"7 	c #00C700",
"8 	c #0B0602",
"9 	c #8E6837",
"0 	c #8D6737",
"a 	c #00E300",
"b 	c #00CF00",
"c 	c #00A600",
"d 	c #005B00",
"e 	c #6E5029",
"f 	c #4F391B",
"g 	c #009700",
"h 	c #00A100",
"i 	c #00EC00",
"j 	c #00DA00",
"k 	c #98703C",
"l 	c #7B5A2E",
"m 	c #005700",
"n 	c #007B00",
"o 	c #00AC00",
"p 	c #453117",
"q 	c #00E900",
"r 	c #3C3326",
"s 	c #00C600",
"t 	c #009300",
"u 	c #664A25",
"v 	c #6C4E28",
"w 	c #00B000",
"x 	c #282218",
"y 	c #645742",
"z 	c #004000",
"A 	c #694C27",
"B 	c #5D4422",
"C 	c #007A00",
"D 	c #5E513E",
"E 	c #009F00",
"F 	c #3A2912",
"G 	c #00F700",
"H 	c #001E00",
"I 	c #8F7C60",
"J 	c #5F523F",
"K 	c #00E500",
"L 	c #00AB00",
"M 	c #4C361A",
"N 	c #966F3B",
"O 	c #020201",
"P 	c #554938",
"Q 	c #007000",
"R 	c #009D00",
"S 	c #563E1E",
"T 	c #76562C",
"U 	c #000300",
"V 	c #009100",
"W 	c #504534",
"X 	c #493E2F",
"Y 	c #00BD00",
"Z 	c #005900",
"` 	c #77572D",
" .	c #2F210D",
"..	c #006300",
"+.	c #004800",
"@.	c #786850",
"#.	c #15110B",
"$.	c #003600",
"%.	c #00F800",
"&.	c #00F000",
"*.	c #8F6937",
"=.	c #73542B",
"-.	c #002300",
";.	c #008C00",
">.	c #AD9675",
",.	c #927E62",
"'.	c #009500",
").	c #00C800",
"!.	c #1E1406",
"~.	c #8C6736",
"{.	c #006D00",
"].	c #009200",
"^.	c #332B20",
"/.	c #645642",
"(.	c #00DC00",
"_.	c #00A300",
":.	c #523B1D",
"<.	c #006B00",
"[.	c #6C5E48",
"}.	c #2D251B",
"|.	c #006500",
"1.	c #008000",
"2.	c #694D27",
"3.	c #020400",
"4.	c #006200",
"5.	c #009B00",
"6.	c #958265",
"7.	c #A48E6F",
"8.	c #00B700",
"9.	c #7E5C30",
"0.	c #886434",
"a.	c #221808",
"b.	c #005C00",
"c.	c #008F00",
"d.	c #00BC00",
"e.	c #1B160F",
"f.	c #75654E",
"g.	c #003D00",
"h.	c #9B723D",
"i.	c #856133",
"j.	c #6A4D27",
"k.	c #4D381B",
"l.	c #0B0902",
"m.	c #005200",
"n.	c #007700",
"o.	c #009900",
"p.	c #008200",
"q.	c #584B39",
"r.	c #453B2C",
"s.	c #008E00",
"t.	c #002D00",
"u.	c #8B6636",
"v.	c #5E4422",
"w.	c #0E1902",
"x.	c #007900",
"y.	c #008B00",
"z.	c #009C00",
"A.	c #007800",
"B.	c #003500",
"C.	c #857359",
"D.	c #00D700",
"E.	c #533C1D",
"F.	c #9F763F",
"G.	c #826032",
"H.	c #433016",
"I.	c #004300",
"J.	c #007D00",
"K.	c #003000",
"L.	c #00CE00",
"M.	c #87755B",
"N.	c #002100",
"O.	c #7D5B2F",
"P.	c #3C2B13",
"Q.	c #008900",
"R.	c #004D00",
"S.	c #009E00",
"T.	c #443A2B",
"U.	c #584C3A",
"V.	c #003B00",
"W.	c #005400",
"X.	c #00A900",
"Y.	c #74644D",
"Z.	c #001F00",
"`.	c #00F100",
" +	c #005F00",
".+	c #008300",
"++	c #00B900",
"@+	c #00CD00",
"#+	c #A08B6C",
"$+	c #968265",
"%+	c #008500",
"&+	c #007F00",
"*+	c #008400",
"=+	c #004C00",
"-+	c #005600",
";+	c #00B100",
">+	c #00F300",
",+	c #00AD00",
"'+	c #292219",
")+	c #6D5E48",
"!+	c #009400",
"~+	c #004400",
"{+	c #006000",
"]+	c #00BF00",
"^+	c #625441",
"/+	c #322B1F",
"(+	c #00A200",
"_+	c #008100",
":+	c #00CA00",
"<+	c #001600",
"[+	c #907D61",
"}+	c #00A700",
"|+	c #00B500",
"1+	c #006A00",
"2+	c #003200",
"3+	c #00D300",
"4+	c #040302",
"5+	c #00ED00",
"6+	c #00C200",
"7+	c #008A00",
"8+	c #007E00",
"9+	c #005E00",
"0+	c #002400",
"a+	c #514635",
"b+	c #4F4433",
"c+	c #007C00",
"d+	c #006700",
"e+	c #7B6A52",
"f+	c #AF9877",
"g+	c #00FE00",
"h+	c #00A400",
"i+	c #5B4E3C",
"j+	c #00A000",
"k+	c #6E5F49",
"l+	c #251F16",
"m+	c #00E700",
"n+	c #978366",
"o+	c #9C8769",
"p+	c #007400",
"q+	c #00BA00",
"r+	c #1C170F",
"s+	c #71624B",
"t+	c #00C100",
"u+	c #3A3125",
"v+	c #00BE00",
"w+	c #00C500",
"x+	c #00CC00",
"y+	c #00D200",
"z+	c #00D400",
"A+	c #00D800",
"B+	c #00DF00",
"C+	c #00E800",
"D+	c #89775C",
"E+	c #000900",
"F+	c #001500",
"G+	c #806F56",
"H+	c #85725A",
"I+	c #C9AE8A",
"J+	c #C7AC89",
"K+	c #C1A785",
"L+	c #BEA582",
"M+	c #BCA281",
"N+	c #B89F7E",
"O+	c #B69E7D",
"P+	c #B69D7D",
"Q+	c #B69D7C",
"R+	c #B59D7C",
"S+	c #B49C7C",
"T+	c #B29A7A",
"U+	c #A79172",
"V+	c #A18B6E",
"W+	c #A08A6D",
"X+	c #524635",
"Y+	c #A89172",
"Z+	c #100C07",
"`+	c #837159",
" @	c #A89173",
".@	c #927F62",
"+@	c #74644E",
"@@	c #635542",
"#@	c #2C251B",
"$@	c #605240",
"%@	c #3D3427",
"&@	c #85735A",
"*@	c #87745B",
"=@	c #8B785E",
"-@	c #927E63",
";@	c #968266",
">@	c #988367",
",@	c #9A8569",
"'@	c #9F896C",
")@	c #A28C6E",
"!@	c #88765C",
"                                                . . . . . . . .                                     ",
"                                          . . + @ # $ % & * = - ; .                                 ",
"                                        . > % , ' ' ' ' ' ' ' ' ) ! .                           . . ",
"                                    . ~ $ ' ' ' ' ' ' ' ' ' ' ' ' ' { . . . . . . . . . ] ^ / / ( . ",
"                            . . . . _ : ' ' ' ' ' ' ' ' ' ' ' ' ' ' < [ } | | | 1 2 3 3 3 3 3 3 4 . ",
"                            5 6 7 8 9 ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 0 . a 3 3 3 3 3 3 3 3 3 b . . ",
"                          . c 3 d e ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' f g 3 3 3 3 3 3 3 3 3 h . . ",
"                          . i j . k ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' l / 3 3 3 3 3 3 3 3 3 m . . ",
"                        . n 3 o p ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' = / 3 3 3 3 3 3 3 3 q . r . ",
"                        . s 3 t u ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' v / 3 3 3 3 3 3 3 3 w x y . ",
"                        z 2 3 t A ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' B / 3 3 3 3 3 3 3 3 C D y . ",
"                      . E 3 3 t u ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' F / 3 3 3 3 3 3 3 G H I J . ",
"                      . K 3 3 L M ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' N ] / 3 3 3 3 3 3 3 7 O   P . ",
"                    . Q 3 3 3 R S ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' T U / 3 3 3 3 3 3 3 V W   X . ",
"                    . Y 3 3 3 Z ` ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' <  .../ 3 3 3 3 3 3 3 +.@.  #.  ",
"                    $.%.3 3 &.. *.' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' =.-.;./ 3 3 3 3 3 3 | . >.,..   ",
"                  . '.3 3 3 ).!.' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ~.] {.]./ 3 3 3 3 3 3 c ^.  /..   ",
"                  . (.3 3 3 _.:.' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ~.~ ^ '.]./ 3 3 3 3 3 3 <.[.  }.    ",
"                . |.3 3 3 3 1.2.' ' ' ' ' ' ' ' ' ' ' ' ' ' < T 3.4.5.h ]./ 3 3 3 3 3 &.. 6.7..     ",
"                . 8.3 3 3 3 / 9.' ' ' ' ' ' ' ' ' ' ' < 0.{ a.b.c.h h h ]./ 3 3 3 3 3 d.e.  f..     ",
"                ( 6 3 3 3 3 g.$ ' ' ' ' ' ' ' h.i.j.k.l.m.n.o.h h h h h ]./ 3 3 3 3 3 p.q.  r..     ",
"              . s.3 3 3 3 3 t.$ ' ' ' ' ' u.v.w.Z x.y.z.h h h h h h h h A.c.3 3 3 3 3 B.C.  .       ",
"              . D.3 3 3 3 3 / E.' ' F.G.H.I.J.5.h h h h h h h h h h h 5.K.D.3 3 3 3 L..   M..       ",
"            . b.3 3 3 3 3 3 V N.j.O.P.m.Q.h h h h h h h h h h h h h '.R.5.3 3 3 3 3 S.T.  U..       ",
"            . w 3 3 3 3 3 3 t n.V.W.s.h h h h h h h h h h h 5.J.d R.t.X.3 3 3 3 3 3 W.Y.  e.        ",
"            Z.`.3 3 3 3 3 3 t 1.S.h h h h h h h h h h h s. +( .+++@+6 3 3 3 3 3 3 q . #+$+.         ",
"          . %+3 3 3 3 3 3 3 t &+h h h h h h h h h h *+=+-+;+>+3 3 3 3 3 3 3 3 3 3 ,+'+  )+.         ",
"          . L.3 3 3 3 3 3 3 !+x.h h h h h h h h .+~+{+]+3 3 3 3 3 3 3 3 3 3 3 3 3 x.^+  /+          ",
"        . R.3 3 3 3 3 3 3 3 (+<.h h h h h E _+I.<.:+3 3 3 3 3 3 3 3 3 3 3 3 3 3 G <+[+>..           ",
"        . }+3 3 3 3 3 3 3 3 |+1+h h h 5.C 2+Q 3+3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 s 4+  @..           ",
"        . 5+3 3 3 3 3 3 3 3 6+=+7+8+9+0+7+D.3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 ;.a+  b+.           ",
"      . c+3 3 3 3 3 3 3 3 3 3 }+d+Q.++`.3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 ~+e+  .             ",
"      . 7 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 | . f+I .             ",
"      z g+3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 h+^.  i+.             ",
"    . j+3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 d+k+  l+              ",
"    . m+3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 &.. n+o+.               ",
"  . p+3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 q+r+  s+.               ",
"  . t+3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 1.U.  u+.               ",
"  <+v+w+s s s s s s s s s s s s s s s ).x+y+y+3+3+3+3+3+3+3+z+A+B+m+C+C+C+6 K.D+  .                 ",
". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . E+F+.   G+.                 ",
". H+I+I+I+I+I+I+I+J+K+L+M+N+O+P+P+P+P+P+P+P+P+P+P+P+Q+R+S+T+U+V+W+W+W+W+W+H+.   X+.                 ",
". H+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+Y+.   Z+                  ",
". `+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+ @. .@.                   ",
". +@I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+Y+. /..                   ",
". @@I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+Y+. #@                    ",
". $@I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+Y+. .                     ",
". $@I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+ @. .                     ",
"  $@I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+I+ @. .                     ",
"  %@H+H+H+H+H+H+H+H+&@*@=@-@;@>@,@'@W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+W+V+)@!@.                       ",
"  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                       "};

"""

class Volume2DCut(Cut):	
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName
		ViewVolume2DCut(obj.ViewObject)
		for prop in obj.PropertiesList:
			obj.setEditorMode(prop,("ReadOnly",))
		FreeCAD.ActiveDocument.recompute()
		
	def run(self, ui, obj, outputUnits,fp):
		self.obj = obj
		self.parent = obj.getParentGroup()
		self.fp = fp
		self.ui = ui
		self.outputUnits = outputUnits
		self.error = obj.MaximumError.Value
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
		
		self.updateActionLabel("Getting Boundaries for " + obj.CutName)
		polys = self.getPolysAtSlice(obj.ObjectToCut,"XY",self.parent.ZOriginValue.Value - obj.PerimeterDepth.Value)
		cutAreaPolys = self.getPolysAtSlice(obj.CutArea,"XY",self.parent.ZOriginValue.Value - obj.PerimeterDepth.Value)
		polys = self.getClipSolutions(cutAreaPolys[0],polys)
		polys = self.moveOrigin2D(polys)
		polyList =[]
		offset = 0
		self.updateActionLabel("Getting offset polygons for " + obj.CutName)
		offset = obj.OffsetFromPerimeter.Value
		offsetPolys = self.getOffset(polys,-offset)
		while len(offsetPolys) > 0:
			for poly in offsetPolys:
				polyList.append(poly)
			offset = offset + obj.StepOver.Value
			offsetPolys = self.getOffset(polys,-offset)
		self.updateActionLabel("Generating cuts for " + obj.CutName)
		currentDepth = obj.StartHeight.Value
		while currentDepth >= -obj.DepthOfCut.Value:
			currentList = polyList[:]
			while len(currentList) > 0:
				self.rapid(z=self.safeHeight)

				poly = self.shortestPoly(currentList)
				self.rapid(poly[0][0],poly[0][1])
				self.cut(z=currentDepth)
				area = self.areaOfPoly(poly)
				reducedPoly = self.smoothePoly(poly)
				if obj.MillingMethod == "Climb": self.cutPolyInsideClimb(reducedPoly)
				else: self.cutPolyInsideConventional(reducedPoly)
				currentList.remove(poly)
				poly = self.nextPoly(poly[0][0],poly[0][1],currentList,self.bitWidth)

				while poly != None:
					length = self.lengthOfPoly(poly)
					lengthTimesWidth = length * obj.StepOver.Value
					if self.areaOfPoly(poly) - lengthTimesWidth > area: break
					reducedPoly = self.smoothePoly(poly)
					if obj.MillingMethod == "Climb": self.cutPolyInsideClimb(reducedPoly)
					else: self.cutPolyInsideConventional(reducedPoly)
					area = self.areaOfPoly(poly)
					currentList.remove(poly)
					poly = self.nextPoly(poly[0][0],poly[0][1],currentList,self.bitWidth)					
			if currentDepth == -obj.DepthOfCut.Value: break
			if currentDepth - obj.StepDown.Value <= -obj.DepthOfCut.Value: currentDepth = -obj.DepthOfCut.Value
			else: currentDepth = currentDepth - obj.StepDown.Value
		self.rapid(z = self.safeHeight)
			

