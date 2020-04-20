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

class ViewPocket3DCut(ViewCut):
	def getIcon(self):
		return """
/* XPM */
static char * pocket3D_xpm[] = {
"50 44 226 2",
"  	c None",
". 	c #000000",
"+ 	c #3C3C3C",
"@ 	c #BCBCBC",
"# 	c #838383",
"$ 	c #3D3D3D",
"% 	c #BBBBBB",
"& 	c #AEAEAE",
"* 	c #A0A0A0",
"= 	c #515151",
"- 	c #1E1E1E",
"; 	c #626262",
"> 	c #5C5C5C",
", 	c #777777",
"' 	c #AAAAAA",
") 	c #5A5A5A",
"! 	c #575757",
"~ 	c #5E7C5E",
"{ 	c #639B63",
"] 	c #67AB67",
"^ 	c #6DBD6D",
"/ 	c #71C071",
"( 	c #74C174",
"_ 	c #7AC67A",
": 	c #82D382",
"< 	c #89D889",
"[ 	c #8FDB8F",
"} 	c #92D692",
"| 	c #8DC58D",
"1 	c #93C693",
"2 	c #8BB18B",
"3 	c #7F987F",
"4 	c #666D66",
"5 	c #717171",
"6 	c #232323",
"7 	c #576D57",
"8 	c #63BB63",
"9 	c #68D068",
"0 	c #6CD26C",
"a 	c #6FD26F",
"b 	c #73D373",
"c 	c #77D577",
"d 	c #7BD67B",
"e 	c #80D880",
"f 	c #85D985",
"g 	c #8ADB8A",
"h 	c #90DD90",
"i 	c #96DE96",
"j 	c #9DE19D",
"k 	c #A5E4A5",
"l 	c #ADE5AD",
"m 	c #B6E8B6",
"n 	c #9AB19A",
"o 	c #606160",
"p 	c #707070",
"q 	c #2C2C2C",
"r 	c #5A615A",
"s 	c #62C462",
"t 	c #65CF65",
"u 	c #A0B2A0",
"v 	c #A9A9A9",
"w 	c #6F6F6F",
"x 	c #5D825D",
"y 	c #62CE62",
"z 	c #676A67",
"A 	c #808080",
"B 	c #737373",
"C 	c #5D8A5D",
"D 	c #60CD60",
"E 	c #64CF64",
"F 	c #66D066",
"G 	c #69D069",
"H 	c #6DD26D",
"I 	c #70D370",
"J 	c #74D474",
"K 	c #78D578",
"L 	c #7CD77C",
"M 	c #82D882",
"N 	c #89DB89",
"O 	c #8FDC8F",
"P 	c #96DF96",
"Q 	c #9EE19E",
"R 	c #A6E3A6",
"S 	c #B1E7B1",
"T 	c #717671",
"U 	c #767676",
"V 	c #9D9D9D",
"W 	c #5C6B5C",
"X 	c #5FCA5F",
"Y 	c #61CE61",
"Z 	c #63CF63",
"` 	c #67D067",
" .	c #6AD16A",
"..	c #70D270",
"+.	c #73D473",
"@.	c #86DA86",
"#.	c #8CDB8C",
"$.	c #93DE93",
"%.	c #9CE19C",
"&.	c #A5E3A5",
"*.	c #B1E6B1",
"=.	c #717771",
"-.	c #898989",
";.	c #B9B9B9",
">.	c #5D965D",
",.	c #646764",
"'.	c #3B3B3B",
").	c #7A7A7A",
"!.	c #869186",
"~.	c #5E915E",
"{.	c #63CB63",
"].	c #819081",
"^.	c #3A3A3A",
"/.	c #5E5E5E",
"(.	c #BCE8BC",
"_.	c #6F986F",
":.	c #5D6A5D",
"<.	c #61A661",
"[.	c #66C966",
"}.	c #94BC94",
"|.	c #6F7C6F",
"1.	c #8CDC8C",
"2.	c #80BD80",
"3.	c #677C67",
"4.	c #608760",
"5.	c #64A364",
"6.	c #6BBB6B",
"7.	c #72D072",
"8.	c #7DCF7D",
"9.	c #7CC27C",
"0.	c #7BB47B",
"a.	c #77A277",
"b.	c #6E886E",
"c.	c #616861",
"d.	c #7E7E7E",
"e.	c #86C186",
"f.	c #729272",
"g.	c #626C62",
"h.	c #636663",
"i.	c #7B857B",
"j.	c #464A46",
"k.	c #757A75",
"l.	c #9B9B9B",
"m.	c #95DE95",
"n.	c #99E099",
"o.	c #9DE09D",
"p.	c #95CE95",
"q.	c #87B187",
"r.	c #7B987B",
"s.	c #799279",
"t.	c #7A917A",
"u.	c #89A589",
"v.	c #90AC90",
"w.	c #A5C4A5",
"x.	c #B9D9B9",
"y.	c #6C7B6C",
"z.	c #727A72",
"A.	c #020202",
"B.	c #505050",
"C.	c #365936",
"D.	c #375937",
"E.	c #4A734A",
"F.	c #537E53",
"G.	c #557F55",
"H.	c #577E57",
"I.	c #597E59",
"J.	c #5A7E5A",
"K.	c #5C7E5C",
"L.	c #5D7D5D",
"M.	c #5F7D5F",
"N.	c #617D61",
"O.	c #657E65",
"P.	c #789278",
"Q.	c #86A086",
"R.	c #637463",
"S.	c #6F7A6F",
"T.	c #313131",
"U.	c #6A6A6A",
"V.	c #535353",
"W.	c #323C32",
"X.	c #0A140A",
"Y.	c #667466",
"Z.	c #B9E7B9",
"`.	c #A1E2A1",
" +	c #AAE4AA",
".+	c #AEE6AE",
"++	c #B3E7B3",
"@+	c #AAD7AA",
"#+	c #9FC59F",
"$+	c #A2C4A2",
"%+	c #8EA98E",
"&+	c #8EA08E",
"*+	c #B8E9B8",
"=+	c #97DE97",
"-+	c #859685",
";+	c #989898",
">+	c #AFE4AF",
",+	c #6E7D6E",
"'+	c #A6A6A6",
")+	c #6D7C6D",
"!+	c #C1C1C1",
"~+	c #202020",
"{+	c #212121",
"]+	c #444444",
"^+	c #B2E5B2",
"/+	c #181818",
"(+	c #3F4B3F",
"_+	c #757B75",
":+	c #525252",
"<+	c #B1E5B1",
"[+	c #465346",
"}+	c #495349",
"|+	c #6D6D6D",
"1+	c #A7E3A7",
"2+	c #8A8A8A",
"3+	c #BBEABB",
"4+	c #BEBEBE",
"5+	c #010101",
"6+	c #555555",
"7+	c #C4C4C4",
"8+	c #3E3E3E",
"9+	c #404040",
"0+	c #7B7B7B",
"a+	c #A8A8A8",
"b+	c #1C1C1C",
"c+	c #323232",
"                                                                                                    ",
"                                                                                    . . . . . . .   ",
"                                    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   ",
"                                  . + @                                                   # . . .   ",
"                                . $     % & & & & & & & & &                             * . = . .   ",
"                              . - ; > > > > > > > > > > > > > > , '                   * . )   . .   ",
"                            . - ! ~ { ] ^ / ( _ : < [ } | 1 2 3 4 > 5               * . )     .     ",
"                          . 6 7 8 9 0 a b c d e f g h i j k l m   n o p           * . )       .     ",
"                        . q r s t 9 0 a b c d e f g h i j k l m     u > v       * . )         .     ",
"                      . ) w x y t 9 0 a b c d e f g h i j k l m       z A     * . )           .     ",
"                    . )   B C D y E F G H I J K L M N O P Q R S       T U   V . )             .     ",
"                . . )     A W X Y Z t `  .0 ..+.c d e @.#.$.%.&.*.    =.U -.. )               .     ",
"              . . w       ;.> >.Y Z t `  .0 ..+.c d e @.#.$.%.&.*.    ,.'.. )                 .     ",
"            . . ).          !.> ~.{.t `  .0 ..+.c d e @.#.$.%.&.*.  ].^.. /.                  .     ",
"          . . ).            (._.> :.<.[. .0 ..+.c d e @.#.$.%.&.}.|.^.. 5                     .     ",
"        . . ).                1.2.3.> > 4.5.6.7.c d 8.9.0.a.b.c.> ^.. ).                      .     ",
"      . . d.                  1.O $.e.f.g.> > > > > > > > > h.i.j.. k.                        .     ",
"    . . l.                    1.O $.m.n.o.p.q.r.s.t.u.v.w.x.  y.. z.                          .     ",
"  . . . . A.+ B.= = = = = = = C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.. S.                            .     ",
"  . T.).U.V.= = = = = = = = = W.X.. . . . . . . . . . . . . . Y.                              .     ",
"  . =                         Z.O $.m.n.o.`.k  +.+++@+#+$+%+. &+                              .     ",
"  . =                           O $.m.n.o.`.k  +.+++*+      . &+                              .     ",
"  . =                           O $.m.n.o.`.k  +.+++*+      . &+                              .     ",
"  . =                           =+$.m.n.o.`.k  +.+++*+      . -+                            ;+.     ",
"  . =                           >+$.m.n.o.`.k  +.+++*+      . ,+                          '+. .     ",
"  . =                             $.m.n.o.`.k  +.+++*+      . )+                        !+~+.       ",
"  . =                             $.m.n.o.`.k  +.+++*+      . )+                        {+.         ",
"  . ]+                            ^+m.n.o.`.k  +.+++*+      A.)+                      $ .           ",
"  . /+                              m.n.o.`.k  +.+++*+      (+_+                    :+.             ",
"  . .                               <+n.o.`.k  +.+++*+      [+).                  ) .               ",
"  . .                                 `.o.`.k  +.+++*+      }+|+                )..                 ",
"  . .                                   1+`.k  +.+++*+      = :+              2+. .                 ",
"  . .                                           3+*+        = =             * . .                   ",
"  . .                                                       = =           4+5+.                     ",
"    .                                                       6+=         7+~+.                       ",
"    .                                                       B =         + .                         ",
"    .                                                       ).=       8+.                           ",
"    .                                                       ).9+    ) .                             ",
"    .                                                       )..   |+.                               ",
"    .                                                       ).. 0+. .                               ",
"    . a+                                                    ).. . .                                 ",
"    . . . . . . . . . . . . . . . . . . 5+b+c+= = = = = = = T.. .                                   ",
"        . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     ",
"                                                                                                    "};
"""

class Pocket3DCut(Cut):	
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName
		ViewPocket3DCut(obj.ViewObject)
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
		
		fc = FreeCAD.ActiveDocument
		
		# Get intersection of workpiece and object to cut
		self.updateActionLabel('making intersection between workpiece and ' + obj.ObjectToCut)
		differenceShape = self.differenceOfShapes(self.parent.WorkPiece,obj.ObjectToCut)		
		level = differenceShape.Shape.BoundBox.ZMax

		mask = None
		while level >= differenceShape.Shape.BoundBox.ZMin:
			self.updateActionLabel('getting slice a z = ' + str(level - self.parent.ZOriginValue.Value))
			polys = self.getPolysAtSlice(differenceShape.Name,"XY",level)
			polys = self.moveOrigin2D(polys)
			if len(polys) == 0: break
			if mask != None:
				polys = self.intersectionOfShapes(mask,polys)
			mask = polys	
			polyList = []
			self.updateActionLabel('Getting offset polygons for z = ' + str(level - self.parent.ZOriginValue.Value))
			offset = obj.OffsetFromPerimeter.Value
			offsetPolys = self.getOffset(polys,-offset)
			while len(offsetPolys) > 0:
				for poly in offsetPolys:
					polyList.append(poly)
				offset = offset + obj.StepOver.Value
				offsetPolys = self.getOffset(polys,-offset)
			self.updateActionLabel('Generating cuts for z = ' + str(level - self.parent.ZOriginValue.Value))
			while len(polyList) > 0:
				self.rapid(z = self.safeHeight)
				poly = self.shortestPoly(polyList)
				self.rapid(poly[0][0],poly[0][1])
				self.cut(z = level - self.parent.ZOriginValue.Value)
				area = self.areaOfPoly(poly)
				reducedPoly = self.smoothePoly(poly)
				if obj.MillingMethod == "Climb": self.cutPolyInsideClimb(reducedPoly)
				else: self.cutPolyInsideConventional(reducedPoly)
				polyList.remove(poly)
				poly = self.nextPoly(poly[0][0],poly[0][1],polyList,self.bitWidth)
				while poly != None:
					length = self.lengthOfPoly(poly)
					lengthTimesWidth = length * obj.StepOver.Value
					if self.areaOfPoly(poly) - lengthTimesWidth > area: break
					reducedPoly = self.smoothePoly(poly)
					if obj.MillingMethod == "Climb": self.cutPolyInsideClimb(reducedPoly)
					else: self.cutPolyInsideConventional(reducedPoly)
					area = self.areaOfPoly(poly)
					polyList.remove(poly)
					poly = self.nextPoly(poly[0][0],poly[0][1],polyList,self.bitWidth)					
			self.rapid(z = self.safeHeight)
			level = level - obj.StepDown.Value
		fc.removeObject(differenceShape.Name)
		return

			
