
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
from PerimeterCut import PerimeterCut
from Pocket2DCut import Pocket2DCut
from Volume2DCut import Volume2DCut
from Pocket3DCut import Pocket3DCut
from Volume3DCut import Volume3DCut
from Surface3DCut import Surface3DCut
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
		ui.cutTypeCB.currentIndexChanged.connect(self.onCutTypeChanged)
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
		ui.faceConventionalRB.clicked.connect(self.validateAllFields)
		ui.faceClimbRB.clicked.connect(self.validateAllFields)
		ui.faceEitherRB.clicked.connect(self.validateAllFields)
		
		ui.perimeterObjectToCutCB.currentIndexChanged.connect(self.validateAllFields)
		ui.perimeterDepthE.textChanged.connect(self.validateAllFields)
		ui.perimeterDepthOfCutE.textChanged.connect(self.validateAllFields)
		ui.perimeterStartHeightE.textChanged.connect(self.validateAllFields)
		ui.perimeterStepDownE.textChanged.connect(self.validateAllFields)
		ui.perimeterWidthOfCutE.textChanged.connect(self.validateAllFields)
		ui.perimeterStepOverE.textChanged.connect(self.validateAllFields)
		ui.perimeterOffsetE.textChanged.connect(self.validateAllFields)
		ui.perimeterConventionalRB.clicked.connect(self.validateAllFields)
		ui.perimeterClimbRB.clicked.connect(self.validateAllFields)
		ui.perimeterEitherRB.clicked.connect(self.validateAllFields)
		ui.perimeterInsideRB.clicked.connect(self.validateAllFields)
		ui.perimeterOutsideRB.clicked.connect(self.validateAllFields)
		ui.perimeterErrorE.textChanged.connect(self.validateAllFields)
		
		ui.pocket2DObjectCB.currentIndexChanged.connect(self.validateAllFields)
		ui.pocket2DPerimeterDepthE.textChanged.connect(self.validateAllFields)
		ui.pocket2DDepthOfCutE.textChanged.connect(self.validateAllFields)
		ui.pocket2DStartHeightE.textChanged.connect(self.validateAllFields)
		ui.pocket2DStepDownE.textChanged.connect(self.validateAllFields)
		ui.pocket2DStepOverE.textChanged.connect(self.validateAllFields)
		ui.pocket2DOffsetFromPerimeterE.textChanged.connect(self.validateAllFields)
		ui.pocket2DMaximumErrorE.textChanged.connect(self.validateAllFields)
		ui.pocket2DConventionalRB.clicked.connect(self.validateAllFields)
		ui.pocket2DClimbRB.clicked.connect(self.validateAllFields)
		ui.pocket2DEitherRB.clicked.connect(self.validateAllFields)

		ui.volume2DObjectToCutCB.currentIndexChanged.connect(self.validateAllFields)
		ui.volume2DCutAreaCB.currentIndexChanged.connect(self.validateAllFields)
		ui.volume2DPerimeterDepthE.textChanged.connect(self.validateAllFields)
		ui.volume2DDepthOfCutE.textChanged.connect(self.validateAllFields)
		ui.volume2DStartHeightE.textChanged.connect(self.validateAllFields)
		ui.volume2DStepDownE.textChanged.connect(self.validateAllFields)
		ui.volume2DStepOverE.textChanged.connect(self.validateAllFields)
		ui.volume2DOffsetFromPerimeterE.textChanged.connect(self.validateAllFields)
		ui.volume2DMaximumErrorE.textChanged.connect(self.validateAllFields)
		ui.volume2DConventionalRB.clicked.connect(self.validateAllFields)
		ui.volume2DClimbRB.clicked.connect(self.validateAllFields)
		ui.volume2DEitherRB.clicked.connect(self.validateAllFields)
		
		ui.pocket3DObjectToCutCB.currentIndexChanged.connect(self.validateAllFields)
		ui.pocket3DStartHeightE.textChanged.connect(self.validateAllFields)
		ui.pocket3DStepDownE.textChanged.connect(self.validateAllFields)
		ui.pocket3DStepOverE.textChanged.connect(self.validateAllFields)
		ui.pocket3DOffsetFromPerimeterE.textChanged.connect(self.validateAllFields)
		ui.pocket3DMaximumErrorE.textChanged.connect(self.validateAllFields)
		ui.pocket3DConventionalRB.clicked.connect(self.validateAllFields)
		ui.pocket3DClimbRB.clicked.connect(self.validateAllFields)
		ui.pocket3DEitherRB.clicked.connect(self.validateAllFields)
		
		ui.volume3DObjectToCutCB.currentIndexChanged.connect(self.validateAllFields)
		ui.volume3DCutAreaCB.currentIndexChanged.connect(self.validateAllFields)
		ui.volume3DStartHeightE.textChanged.connect(self.validateAllFields)
		ui.volume3DStepDownE.textChanged.connect(self.validateAllFields)
		ui.volume3DStepOverE.textChanged.connect(self.validateAllFields)
		ui.volume3DOffsetFromPerimeterE.textChanged.connect(self.validateAllFields)
		ui.volume3DMaximumErrorE.textChanged.connect(self.validateAllFields)
		ui.volume3DConventionalRB.clicked.connect(self.validateAllFields)
		ui.volume3DClimbRB.clicked.connect(self.validateAllFields)
		ui.volume3DEitherRB.clicked.connect(self.validateAllFields)
		
		ui.buttonBox.accepted.connect(self.accept)
		ui.buttonBox.rejected.connect(self.reject)
		
		self.originalCutName = ''
		self.selectedObject = None
		setGUIMode('None')
		
	def GetResources(self):
		return {'Pixmap'  : os.path.dirname(__file__) +  "/resources/svg/cutsymbol.svg", # the name of a svg file available in the resources
                'MenuText': "New Cut",
                'ToolTip' : "Sets up a new cut that can be added to a g-code job"}
	
	def setUnits(self):
		ui = self.createCutUi
		if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema") in [0, 1, 4, 6]:
			self.units = 'mm'
			ui.unitsLabel.setText("Default units are mm, mm/min, and rpm")
		else:
			ui.unitsLabel.setText("Default units are in, in/min, and rpm")
			self.units = 'in'
	
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
		toolLabel = toolLabel.lstrip('0123456789')
		toolLabel = toolLabel.lstrip(' ')
		if toolLabel != "None Selected...":
			obj = FreeCAD.ActiveDocument.getObjectsByLabel(toolLabel)[0]
			if hasattr(obj,'SpindleSpeed'): ui.spindleSpeedL.setText('Spindle Speed (' + obj.SpindleSpeed + ')')
			if hasattr(obj,'FeedRate'): ui.feedRateL.setText('Feed Rate (' + str(obj.FeedRate.UserString) + ')')
			if hasattr(obj,'PlungeRate'): ui.plungeRateL.setText('Plunge Rate (' + str(obj.PlungeRate.UserString) + ')')
			
	def getToolWidth(self):
		ui = self.createCutUi
		toolLabel = ui.toolCB.currentText()
		if toolLabel == "None Selected...": return 0.0
		toolLabel = toolLabel.lstrip('0123456789')
		toolLabel = toolLabel.lstrip(' ')
		obj = FreeCAD.ActiveDocument.getObjectsByLabel(toolLabel)[0]
		if hasattr(obj,'Diameter'): return obj.Diameter.Value
		if hasattr(obj, 'BallDiameter'): return obj.BallDiameter.Value
		return obj.TopDiameter.Value		
			
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
			if ui.faceConventionalRB.isChecked() == True or ui.faceClimbRB.isChecked() == True or ui.faceEitherRB.isChecked() == True:
				VAL.setLabel(ui.faceMillingMethodL,'VALID')
			else:
				VAL.setLabel(ui.faceMillingMethodL,'INVALID')
				valid = False
		elif cutType == "Perimeter":
			if ui.perimeterObjectToCutCB.currentIndex() == 0:			
				VAL.setLabel(ui.perimeterObjectToCutL,'INVALID')
				valid = False
			else: VAL.setLabel(ui.perimeterObjectToCutL,'VALID')
			valid = VAL.validate(ui.perimeterDepthE, ui.perimeterDepthL,True,valid,VAL.LENGTH)	
			valid = VAL.validate(ui.perimeterDepthOfCutE, ui.perimeterDepthOfCutL,True,valid,VAL.LENGTH)	
			valid = VAL.validate(ui.perimeterStartHeightE, ui.perimeterStartHeightL,True,valid,VAL.LENGTH)	
			valid = VAL.validate(ui.perimeterStepDownE, ui.perimeterStepDownL,True,valid,VAL.LENGTH)	
			if VAL.validate(ui.perimeterWidthOfCutE, ui.perimeterWidthOfCutL,True,valid,VAL.LENGTH) == True:
				if VAL.toSystemValue(ui.perimeterWidthOfCutE,'length') < self.getToolWidth():
					VAL.setLabel(ui.perimeterWidthOfCutL,'INVALID')
					valid = False
			else: valid = False
			valid = VAL.validate(ui.perimeterStepOverE, ui.perimeterStepOverL,True,valid,VAL.LENGTH)	
			valid = VAL.validate(ui.perimeterOffsetE, ui.perimeterOffsetL,True,valid,VAL.LENGTH)	
			if ui.perimeterInsideRB.isChecked() == True or ui.perimeterOutsideRB.isChecked() == True:
				VAL.setLabel(ui.perimeterSideL,'VALID')
			else:
				VAL.setLabel(ui.perimeterSideL,'INVALID')
				valid = False
			if ui.perimeterConventionalRB.isChecked() == True or ui.perimeterClimbRB.isChecked() == True or ui.perimeterEitherRB.isChecked() == True:
				VAL.setLabel(ui.perimeterMillingMethodL,'VALID')
			else:
				VAL.setLabel(ui.perimeterMillingMethodL,'INVALID')
				valid = False
			valid = VAL.validate(ui.perimeterErrorE, ui.perimeterErrorL, True, valid, VAL.LENGTH)
		elif cutType == "Pocket2D":
			if ui.pocket2DObjectCB.currentIndex() == 0:
				VAL.setLabel(ui.pocket2DObjectL,'INVALID')
				valid = False
			else: VAL.setLabel(ui.pocket2DObjectL,'VALID')
			valid = VAL.validate(ui.pocket2DPerimeterDepthE, ui.pocket2DPerimeterDepthL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.pocket2DDepthOfCutE, ui.pocket2DDepthOfCutL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.pocket2DStartHeightE, ui.pocket2DStartHeightL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.pocket2DStepDownE, ui.pocket2DStepDownL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.pocket2DStepOverE, ui.pocket2DStepOverL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.pocket2DOffsetFromPerimeterE, ui.pocket2DOffsetFromPerimeterL,True,valid,VAL.LENGTH)
			if ui.pocket2DConventionalRB.isChecked() == True or ui.pocket2DClimbRB.isChecked() == True or ui.pocket2DEitherRB.isChecked() == True:
				VAL.setLabel(ui.pocket2DMillingMethodL,'VALID')
			else:
				VAL.setLabel(ui.pocket2DMillingMethodL,'INVALID')
				valid = False			
			valid = VAL.validate(ui.pocket2DMaximumErrorE, ui.pocket2DMaximumErrorL,True,valid,VAL.LENGTH)
		elif cutType == "Volume2D":
			if ui.volume2DObjectToCutCB.currentIndex() == 0:
				VAL.setLabel(ui.volume2DObjectToCutL,'INVALID')
				valid = False
			else: VAL.setLabel(ui.volume2DObjectToCutL,'VALID')
			if ui.volume2DCutAreaCB.currentIndex() == 0:
				VAL.setLabel(ui.volume2DCutAreaL,'INVALID')
				valid = False
			else: VAL.setLabel(ui.volume2DCutAreaL,'VALID')
			valid = VAL.validate(ui.volume2DPerimeterDepthE, ui.volume2DPerimeterDepthL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.volume2DDepthOfCutE, ui.volume2DDepthOfCutL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.volume2DStartHeightE, ui.volume2DStartHeightL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.volume2DStepDownE, ui.volume2DStepDownL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.volume2DStepOverE, ui.volume2DStepOverL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.volume2DOffsetFromPerimeterE, ui.volume2DOffsetFromPerimeterL,True,valid,VAL.LENGTH)
			if ui.volume2DConventionalRB.isChecked() == True or ui.volume2DClimbRB.isChecked() == True or ui.volume2DEitherRB.isChecked() == True:
				VAL.setLabel(ui.volume2DMillingMethodL,'VALID')
			else:
				VAL.setLabel(ui.volume2DMillingMethodL,'INVALID')
				valid = False			
			valid = VAL.validate(ui.volume2DMaximumErrorE, ui.volume2DMaximumErrorL,True,valid,VAL.LENGTH)
		elif cutType == "Pocket3D":
			if ui.pocket3DObjectToCutCB.currentIndex() == 0:
				VAL.setLabel(ui.pocket3DObjectToCutL,'INVALID')
				valid = False
			else: VAL.setLabel(ui.pocket3DObjectToCutL,'VALID')
			valid = VAL.validate(ui.pocket3DStartHeightE, ui.pocket3DStartHeightL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.pocket3DStepDownE, ui.pocket3DStepDownL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.pocket3DStepOverE, ui.pocket3DStepOverL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.pocket3DOffsetFromPerimeterE, ui.pocket3DOffsetFromPerimeterL,True,valid,VAL.LENGTH)
			if ui.pocket3DConventionalRB.isChecked() == True or ui.pocket3DClimbRB.isChecked() == True or ui.pocket3DEitherRB.isChecked() == True:
				VAL.setLabel(ui.pocket3DMillingMethodL,'VALID')
			else:
				VAL.setLabel(ui.pocket3DMillingMethodL,'INVALID')
				valid = False			
			valid = VAL.validate(ui.pocket3DMaximumErrorE, ui.pocket3DMaximumErrorL,True,valid,VAL.LENGTH)
		elif cutType == "Volume3D":
			if ui.volume3DObjectToCutCB.currentIndex() == 0:
				VAL.setLabel(ui.volume3DObjectToCutL,'INVALID')
				valid = False
			else: VAL.setLabel(ui.volume3DObjectToCutL,'VALID')
			if ui.volume3DCutAreaCB.currentIndex() == 0:
				VAL.setLabel(ui.volume3DCutAreaL,'INVALID')
				valid = False
			else: VAL.setLabel(ui.volume3DCutAreaL,'VALID')
			valid = VAL.validate(ui.volume3DStartHeightE, ui.volume3DStartHeightL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.volume3DStepDownE, ui.volume3DStepDownL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.volume3DStepOverE, ui.volume3DStepOverL,True,valid,VAL.LENGTH)
			valid = VAL.validate(ui.volume3DOffsetFromPerimeterE, ui.volume3DOffsetFromPerimeterL,True,valid,VAL.LENGTH)
			if ui.volume3DConventionalRB.isChecked() == True or ui.volume3DClimbRB.isChecked() == True or ui.volume3DEitherRB.isChecked() == True:
				VAL.setLabel(ui.volume3DMillingMethodL,'VALID')
			else:
				VAL.setLabel(ui.volume3DMillingMethodL,'INVALID')
				valid = False			
			valid = VAL.validate(ui.volume3DMaximumErrorE, ui.volume3DMaximumErrorL,True,valid,VAL.LENGTH)
		ui.buttonBox.buttons()[0].setEnabled(valid)
		FreeCAD.ActiveDocument.recompute()	
		return valid

	def setCutProperties(self):
		ui = self.createCutUi
		if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema") in [0, 1, 4, 6]: units = 1
		else: units = 25.4
		S = "App::PropertyString"
		I = "App::PropertyInteger"
		L = "App::PropertyDistance"
		A = "App::PropertyAngle"
		V = "App::PropertySpeed"
		Q = "App::PropertyQuantity"
		VL = "App::PropertyVectorList"
		toolLabel = ui.toolCB.currentText().lstrip('0123456789')
		toolLabel = toolLabel.lstrip(' ')
		cuttype = ui.cutTypeCB.currentText()
		p = [[S,	"CutName",				ui.nameLE.text()],
			 [S,	"ObjectType",		cuttype + "Cut"],	     
		     [S,	"CutType",			cuttype],
		     [S,	"Tool",				toolLabel],
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
			if ui.faceConventionalRB.isChecked() == True: method = "Conventional"
			elif ui.faceClimbRB.isChecked() == True: method = "Climb"
			else: method = "Either"
			p.append([S,	"MillingMethod",	method])
		elif cuttype == "Perimeter":
			p.append([S,	"ObjectToCut",		ui.perimeterObjectToCutCB.currentText()])
			p.append([L,	"Depth",			VAL.toSystemValue(ui.perimeterDepthE,'length')])
			p.append([L,	"DepthOfCut",		VAL.toSystemValue(ui.perimeterDepthOfCutE,'length')])
			p.append([L,	"StartHeight",		VAL.toSystemValue(ui.perimeterStartHeightE,'length')])
			p.append([L,	"StepDown",			VAL.toSystemValue(ui.perimeterStepDownE,'length')])
			p.append([L,	"WidthOfCut",		VAL.toSystemValue(ui.perimeterWidthOfCutE,'length')])
			p.append([L,	"StepOver",			VAL.toSystemValue(ui.perimeterStepOverE,'length')])
			p.append([L,	"Offset",		 	VAL.toSystemValue(ui.perimeterOffsetE,'length')])
			if ui.perimeterConventionalRB.isChecked() == True: method = "Conventional"
			elif ui.perimeterClimbRB.isChecked() == True: method = "Climb"
			else: method = "Either"
			p.append([S,	"MillingMethod",	method])
			if ui.perimeterInsideRB.isChecked() == True: side = "Inside"
			else: side = "Outside"
			p.append([S,	"Side",				side])
			p.append([L,	"MaximumError",		VAL.toSystemValue(ui.perimeterErrorE,'length')])
		elif cuttype == "Pocket2D":
			p.append([S,	"ObjectToCut",		ui.pocket2DObjectCB.currentText()])
			p.append([L,	"PerimeterDepth",	VAL.toSystemValue(ui.pocket2DPerimeterDepthE,'length')])
			p.append([L,	"DepthOfCut",		VAL.toSystemValue(ui.pocket2DDepthOfCutE,'length')])
			p.append([L,	"StartHeight",		VAL.toSystemValue(ui.pocket2DStartHeightE,'length')])
			p.append([L,	"StepDown",			VAL.toSystemValue(ui.pocket2DStepDownE,'length')])
			p.append([L,	"StepOver",			VAL.toSystemValue(ui.pocket2DStepOverE,'length')])
			p.append([L,	"OffsetFromPerimeter",	VAL.toSystemValue(ui.pocket2DOffsetFromPerimeterE,'length')])
			if ui.pocket2DConventionalRB.isChecked() == True: method = "Conventional"
			elif ui.pocket2DClimbRB.isChecked() == True: method = "Climb"
			else: method = "Either"
			p.append([S,	"MillingMethod",	method])
			p.append([L,	"MaximumError",		VAL.toSystemValue(ui.pocket2DMaximumErrorE,'length')])
		elif cuttype == "Volume2D":
			p.append([S,	"ObjectToCut",		ui.volume2DObjectToCutCB.currentText()])
			p.append([S,	"CutArea",			ui.volume2DCutAreaCB.currentText()])
			p.append([L,	"PerimeterDepth",	VAL.toSystemValue(ui.volume2DPerimeterDepthE,'length')])
			p.append([L,	"DepthOfCut",		VAL.toSystemValue(ui.volume2DDepthOfCutE,'length')])
			p.append([L,	"StartHeight",		VAL.toSystemValue(ui.volume2DStartHeightE,'length')])
			p.append([L,	"StepDown",			VAL.toSystemValue(ui.volume2DStepDownE,'length')])
			p.append([L,	"StepOver",			VAL.toSystemValue(ui.volume2DStepOverE,'length')])
			p.append([L,	"OffsetFromPerimeter",	VAL.toSystemValue(ui.volume2DOffsetFromPerimeterE,'length')])
			if ui.volume2DConventionalRB.isChecked() == True: method = "Conventional"
			elif ui.volume2DClimbRB.isChecked() == True: method = "Climb"
			else: method = "Either"
			p.append([S,	"MillingMethod",	method])
			p.append([L,	"MaximumError",		VAL.toSystemValue(ui.volume2DMaximumErrorE,'length')])
		elif cuttype == "Pocket3D":
			p.append([S,	"ObjectToCut",		ui.pocket3DObjectToCutCB.currentText()])
			p.append([L,	"StartHeight",		VAL.toSystemValue(ui.pocket3DStartHeightE,'length')])
			p.append([L,	"StepDown",			VAL.toSystemValue(ui.pocket3DStepDownE,'length')])
			p.append([L,	"StepOver",			VAL.toSystemValue(ui.pocket3DStepOverE,'length')])
			p.append([L,	"OffsetFromPerimeter",	VAL.toSystemValue(ui.pocket3DOffsetFromPerimeterE,'length')])
			if ui.pocket3DConventionalRB.isChecked() == True: method = "Conventional"
			elif ui.pocket3DClimbRB.isChecked() == True: method = "Climb"
			else: method = "Either"
			p.append([S,	"MillingMethod",	method])
			p.append([L,	"MaximumError",		VAL.toSystemValue(ui.pocket3DMaximumErrorE,'length')])
		elif cuttype == "Volume3D":
			p.append([S,	"ObjectToCut",		ui.volume3DObjectToCutCB.currentText()])
			p.append([S,	"CutArea",			ui.volume3DCutAreaCB.currentText()])
			p.append([L,	"StartHeight",		VAL.toSystemValue(ui.volume3DStartHeightE,'length')])
			p.append([L,	"StepDown",			VAL.toSystemValue(ui.volume3DStepDownE,'length')])
			p.append([L,	"StepOver",			VAL.toSystemValue(ui.volume3DStepOverE,'length')])
			p.append([L,	"OffsetFromPerimeter",	VAL.toSystemValue(ui.volume3DOffsetFromPerimeterE,'length')])
			if ui.volume3DConventionalRB.isChecked() == True: method = "Conventional"
			elif ui.volume3DClimbRB.isChecked() == True: method = "Climb"
			else: method = "Either"
			p.append([S,	"MillingMethod",	method])
			p.append([L,	"MaximumError",		VAL.toSystemValue(ui.volume3DMaximumErrorE,'length')])
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
					if p[2] == "X Axis":	ui.registrationXAxisRB.setChecked(True)
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
				if p[1] == "MillingMethod":
					if p[2] == "Conventional": ui.faceConventionalRB.setChecked(True)
					elif p[2] == "Climb":   ui.faceClimbRB.setChecked(True)
					else: ui.faceEitherRB.setChecked(True)
		elif cutType == "Perimeter":
			for p in props:
				if p[1] == "ObjectToCut": 	ui.perimeterObjectToCutCB.setCurrentIndex(ui.perimeterObjectToCutCB.findText(p[2]))
				if p[1] == "Depth":			ui.perimeterDepthE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "DepthOfCut": 	ui.perimeterDepthOfCutE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StartHeight": 	ui.perimeterStartHeightE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepDown":   	ui.perimeterStepDownE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "WidthOfCut": 	ui.perimeterWidthOfCutE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepOver":   	ui.perimeterStepOverE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "Offset":     	ui.perimeterOffsetE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "MillingMethod":
					if p[2] == "Conventional": ui.perimeterConventionalRB.setChecked(True)
					elif p[2] == "Climb":   ui.perimeterClimbRB.setChecked(True)
					else: ui.perimeterEitherRB.setChecked(True)
				if p[1] == "Side":
					if p[2] == "Inside": ui.perimeterInsideRB.setChecked(True)
					else: ui.perimeterOutsideRB.setChecked(True)
				if p[1] == "MaximumError":	ui.perimeterErrorE.setText(VAL.fromSystemValue('length',p[2]))
		elif cutType == "Pocket2D":
			for p in props:
				if p[1] == "ObjectToCut":	ui.pocket2DObjectCB.setCurrentIndex(ui.pocket2DObjectCB.findText(p[2]))
				if p[1] == "PerimeterDepth": ui.pocket2DPerimeterDepthE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "DepthOfCut":	ui.pocket2DDepthOfCutE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StartHeight":	ui.pocket2DStartHeightE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepDown":		ui.pocket2DStepDownE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepOver":		ui.pocket2DStepOverE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "OffsetFromPerimeter":	ui.pocket2DOffsetFromPerimeterE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "MillingMethod":
					if p[2] == "Conventional": ui.pocket2DConventionalRB.setChecked(True)
					elif p[2] == "Climb":   ui.pocket2DClimbRB.setChecked(True)
					else: ui.pocket2DEitherRB.setChecked(True)
				if p[1] == "MaximumError":	ui.pocket2DMaximumErrorE.setText(VAL.fromSystemValue('length',p[2]))
		elif cutType == "Volume2D":
			for p in props:
				if p[1] == "ObjectToCut":	ui.volume2DObjectToCutCB.setCurrentIndex(ui.volume2DObjectToCutCB.findText(p[2]))
				if p[1] == "CutArea":		ui.volume2DCutAreaCB.setCurrentIndex(ui.volume2DCutAreaCB.findText(p[2]))
				if p[1] == "PerimeterDepth": ui.volume2DPerimeterDepthE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "DepthOfCut":	ui.volume2DDepthOfCutE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StartHeight":	ui.volume2DStartHeightE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepDown":		ui.volume2DStepDownE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepOver":		ui.volume2DStepOverE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "OffsetFromPerimeter":	ui.volume2DOffsetFromPerimeterE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "MillingMethod":
					if p[2] == "Conventional": ui.volume2DConventionalRB.setChecked(True)
					elif p[2] == "Climb":   ui.volume2DClimbRB.setChecked(True)
					else: ui.volume2DEitherRB.setChecked(True)
				if p[1] == "MaximumError":	ui.volume2DMaximumErrorE.setText(VAL.fromSystemValue('length',p[2]))
		elif cutType == "Pocket3D":
			for p in props:
				if p[1] == "ObjectToCut":	ui.pocket3DObjectToCutCB.setCurrentIndex(ui.pocket3DObjectToCutCB.findText(p[2]))
				if p[1] == "StartHeight":	ui.pocket3DStartHeightE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepDown":		ui.pocket3DStepDownE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepOver":		ui.pocket3DStepOverE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "OffsetFromPerimeter":	ui.pocket3DOffsetFromPerimeterE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "MillingMethod":
					if p[2] == "Conventional": ui.pocket3DConventionalRB.setChecked(True)
					elif p[2] == "Climb":   ui.pocket3DClimbRB.setChecked(True)
					else: ui.pocket3DEitherRB.setChecked(True)
				if p[1] == "MaximumError":	ui.pocket3DMaximumErrorE.setText(VAL.fromSystemValue('length',p[2]))
		elif cutType == "Volume3D":
			for p in props:
				if p[1] == "ObjectToCut":	ui.volume3DObjectToCutCB.setCurrentIndex(ui.volume3DObjectToCutCB.findText(p[2]))
				if p[1] == "CutArea":		ui.volume3DCutAreaCB.setCurrentIndex(ui.volume3DCutAreaCB.findText(p[2]))
				if p[1] == "StartHeight":	ui.volume3DStartHeightE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepDown":		ui.volume3DStepDownE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "StepOver":		ui.volume3DStepOverE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "OffsetFromPerimeter":	ui.volume3DOffsetFromPerimeterE.setText(VAL.fromSystemValue('length',p[2]))
				if p[1] == "MillingMethod":
					if p[2] == "Conventional": ui.volume3DConventionalRB.setChecked(True)
					elif p[2] == "Climb":   ui.volume3DClimbRB.setChecked(True)
					else: ui.volume3DEitherRB.setChecked(True)
				if p[1] == "MaximumError":	ui.volume3DMaximumErrorE.setText(VAL.fromSystemValue('length',p[2]))
					
	def accept(self):
		ui = self.createCutUi
		ui.hide()
		setStatus('hidden')
		p = self.setCutProperties()
		mode = getGUIMode()
		if mode in ["AddingCutFromGUI", "EditingCutFromGUI"]:
			setGUIProperties(p)
			return True
		elif mode == "AddingCutFromIcon":
			for prop in p:
				if prop[1] == "CutType":
					if prop[2] == "Registration": self.cut = RegistrationCut(self.selectedObject)
					elif prop[2] == "Drill": self.cut = DrillCut(self.selectedObject)
					elif prop[2] == "Facing": self.cut = FaceCut(self.selectedObject)
					elif prop[2] == "Perimeter": self.cut = PerimeterCut(self.selectedObject)
					elif prop[2] == "Pocket2D": self.cut = Pocket2DCut(self.selectedObject)
					elif prop[2] == "Volume2D": self.cut = Volume2DCut(self.selectedObject)	
					elif prop[2] == "Pocket3D": self.cut = Pocket3DCut(self.selectedObject)				
					elif prop[2] == "Volume3D": self.cut = Volume3DCut(self.selectedObject)				
					else: self.cut = Cut(self.selectedObject)
			self.cut.getObject().Label = ui.nameLE.text()
			self.cut.setProperties(p,self.cut.getObject())
			setGUIMode("None")
			return True				
		elif mode == "EditingCutFromIcon":
			self.cut = self.selectedObject.Proxy
			self.cut.Label = ui.nameLE.text()
			print p
			self.cut.setProperties(p,self.selectedObject)
			setGUIMode("None")
			return True
		else:
			print "unexpected mode (" + mode + ")"

		return False
				
	def reject(self):
		ui = self.createCutUi
		ui.hide()
		setGUIMode('None')
		setStatus('hidden')
		return False

	def onCutTypeChanged(self):
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
		
		ui.perimeterObjectToCutCB.setCurrentIndex(0)
		ui.perimeterDepthE.clear()
		ui.perimeterDepthOfCutE.clear()
		ui.perimeterStartHeightE.clear()
		ui.perimeterStepDownE.clear()
		ui.perimeterWidthOfCutE.clear()
		ui.perimeterStepOverE.clear()
		ui.perimeterOffsetE.clear()
		ui.perimeterInsideRB.setChecked(False)
		ui.perimeterOutsideRB.setChecked(False)
		ui.perimeterConventionalRB.setChecked(False)
		ui.perimeterClimbRB.setChecked(False)
		ui.perimeterEitherRB.setChecked(False)
		ui.perimeterErrorE.clear()
		
		ui.pocket2DObjectCB.setCurrentIndex(0)
		ui.pocket2DPerimeterDepthE.clear()
		ui.pocket2DDepthOfCutE.clear()
		ui.pocket2DStartHeightE.clear()
		ui.pocket2DStepDownE.clear()
		ui.pocket2DStepOverE.clear()
		ui.pocket2DOffsetFromPerimeterE.clear()
		ui.pocket2DConventionalRB.setChecked(False)
		ui.pocket2DClimbRB.setChecked(False)
		ui.pocket2DEitherRB.setChecked(False)
		ui.pocket2DMaximumErrorE.clear()

		ui.volume2DObjectToCutCB.setCurrentIndex(0)
		ui.volume2DPerimeterDepthE.clear()
		ui.volume2DDepthOfCutE.clear()
		ui.volume2DStartHeightE.clear()
		ui.volume2DStepDownE.clear()
		ui.volume2DStepOverE.clear()
		ui.volume2DOffsetFromPerimeterE.clear()
		ui.volume2DConventionalRB.setChecked(False)
		ui.volume2DClimbRB.setChecked(False)
		ui.volume2DEitherRB.setChecked(False)
		ui.volume2DMaximumErrorE.clear()
		
		ui.pocket3DObjectToCutCB.setCurrentIndex(0)
		ui.pocket3DStartHeightE.clear()
		ui.pocket3DStepDownE.clear()
		ui.pocket3DStepOverE.clear()
		ui.pocket3DOffsetFromPerimeterE.clear()
		ui.pocket3DConventionalRB.setChecked(False)
		ui.pocket3DClimbRB.setChecked(False)
		ui.pocket3DEitherRB.setChecked(False)
		ui.pocket3DMaximumErrorE.clear()

		ui.volume3DObjectToCutCB.setCurrentIndex(0)
		ui.volume3DCutAreaCB.setCurrentIndex(0)
		ui.volume3DStartHeightE.clear()
		ui.volume3DStepDownE.clear()
		ui.volume3DStepOverE.clear()
		ui.volume3DOffsetFromPerimeterE.clear()
		ui.volume3DConventionalRB.setChecked(False)
		ui.volume3DClimbRB.setChecked(False)
		ui.volume3DEitherRB.setChecked(False)
		ui.volume3DMaximumErrorE.clear()

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
			if obj.MillingMethod == "Conventional": ui.faceConventionalRB.setChecked(True)
			elif obj.MillingMethod == "Climb": ui.faceClimbRB.setChecked(True)
			else: ui.faceEitherRB.setChecked(True)
		elif obj.CutType == "Perimeter":
			ui.perimeterObjectToCutCB.setCurrentIndex(ui.perimeterObjectToCutCB.findText(obj.ObjectToCut))
			ui.perimeterDepthE.setText(VAL.fromSystemValue('length',obj.Depth))
			ui.perimeterDepthOfCutE.setText(VAL.fromSystemValue('length',obj.DepthOfCut))
			ui.perimeterStartHeightE.setText(VAL.fromSystemValue('length',obj.StartHeight))
			ui.perimeterStepDownE.setText(VAL.fromSystemValue('length',obj.StepDown))
			ui.perimeterWidthOfCutE.setText(VAL.fromSystemValue('length',obj.WidthOfCut))
			ui.perimeterStepOverE.setText(VAL.fromSystemValue('length',obj.StepOver))
			ui.perimeterOffsetE.setText(VAL.fromSystemValue('length',obj.Offset))
			if obj.MillingMethod == "Conventional": ui.perimeterConventionalRB.setChecked(True)
			elif obj.MillingMethod == "Climb": ui.perimeterClimbRB.setChecked(True)
			else: ui.perimeterEitherRB.setChecked(True)
			if obj.Side == "Inside": ui.perimeterInsideRB.setChecked(True)
			else: ui.perimeterOutsideRB.setChecked(True)
			ui.perimeterErrorE.setText(VAL.fromSystemValue('length',obj.MaximumError))
		elif obj.CutType == "Pocket2D":
			ui.pocket2DObjectCB.setCurrentIndex(ui.pocket2DObjectCB.findText(obj.ObjectToCut))
			ui.pocket2DPerimeterDepthE.setText(VAL.fromSystemValue('length',obj.PerimeterDepth))
			ui.pocket2DDepthOfCutE.setText(VAL.fromSystemValue('length',obj.DepthOfCut))
			ui.pocket2DStartHeightE.setText(VAL.fromSystemValue('length',obj.StartHeight))
			ui.pocket2DStepDownE.setText(VAL.fromSystemValue('length',obj.StepDown))
			ui.pocket2DStepOverE.setText(VAL.fromSystemValue('length',obj.StepOver))
			ui.pocket2DPerimeterDepthE.setText(VAL.fromSystemValue('length',obj.PerimeterDepth))
			ui.pocket2DOffsetFromPerimeterE.setText(VAL.fromSystemValue('length',obj.OffsetFromPerimeter))
			if obj.MillingMethod == "Conventional": ui.pocket2DConventionalRB.setChecked(True)
			elif obj.MillingMethod == "Climb": ui.pocket2DClimbRB.setChecked(True)
			else: ui.pocket2DEitherRB.setChecked(True)
			ui.pocket2DMaximumErrorE.setText(VAL.fromSystemValue('length',obj.MaximumError))
		elif obj.CutType == "Volume2D":
			ui.volume2DObjectToCutCB.setCurrentIndex(ui.volume2DObjectToCutCB.findText(obj.ObjectToCut))
			ui.volume2DCutAreaCB.setCurrentIndex(ui.volume2DCutAreaCB.findText(obj.ObjectToCut))
			ui.volume2DPerimeterDepthE.setText(VAL.fromSystemValue('length',obj.PerimeterDepth))
			ui.volume2DDepthOfCutE.setText(VAL.fromSystemValue('length',obj.DepthOfCut))
			ui.volume2DStartHeightE.setText(VAL.fromSystemValue('length',obj.StartHeight))
			ui.volume2DStepDownE.setText(VAL.fromSystemValue('length',obj.StepDown))
			ui.volume2DStepOverE.setText(VAL.fromSystemValue('length',obj.StepOver))
			ui.volume2DPerimeterDepthE.setText(VAL.fromSystemValue('length',obj.PerimeterDepth))
			ui.volume2DOffsetFromPerimeterE.setText(VAL.fromSystemValue('length',obj.OffsetFromPerimeter))
			if obj.MillingMethod == "Conventional": ui.volume2DConventionalRB.setChecked(True)
			elif obj.MillingMethod == "Climb": ui.volume2DClimbRB.setChecked(True)
			else: ui.volume2DEitherRB.setChecked(True)
			ui.volume2DMaximumErrorE.setText(VAL.fromSystemValue('length',obj.MaximumError))
		elif obj.CutType == "Pocket3D":
			ui.pocket3DObjectToCutCB.setCurrentIndex(ui.pocket3DObjectToCutCB.findText(obj.ObjectToCut))
			ui.pocket3DStartHeightE.setText(VAL.fromSystemValue('length',obj.StartHeight))
			ui.pocket3DStepDownE.setText(VAL.fromSystemValue('length',obj.StepDown))
			ui.pocket3DStepOverE.setText(VAL.fromSystemValue('length',obj.StepOver))
			ui.pocket3DOffsetFromPerimeterE.setText(VAL.fromSystemValue('length',obj.OffsetFromPerimeter))
			if obj.MillingMethod == "Conventional": ui.pocket3DConventionalRB.setChecked(True)
			elif obj.MillingMethod == "Climb": ui.pocket3DClimbRB.setChecked(True)
			else: ui.pocket3DEitherRB.setChecked(True)
			ui.pocket3DMaximumErrorE.setText(VAL.fromSystemValue('length',obj.MaximumError))
		elif obj.CutType == "Volume3D":
			ui.volume3DObjectToCutCB.setCurrentIndex(ui.volume3DObjectToCutCB.findText(obj.ObjectToCut))
			ui.volume3DCutAreaCB.setCurrentIndex(ui.volume3DCutAreaCB.findText(obj.CutArea))
			ui.volume3DStartHeightE.setText(VAL.fromSystemValue('length',obj.StartHeight))
			ui.volume3DStepDownE.setText(VAL.fromSystemValue('length',obj.StepDown))
			ui.volume3DStepOverE.setText(VAL.fromSystemValue('length',obj.StepOver))
			ui.volume3DOffsetFromPerimeterE.setText(VAL.fromSystemValue('length',obj.OffsetFromPerimeter))
			if obj.MillingMethod == "Conventional": ui.volume3DConventionalRB.setChecked(True)
			elif obj.MillingMethod == "Climb": ui.volume3DClimbRB.setChecked(True)
			else: ui.volume3DEitherRB.setChecked(True)
			ui.volume3DMaximumErrorE.setText(VAL.fromSystemValue('length',obj.MaximumError))
		
	def Activated(self):
		self.setUnits()
		ui = self.createCutUi
		self.reset()
		if hasattr(FreeCAD.ActiveDocument,"Objects"):
			while ui.faceCutAreaCB.count() > 1: ui.faceCutAreaCB.removeItem(1)
			while ui.perimeterObjectToCutCB.count() > 1: ui.perimeterObjectToCutCB.removeItem(1)
			while ui.pocket2DObjectCB.count() > 1: ui.pocket2DObjectCB.removeItem(1)
			while ui.volume2DObjectToCutCB.count() > 1: ui.volume2DObjectToCutCB.removeItem(1)
			while ui.volume2DCutAreaCB.count() > 1: ui.volume2DCutAreaCB.removeItem(1)
			while ui.pocket3DObjectToCutCB.count() > 1: ui.pocket3DObjectToCutCB.removeItem(1)
			while ui.volume3DObjectToCutCB.count() > 1: ui.volume3DObjectToCutCB.removeItem(1)
			while ui.volume3DCutAreaCB.count() > 1: ui.volume3DCutAreaCB.removeItem(1)
			for obj in FreeCAD.ActiveDocument.Objects:
				if hasattr(obj,"Shape"):
					ui.faceCutAreaCB.addItem(obj.Label)
					ui.perimeterObjectToCutCB.addItem(obj.Label)
					ui.pocket2DObjectCB.addItem(obj.Label)
					ui.volume2DObjectToCutCB.addItem(obj.Label)
					ui.volume2DCutAreaCB.addItem(obj.Label)		
					ui.pocket3DObjectToCutCB.addItem(obj.Label)
					ui.volume3DObjectToCutCB.addItem(obj.Label)
					ui.volume3DCutAreaCB.addItem(obj.Label)
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
			for tool in group:
				ui.toolCB.addItem(str(tool.Number) + " " + tool.Label)
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
