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

class ViewVolume3DCut(ViewCut):
	def getIcon(self):
		return """
/* XPM */
static char * volume3D_xpm[] = {
"50 41 193 2",
"  	c None",
". 	c #000000",
"+ 	c #005300",
"@ 	c #008200",
"# 	c #009B00",
"$ 	c #009E00",
"% 	c #005000",
"& 	c #007500",
"* 	c #01DD00",
"= 	c #01FF00",
"- 	c #01FA00",
"; 	c #008700",
"> 	c #00A800",
", 	c #01FB00",
"' 	c #007100",
") 	c #01E800",
"! 	c #006900",
"~ 	c #00A300",
"{ 	c #01DF00",
"] 	c #01EE00",
"^ 	c #000900",
"/ 	c #009100",
"( 	c #00A100",
"_ 	c #01E400",
": 	c #008500",
"< 	c #007B00",
"[ 	c #01D100",
"} 	c #01CA00",
"| 	c #004200",
"1 	c #01F800",
"2 	c #003600",
"3 	c #00A600",
"4 	c #009C00",
"5 	c #01DC00",
"6 	c #004800",
"7 	c #01FE00",
"8 	c #003200",
"9 	c #004B00",
"0 	c #009D00",
"a 	c #00B400",
"b 	c #007700",
"c 	c #008C00",
"d 	c #006800",
"e 	c #010000",
"f 	c #004000",
"g 	c #008D00",
"h 	c #01D600",
"i 	c #01E900",
"j 	c #007400",
"k 	c #00B000",
"l 	c #009300",
"m 	c #000D00",
"n 	c #714D41",
"o 	c #583C32",
"p 	c #002200",
"q 	c #009F00",
"r 	c #01F700",
"s 	c #007C00",
"t 	c #002D00",
"u 	c #00AD00",
"v 	c #002400",
"w 	c #593C32",
"x 	c #AB7765",
"y 	c #65453A",
"z 	c #008300",
"A 	c #00AE00",
"B 	c #002700",
"C 	c #008E00",
"D 	c #01C900",
"E 	c #008F00",
"F 	c #004400",
"G 	c #2E1D17",
"H 	c #A47261",
"I 	c #AD7866",
"J 	c #724D41",
"K 	c #004900",
"L 	c #009800",
"M 	c #01C000",
"N 	c #003900",
"O 	c #005900",
"P 	c #8B6051",
"Q 	c #009000",
"R 	c #007900",
"S 	c #01ED00",
"T 	c #00A700",
"U 	c #001A00",
"V 	c #55392F",
"W 	c #634338",
"X 	c #006100",
"Y 	c #00A000",
"Z 	c #007E00",
"` 	c #006E00",
" .	c #996A59",
"..	c #966858",
"+.	c #006600",
"@.	c #01D900",
"#.	c #01EC00",
"$.	c #000200",
"%.	c #5C3E34",
"&.	c #AA7664",
"*.	c #493028",
"=.	c #00AF00",
"-.	c #003A00",
";.	c #003800",
">.	c #01E100",
",.	c #00B200",
"'.	c #002C00",
").	c #000100",
"!.	c #008000",
"~.	c #9A6B5A",
"{.	c #80584A",
"].	c #002900",
"^.	c #000A00",
"/.	c #01BA00",
"(.	c #01F000",
"_.	c #00B100",
":.	c #003D00",
"<.	c #00AA00",
"[.	c #5A3D33",
"}.	c #A37160",
"|.	c #231510",
"1.	c #00A500",
"2.	c #004F00",
"3.	c #01BE00",
"4.	c #008100",
"5.	c #644439",
"6.	c #008800",
"7.	c #003F00",
"8.	c #00A900",
"9.	c #008400",
"0.	c #000300",
"a.	c #002500",
"b.	c #006C00",
"c.	c #009900",
"d.	c #004100",
"e.	c #936656",
"f.	c #005D00",
"g.	c #003C00",
"h.	c #001100",
"i.	c #412B23",
"j.	c #002800",
"k.	c #005400",
"l.	c #7C5548",
"m.	c #009600",
"n.	c #9F6E5D",
"o.	c #A06F5E",
"p.	c #1F120E",
"q.	c #004D00",
"r.	c #724E41",
"s.	c #5F4036",
"t.	c #002E00",
"u.	c #005B00",
"v.	c #005600",
"w.	c #003300",
"x.	c #000E00",
"y.	c #33211A",
"z.	c #A87563",
"A.	c #906354",
"B.	c #6C4A00",
"C.	c #895E00",
"D.	c #8A5F00",
"E.	c #8B6000",
"F.	c #8C6100",
"G.	c #8F6300",
"H.	c #946700",
"I.	c #9B6B00",
"J.	c #9C6C00",
"K.	c #7C5500",
"L.	c #52372D",
"M.	c #39251E",
"N.	c #AD7800",
"O.	c #5B3E34",
"P.	c #775245",
"Q.	c #7F5700",
"R.	c #6E4B3F",
"S.	c #A06E5E",
"T.	c #080403",
"U.	c #724E00",
"V.	c #573A31",
"W.	c #724D00",
"X.	c #34211B",
"Y.	c #5F4000",
"Z.	c #755000",
"`.	c #734E00",
" +	c #714D00",
".+	c #684700",
"++	c #664500",
"@+	c #644400",
"#+	c #5D3F00",
"$+	c #573A00",
"%+	c #533800",
"&+	c #523700",
"*+	c #332100",
"                                                . . . . . .                                         ",
"                                              . . + @ # $ % . .                                     ",
"                                          . . & * = = = = - ; .                                     ",
"                                        . . > , = = = = = = - ' .                                   ",
"                                        . $ = = = = = = = = = ) . .                                 ",
"                                      . ! - = = = = = = = = = = ~ .                                 ",
"                                    . . { = = = = = = = = = = = ] ^ .                               ",
"                                    . / = = = = = = = = = = = = = ( .                               ",
"                                  . . _ = = = = = = = = = = = = = _ . .                             ",
"                                  . : = = = = = = = = = = = = = = = < .                             ",
"                                  . [ = = = = = = = = = = = = = = = } .                             ",
"                                . | , = = = = = = = = = = = = = = = 1 2 .                           ",
"                                . 3 = = = = = = = = = = = = = = = = = 4 .                           ",
"                                . 5 = = = = = = = = = = = = = = = = = 5 .                           ",
"                              . 6 7 = = = = = = = = = = = = = = = = = = + . . . . . . . . . . . .   ",
"                        . 8 9 . 0 = = = = = = = = = = = = = = = = = = = a . b c c c c c c d . e     ",
"                      . f 3 g . h = = = = = = = = = = = = = = = = = = = i . j k k k k k l m n o     ",
"                      p q k d . r = = = = = = = = = = = = = = = = = = = = s t u k k k q v w x y     ",
"                    . z k A B C = = = = = = = = = = = = = = = = = = = = = D . E k k u F G H I J     ",
"                    K A k L . M = = = = = = = = = = = = = = = = = = = = = 1 N O k k < . P I I J .   ",
"                  . Q k k R . S = = = = = = = = = = = = = = = = = = = = = = T . $ ~ U V I I I W .   ",
"                  9 k k k f X = = = = = = = = = = = = = = = = = = = = = = , Y . Z ` .  .I I ...     ",
"                . E k k k +.. @.= = = = = = = = = = = = = = = = = = = = #.R . X ( $.%.I I &.*.      ",
"                F =.k k k T -.;.>.= = = = = = = = = = = = = = = = = r ,.'.).!.k b . ~.I I {..       ",
"              . c k k k k k 4 ].^./.- = = = = = = = = = = = = = (._.:.. % q k <.v [.I I }.|.        ",
"              6 =.k k k k k k 1.2.. % /.) = = = = = = = 7 _ 3.4.. . 9 Q k k k ; .  .I I 5..         ",
"            . / k k k k k k k k =.6.7.. . f s # <.8.9.j 0.. . a.b.c.k k k k k d.w I I e..           ",
"          . X k k k k k k k k k k k k L s f.g.. . . h.2.+.!.L =.k k k k k k Q .  .I &.i.            ",
"          j.3 k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k.%.I I l..             ",
"        . m.k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k L . n.I o.p.              ",
"      . c k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k q.r.I I s..               ",
"  . . t.u.v.k.+ + + + + + + + + + + + + + + + + 6 ;.w.8 a.x.$.. . . . . . y.z.I A..                 ",
"  . B.C.C.C.C.C.C.C.C.C.C.C.C.C.C.C.C.D.D.E.F.G.H.I.J.J.J.J.J.J.J.J.J.J.K.L.I &.M.                  ",
"  . C.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.C.O.I P..                   ",
"  . C.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.Q.R.S.T.                    ",
"  . C.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.U.J V..                     ",
"  . C.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.W.X..                       ",
"  . C.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.N.W..                         ",
"  . Y.Z.`.U.W.W.W.W.W.W.W.W.W.W.W.W.W.W.W. +B..+++@+#+$+%+&+&+&+&+&+&+&+*+.                         ",
"    . . . . . . . . . . . . . . . . . . .                               .                           ",
"                                                                                                    "};
"""

class Volume3DCut(Cut):	
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName
		ViewVolume3DCut(obj.ViewObject)
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
		self.lastSlice = None
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
		
		# subtract object to cut from CutArea
		self.updateActionLabel('making mold by removing ' + obj.ObjectToCut + ' from ' + obj.CutArea)
		mold = self.differenceOfShapes(obj.CutArea, obj.ObjectToCut)
		
		level = obj.StartHeight.Value + self.parent.ZOriginValue.Value
		bottom = round(mold.Shape.BoundBox.ZMin,4) +.0001
		mask = None
		while level >= bottom:
			self.updateActionLabel('getting slice at z = ' + str(level - self.parent.ZOriginValue.Value))
			polys = self.getPolysAtSlice(mold.Name,"XY",level)
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
			if level == bottom: break
			level = level - obj.StepDown.Value
			if level < bottom: level = bottom
		# fc.removeObject(mold.Name)
		return
			
