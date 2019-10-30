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
import CutGui
from Cut import Cut
from RegistrationCut import RegistrationCut
from DrillCut import DrillCut
from FaceCut import FaceCut
from PerimeterCut import PerimeterCut
from Pocket2DCut import Pocket2DCut
from Volume2DCut import Volume2DCut
import os
import validator as VAL

class ViewGCode:
	def __init__(self,obj):
		obj.Proxy = self
		
	def attach(self,obj):
		return
		
	def getDefaultDisplayMode(self):
		return 'Shaded'
		
	def getIcon(self):
		return """
           /* XPM */
static char * cnc_xpm[] = {
"25 25 100 2",
"  	c None",
". 	c #E7E7E7",
"+ 	c #E8E8E8",
"@ 	c #C0C0C0",
"# 	c #313131",
"$ 	c #010101",
"% 	c #3E3E3E",
"& 	c #D4D4D4",
"* 	c #E6E6E6",
"= 	c #E5E5E5",
"- 	c #E4E4E4",
"; 	c #E3E3E3",
"> 	c #E9E9E9",
", 	c #EAEAEA",
"' 	c #0D0D0D",
") 	c #676767",
"! 	c #E2E2E2",
"~ 	c #E1E1E1",
"{ 	c #E0E0E0",
"] 	c #DFDFDF",
"^ 	c #EBEBEB",
"/ 	c #020202",
"( 	c #121212",
"_ 	c #C7C7C7",
": 	c #ECECEC",
"< 	c #A8A8A8",
"[ 	c #9C9C9C",
"} 	c #DEDEDE",
"| 	c #DDDDDD",
"1 	c #DCDCDC",
"2 	c #EDEDED",
"3 	c #202020",
"4 	c #484848",
"5 	c #F2F2F2",
"6 	c #F0F0F0",
"7 	c #EFEFEF",
"8 	c #EEEEEE",
"9 	c #DADADA",
"0 	c #D9D9D9",
"a 	c #DBDBDB",
"b 	c #030303",
"c 	c #F5F5F5",
"d 	c #F3F3F3",
"e 	c #131313",
"f 	c #D7D7D7",
"g 	c #D5D5D5",
"h 	c #757575",
"i 	c #919191",
"j 	c #F8F8F8",
"k 	c #7A7A7A",
"l 	c #D2D2D2",
"m 	c #161616",
"n 	c #C8C8C8",
"o 	c #C6C6C6",
"p 	c #C4C4C4",
"q 	c #C3C3C3",
"r 	c #565656",
"s 	c #AEAEAE",
"t 	c #B8B8B8",
"u 	c #B7B7B7",
"v 	c #B5B5B5",
"w 	c #B3B3B3",
"x 	c #373737",
"y 	c #363636",
"z 	c #353535",
"A 	c #181818",
"B 	c #2F2F2F",
"C 	c #303030",
"D 	c #D8D8D8",
"E 	c #6A6A6A",
"F 	c #D3D3D3",
"G 	c #1C1C1C",
"H 	c #6C6C6C",
"I 	c #5C5C5C",
"J 	c #A1A1A1",
"K 	c #6D6D6D",
"L 	c #ABABAB",
"M 	c #424242",
"N 	c #727272",
"O 	c #3A3A3A",
"P 	c #888888",
"Q 	c #AAAAAA",
"R 	c #616161",
"S 	c #646464",
"T 	c #070707",
"U 	c #B9B9B9",
"V 	c #0A0A0A",
"W 	c #0B0B0B",
"X 	c #F7F7F7",
"Y 	c #8F8F8F",
"Z 	c #F4F4F4",
"` 	c #D6D6D6",
" .	c #696969",
"..	c #F1F1F1",
"+.	c #444444",
"@.	c #A9A9A9",
"#.	c #050505",
"$.	c #414141",
"%.	c #0F0F0F",
"&.	c #717171",
". . + + @ # $ $ $ $ % & * = = = - - - ; ; ; ; ; ; ",
"> , . ' $ $ $ $ $ $ $ $ ) = - ; ; ! ~ ~ { { ] { ~ ",
"^ ^ / $ ( _ : ^ , > < $ $ [ - ; ! { ] } | 1 1 | } ",
"2 3 $ 4 5 6 7 8 : ^ > 9 $ $ ; ~ { ] | 1 9 0 0 9 a ",
"+ $ b c c d 5 6 8 : , + e $ { ~ ] | a 0 f g g f 0 ",
"h $ i j j $ e 5 6 8 ^ k $ $ $ 9 } 1 0 f $ $ l & f ",
"m $ c j j $ / n o p q r $ $ $ s t u v w $ $ l & f ",
"$ $ d c c $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ g f 0 ",
"$ $ 6 5 5 $ $ x y y z A $ $ $ B # # # C $ $ D 9 a ",
"/ $ 2 8 8 $ / ^ , > + E $ $ $ F ! ~ ] } $ $ 1 | } ",
"G $ + ^ ^ $ / > > + . H $ $ $ F ; ! ~ ~ $ $ ] { ~ ",
"I $ J + + $ / . . . * K $ $ $ & = - - - $ $ ; ; ; ",
"L $ M - = $ / = = = = N $ $ $ f = = = * $ $ * * * ",
"; $ / ~ ~ $ / ; ; ; - = O $ P . . . + > $ $ > > > ",
"~ $ $ 9 } $ / { ~ ! ; - q Q 9 . + > , ^ $ $ : : ^ ",
"] R $ S a $ / } { ~ ! ; = * . > , ^ : 8 $ $ 6 7 8 ",
"1 g $ / f $ / 1 } ] ~ ; - * . > ^ : 8 6 $ $ d 5 6 ",
"9 D T $ U $ $ V V W W W W W W W W W W W $ $ X c d ",
"0 f Y $ W $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ X X Z ",
"9 D ` $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ M c d ",
"1 9 D  .$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ ..6 ",
"} | 1 b $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ +.8 ",
"~ { @.$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ ^ ",
"; ! #.$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $.",
"- - %.$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ &."};
           """
	
class GCodeProject():
	def __init__(self):
		self.jobList = []
		self.defineJobUi = FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + '/resources/ui/createjob.ui')
		self.AYS = FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + '/resources/ui/AreYouSure.ui')
		ui = self.defineJobUi
		ui.logoL.setPixmap(QtGui.QPixmap(os.path.dirname(__file__) + "/resources/ui/logo side by side.png"))				
		ui.buttonBox.accepted.connect(self.accept)
		ui.buttonBox.rejected.connect(self.reject)
		ui.buttonBox.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.apply)
		ui.nameLE.textChanged.connect(self.validateAllFields)
		ui.toolTableCB.currentIndexChanged.connect(self.validateAllFields)
		ui.workpieceCB.currentIndexChanged.connect(self.validateAllFields)
		ui.xaxisCB.currentIndexChanged.connect(self.validateAllFields)
		ui.xaxisLE.textChanged.connect(self.validateAllFields)
		ui.yaxisCB.currentIndexChanged.connect(self.validateAllFields)
		ui.yaxisLE.textChanged.connect(self.validateAllFields)
		ui.zaxisCB.currentIndexChanged.connect(self.validateAllFields)
		ui.zaxisLE.textChanged.connect(self.validateAllFields)
		
		ui.tableWidget.itemSelectionChanged.connect(self.validateAllFields)
		ui.addB.clicked.connect(self.addCut)
		ui.editB.clicked.connect(self.editCut)
		ui.deleteB.clicked.connect(self.deleteCut)
		ui.upB.clicked.connect(self.moveUp)
		ui.downB.clicked.connect(self.moveDown)
		ui.skipB.clicked.connect(self.toggleSkip)
		ui.metricRB.clicked.connect(self.validateAllFields)
		ui.imperialRB.clicked.connect(self.validateAllFields)
		ui.outFileB.clicked.connect(self.setOutputFile)
		ui.runB.clicked.connect(self.run)
		
		self.selectedObject = None
		self.waitingOnCutGui = False
		self.cutList = []
		self.outputState = 'Idle'
		CutGui.setGUIMode('None')
		self.origin = (0,0,0)
		self.dirty = False
		
	def GetResources(self):
		return {'Pixmap'  : os.path.dirname(__file__) + '/resources/svg/cnc.svg', # the name of a svg file available in the resources
                'MenuText': "New GCode Project",
                'ToolTip' : "Sets up a new project for creating G-Code paths from FreeCAD Shapes"}

	def setUnits(self):
		ui = self.defineJobUi
		if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema") in [0, 1, 4, 6]:
			self.units = 'mm'
			ui.unitsLabel.setText("Default units are mm, mm/min, and rpm")
		else:
			ui.unitsLabel.setText("Default units are in, in/min, and rpm")
			self.units = 'in'
		
	def reset(self):
		ui = self.defineJobUi
		ui.nameLE.setText("")
		ui.toolTableCB.setCurrentIndex(0)
		ui.workpieceCB.setCurrentIndex(0)
		ui.xaxisCB.setCurrentIndex(0)
		ui.yaxisCB.setCurrentIndex(0)
		ui.zaxisCB.setCurrentIndex(0)
		ui.xaxisLE.setText("")
		ui.yaxisLE.setText("")
		ui.zaxisLE.setText("")
		self.cutList = []
		while ui.tableWidget.rowCount() > 0: ui.tableWidget.removeRow(0)
		ui.metricRB.setChecked(False)
		ui.imperialRB.setChecked(False)
		ui.outFileL.setText('None Selected...')
			
	def deleteCut(self):
		table = self.defineJobUi.tableWidget
		item = table.selectedItems()[0]
		row = table.row(item)
		self.AYS.questionLabel.setText('Deleting "' + table.item(row,2).text() + '"\nClick Cancel to abort')
		if self.AYS.exec_() == QtGui.QDialog.Rejected: return
		table.removeRow(row)
		self.cutList.pop(row)
		self.dirty = True
	
	def editCut(self):
		ui = self.defineJobUi
		CutGui.setGUIMode("EditingCutFromGUI")
		props = self.cutList[ui.tableWidget.currentRow()]
		props.append(["App::PropertyString", "ToolTable", ui.toolTableCB.currentText()])
		CutGui.setGUIProperties(props)
		FreeCADGui.runCommand('New_Cut')
		self.waitingOnCutGui = True
		self.validateAllFields()
	
	def addCut(self):
		ui = self.defineJobUi
		CutGui.setGUIMode("AddingCutFromGUI")
		props = [["App::PropertyString", "ToolTable", ui.toolTableCB.currentText()]]
		CutGui.setGUIProperties(props)
		FreeCADGui.runCommand('New_Cut')
		self.waitingOnCutGui = True
		self.validateAllFields()
		
	def moveUp(self):
		table = self.defineJobUi.tableWidget
		item = table.selectedItems()[0]
		row = table.row(item)
		cutType = table.takeItem(row,0)
		toolNumber = table.takeItem(row,1)
		cutName = table.takeItem(row,2)
		table.removeRow(row)
		table.insertRow(row-1)
		table.setItem(row-1,0,cutType)
		table.setItem(row-1,1,toolNumber)
		table.setItem(row-1,2,cutName)
		table.item(row-1,0).setSelected(True)
		cut = self.cutList.pop(row)
		self.cutList.insert(row-1,cut)
	
	def moveDown(self):
		table = self.defineJobUi.tableWidget
		item = table.selectedItems()[0]
		row = table.row(item)
		cutType = table.takeItem(row,0)
		toolNumber = table.takeItem(row,1)
		cutName = table.takeItem(row,2)
		table.removeRow(row)
		table.insertRow(row+1)
		table.setItem(row+1,0,cutType)
		table.setItem(row+1,1,toolNumber)
		table.setItem(row+1,2,cutName)
		table.item(row+1,0).setSelected(True)
		cut = self.cutList.pop(row)
		self.cutList.insert(row+1,cut)
		
	def selectedRows(self):
		ui = self.defineJobUi
		rows = []
		for i in ui.tableWidget.selectedItems():
			if i.row() not in rows: rows.append(i.row())
		return rows
		
	def toggleSkip(self):
		ui = self.defineJobUi
		row = self.selectedRows()[0]
		item = ui.tableWidget.item(row,0)
		if item.foreground() == QtCore.Qt.gray: color = QtCore.Qt.black
		else: color = QtCore.Qt.gray
		for col in range(3): ui.tableWidget.item(row,col).setForeground(color)
		
	def setOutputFile(self):
		ui = self.defineJobUi
		filename = QtGui.QFileDialog.getSaveFileName(caption='Select output file')[0]
		if filename != "": ui.outFileL.setText(filename)
		self.validateAllFields()

	def writeGCodeLine(self,line):
		ui = self.defineJobUi
		self.fp.write(line + '\n')
		try:
			lc = int(ui.lcL.text())
		except:
			lc = 0
		ui.lcL.setText(str(lc + 1))		
	
	def run(self):
		ui = self.defineJobUi
		ui.lcL.setText("")
		outFile = ui.outFileL.text()
		obj = self.selectedObject
		if os.path.exists(outFile) == True:
			self.AYS.questionLabel.setText('Overwriting "' + outFile + '"\nClick Cancel to abort')
			if self.AYS.exec_() == QtGui.QDialog.Rejected: return
		try:
			self.fp = open(ui.outFileL.text(),'w+')
			self.outputState = "Running"
		except:
			ui.actionLabel.setText("failed to open " + ui.outFileL.text() + " for writing")
			self.outputState = "Idle"
			return
		origin = [obj.XOriginValue,obj.YOriginValue,obj.ZOriginValue]
		if ui.metricRB.isChecked() == True:
			outputUnits = 'METRIC'
			self.writeGCodeLine("G21")
		else:
			outputUnits = 'IMPERIAL'
			self.writeGCodeLine("G20")
		for i in range(len(self.cutList)):
			if ui.tableWidget.item(i,0).foreground() == QtCore.Qt.gray: continue			
			for prop in self.cutList[i]:
				if prop[1] == 'CutName': name = prop[2]
			cut = FreeCAD.ActiveDocument.getObjectsByLabel(name)[0]
			ui.cutNameL.setText(cut.CutName)
			FreeCADGui.updateGui()
			cut.Proxy.run(ui,cut,outputUnits,self.fp)
			ui.cutNameL.clear()
			ui.actionL.clear()
		self.writeGCodeLine("M2")
		self.writeGCodeLine("%")
		self.fp.close()
		ui.actionL.setText("All cuts completed")
		FreeCADGui.updateGui()
		self.outputState = "Idle"
		self.validateAllFields()
		
	def processCutGUIResult(self):
		ui = self.defineJobUi
		self.waitingOnCutGui = False
		mode = CutGui.getGUIMode()
		if mode == "AddingCutFromGUI":
			props = CutGui.getGUIProperties()
			self.cutList.append(props)
			row = ui.tableWidget.rowCount()
			ui.tableWidget.insertRow(row)
			for prop in props:
				if prop[1] == 'CutType': ui.tableWidget.setItem(row,0,QtGui.QTableWidgetItem(prop[2]))
				elif prop[1] == 'ToolNumber': ui.tableWidget.setItem(row,1,QtGui.QTableWidgetItem(str(prop[2])))
				elif prop[1] == 'CutName': ui.tableWidget.setItem(row,2,QtGui.QTableWidgetItem(prop[2]))
		elif mode == "EditingCutFromGUI":
			props = CutGui.getGUIProperties()
			row = ui.tableWidget.currentRow()
			self.cutList[row] = props
			for prop in props:
				if prop[1] == 'CutType': ui.tableWidget.setItem(row,0,QtGui.QTableWidgetItem(prop[2]))
				elif prop[1] == 'ToolNumber': ui.tableWidget.setItem(row,1,QtGui.QTableWidgetItem(str(prop[2])))
				elif prop[1] == 'CutName': ui.tableWidget.setItem(row,2,QtGui.QTableWidgetItem(prop[2]))
			self.validateAllFields()
		self.dirty = True
		CutGui.setGUIMode('None')
							    
	def setAxis(self,axis):
		ui = self.defineJobUi		
		wpcb = ui.workpieceCB
		if axis == 'x':
			cb = ui.xaxisCB
			le = ui.xaxisLE
		elif axis == 'y':
			cb = ui.yaxisCB
			le = ui.yaxisLE
		else:
			cb = ui.zaxisCB
			le = ui.zaxisLE
		if wpcb.currentIndex() <= 0:
			cb.setEnabled(False)
			le.setEnabled(False)
		elif cb.currentText() == 'None Selected...':
			le.setText("")
			le.setEnabled(False)
			cb.setEnabled(True)
		else:
			cb.setEnabled(True)
			sel = cb.currentText()
			if sel == 'Custom': le.setEnabled(True)
			else: le.setEnabled(False)
			obj = FreeCAD.ActiveDocument.getObjectsByLabel(wpcb.currentText())[0]
			box = obj.Shape.BoundBox
			if axis == 'x':
				if sel == 'Left': le.setText(VAL.fromSystemValue('length',0))
				elif sel == 'Middle': le.setText(VAL.fromSystemValue('length',(box.XMax - box.XMin) / 2.))
				elif sel == 'Right': le.setText(VAL.fromSystemValue('length',box.XMax - box.XMin))
			elif axis == 'y':
				if sel == 'Front': le.setText(VAL.fromSystemValue('length',0))
				elif sel == 'Middle': le.setText(VAL.fromSystemValue('length',(box.YMax - box.YMin) / 2.))
				elif sel == 'Back': le.setText(VAL.fromSystemValue('length',box.YMax - box.YMin))
			elif axis == 'z':
				if sel == 'Top': le.setText(VAL.fromSystemValue('length',box.ZMax - box.ZMin))
				elif sel == 'Middle': le.setText(VAL.fromSystemValue('length',(box.ZMax - box.ZMin) / 2.))
				elif sel == 'Bottom': le.setText(VAL.fromSystemValue('length',0))

	def setButtonStates(self,valid):
		ui = self.defineJobUi
		table = ui.tableWidget
		if valid == True:
			ui.buttonBox.buttons()[0].setEnabled(self.dirty)
			ui.buttonBox.button(QtGui.QDialogButtonBox.Apply).setEnabled(self.dirty)
		else:
			ui.buttonBox.buttons()[0].setEnabled(False)
			ui.buttonBox.button(QtGui.QDialogButtonBox.Apply).setEnabled(False)				
		if ui.toolTableCB.currentIndex() == 0: ui.addB.setEnabled(False)
		else: ui.addB.setEnabled(True)		
		if len(self.selectedRows()) == 1:
			ui.editB.setEnabled(True)
			ui.deleteB.setEnabled(True)
			ui.skipB.setEnabled(True)
			row = self.selectedRows()[0]
			if row == 0: ui.upB.setEnabled(False)
			else: ui.upB.setEnabled(True)
			if row == (table.rowCount() - 1): ui.downB.setEnabled(False)
			else: ui.downB.setEnabled(True)
		else:
			ui.editB.setEnabled(False)
			ui.deleteB.setEnabled(False)
			ui.upB.setEnabled(False)
			ui.downB.setEnabled(False)
			ui.skipB.setEnabled(False)
		if ui.outFileL.text() == 'No File Selected...':
			ui.runB.setEnabled(False)
			ui.pauseB.setEnabled(False)
			ui.stopB.setEnabled(False)
		elif self.outputState == 'Idle':
			ui.runB.setEnabled(True)
			ui.pauseB.setEnabled(False)
			ui.stopB.setEnabled(False)
		elif self.outputState == 'Running':
			ui.runB.setEnabled(False)
			ui.pauseB.setEnabled(True)
			ui.stopB.setEnabled(True)
		elif self.outPutState == "Paused":
			self.runB.setEnabled(True)
			self.pauseB.setEnabled(False)
			self.stopB.setEnabled(True)
	
	def validateAllFields(self):
		ui = self.defineJobUi
		valid = True
		if ui.nameLE.text().strip() == "": valid = False
		else:
			try:
				sameName = FreeCAD.ActiveDocument.getObjectsByLabel(ui.nameLE.text().strip())
				if len(sameName) == 0: pass
				elif len(sameName) > 1: valid = False
				elif self.selectedObject in sameName: pass
				else: valid = False		
			except:
				pass
		if valid == True: VAL.setLabel(ui.nameLabel,'VALID')
		else: VAL.setLabel(ui.nameLabel,'INVALID')
		
		if ui.toolTableCB.currentIndex() == 0:
			VAL.setLabel(ui.toolTableL,'INVALID')
			valid = False
		else: VAL.setLabel(ui.toolTableL,'VALID')		
		
		if ui.workpieceCB.currentIndex() == 0:
			VAL.setLabel(ui.workpieceL,'INVALID')
			valid = False
		else:
			VAL.setLabel(ui.workpieceL,'VALID')
		self.setAxis('x')		
		self.setAxis('y')		
		self.setAxis('z')
		if ui.xaxisCB.currentText() == 'None Selected...' or (ui.xaxisCB.currentText() == 'Custom' and ui.xaxisLE.text() == ''):
			VAL.setLabel(ui.xaxisL,'INVALID')
			valid = False
		else:
			VAL.setLabel(ui.xaxisL,'VALID')
		if ui.yaxisCB.currentText() == 'None Selected...' or (ui.yaxisCB.currentText() == 'Custom' and ui.yaxisLE.text() == ''):
			VAL.setLabel(ui.yaxisL,'INVALID')
			valid = False
		else:
			VAL.setLabel(ui.yaxisL,'VALID')
		if ui.zaxisCB.currentText() == 'None Selected...' or (ui.zaxisCB.currentText() == 'Custom' and ui.zaxisLE.text() == ''):
			VAL.setLabel(ui.zaxisL,'INVALID')
			valid = False
		else:
			VAL.setLabel(ui.zaxisL,'VALID')
		if ui.metricRB.isChecked() == False and ui.imperialRB.isChecked() == False:
			VAL.setLabel(ui.outputUnitsL,'INVALID')
			valid = False
		else:
			VAL.setLabel(ui.outputUnitsL, 'VALID')
		
		self.setButtonStates(valid)
		ui.runB.setEnabled(False)
		self.dirty = True
		return valid
		
	def getPropertiesFromCut(self,cut):
		p = []
		S = "App::PropertyString"
		I = "App::PropertyInteger"
		L = "App::PropertyLength"
		A = "App::PropertyAngle"
		V = "App::PropertySpeed"
		Q = "App::PropertyQuantity"
		VL = "App::PropertyVectorList"	
		p = [[S,		"ObjectType",	cut.ObjectType],
			 [S,		"CutName",		cut.CutName],
			 [S,		"Tool",			cut.Tool],
			 [I,		"ToolNumber",	cut.ToolNumber],
			 [S,		"CutType",		cut.CutType],
			 [L,		"SafeHeight",	cut.SafeHeight],
			 [S,		"SpindleSpeed",	cut.SpindleSpeed],			 
			 [V,		"PlungeRate",	cut.PlungeRate],
			 [L,		"XToolChangeLocation", cut.XToolChangeLocation],
			 [L,		"YToolChangeLocation", cut.YToolChangeLocation],
			 [L,		"ZToolChangeLocation", cut.ZToolChangeLocation]]
		if hasattr(cut, "FeedRate"):	p.append([V,		"FeedRate",		cut.FeedRate])
		if hasattr(cut, "DrillDepth"):	p.append([L,		"DrillDepth",	cut.DrillDepth])
		if hasattr(cut, "PeckDepth"):	p.append([L,		"PeckDepth",	cut.PeckDepth])
		if hasattr(cut,	"FirstX"):		p.append([L,		"FirstX",		cut.FirstX])
		if hasattr(cut,	"SecondX"):		p.append([L,		"SecondX",		cut.SecondX])
		if hasattr(cut,	"FirstY"):		p.append([L,		"FirstY",		cut.FirstY])
		if hasattr(cut,	"SecondY"):		p.append([L,		"SecondY",		cut.SecondY])
		if hasattr(cut, "RegistrationAxis"): p.append([S,	"RegistrationAxis",cut.RegistrationAxis])
		if hasattr(cut, "DrillPointList"): p.append([VL,	"DrillPointList", cut.DrillPointList])
		if hasattr(cut, "FacingPattern"): p.append([S,		"FacingPattern", cut.FacingPattern])
		if hasattr(cut,	"CutArea"):		p.append([S,		"CutArea",		cut.CutArea])
		if hasattr(cut, "StartHeight"):  p.append([L,		"StartHeight",	cut.StartHeight])
		if hasattr(cut, "Depth"):		p.append([L,		"Depth",		cut.Depth])
		if hasattr(cut, "StepOver"):	p.append([L,		"StepOver",		cut.StepOver])
		if hasattr(cut, "StepDown"):	p.append([L,		"StepDown",		cut.StepDown])
		if hasattr(cut, "MillingMethod"): p.append([S,		"MillingMethod", cut.MillingMethod])
		if hasattr(cut, "DepthOfCut"):	p.append([L,		"DepthOfCut",	cut.DepthOfCut])
		if hasattr(cut, "WidthOfCut"):	p.append([L,		"WidthOfCut",	cut.WidthOfCut])
		if hasattr(cut, "Offset"):		p.append([L,		"Offset",		cut.Offset])
		if hasattr(cut, "Side"):		p.append([S,		"Side",			cut.Side])
		if hasattr(cut,	"ObjectToCut"): p.append([S,		"ObjectToCut",	cut.ObjectToCut])
		if hasattr(cut, "MaximumError"): p.append([L,		"MaximumError", cut.MaximumError])
		if hasattr(cut, "PerimeterDepth"): p.append([L,		"PerimeterDepth", cut.PerimeterDepth])
		if hasattr(cut, "OffsetFromPerimeter"): p.append([L,"OffsetFromPerimeter", cut.OffsetFromPerimeter])
		
		return p

	def Activated(self):
		self.setUnits()
		ui = self.defineJobUi
		self.reset()
		ui.toolTableCB.clear()
		ui.toolTableCB.addItem('None Selected...')
		ui.toolTableCB.setCurrentIndex(0)
		if hasattr(FreeCAD.ActiveDocument,"Objects"):
			for obj in FreeCAD.ActiveDocument.Objects:
				if hasattr(obj,"ObjectType") == True:
					if obj.ObjectType == "ToolTable":
						ui.toolTableCB.addItem(obj.Label)
		ui.workpieceCB.clear()
		ui.workpieceCB.addItem("None Selected...")
		ui.workpieceCB.setCurrentIndex(0)	
		if hasattr(FreeCAD.ActiveDocument,"Objects"):
			for obj in FreeCAD.ActiveDocument.Objects:
				if hasattr(obj,"Shape"):
					ui.workpieceCB.addItem(obj.Label)
		self.cutList = []
		if self.selectedObject != None:
			ui.nameLE.setText(self.selectedObject.Label)
			if hasattr(self.selectedObject,'ToolTable') == True:
				index = ui.toolTableCB.findText(self.selectedObject.ToolTable)
				if index > 0: ui.toolTableCB.setCurrentIndex(index)
			if hasattr(self.selectedObject,'WorkPiece') == True:
				index = ui.workpieceCB.findText(self.selectedObject.WorkPiece)
				if index > 0: ui.workpieceCB.setCurrentIndex(index)
			ui.xaxisCB.setCurrentIndex(ui.xaxisCB.findText(self.selectedObject.XOrigin))
			ui.xaxisLE.setText(VAL.fromSystemValue('length',self.selectedObject.XOriginValue))
			ui.yaxisCB.setCurrentIndex(ui.yaxisCB.findText(self.selectedObject.YOrigin))
			ui.yaxisLE.setText(VAL.fromSystemValue('length',self.selectedObject.YOriginValue))
			ui.zaxisCB.setCurrentIndex(ui.zaxisCB.findText(self.selectedObject.ZOrigin))
			ui.zaxisLE.setText(VAL.fromSystemValue('length',self.selectedObject.ZOriginValue))
			while ui.tableWidget.rowCount() > 0: ui.tableWidget.removeRow(0)
			for cut in self.selectedObject.Group:
				props = self.getPropertiesFromCut(cut)
				for prop in props:
					if prop[1] == "CutType": cutType = prop[2]
					if prop[1] == "ToolNumber": toolNumber = prop[2]
					if prop[1] == "CutName": name = prop[2]
				row = ui.tableWidget.rowCount()
				ui.tableWidget.insertRow(row)
				ui.tableWidget.setItem(row,0,QtGui.QTableWidgetItem(cutType))
				ui.tableWidget.setItem(row,1,QtGui.QTableWidgetItem(str(toolNumber)))
				ui.tableWidget.setItem(row,2,QtGui.QTableWidgetItem(name))
				self.cutList.append(props)
			if self.selectedObject.OutputUnits == 'METRIC': ui.metricRB.setChecked(True)
			else: ui.imperialRB.setChecked(True)
			ui.outFileL.setText(self.selectedObject.OutputFile)

		if self.validateAllFields() == True: ui.runB.setEnabled(True)
		else: ui.runB.setEnabled(False)
		ui.show()     
		return
		
	def accept(self):
		ui = self.defineJobUi
		ui.hide()
		self.apply()
		FreeCAD.ActiveDocument.recompute()
		return True
		
	def reject(self):
		self.defineJobUi.hide()
		return False

	def apply(self):
		ui = self.defineJobUi
		if self.selectedObject == None:
			obj = FreeCAD.ActiveDocument.addObject('App::DocumentObjectGroupPython', "GCodeJob")
			ViewGCode(obj.ViewObject)
			self.selectedObject = obj
		obj = self.selectedObject
		obj.Label = ui.nameLE.text()
		if hasattr(obj,"ObjectType") == False: obj.addProperty("App::PropertyString","ObjectType").ObjectType = "GCodeJob"
		if hasattr(obj, 'ToolTable') == False: obj.addProperty("App::PropertyString","ToolTable")
		obj.ToolTable = ui.toolTableCB.currentText()
		if hasattr(obj, 'WorkPiece') == False: obj.addProperty("App::PropertyString","WorkPiece")
		obj.WorkPiece = ui.workpieceCB.currentText()
		if hasattr(obj, 'XOrigin') == False: obj.addProperty("App::PropertyString","XOrigin")
		obj.XOrigin = ui.xaxisCB.currentText()
		if hasattr(obj, 'XOriginValue') == False: obj.addProperty("App::PropertyLength","XOriginValue")
		obj.XOriginValue = VAL.toSystemValue(ui.xaxisLE,'length')
		if hasattr(obj, 'YOrigin') == False: obj.addProperty("App::PropertyString","YOrigin")
		obj.YOrigin = ui.yaxisCB.currentText()
		if hasattr(obj, 'YOriginValue') == False: obj.addProperty("App::PropertyLength","YOriginValue")
		obj.YOriginValue = VAL.toSystemValue(ui.yaxisLE, 'length')
		if hasattr(obj, 'ZOrigin') == False: obj.addProperty("App::PropertyString","ZOrigin")
		obj.ZOrigin = ui.zaxisCB.currentText()
		if hasattr(obj, 'ZOriginValue') == False: obj.addProperty("App::PropertyLength","ZOriginValue")
		obj.ZOriginValue = VAL.toSystemValue(ui.zaxisLE,'length')
		for cut in obj.Group:
			FreeCAD.ActiveDocument.removeObject(cut.Name)
		for line in self.cutList:
			for prop in line:
				if prop[1] == "CutType":
					if prop[2] == "Registration": cut = RegistrationCut(obj)
					elif prop[2] == "Drill": cut = DrillCut(obj)
					elif prop[2] == "Facing": cut = FaceCut(obj)
					elif prop[2] == "Perimeter": cut = PerimeterCut(obj)
					elif prop[2] == "Pocket2D": cut = Pocket2DCut(obj)
					elif prop[2] == "Volume2D": cut = Volume2DCut(obj)
					else: cut = Cut(obj)
			cut.getObject().Label = ui.nameLE.text()
			cut.setProperties(line,cut.getObject())
		if hasattr(obj,"OutputUnits") == False: obj.addProperty("App::PropertyString","OutputUnits")
		if ui.metricRB.isChecked() == True: obj.OutputUnits = 'METRIC'
		else: obj.OutputUnits = 'IMPERIAL'
		if hasattr(obj,"OutputFile") == False: obj.addProperty("App::PropertyString","OutputFile")
		obj.OutputFile = ui.outFileL.text()
		self.dirty = False
		ui.runB.setEnabled(True)		

	def IsActive(self):
		if self.waitingOnCutGui == True:
			if CutGui.getStatus() == 'hidden': self.processCutGUIResult()
		mw = FreeCADGui.getMainWindow()
		tree = mw.findChildren(QtGui.QTreeWidget)[0]
		if len(tree.selectedItems()) != 1:
			self.selectedObject = None
		else:
			item = tree.selectedItems()[0]
			obj = FreeCAD.ActiveDocument.getObjectsByLabel(item.text(0))[0]
			if obj.ObjectType == "GCodeJob":
				self.selectedObject = obj
			else: self.selectedObject = None			
		return True

FreeCADGui.addCommand('New_Project',GCodeProject())
