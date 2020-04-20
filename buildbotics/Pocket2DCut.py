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

class ViewPocket2DCut(ViewCut):
	def getIcon(self):
		return """
/* XPM */
static char * pocket2D_xpm[] = {
"50 50 281 2",
"  	c None",
". 	c #000000",
"+ 	c #0C0906",
"@ 	c #4A3F30",
"# 	c #4E4333",
"$ 	c #574B3A",
"% 	c #372F23",
"& 	c #2D261C",
"* 	c #4D4232",
"= 	c #4F4334",
"- 	c #5F523F",
"; 	c #71624C",
"> 	c #72624C",
", 	c #837259",
"' 	c #8E7B61",
") 	c #8F7C61",
"! 	c #907D62",
"~ 	c #A28D6F",
"{ 	c #AB9475",
"] 	c #AE9777",
"^ 	c #C0A784",
"/ 	c #C7AD89",
"( 	c #3A3225",
"_ 	c #564A39",
": 	c #B39B7B",
"< 	c #917E63",
"[ 	c #87745B",
"} 	c #211B13",
"| 	c #C1A784",
"1 	c #5D503E",
"2 	c #342C20",
"3 	c #6E5F4A",
"4 	c #C2A885",
"5 	c #19140E",
"6 	c #665843",
"7 	c #A79172",
"8 	c #8B795F",
"9 	c #958165",
"0 	c #AF9878",
"a 	c #9E896C",
"b 	c #2E271C",
"c 	c #7A6A52",
"d 	c #3A3125",
"e 	c #B69E7D",
"f 	c #84725A",
"g 	c #5B4F3D",
"h 	c #201B13",
"i 	c #30281E",
"j 	c #796952",
"k 	c #BBA381",
"l 	c #776750",
"m 	c #615440",
"n 	c #6B5C47",
"o 	c #7F6E56",
"p 	c #A58F71",
"q 	c #5C4F3D",
"r 	c #0C4405",
"s 	c #1F8012",
"t 	c #2AA119",
"u 	c #2EAE1C",
"v 	c #35C321",
"w 	c #36C822",
"x 	c #34BF20",
"y 	c #2AA219",
"z 	c #1C760F",
"A 	c #948065",
"B 	c #3C3327",
"C 	c #8F7C60",
"D 	c #655743",
"E 	c #B59E7D",
"F 	c #BFA683",
"G 	c #665844",
"H 	c #0B4005",
"I 	c #279817",
"J 	c #3EE027",
"K 	c #38CD23",
"L 	c #1E7C11",
"M 	c #86745B",
"N 	c #645742",
"O 	c #594D3B",
"P 	c #3B3226",
"Q 	c #052C02",
"R 	c #3CDB26",
"S 	c #2BA51A",
"T 	c #968266",
"U 	c #8A775E",
"V 	c #4B4031",
"W 	c #927E63",
"X 	c #BEA583",
"Y 	c #104F07",
"Z 	c #38CE23",
"` 	c #289A18",
" .	c #201A13",
"..	c #BAA280",
"+.	c #5F513F",
"@.	c #76664F",
"#.	c #3F3528",
"$.	c #C1A885",
"%.	c #6C5D48",
"&.	c #3AD324",
"*.	c #17650C",
"=.	c #6D5E49",
"-.	c #C3AA86",
";.	c #1F1912",
">.	c #A38E6F",
",.	c #6C5D49",
"'.	c #B79F7E",
").	c #35C320",
"!.	c #0F0B07",
"~.	c #A08A6D",
"{.	c #292218",
"].	c #88765B",
"^.	c #196C0D",
"/.	c #38CB23",
"(.	c #010100",
"_.	c #7A6952",
":.	c #5D503D",
"<.	c #594C3A",
"[.	c #299D18",
"}.	c #34C220",
"|.	c #483D2F",
"1.	c #41372A",
"2.	c #8D7B5F",
"3.	c #251F16",
"4.	c #816F57",
"5.	c #2EAD1C",
"6.	c #2BA41A",
"7.	c #635642",
"8.	c #9E896B",
"9.	c #289B18",
"0.	c #1C7710",
"a.	c #85735A",
"b.	c #8D7A60",
"c.	c #473D2E",
"d.	c #72634C",
"e.	c #594C3B",
"f.	c #8A785E",
"g.	c #39D024",
"h.	c #B59D7C",
"i.	c #625542",
"j.	c #73644D",
"k.	c #453B2C",
"l.	c #635542",
"m.	c #279717",
"n.	c #218613",
"o.	c #C6AC89",
"p.	c #241E16",
"q.	c #9F8A6C",
"r.	c #1E1912",
"s.	c #31B71E",
"t.	c #A89273",
"u.	c #A28C6F",
"v.	c #282118",
"w.	c #8B795E",
"x.	c #9A8669",
"y.	c #35C220",
"z.	c #7D6C55",
"A.	c #5A4D3B",
"B.	c #A48E70",
"C.	c #70614B",
"D.	c #269516",
"E.	c #031B01",
"F.	c #C6AC88",
"G.	c #4A4031",
"H.	c #8A775D",
"I.	c #272117",
"J.	c #3C3326",
"K.	c #443A2C",
"L.	c #32BB1F",
"M.	c #18690D",
"N.	c #C4AA87",
"O.	c #BAA180",
"P.	c #806F57",
"Q.	c #C5AB88",
"R.	c #3BD625",
"S.	c #30B31D",
"T.	c #1A6E0E",
"U.	c #30291E",
"V.	c #9A8569",
"W.	c #948165",
"X.	c #413729",
"Y.	c #AC9576",
"Z.	c #021901",
"`.	c #37CA22",
" +	c #2BA61A",
".+	c #1D7A10",
"++	c #052802",
"@+	c #332B20",
"#+	c #89765D",
"$+	c #71614B",
"%+	c #463C2D",
"&+	c #584C3B",
"*+	c #093804",
"=+	c #37C922",
"-+	c #299E18",
";+	c #1A700E",
">+	c #031C01",
",+	c #2B241A",
"'+	c #685A46",
")+	c #9D886B",
"!+	c #2F271D",
"~+	c #998567",
"{+	c #937F64",
"]+	c #105007",
"^+	c #3D3427",
"/+	c #695B46",
"(+	c #88765D",
"_+	c #A99374",
":+	c #A89173",
"<+	c #8D7A5F",
"[+	c #4F4434",
"}+	c #2FB11D",
"|+	c #34C020",
"1+	c #238B14",
"2+	c #574A39",
"3+	c #010000",
"4+	c #584B3A",
"5+	c #837159",
"6+	c #544837",
"7+	c #827157",
"8+	c #292319",
"9+	c #AA9374",
"0+	c #BCA381",
"a+	c #A48E6F",
"b+	c #998569",
"c+	c #6B5C48",
"d+	c #4C4131",
"e+	c #B79F7D",
"f+	c #31291F",
"g+	c #968265",
"h+	c #5B4E3C",
"i+	c #AB9575",
"j+	c #18130D",
"k+	c #907D61",
"l+	c #927F64",
"m+	c #524736",
"n+	c #60533F",
"o+	c #1C1710",
"p+	c #BDA482",
"q+	c #7D6C54",
"r+	c #2A241A",
"s+	c #0B0906",
"t+	c #1F1B14",
"u+	c #352D22",
"v+	c #382F24",
"w+	c #383024",
"x+	c #3A3226",
"y+	c #40372A",
"z+	c #433A2D",
"A+	c #493E30",
"B+	c #5F5240",
"C+	c #A69171",
"D+	c #655744",
"E+	c #85725A",
"F+	c #847259",
"G+	c #7E6C55",
"H+	c #74644E",
"I+	c #675945",
"J+	c #615341",
"K+	c #605240",
"L+	c #342C21",
"M+	c #16120C",
"N+	c #040302",
"O+	c #0A0805",
"P+	c #77674F",
"Q+	c #C9AE8A",
"R+	c #B69D7D",
"S+	c #0E0B07",
"T+	c #635541",
"U+	c #2F281D",
"V+	c #030201",
"W+	c #776650",
"X+	c #020201",
"Y+	c #070503",
"Z+	c #393025",
"`+	c #554938",
" @	c #625441",
".@	c #72624D",
"+@	c #75654F",
"@@	c #7C6B54",
"#@	c #786751",
"                                                                            . . . . . . . . . . . . ",
"                              . . . . . . . . . . . . . . . . . . . . . . . . . . . + @ # # # $ % . ",
"                            . . . . & * # # = - ; ; ; > , ' ) ) ! ~ { { { ] ^ / / / / / / / / / ( . ",
"                            _ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / : . . ",
"                          . < / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / [ . . ",
"                          } | / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 1 2 . ",
"                        . 3 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 4 5 6 . ",
"                        . ~ / / / / / / / / / / : 7 ! ) ' 8 ) 9 0 / / / / / / / / / / / / / a b c . ",
"                        d / / / / / / / e f g h . . . . . . . . . i j k / / / / / / / / / / l m n . ",
"                      . o / / / / / p q . . r s t u v w w w w x y z . h A / / / / / / / / / B C D . ",
"                      . E / / / F G . H I w J J J J J J J J J J J J K L . M / / / / / / / E .   N . ",
"                      O / / / e P Q y R J J J J J J J J J J J J J J J J S . T / / / / / / U V   N . ",
"                    . W / / X P Y Z J J J J J J J J J J J J J J J J J J J `  .../ / / / / +.@.  #.  ",
"                    h $./ / %.Y &.J J J J J J J J J J J J J J J J J J J J J *.=./ / / / -.;.>.  .   ",
"                  . ,./ / '.. v J J J J J J J J J J J J J J J J J J J J J J ).!./ / / / ~.{.  ]..   ",
"                  . ~ / / U ^.J J J J J J J J J J J J J J J J J J J J J J J /.(./ / / / _.:.  <..   ",
"                  P / / / ; [.J J J J J J J J J J J J J J J J J J J J J J J }.|./ / / / 1.2.  3.    ",
"                . 4./ / / ; 5.J J J J J J J J J J J J J J J J J J J J J J J 6.7./ / / e .   8..     ",
"                . e / / / ; 9.J J J J J J J J J J J J J J J J J J J J J J J 0.a./ / / b.c.  d..     ",
"                e./ / / / f.0.J J J J J J J J J J J J J J J J J J J J J J g.. h./ / / i.j.  k.      ",
"              . < / / / / l.m.J J J J J J J J J J J J J J J J J J J J J J n._ / / / o.p.q.  .       ",
"              } | / / / ^ r.w J J J J J J J J J J J J J J J J J J J J J s.. t./ / / u.v.  w..       ",
"            . 3 / / / / x.Y J J J J J J J J J J J J J J J J J J J J J y.Q _./ / / / z.O   A..       ",
"            . B./ / / / C.D.J J J J J J J J J J J J J J J J J J J J 6.E.1 F./ / / / G.H.  I.        ",
"            J./ / / / / K.L.J J J J J J J J J J J J J J J J J J v M.. ; N./ / / / O..   q..         ",
"          . P./ / / / Q.. R.J J J J J J J J J J J J J J J R S.T.. U.V./ / / / / / W.X.  j..         ",
"          . e / / / / Y.Z.J J J J J J J J J J J J J `. +.+++. @+#+$./ / / / / / / G $+  %+          ",
"          &+/ / / / / { *+J J J J J J J J J =+-+;+>+. . ,+'+)+/ / / / / / / / / / !+~+  .           ",
"        . {+/ / / / / ... R.J J J J J =+9.]+. . ^+/+(+_+/ / / / / / / / / / / / :+;.  <+.           ",
"        } $./ / / / / / [+*.}+|+5.1+Y . . # , h./ / / / / / / / / / / / / / / / 4.2+  :..           ",
"      . 3 / / / / / / / { @+. . . 3+4+5+e / / / / / / / / / / / / / / / / / / / 6+7+  8+            ",
"      . ~ / / / / / / / / $.u.< 9+$./ / / / / / / / / / / / / / / / / / / / / 0+.   a+.             ",
"      P / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / b+%   @..             ",
"    . 4./ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / c+=.  d+              ",
"    . e+/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / f+g+  .               ",
"    h+/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / i+j+  k+.               ",
"  . l+/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 5+m+  n+.               ",
"  o+..p+..'.E h.h.h.h.h.h.h.h.h.h.h.h.h.h.h.h.h.h.h.h.h.h.'.0+$.F./ / / / / $ q+  r+                ",
". . . . . . . . . . . . . . . (.s+t+u+v+v+v+v+v+v+v+v+v+v+v+v+v+w+x+y+z+A+B+.   C+.                 ",
". D+E+E+E+E+E+E+E+E+E+E+E+F+G+_.H+I+J+K+K+K+K+K+K+K+K+K+K+K+K+K++.|.L+v.M+N+O+  P+.                 ",
". ! Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+R+S+  *                   ",
". E+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+R+S+  .                   ",
". E+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+R+S+k+.                   ",
"  E+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+R+S+T+.                   ",
"  E+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+R+S+U+                    ",
"  E+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+R+V+.                     ",
"  E+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+R+. .                     ",
"  W+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+Q+R+.                       ",
"  . X+Y+r.Z+`+K+K+K+K+K+K+K+K+K+K+K+K+K+K+K+K+K+K+ @G =..@+@@@5+E+E+E+E+E+#@.                       ",
"  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                       "};
"""

class Pocket2DCut(Cut):
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName
		ViewPocket2DCut(obj.ViewObject)
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
		
		self.updateActionLabel("Getting Boundaries for " + obj.CutName)
		polys = self.getPolysAtSlice(obj.ObjectToCut,"XY",self.parent.ZOriginValue.Value - obj.PerimeterDepth.Value)
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
			
