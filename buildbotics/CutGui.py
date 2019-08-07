
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

from Cut import Cut
from RegistrationCut import RegistrationCut
from DrillCut import DrillCut
from FaceCut import FaceCut
import validator as VAL

GUI_STATUS = 'hidden'
def getStatus():
	return GUI_STATUS
	
def setStatus(status):
	global GUI_STATUS
	GUI_STATUS = status

GUI_MODE = 'None'
def getGUIMode():
	return GUI_MODE
	
def setGUIMode(mode):
	global GUI_MODE
	GUI_MODE = mode
	
GUI_PROPERTIES = []
def getGUIProperties():
	return GUI_PROPERTIES
	
def setGUIProperties(properties):
	global GUI_PROPERTIES
	GUI_PROPERTIES = properties

class CutGui():
	def __init__(self):
		self.createCutUi = FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + "/resources/ui/cut.ui")
		ui = self.createCutUi
		
		self.cutTypes = ["Drill", "Registration", "Facing", "Perimeter", "Pocket2D", 
		                 "Volume2D", "Pocket3D", "Volume3D", "Surface3D", "Tabs", "Laser"]
		self.objectTypes = []
		for cut in self.cutTypes:
			self.objectTypes.append(cut + 'Cut')
			ui.cutTypeCB.addItem(cut)
		
		ui.logoL.setPixmap(QtGui.QPixmap(os.path.dirname(__file__) + "/resources/ui/logo side by side.png"))			
		ui.cutTypeCB.currentIndexChanged.connect(self.onToolTypeChanged)
		ui.toolCB.currentIndexChanged.connect(self.validateAllFields)
		ui.nameLE.textChanged.connect(self.validateAllFields)
		ui.safeHeightLE.textChanged.connect(self.validateAllFields)
		ui.spindleSpeedE.textChanged.connect(self.validateAllFields)
		ui.feedRateE.textChanged.connect(self.validateAllFields)
		ui.plungeRateE.textChanged.connect(self.validateAllFields)
		ui.tclXLE.textChanged.connect(self.validateAllFields)
		ui.tclYLE.textChanged.connect(self.validateAllFields)
		ui.tclZLE.textChanged.connect(self.validateAllFields)
		
		ui.registrationFirstXE.textChanged.connect(self.validateAllFields)
		ui.registrationSecondXE.textChanged.connect(self.validateAllFields)
		ui.registrationFirstYE.textChanged.connect(self.validateAllFields)
		ui.registrationSecondYE.textChanged.connect(self.validateAllFields)
		ui.registrationDrillDepthE.textChanged.connect(self.validateAllFields)
		ui.registrationPeckDepthE.textChanged.connect(self.validateAllFields)
		ui.registrationXAxisRB.clicked.connect(self.validateAllFields)
		ui.registrationYAxisRB.clicked.connect(self.validateAllFields)
		
		ui.drillTW.itemSelectionChanged.connect(self.validateAllFields)
		ui.drillAddB.clicked.connect(self.addDrillPoint)
		ui.drillRemoveB.clicked.connect(self.removeDrillPoint)
		ui.drillUpB.clicked.connect(self.moveDrillPointUp)
		ui.drillDownB.clicked.connect(self.moveDrillPointDown)
		ui.drillSaveB.clicked.connect(self.saveDrillList)
		ui.drillLoadB.clicked.connect(self.loadDrillList)
		ui.drillPeckDepthE.textChanged.connect(self.validateAllFields)
		
		ui.facePatternCB.currentIndexChanged.connect(self.validateAllFields)
		ui.faceCutAreaCB.currentIndexChanged.connect(self.validateAllFields)
		ui.faceStartHeightE.textChanged.connect(self.validateAllFields)
		ui.faceDepthE.textChanged.connect(self.validateAllFields)
		ui.faceStepOverE.textChanged.connect(self.validateAllFields)
		ui.faceStepDownE.textChanged.connect(self.validateAllFields)
		
		ui.buttonBox.accepted.connect(self.accept)
		ui.buttonBox.rejected.connect(self.reject)
		
		self.originalCutName = ''
		self.selectedObject = None
		setGUIMode('None')
		
	def GetResources(self):
		return {'Pixmap'  : os.path.dirname(__file__) +  "/resources/svg/cutsymbol.svg", # the name of a svg file available in the resources
                'MenuText': "New Cut",
                'ToolTip' : "Sets up a new cut that can be added to a g-code job"}
	
	def addDrillPoint(self):
		tw = self.createCutUi.drillTW
		row = tw.rowCount()
		tw.insertRow(row)
		if row != 0:
			tw.setItem(row,0,tw.item(row-1,0).clone())
			tw.setItem(row,1,tw.item(row-1,1).clone())
			tw.setItem(row,2,tw.item(row-1,2).clone())
		else:
			tw.setItem(row,0,QtGui.QTableWidgetItem())
			tw.setItem(row,1,QtGui.QTableWidgetItem())
			tw.setItem(row,2,QtGui.QTableWidgetItem())

		tw.editItem(tw.item(row,0))
		
	def removeDrillPoint(self):
		tw = self.createCutUi.drillTW
		row = tw.row(tw.selectedItems()[0])
		tw.removeRow(row)
		self.validateAllFields()
		
	def moveDrillPointUp(self):
		tw = self.createCutUi.drillTW
		row = tw.row(tw.selectedItems()[0])
		x = tw.item(row,0).text()
		y = tw.item(row,1).text()
		z = tw.item(row,2).text()
		tw.removeRow(row)
		tw.insertRow(row-1)
		tw.setItem(row-1,0,QtGui.QTableWidgetItem(x))
		tw.setItem(row-1,1,QtGui.QTableWidgetItem(y))
		tw.setItem(row-1,2,QtGui.QTableWidgetItem(z))
		tw.setCurrentCell(row-1,0)
		
	def moveDrillPointDown(self):
		tw = self.createCutUi.drillTW
		row = tw.row(tw.selectedItems()[0])
		x = tw.item(row,0).text()
		y = tw.item(row,1).text()
		z = tw.item(row,2).text()
		tw.removeRow(row)
		tw.insertRow(row+1)
		tw.setItem(row+1,0,QtGui.QTableWidgetItem(x))
		tw.setItem(row+1,1,QtGui.QTableWidgetItem(y))
		tw.setItem(row+1,2,QtGui.QTableWidgetItem(z))
		tw.setCurrentCell(row+1,0)
	
	def makeRecommendationsFromTool(self):
		ui = self.createCutUi
		toolLabel = ui.toolCB.currentText()
		ui.spindleSpeedL.setText('Spindle Speed')
		ui.feedRateL.setText('Feed Rate')
		ui.plungeRateL.setText('Plunge Rate')
		toolLabel = toolLabel.lstrip('0123456789 ')
		if toolLabel != "None Selected...":
			obj = FreeCAD.ActiveDocument.getObjectsByLabel(toolLabel)[0]
			if hasattr(obj,'SpindleSpeed'): ui.spindleSpeedL.setText('Spindle Speed (' + obj.SpindleSpeed + ')')
			if hasattr(obj,'FeedRate'): ui.feedRateL.setText('Feed Rate (' + str(obj.FeedRate.UserString) + ')')
			if hasattr(obj,'PlungeRate'): ui.plungeRateL.setText('Plunge Rate (' + str(obj.PlungeRate.UserString) + ')')
			
	def saveDrillList(self):
		filename = QtGui.QFileDialog.getSaveFileName(caption='Select output file')[0]
		if filename != "":
			tw = self.createCutUi.drillTW
			fp = open(filename,'w+')
			for line in range(tw.rowCount()):
				fp.write(tw.item(line,0).text() + ',' + tw.item(line,1).text() + ',' + tw.item(line,2).text() + '\n')
			fp.close()
	
	def loadDrillList(self):	
		filename = QtGui.QFileDialog.getOpenFileName(caption='Select drill file')[0]
		if filename != "":
			fp = open(filename,'r')
			tw = self.createCutUi.drillTW
			while tw.rowCount() > 0: tw.removeRow(0)
			row = 0
			for line in fp:
				tw.insertRow(row)
				tw.setItem(row,0,QtGui.QTableWidgetItem(line.strip().split(',')[0]))
				tw.setItem(row,1,QtGui.QTableWidgetItem(line.strip().split(',')[1]))
				tw.setItem(row,2,QtGui.QTableWidgetItem(line.strip().split(',')[2]))
				row = row + 1
			fp.close()
			self.validateAllFields()		
	
	def setDrillButtonStates(self):
		ui = self.createCutUi
		tw = ui.drillTW
		items = tw.selectedItems()
		ui.drillRemoveB.setEnabled(True)
		ui.drillUpB.setEnabled(True)
		ui.drillDownB.setEnabled(True)
		ui.drillSaveB.setEnabled(True)
		if tw.rowCount() == 0: ui.drillSaveB.setEnabled(False)
		if len(items) == 0:
			ui.drillRemoveB.setEnabled(False)
		if len(items) > 1:
			ui.drillUpB.setEnabled(False)
			ui.drillDownB.setEnabled(False)
		if len(items) == 1:
			if tw.row(items[0]) == 0: ui.drillUpB.setEnabled(False)
			if tw.row(items[0]) == tw.rowCount() - 1: ui.drillDownB.setEnabled(False)

	def validateAllFields(self):
		ui = self.createCutUi
		valid = True
		VAL.setLabel(ui.nameL, 'VALID')
		if ui.nameLE.text() == "":
			valid = False
			VAL.setLabel(ui.nameL,'INVALID')
		mode = getGUIMode()
		sameName = FreeCAD.ActiveDocument.getObjectsByLabel(ui.nameLE.text())
		if (len(sameName) > 0):
			if len(sameName) > 1:
				valid = False
				VAL.setLabel(ui.nameL,'INVALID')
			elif mode != 'EditingCutFromIcon' and mode != 'EditingCutFromGUI':
				valid = False				
				VAL.setLabel(ui.nameL,'INVALID')
			else:
				if ui.nameLE.text() == self.originalCutName:
					VAL.setLabel(ui.nameL,'VALID')
				else:
					VAL.setLabel(ui.nameL,'INVALID')
					valid = False
		cutType = ui.cutTypeCB.currentText()
		if cutType == 'None Selected...':
			VAL.setLabel(ui.typeL,'INVALID')
			valid = False
		else:
			VAL.setLabel(ui.typeL,'VALID')
		tool = ui.toolCB.currentText()
		if tool == 'None Selected...':
			VAL.setLabel(ui.toolL,'INVALID')
			valid = False
		else:
			VAL.setLabel(ui.toolL,'VALID')
		self.makeRecommendationsFromTool()
		
		valid = VAL.validate(ui.feedRateE,ui.feedRateL,False if cutType in ["Registration", "Drill"] else True ,valid,VAL.VELOCITY)
		valid = VAL.validate(ui.plungeRateE,ui.plungeRateL,True,valid,VAL.VELOCITY)
		valid = VAL.validate(ui.spindleSpeedE,ui.spindleSpeedL,True,valid,VAL.ANGULAR_VELOCITY)
		valid = VAL.validate(ui.safeHeightLE,ui.safeHeightL,True,valid,VAL.LENGTH)
		valid = VAL.validate(ui.tclXLE,ui.tclXL,True,valid,VAL.LENGTH)
		valid = VAL.validate(ui.tclYLE,ui.tclYL,True,valid,VAL.LENGTH)
		valid = VAL.validate(ui.tclZLE,ui.tclZL,True,valid,VAL.LENGTH)
		
		if cutType == "Registration":
			valid = VAL.validate(ui.registrationDrillDepthE,ui.registrationDrillDepthL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.registrationPeckDepthE,ui.registrationPeckDepthL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.registrationFirstXE,ui.registrationFirstXL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.registrationSecondXE,ui.registrationSecondXL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.registrationFirstYE,ui.registrationFirstYL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.registrationSecondYE,ui.registrationSecondYL,True,valid,VAL.LENGTH)
			if ui.registrationXAxisRB.isChecked() == True or ui.registrationYAxisRB.isChecked() == True:
				VAL.setLabel(ui.registrationAORL,'VALID')
			else:
				VAL.setLabel(ui.registrationAORL,'INVALID')
				valid = False
		elif cutType == "Drill":
			tw = ui.drillTW
			for row in range(tw.rowCount()):
				valid = VAL.validateTableCell(tw.item(row,0),valid,VAL.LENGTH)
				valid = VAL.validateTableCell(tw.item(row,1),valid,VAL.LENGTH)
				valid = VAL.validateTableCell(tw.item(row,2),valid,VAL.LENGTH)
			self.setDrillButtonStates()
			valid = VAL.validate(ui.drillPeckDepthE,ui.drillPeckDepthL,True,valid,VAL.LENGTH)
		elif cutType == "Facing":
			if ui.facePatternCB.currentIndex() == 0:
				VAL.setLabel(ui.facePatternL,'INVALID')
				valid = False
			else: VAL.setLabel(ui.facePatternL,'VALID')	
			if ui.faceCutAreaCB.currentIndex() == 0:			
				VAL.setLabel(ui.faceCutAreaL,'INVALID')
				valid = False
			else: VAL.setLabel(ui.faceCutAreaL,'VALID')
			valid = VAL.validate(ui.faceStartHeightE,ui.faceStartHeightL,True,valid,VAL.LENGTH)	
			valid = VAL.validate(ui.faceDepthE,ui.faceDepthL,True,valid,VAL.LENGTH)	
			valid = VAL.validate(ui.faceStepOverE,ui.faceStepOverL,True,valid,VAL.LENGTH)	
			valid = VAL.validate(ui.faceStepDownE,ui.faceStepDownL,True,valid,VAL.LENGTH)	
		ui.buttonBox.buttons()[0].setEnabled(valid)
		FreeCAD.ActiveDocument.recompute()	
		return valid

	def setCutProperties(self):
		ui = self.createCutUi
		if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema") in [0, 1, 4, 6]: units = 1
		else: units = 25.4
		S = "App::PropertyString"
		I = "App::PropertyInteger"
		L = "App::PropertyLength"
		A = "App::PropertyAngle"
		V = "App::PropertySpeed"
		Q = "App::PropertyQuantity"
		VL = "App::PropertyVectorList"
		cuttype = ui.cutTypeCB.currentText()
		p = [[S,	"CutName",				ui.nameLE.text()],
			 [S,	"ObjectType",		cuttype + "Cut"],	     
		     [S,	"CutType",			cuttype],
		     [S,	"Tool",				ui.toolCB.currentText().lstrip('0123456789 ')],
		     [I,	"ToolNumber",		eval(ui.toolCB.currentText().split()[0])],
		     [L,	"SafeHeight",		VAL.toSystemValue(ui.safeHeightLE,'length')],
		     [S,	"SpindleSpeed",		VAL.toSystemValue(ui.spindleSpeedE, 'angularVelocity')],
		     [V,	"PlungeRate",		VAL.toSystemValue(ui.plungeRateE, 'velocity')],
		     [L,	"XToolChangeLocation",VAL.toSystemValue(ui.tclXLE, 'length')],	
		     [L,	"YToolChangeLocation",VAL.toSystemValue(ui.tclYLE, 'length')],	
		     [L,	"ZToolChangeLocation",VAL.toSystemValue(ui.tclZLE, 'length')]]
		if cuttype not in ["Registration", "Drill"]:
			p.append([V,	"FeedRate",		VAL.toSystemValue(ui.feedRateE, 'velocity')])
		if cuttype == "Registration":
			p.append([L, "DrillDepth",		VAL.toSystemValue(ui.registrationDrillDepthE, 'length')])
			p.append([L, "PeckDepth",		VAL.toSystemValue(ui.registrationPeckDepthE, 'length')])
			p.append([L, "FirstX",		VAL.toSystemValue(ui.registrationFirstXE, 'length')])
			p.append([L, "SecondX",		VAL.toSystemValue(ui.registrationSecondXE, 'length')])
			p.append([L, "FirstY",		VAL.toSystemValue(ui.registrationFirstYE, 'length')])
			p.append([L, "SecondY",		VAL.toSystemValue(ui.registrationSecondYE, 'length')])
			if ui.registrationXAxisRB.isChecked() == True: axis = "X Axis"
			else: axis = "Y Axis"
			p.append([S, "RegistrationAxis",	axis])
		elif cuttype == "Drill":
			p.append([L, "PeckDepth",	VAL.toSystemValue(ui.drillPeckDepthE,'length')])
			vl = []
			fv = FreeCAD.Vector
			tw = ui.drillTW
			for row in range(tw.rowCount()):
				x = VAL.toSystemValue(tw.item(row,0),'length')
				y = VAL.toSystemValue(tw.item(row,1),'length')
				z = VAL.toSystemValue(tw.item(row,2),'length')
				vl.append(fv(x,y,z))
			p.append([VL, "DrillPointList", vl])
		elif cuttype == "Facing":
			p.append([S,	"FacingPattern",	ui.facePatternCB.currentText()])
			p.append([S,	"CutArea",			ui.faceCutAreaCB.currentText()])
			p.append([L,	"StartHeight",		VAL.toSystemValue(ui.faceStartHeightE, 'length')])		
			p.append([L,	"Depth",			VAL.toSystemValue(ui.faceDepthE, 'length')])		
			p.append([L,	"StepOver",			VAL.toSystemValue(ui.faceStepOverE, 'length')])		
			p.append([L,	"StepDown",			VAL.toSystemValue(ui.faceStepDownE, 'length')])		
		return p
	
	def getCutProperties(self,props):
		ui = self.createCutUi
		for p in props:
			if p[1] == "CutName":		ui.nameLE.setText(p[2])
			elif p[1] == "CutType":
				cutType = p[2]
				ui.cutTypeCB.setCurrentIndex(ui.cutTypeCB.findText(p[2]))
			elif p[1] == "Tool":		toolName = p[2]
			elif p[1] == "ToolNumber":	toolNumber = p[2]
			elif p[1] == "SafeHeight":	ui.safeHeightLE.setText(VAL.fromSystemValue('length',p[2]))
			elif p[1] == "SpindleSpeed": ui.spindleSpeedE.setText(p[2])
			elif p[1] == "FeedRate":	ui.feedRateE.setText(VAL.fromSystemValue('velocity',p[2]))
			elif p[1] == "PlungeRate":	ui.plungeRateE.setText(VAL.fromSystemValue('velocity',p[2]))
			elif p[1] == "XToolChangeLocation":	ui.tclXLE.setText(VAL.fromSystemValue('length',p[2]))
			elif p[1] == "YToolChangeLocation":	ui.tclYLE.setText(VAL.fromSystemValue('length',p[2]))
			elif p[1] == "ZToolChangeLocation":	ui.tclZLE.setText(VAL.fromSystemValue('length',p[2]))
		ui.toolCB.setCurrentIndex(ui.toolCB.findText(str(toolNumber) + ' ' + toolName))
		if cutType == "Registration":
			for p in props:
				if p[1] == "DrillDepth":	ui.registrationDrillDepthE.setText(VAL.fromSystemValue('length',p[2]))
				elif p[1] == "PeckDepth":		ui.registrationPeckDepthE.setText(VAL.fromSystemValue('length',p[2]))
				elif p[1] == "RegistrationAxis":
					if p[1] == "X Axis":	ui.registrationXAxisRB.setChecked(True)
					else: ui.registrationYAxisRB.setChecked(True)
				elif p[1] == "FirstX":	ui.registrationFirstXE.setText(VAL.fromSystemValue('length',p[2]))
				elif p[1] == "SecondX":	ui.registrationSecondXE.setText(VAL.fromSystemValue('length',p[2]))
				elif p[1] == "FirstY":	ui.registrationFirstYE.setText(VAL.fromSystemValue('length',p[2]))
				elif p[1] == "SecondY":	ui.registrationSecondYE.setText(VAL.fromSystemValue('length',p[2]))	
		elif cutType == "Drill":
			for p in props:
				if p[1] == "PeckDepth": ui.drillPeckDepthE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "DrillPointList":
					tw = ui.drillTW
					while tw.rowCount() > 0: tw.removeRow(0)
					for point in p[2]:
						row = tw.rowCount()
						tw.insertRow(row)
						tw.setItem(row,0,QtGui.QTableWidgetItem(VAL.fromSystemValue('length',point[0])))
						tw.setItem(row,1,QtGui.QTableWidgetItem(VAL.fromSystemValue('length',point[1])))
						tw.setItem(row,2,QtGui.QTableWidgetItem(VAL.fromSystemValue('length',point[2])))
		elif cutType == "Facing":
			for p in props:
				if p[1] == "FacingPattern": ui.facePatternCB.setCurrentIndex(ui.facePatternCB.findText(p[2]))
				if p[1] == "CutArea":		ui.faceCutAreaCB.setCurrentIndex(ui.faceCutAreaCB.findText(p[2]))
				if p[1] == "Depth":			ui.faceDepthE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StartHeight":	ui.faceStartHeightE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepOver":		ui.faceStepOverE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepDown":		ui.faceStepDownE.setText(VAL.fromSystemValue('length',p[2]))

	def accept(self):
		ui = self.createCutUi
		ui.hide()
		p = self.setCutProperties()
		mode = getGUIMode()
		if mode in ["AddingCutFromGUI", "EditingCutFromGUI"]:
			setGUIProperties(p)
		elif mode == "AddingCutFromIcon":
			for prop in p:
				if prop[1] == "CutType":
					if prop[2] == "Registration": self.cut = RegistrationCut(self.selectedObject)
					elif prop[2] == "Drill": self.cut = DrillCut(self.selectedObject)
					elif prop[2] == "Facing": self.cut = FaceCut(self.selectedObject)
					else: self.cut = Cut(self.selectedObject)
			self.cut.getObject().Label = ui.nameLE.text()
			self.cut.setProperties(p,self.cut.getObject())
			setGUIMode("None")				
		elif mode == "EditingCutFromIcon":
			self.cut = self.selectedObject.Proxy
			self.cut.Label = ui.nameLE.text()
			self.cut.setProperties(p,self.selectedObject)
		setStatus('hidden')
		return True
				
	def reject(self):
		ui = self.createCutUi
		ui.close()
		setGUIMode('None')
		setStatus('hidden')

	def onToolTypeChanged(self):
		ui = self.createCutUi
		ui.stackedWidget.setCurrentIndex(ui.cutTypeCB.currentIndex())
		self.validateAllFields()
	
	def reset(self):
		ui = self.createCutUi
		ui.nameLE.clear()
		ui.cutTypeCB.setCurrentIndex(0)
		ui.toolCB.setCurrentIndex(0)
		ui.stackedWidget.setCurrentIndex(0)
		ui.safeHeightLE.clear()
		ui.spindleSpeedE.clear()
		ui.feedRateE.clear()
		ui.plungeRateE.clear()
		ui.tclXLE.clear()
		ui.tclYLE.clear()
		ui.tclZLE.clear()
		
		ui.registrationDrillDepthE.clear()
		ui.registrationPeckDepthE.clear()
		ui.registrationXAxisRB.setChecked(False)
		ui.registrationYAxisRB.setChecked(False)
		ui.registrationFirstXE.clear()
		ui.registrationFirstYE.clear()
		ui.registrationSecondXE.clear()
		ui.registrationSecondYE.clear()
		
		ui.drillPeckDepthE.setText("")
		tw = ui.drillTW
		while tw.rowCount() > 0: tw.removeRow(0)
		
		ui.facePatternCB.setCurrentIndex(0)
		ui.faceCutAreaCB.setCurrentIndex(0)
		ui.faceStartHeightE.clear()
		ui.faceDepthE.clear()
		ui.faceStepOverE.clear()
		ui.faceStepDownE.clear()

	def setMode(self):
		if self.selectedObject == None: mode = getGUIMode()
		elif self.selectedObject.ObjectType in self.objectTypes: mode = "EditingCutFromIcon"
		elif self.selectedObject.ObjectType == "GCodeJob":
			if getGUIMode() == 'None': mode = "AddingCutFromIcon"
			else: mode = getGUIMode()
		setGUIMode(mode)
		return mode

	def getPropertiesFromExistingCut(self,obj):
		ui = self.createCutUi
		fc = FreeCAD.ActiveDocument
		ui.cutTypeCB.setCurrentIndex(ui.cutTypeCB.findText(obj.CutType))
		ui.nameLE.setText(obj.CutName)

		ttName = obj.getParentGroup().ToolTable
		group = fc.getObjectsByLabel(ttName)[0].Group		
		for tool in group:
			ui.toolCB.addItem(str(tool.Number) + " " + tool.Label)
		ui.toolCB.setCurrentIndex(ui.toolCB.findText(str(obj.ToolNumber) + ' ' + obj.Tool))
		ui.safeHeightLE.setText(VAL.fromSystemValue('length',obj.SafeHeight))
		ui.spindleSpeedE.setText(obj.SpindleSpeed)
		if hasattr(obj,"FeedRate"): ui.feedRateE.setText(VAL.fromSystemValue('velocity',obj.FeedRate))
		ui.plungeRateE.setText(VAL.fromSystemValue('velocity',obj.PlungeRate))
		ui.tclXLE.setText(VAL.fromSystemValue('length',obj.XToolChangeLocation))
		ui.tclYLE.setText(VAL.fromSystemValue('length',obj.YToolChangeLocation))
		ui.tclZLE.setText(VAL.fromSystemValue('length',obj.ZToolChangeLocation))
		if obj.CutType == "Registration":
			ui.registrationDrillDepthE.setText(VAL.fromSystemValue('length',obj.DrillDepth))
			ui.registrationPeckDepthE.setText(VAL.fromSystemValue('length',obj.PeckDepth))
			ui.registrationFirstXE.setText(VAL.fromSystemValue('length',obj.FirstX))
			ui.registrationSecondXE.setText(VAL.fromSystemValue('length',obj.SecondX))
			ui.registrationFirstYE.setText(VAL.fromSystemValue('length',obj.FirstY))
			ui.registrationSecondYE.setText(VAL.fromSystemValue('length',obj.SecondY))
			if obj.RegistrationAxis == "X Axis": ui.registrationXAxisRB.setChecked(True)
			else: ui.registrationYAxisRB.setChecked(True)
		elif obj.CutType == "Drill":
			ui.drillPeckDepthE.setText(VAL.fromSystemValue('length',obj.PeckDepth))
			tw = ui.drillTW
			while tw.rowCount() > 0: tw.removeRow(0)
			for point in obj.DrillPointList:
				row = tw.rowCount()
				tw.insertRow(row)
				tw.setItem(row,0,QtGui.QTableWidgetItem(VAL.fromSystemValue('length',point[0])))
				tw.setItem(row,1,QtGui.QTableWidgetItem(VAL.fromSystemValue('length',point[1])))
				tw.setItem(row,2,QtGui.QTableWidgetItem(VAL.fromSystemValue('length',point[2])))
		elif obj.CutType == "Facing":
			ui.facePatternCB.setCurrentIndex(ui.facePatternCB.findText(obj.FacingPattern))
			ui.faceCutAreaCB.setCurrentIndex(ui.faceCutAreaCB.findText(obj.CutArea))
			ui.faceStartHeightE.setText(VAL.fromSystemValue('length',obj.StartHeight))
			ui.faceDepthE.setText(VAL.fromSystemValue('length',obj.Depth))
			ui.faceStepOverE.setText(VAL.fromSystemValue('length',obj.StepOver))
			ui.faceStepDownE.setText(VAL.fromSystemValue('length',obj.StepDown))
		
	def Activated(self):
		ui = self.createCutUi
		self.reset()
		
		if hasattr(FreeCAD.ActiveDocument,"Objects"):
			while ui.faceCutAreaCB.count() > 1: ui.faceCutAreaCB.removeItem(1)
			for obj in FreeCAD.ActiveDocument.Objects:
				if hasattr(obj,"Shape"):
					ui.faceCutAreaCB.addItem(obj.Label)
		
		mode = self.setMode()
		if mode == "AddingCutFromIcon":
			self.originalCutName = ''
			while ui.toolCB.count() > 1: ui.toolCB.removeItem(ui.toolCB.count()-1)
			group = FreeCAD.ActiveDocument.getObjectsByLabel(self.selectedObject.ToolTable)[0].Group
			for tool in group:
				ui.toolCB.addItem(str(tool.Number) + " " + tool.Label)
			self.reset()			
		elif mode == "EditingCutFromIcon":
			self.reset()
			self.originalCutName = self.selectedObject.Label
			while ui.toolCB.count() > 1: ui.toolCB.removeItem(ui.toolCB.count()-1)
			parent = self.selectedObject.getParentGroup()
			group = FreeCAD.ActiveDocument.getObjectsByLabel(parent.ToolTable)[0].Group
			self.getPropertiesFromExistingCut(self.selectedObject)
		elif mode == "AddingCutFromGUI":
			self.originalCutName = ""
			self.reset()
			props = getGUIProperties()
			for prop in props:
				if prop[1] == "ToolTable": self.tooltable = prop[2]
			while ui.toolCB.count() > 1: ui.toolCB.removeItem(ui.toolCB.count()-1)
			group = FreeCAD.ActiveDocument.getObjectsByLabel(self.tooltable)[0].Group
			for tool in group:
				ui.toolCB.addItem(str(tool.Number) + " " + tool.Label)
		elif mode == "EditingCutFromGUI":
			props = getGUIProperties()
			for prop in props:
				if prop[1] == "ToolTable": self.tooltable = prop[2]
			while ui.toolCB.count() > 1: ui.toolCB.removeItem(ui.toolCB.count()-1)
			group = FreeCAD.ActiveDocument.getObjectsByLabel(self.tooltable)[0].Group
			for tool in group:
				ui.toolCB.addItem(str(tool.Number) + " " + tool.Label)
			self.getCutProperties(props)
			self.originalCutName = ui.nameLE.text()
		self.createCutUi.show()
		setStatus('showing')
		self.validateAllFields()
		
	def IsActive(self):
		if getGUIMode() in ["EditingCutFromGUI", "AddingCutFromGUI"]:
			return True
		mw = FreeCADGui.getMainWindow()
		tree = mw.findChildren(QtGui.QTreeWidget)[0]
		if len(tree.selectedItems()) != 1:
			self.selectedObject = None
			return False
		item = tree.selectedItems()[0]
		obj = FreeCAD.ActiveDocument.getObjectsByLabel(item.text(0))[0]
		if hasattr(obj,"ObjectType"):
			if obj.ObjectType in ["GCodeJob"] + self.objectTypes:
				self.selectedObject = obj
				return True
		self.selectedObject = None
		return False
		
FreeCADGui.addCommand('New_Cut',CutGui())
