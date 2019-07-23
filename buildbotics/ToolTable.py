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
import os
import validator as VAL
import ToolGui
from Tool import Tool
import json

class ViewToolTable:
	def __init__(self,obj):
		obj.Proxy = self
		
	def attach(self,obj):
		return
		
	def getDefaultDisplayMode(self):
		return 'Shaded'
		
	def getIcon(self):
		return """
           /* XPM */
static char * tooltable_xpm[] = {
"25 25 124 2",
"  	c None",
". 	c #A0A0A0",
"+ 	c #A1A1A1",
"@ 	c #9F9F9F",
"# 	c #9A9A9A",
"$ 	c #868686",
"% 	c #7D7D7D",
"& 	c #717171",
"* 	c #8F8F8F",
"= 	c #6D6D6D",
"- 	c #5B5B5B",
"; 	c #5E5E5E",
"> 	c #7B7B7B",
", 	c #646464",
"' 	c #666666",
") 	c #797979",
"! 	c #7C7C7C",
"~ 	c #7A7A7A",
"{ 	c #949494",
"] 	c #808080",
"^ 	c #31312F",
"/ 	c #909090",
"( 	c #212120",
"_ 	c #080808",
": 	c #828282",
"< 	c #40403F",
"[ 	c #0C0C0C",
"} 	c #4A4A4A",
"| 	c #848484",
"1 	c #0A0A09",
"2 	c #0D0D0D",
"3 	c #747474",
"4 	c #414141",
"5 	c #0A0A0A",
"6 	c #10100F",
"7 	c #050505",
"8 	c #020202",
"9 	c #353534",
"0 	c #616161",
"a 	c #5B5B59",
"b 	c #585855",
"c 	c #525252",
"d 	c #5C5C5B",
"e 	c #3E3E3C",
"f 	c #4F4F4C",
"g 	c #474746",
"h 	c #545452",
"i 	c #595956",
"j 	c #42423F",
"k 	c #0E0E0D",
"l 	c #393937",
"m 	c #2D2D2C",
"n 	c #6C6C6C",
"o 	c #3F3F3E",
"p 	c #3C3C3A",
"q 	c #767675",
"r 	c #575756",
"s 	c #444442",
"t 	c #555555",
"u 	c #696968",
"v 	c #333332",
"w 	c #373735",
"x 	c #7B7B7A",
"y 	c #5E5E5D",
"z 	c #434340",
"A 	c #363635",
"B 	c #0D0D0C",
"C 	c #0E0E0E",
"D 	c #565653",
"E 	c #1F1F1E",
"F 	c #393938",
"G 	c #313130",
"H 	c #2C2C2B",
"I 	c #4A4A48",
"J 	c #242422",
"K 	c #151514",
"L 	c #2B2B2A",
"M 	c #4A4A47",
"N 	c #161616",
"O 	c #1B1B1A",
"P 	c #262625",
"Q 	c #0B0B0B",
"R 	c #444441",
"S 	c #4E4E4C",
"T 	c #41413F",
"U 	c #50504D",
"V 	c #52524F",
"W 	c #575754",
"X 	c #222222",
"Y 	c #040404",
"Z 	c #090909",
"` 	c #141413",
" .	c #0F0F0E",
"..	c #141414",
"+.	c #101010",
"@.	c #0B0B0A",
"#.	c #151515",
"$.	c #1B1B1B",
"%.	c #4C4C4C",
"&.	c #929292",
"*.	c #979797",
"=.	c #939393",
"-.	c #8E8E8E",
";.	c #707070",
">.	c #6A6A6A",
",.	c #5F5F5F",
"'.	c #696969",
").	c #737373",
"!.	c #606060",
"~.	c #787878",
"{.	c #8D8D8D",
"].	c #969696",
"^.	c #898989",
"/.	c #999999",
"(.	c #7F7F7F",
"_.	c #767676",
":.	c #8B8B8B",
"<.	c #6E6E6E",
"[.	c #5A5A5A",
"}.	c #626262",
"|.	c #6B6B6B",
"1.	c #777777",
"2.	c #989898",
"3.	c #9E9E9E",
"                                                  ",
"              .     .       .     .               ",
"              .     .       +     .               ",
"              .     .       +     .               ",
"              .     @       .     #               ",
"              $     %     & *     =               ",
"              -     ;     > ,     '               ",
"              )     $ !   + ~     { ]             ",
"            ^ / ( _ : < [ } | 1 2 3 4 5 [ 6 7 8   ",
"          [ 9 0 a b ; c b d ' e f ; g h i j k     ",
"        [ l m n o p q r s t u v w x y z A B       ",
"      C z D E F G e H ( I J K L M N O P Q         ",
"    [ R i i S T D i U V i i i i i W X             ",
"  Y 5 5 5 Q Z `  .B ..+.@.#...5 Q $.%.            ",
"              &.    *.      =.    -.              ",
"              ;.    >.    ;.!     0               ",
"              ,.    '.).    !.    ~.&             ",
"              {.    ].)     ^.    /.              ",
"              (.    !     _.:.    <.              ",
"              [.    }.      ,.    |.&             ",
"              ]     :.;.    1.    2.3             ",
"              .     .       3.    .               ",
"              .     .       @     +               ",
"                                                  ",
"                                                  "};
		"""
		

class ToolTable():
	def __init__(self):
		self.createTTUi = FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + "/resources/ui/tooltable.ui")
		ui = self.createTTUi
		ui.logoL.setPixmap(QtGui.QPixmap(os.path.dirname(__file__) + "/resources/ui/logo side by side.png"))				
		ui.buttonBox.accepted.connect(self.accept)
		ui.buttonBox.rejected.connect(self.reject)
		ui.buttonBox.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.apply)
		ui.nameLE.textChanged.connect(self.onNameChanged)
		ui.tableWidget.itemSelectionChanged.connect(self.validateAllFields)
		ui.addBtn.clicked.connect(self.addTool)
		ui.editBtn.clicked.connect(self.editTool)
		ui.removeBtn.clicked.connect(self.removeTool)
		ui.upBtn.clicked.connect(self.moveToolUp)
		ui.downBtn.clicked.connect(self.moveToolDown)

		self.waitingOnToolGui = False
		self.dirty = False
		self.toolList = []
		self.validateAllFields()

	def GetResources(self):
		return {'Pixmap'  : os.path.dirname(__file__) +  "/resources/svg/tooltable.svg", # the name of a svg file available in the resources
                'MenuText': "New Tool Table",
                'ToolTip' : "Sets up a new tool table that an be used for creating G-Code paths from FreeCAD Shapes"}

	def addTool(self):
		ToolGui.setGUIMode("AddingToolFromGUI")
		FreeCADGui.runCommand('New_Tool')
		self.waitingOnToolGui = True
		self.validateAllFields()
		
	def editTool(self):
		ui = self.createTTUi
		row = ui.tableWidget.row(ui.tableWidget.selectedItems()[0])
		ToolGui.setGUIProperties(self.toolList[row]['label'],self.toolList[row]['properties'])
		ToolGui.setGUIMode("EditingToolFromGUI")
		FreeCADGui.runCommand('New_Tool')
		self.waitingOnToolGui = True
		self.validateAllFields()
		
	def removeTool(self):
		table = self.createTTUi.tableWidget
		row = table.row(table.selectedItems()[0])
		table.removeRow(row)
		self.toolList.pop(row)
		self.dirty = True
		self.validateAllFields()
		
	def moveToolUp(self):
		table = self.createTTUi.tableWidget
		row = table.row(table.selectedItems()[0])
		toolNumber = table.item(row,0).text()
		toolType = table.item(row,1).text()
		toolLabel = table.item(row,2).text()
		line = self.toolList.pop(row)
		self.toolList.insert(row-1,line)
		table.removeRow(row)
		table.insertRow(row-1)
		table.setItem(row-1,0,QtGui.QTableWidgetItem(toolNumber))
		table.setItem(row-1,1,QtGui.QTableWidgetItem(toolType))
		table.setItem(row-1,2,QtGui.QTableWidgetItem(toolLabel))
		table.item(row-1,0).setSelected(True)
		self.dirty = True
		self.validateAllFields()
		
	def moveToolDown(self):
		table = self.createTTUi.tableWidget
		row = table.row(table.selectedItems()[0])
		toolNumber = table.item(row,0).text()
		toolType = table.item(row,1).text()
		toolLabel = table.item(row,2).text()
		line = self.toolList.pop(row)
		self.toolList.insert(row+1,line)
		table.removeRow(row)
		table.insertRow(row+1)
		table.setItem(row+1,0,QtGui.QTableWidgetItem(toolNumber))
		table.setItem(row+1,1,QtGui.QTableWidgetItem(toolType))
		table.setItem(row+1,2,QtGui.QTableWidgetItem(toolLabel))
		table.item(row+1,0).setSelected(True)
		self.dirty = True
		self.validateAllFields()

	def onNameChanged(self):
		self.dirty = True
		self.validateAllFields()

	def processToolGuiResult(self):
		ui = self.createTTUi
		table = ui.tableWidget
		self.waitingOnToolGui = False
		mode = ToolGui.getGUIMode()
		if mode == "AddingToolFromGUI":
			props = ToolGui.getGUIProperties()
			for prop in props["properties"]:
				if prop[1] == 'ToolType': toolType = prop[2]
				if prop[1] == 'Number': toolNumber = str(prop[2])
			toolLabel = props["label"]
			row = table.rowCount()
			table.insertRow(row)
			table.setItem(row,0,QtGui.QTableWidgetItem(toolNumber))
			table.setItem(row,1,QtGui.QTableWidgetItem(toolType))
			table.setItem(row,2,QtGui.QTableWidgetItem(toolLabel))
			self.toolList.append(props)
			self.dirty = True
		elif mode == "EditingToolFromGUI":
			props = ToolGui.getGUIProperties()
			for prop in props["properties"]:
				if prop[1] == 'ToolType': toolType = prop[2]
				if prop[1] == 'Number': toolNumber = str(prop[2])
			toolLabel = props["label"]
			row = table.row(table.selectedItems()[0])
			table.setItem(row,0,QtGui.QTableWidgetItem(toolNumber))
			table.setItem(row,1,QtGui.QTableWidgetItem(toolType))
			table.setItem(row,2,QtGui.QTableWidgetItem(toolLabel))
			self.toolList[row] = props
			self.dirty = True
		ToolGui.setGUIMode('None')
		self.validateAllFields()
				
	def validateAllFields(self):
		ui = self.createTTUi
		valid = True
		try:
			sameName = FreeCAD.ActiveDocument.getObjectsByLabel(ui.nameLE.text())
		except:
			return False
		if ui.nameLE.text() == "":
			valid = False
		elif len(sameName) > 1:
			valid = False
			VAL.setLabel(ui.ttNameLabel,'INVALID')
		else:
			for obj in sameName:
				if obj == self.selectedObject: continue
				valid = False			
		if valid == True: VAL.setLabel(ui.ttNameLabel,'VALID')
		else: VAL.setLabel(ui.ttNameLabel,'INVALID')
		
		table = ui.tableWidget
		for i in range(table.rowCount()):
			name = table.item(i,2).text()
			number = table.item(i,0).text()
			names = [i]
			numbers = [i]
			for j in range(table.rowCount()):
				if i == j: continue
				if name == table.item(j,2).text():
					names.append(j)
				if number == table.item(j,0).text():
					numbers.append(j)
				if len(names) > 1:
					valid = False
					for k in names:
						table.item(k,2).setBackground(QtGui.QColor('red'))					
				if len(numbers) > 1:
					valid = False
					for k in numbers:
						table.item(k,0).setBackground(QtGui.QColor('red'))					
		self.setButtonStates(valid)
		return valid
		
	def setButtonStates(self,valid):
		ui = self.createTTUi
		table = ui.tableWidget
		if valid == True:
			ui.buttonBox.buttons()[0].setEnabled(self.dirty)
			ui.buttonBox.button(QtGui.QDialogButtonBox.Apply).setEnabled(self.dirty)
		else:
			ui.buttonBox.buttons()[0].setEnabled(False)
			ui.buttonBox.button(QtGui.QDialogButtonBox.Apply).setEnabled(False)			
		if len(table.selectedItems()) == 1:
			ui.editBtn.setEnabled(True)
			ui.removeBtn.setEnabled(True)
			row = table.row(table.selectedItems()[0])
			if row == 0: ui.upBtn.setEnabled(False)
			else: ui.upBtn.setEnabled(True)
			if row == (table.rowCount() - 1): ui.downBtn.setEnabled(False)
			else: ui.downBtn.setEnabled(True)
		else:
			ui.editBtn.setEnabled(False)
			ui.removeBtn.setEnabled(False)
			ui.upBtn.setEnabled(False)
			ui.downBtn.setEnabled(False)
			
	def getPropertiesFromTool(self,tool):
		p = []
		S = "App::PropertyString"
		I = "App::PropertyInteger"
		L = "App::PropertyLength"
		A = "App::PropertyAngle"
		V = "App::PropertySpeed"
		Q = "App::PropertyQuantity"	
		p = [[S,	"ObjectType",		tool.ObjectType],
		     [I,	"Number",			tool.Number],		     
		     [S,	"ToolType",			tool.ToolType]]
		if hasattr(tool,"Make"): p.append([S,'Make',tool.Make])
		if hasattr(tool,"Model"): p.append([S,'Model',tool.Model])
		if hasattr(tool,"StockMaterial"): p.append([S,'StockMaterial',tool.StockMaterial])
		if hasattr(tool,"FeedRate"): p.append([V,'FeedRate',tool.FeedRate])
		if hasattr(tool,"PlungeRate"): p.append([V,'PlungeRate',tool.PlungeRate])
		if hasattr(tool,"SpindleSpeed"): p.append([S,'SpindleSpeed',tool.SpindleSpeed])
		if hasattr(tool,"StepOver"): p.append([L,'StepOver',tool.StepOver])
		if hasattr(tool,"DepthOfCut"): p.append([L,'DepthOfCut',tool.DepthOfCut])
		
		if hasattr(tool,"Diameter"): p.append([L,'Diameter',tool.Diameter])
		if hasattr(tool,"CutLength"): p.append([L,'CutLength',tool.CutLength])
		if hasattr(tool,"ToolLength"): p.append([L,'ToolLength',tool.ToolLength])
		if hasattr(tool,"ShaftDiameter"): p.append([L,'ShaftDiameter',tool.ShaftDiameter])
		if hasattr(tool,"TopDiameter"): p.append([L,'TopDiameter',tool.TopDiameter])
		if hasattr(tool,"BottomDiameter"): p.append([L,'BottomDiameter',tool.BottomDiameter])
		if hasattr(tool,"CutAngle"): p.append([A,'CutAngle',tool.CutAngle])
		if hasattr(tool,"BallDiameter"): p.append([L,'BallDiameter',tool.BallDiameter])
		return {'label': tool.Label, 'properties': p}

	def Activated(self):
		ui = self.createTTUi
		if self.selectedObject == None:
			self.toolList = []
			ui.nameLE.setText("")
			while ui.tableWidget.rowCount() > 0: ui.tableWidget.removeRow(0)
		else:
			ui.nameLE.setText(self.selectedObject.Label)
			table = ui.tableWidget
			while table.rowCount() > 0: ui.tableWidget.removeRow(0)
			self.toolList = []
			for tool in self.selectedObject.Group:
				self.toolList.append(self.getPropertiesFromTool(tool))
				row = table.rowCount()
				table.insertRow(row)
				table.setItem(row,0,QtGui.QTableWidgetItem(str(tool.Number)))
				table.setItem(row,1,QtGui.QTableWidgetItem(tool.ToolType))
				table.setItem(row,2,QtGui.QTableWidgetItem(tool.Label))

		self.validateAllFields()
		self.dirty = False        
		self.createTTUi.show()       
		return
		
	def apply(self):
		ui = self.createTTUi
		if self.dirty == True:
			if self.selectedObject == None:
				obj = FreeCAD.ActiveDocument.addObject('App::DocumentObjectGroupPython', "ToolTable")
				ViewToolTable(obj.ViewObject)
				obj.addProperty("App::PropertyString","ObjectType")
				obj.ObjectType = "ToolTable"
				obj.setEditorMode("ObjectType",("ReadOnly",))
				self.selectedObject = obj
				FreeCADGui.Selection.clearSelection()
				FreeCADGui.Selection.addSelection(obj)
			for tool in self.selectedObject.Group:
				FreeCAD.ActiveDocument.removeObject(tool.Name)				
			for line in self.toolList:
				tool = Tool(self.selectedObject)
				tool.getObject().Label = line['label']
				tool.setProperties(line['properties'], tool.getObject())
			self.selectedObject.Label = ui.nameLE.text()
			self.dirty = False
			FreeCAD.ActiveDocument.recompute()
			
	def accept(self):
		ui = self.createTTUi
		ui.hide()
		while ui.tableWidget.rowCount() > 0: ui.tableWidget.removeRow(0)
		self.apply()
		return True
		
	def reject(self):
		ui = self.createTTUi
		ui.hide()
		while ui.tableWidget.rowCount() > 0: ui.tableWidget.removeRow(0)
		self.dirty = False
		self.toolList = []
		return False

	def IsActive(self):
		"""Here you can define if the command must be active or not (greyed) if certain conditions
		are met or not. This function is optional."""
		if self.waitingOnToolGui == True:
			if ToolGui.getStatus() == 'hidden': self.processToolGuiResult()
		mw = FreeCADGui.getMainWindow()
		tree = mw.findChildren(QtGui.QTreeWidget)[0]
		if len(tree.selectedItems()) != 1:
			self.selectedObject = None
			return True
		item = tree.selectedItems()[0]
		obj = FreeCAD.ActiveDocument.getObjectsByLabel(item.text(0))[0]
		if obj.ObjectType == "ToolTable":
			self.selectedObject = obj
			return True
		self.selectedObject = None
		return True

FreeCADGui.addCommand('New_Tooltable',ToolTable())
