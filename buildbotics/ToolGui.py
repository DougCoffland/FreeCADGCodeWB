
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

from Tool import Tool
import validator as VAL

ANGULAR_VELOCITY = ['rpm', 'r/m', 'rev/m','rev/min', 'rps', 'r/s', 'r/sec', 'rev/s', 'rev/sec']
VELOCITY = ['mm/min','mm/m','mmpm',
			'mm/sec', 'mm/s', 'mmps',
			'm/min', 'm/m', 'mpm',
			'm/s', 'm/sec', 'mps',
            'in/m','in/min', '"/m',"/min", 'ipm',
            'in/sec','in/s','"/s','"/sec', 'ips',
            'f/s', 'ft/sec', 'fps',
            'ft/m', 'ft/min', 'fpm',
            'kph',
            'mph']
LENGTH = ['mm',
		  'm',
		  'in', '"',
		  'f', 'ft', "'"]
ANGLE = ['degree', 'degrees','deg', 'd', 'rad', 'r', 'radian', 'radians']

class ToolGui():
	def __init__(self):			
		self.createToolUi = FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + "/resources/ui/tool.ui")
		
		self.straightToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/straightBitPic.png")				
		self.taperedToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/taperedBitPic.png")				
		self.conicalToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/conicalBitPic.png")				
		self.ballToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/ballBitPic.png")				
		self.taperedBallToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/taperedBallBitPic.png")
		
		self.toolTypes = ["StraightTool", "TaperedTool","ConicalTool", "BallTool", "TaperedBallTool"]
		
		ui = self.createToolUi
		iv = VAL.MyIntValidator()

		ui.numberEdit.setValidator(iv)
		ui.feedRateEdit.textChanged.connect(lambda: VAL.validate(ui.feedRateEdit,ui.feedRateL,VELOCITY))
		ui.plungeRateEdit.textChanged.connect(lambda: VAL.validate(ui.plungeRateEdit,ui.plungeRateL,VELOCITY))
		ui.spindleSpeedEdit.textChanged.connect(lambda: VAL.validate(ui.spindleSpeedEdit,ui.spindleSpeedLabel,ANGULAR_VELOCITY))
		ui.stepOverEdit.textChanged.connect(lambda: VAL.validate(ui.stepOverEdit,ui.stepOverL,LENGTH))
		ui.depthOfCutEdit.textChanged.connect(lambda: VAL.validate(ui.depthOfCutEdit,ui.docL,LENGTH))
		
		ui.straightDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.straightDiameterEdit,ui.straightDiameterL,LENGTH))
		ui.straightCutLengthEdit.textChanged.connect(lambda: VAL.validate(ui.straightCutLengthEdit,ui.straightCutLenL,LENGTH))
		ui.straightToolLengthEdit.textChanged.connect(lambda: VAL.validate(ui.straightToolLengthEdit,ui.straightToolLenL,LENGTH))
		ui.straightShaftDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.straightShaftDiameterEdit,ui.staightShaftDiameterL,LENGTH))

		ui.taperedTopDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.taperedTopDiameterEdit,ui.taperedTopDiameterL,LENGTH))
		ui.taperedBottomDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.taperedBottomDiameterEdit,ui.taperedBottomDiameterL,LENGTH))
		ui.taperedCutLengthEdit.textChanged.connect(lambda: VAL.validate(ui.taperedCutLengthEdit,ui.taperedCutLengthL,LENGTH))
		ui.taperedToolLengthEdit.textChanged.connect(lambda: VAL.validate(ui.taperedToolLengthEdit,ui.taperedToolLengthL,LENGTH))
		ui.taperedShaftDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.taperedShaftDiameterEdit,ui.taperedShaftDiameterL,LENGTH))

		ui.conicalTopDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.conicalTopDiameterEdit,ui.conicalTopDiameterL,LENGTH))
		ui.conicalCutAngleEdit.textChanged.connect(lambda: VAL.validate(ui.conicalCutAngleEdit,ui.conicalCutAngleL,ANGLE))
		ui.conicalToolLengthEdit.textChanged.connect(lambda: VAL.validate(ui.conicalToolLengthEdit,ui.conicalToolLengthL,LENGTH))
		ui.conicalShaftDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.conicalShaftDiameterEdit,ui.conicalShaftDiameterL,LENGTH))

		ui.ballDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.ballDiameterEdit,ui.ballDiameterL,LENGTH))
		ui.ballToolLengthEdit.textChanged.connect(lambda: VAL.validate(ui.ballToolLengthEdit,ui.ballToolLengthL,LENGTH))
		ui.ballShaftDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.ballShaftDiameterEdit,ui.ballShaftDiameterL,LENGTH))

		ui.taperedBallTopDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.taperedBallTopDiameterEdit,ui.taperedBallTopDiameterL,LENGTH))
		ui.taperedBallDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.taperedBallDiameterEdit,ui.taperedBallBallDiameterL,LENGTH))
		ui.taperedBallCutLengthEdit.textChanged.connect(lambda: VAL.validate(ui.taperedBallCutLengthEdit,ui.taperedBallCutLengthL,LENGTH))
		ui.taperedBallToolLengthEdit.textChanged.connect(lambda: VAL.validate(ui.taperedBallToolLengthEdit,ui.TaperedBallToolLengthL,LENGTH))
		ui.taperedBallShaftDiameterEdit.textChanged.connect(lambda: VAL.validate(ui.taperedBallShaftDiameterEdit,ui.taperedBallShaftDiameterL,LENGTH))
				
		ui.buttonBox.accepted.connect(self.accept)
		ui.buttonBox.rejected.connect(self.reject)
		ui.toolTypeCB.currentIndexChanged.connect(self.changeToolTypeWidget)
		
	def reset(self):
		ui = self.createToolUi
		ui.stackedWidget.setCurrentIndex(0)       
		ui.nameEdit.clear()
		ui.numberEdit.clear()
		ui.makeEdit.clear()
		ui.modelEdit.clear()
		ui.toolTypeCB.setCurrentIndex(0)
		ui.materialEdit.clear()
		ui.feedRateEdit.clear()
		ui.plungeRateEdit.clear()
		ui.spindleSpeedEdit.clear()
		ui.stepOverEdit.clear()
		ui.depthOfCutEdit.clear()
		ui.straightDiameterEdit.clear()
		ui.straightCutLengthEdit.clear()
		ui.straightToolLengthEdit.clear()
		ui.straightShaftDiameterEdit.clear()
		ui.taperedTopDiameterEdit.clear()
		ui.taperedBottomDiameterEdit.clear()
		ui.taperedCutLengthEdit.clear()
		ui.taperedToolLengthEdit.clear()
		ui.taperedShaftDiameterEdit.clear()
		ui.conicalTopDiameterEdit.clear()
		ui.conicalCutAngleEdit.clear()
		ui.conicalToolLengthEdit.clear()
		ui.conicalShaftDiameterEdit.clear()
		ui.ballDiameterEdit.clear()
		ui.ballToolLengthEdit.clear()
		ui.ballShaftDiameterEdit.clear()
		ui.taperedBallTopDiameterEdit.clear()
		ui.taperedBallDiameterEdit.clear()
		ui.taperedBallCutLengthEdit.clear()
		ui.taperedBallToolLengthEdit.clear()
		ui.taperedBallShaftDiameterEdit.clear()
		
	def GetResources(self):
		return {'Pixmap'  : os.path.dirname(__file__) +  "/resources/svg/tool.svg", # the name of a svg file available in the resources
                'MenuText': "New Tool",
                'ToolTip' : "Sets up a new tool that can be added to a tool table"}
                
	def changeToolTypeWidget(self):
		i = self.createToolUi.toolTypeCB.currentIndex()
		self.createToolUi.stackedWidget.setCurrentIndex(i)
		if i == 1: self.createToolUi.imageLabel.setPixmap(self.straightToolPic)
		elif i == 2: self.createToolUi.imageLabel.setPixmap(self.taperedToolPic)
		elif i == 3: self.createToolUi.imageLabel.setPixmap(self.conicalToolPic)
		elif i == 4: self.createToolUi.imageLabel.setPixmap(self.ballToolPic)
		elif i == 5: self.createToolUi.imageLabel.setPixmap(self.taperedBallToolPic)
		else: self.createToolUi.imageLabel.setPixmap(None)
		
	def setUnits(self):
		ui = self.createToolUi
		if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema") in [0, 1, 4, 6]:
			self.units = 'mm'
			ui.unitsLabel.setText("Default units are mm, mm/min, and rpm")
		else:
			ui.unitsLabel.setText("Default units are in, in/min, and rpm")
			self.units = 'in'

	def getToolProperties(self,obj):
		ui = self.createToolUi
		if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema") in [0, 1, 4, 6]: units = 1
		else: units = 1/25.4
		
		ui.stackedWidget.setCurrentIndex(self.toolTypes.index(obj.ObjectType) + 1)      
		ui.nameEdit.setText(obj.Label)
		ui.numberEdit.setText(str(obj.Number))
		ui.makeEdit.setText(obj.Make)
		ui.modelEdit.setText(obj.Model)
		ui.toolTypeCB.setCurrentIndex(self.toolTypes.index(obj.ObjectType) + 1)
		ui.materialEdit.setText(obj.StockMaterial)
		ui.feedRateEdit.setText(obj.FeedRate.UserString)
		ui.plungeRateEdit.setText(obj.PlungeRate.UserString)
		ui.spindleSpeedEdit.setText(obj.SpindleSpeed)
		ui.stepOverEdit.setText(obj.StepOver.UserString)
		ui.depthOfCutEdit.setText(obj.DepthOfCut.UserString)
		
		toolType = ui.toolTypeCB.currentText()
		if toolType == "Straight":		
			ui.straightDiameterEdit.setText(obj.Diameter.UserString)
			ui.straightCutLengthEdit.setText(obj.CutLength.UserString)
			ui.straightToolLengthEdit.setText(obj.ToolLength.UserString)
			ui.straightShaftDiameterEdit.setText(obj.ShaftDiameter.UserString)
		elif toolType == "Tapered":
			ui.taperedTopDiameterEdit.setText(obj.TopDiameter.UserString)
			ui.taperedBottomDiameterEdit.setText(obj.BottomDiameter.UserString)
			ui.taperedCutLengthEdit.setText(obj.CutLength.UserString)
			ui.taperedToolLengthEdit.setText(obj.ToolLength.UserString)
			ui.taperedShaftDiameterEdit.setText(obj.ShaftDiameter.UserString)
		elif toolType == "Conical":
			ui.conicalTopDiameterEdit.setText(obj.TopDiameter.UserString)
			ui.conicalCutAngleEdit.setText(obj.CutAngle.UserString)
			ui.conicalToolLengthEdit.setText(obj.ToolLength.UserString)
			ui.conicalShaftDiameterEdit.setText(obj.ShaftDiameter.UserString)
		elif toolType == "Ball":
			ui.ballDiameterEdit.setText(obj.BallDiameter.UserString)
			ui.ballToolLengthEdit.setText(obj.ToolLength.UserString)
			ui.ballShaftDiameterEdit.setText(obj.ShaftDiameter.UserString)
		elif toolType == "TaperedBall":
			ui.taperedBallTopDiameterEdit.setText(obj.TopDiameter.UserString)
			ui.taperedBallDiameterEdit.setText(obj.BallDiameter.UserString)
			ui.taperedBallCutLengthEdit.setText(obj.CutAngle.UserString)
			ui.taperedBallToolLengthEdit.setText(obj.ToolLength.UserString)
			ui.taperedBallShaftDiameterEdit.setText(obj.ShaftDiameter.UserString)		
					
	def setToolProperties(self, obj):
		ui = self.createToolUi
		if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema") in [0, 1, 4, 6]: units = 1
		else: units = 25.4
		S = "App::PropertyString"
		I = "App::PropertyInteger"
		L = "App::PropertyLength"
		A = "App::PropertyAngle"
		V = "App::PropertySpeed"
		Q = "App::PropertyQuantity"
		tooltype = ui.toolTypeCB.currentText().replace(" ","")
		p = [[S,	"ObjectType",		tooltype + "Tool"],
			 [S,	"Name",				ui.nameEdit.text()],
		     [I,	"Number",			eval(ui.numberEdit.text())],
		     [S,	"Make",				ui.makeEdit.text()],
		     [S,	"Model",			ui.modelEdit.text()],
		     [S,	"ToolType",			tooltype],
		     [S,	"StockMaterial",	ui.materialEdit.text()],
		     [V,	"FeedRate",			VAL.toSystemValue(ui.feedRateEdit, 'velocity')],
		     [V,	"PlungeRate",		VAL.toSystemValue(ui.plungeRateEdit, 'velocity')],
		     [S,	"SpindleSpeed",		VAL.toSystemValue(ui.spindleSpeedEdit, 'angularVelocity')],
		     [L,	"StepOver",			VAL.toSystemValue(ui.stepOverEdit, 'length')],
		     [L,	"DepthOfCut",		VAL.toSystemValue(ui.depthOfCutEdit, 'length')]]
		if tooltype == "Straight":
			p.append([L,			"Diameter",			VAL.toSystemValue(ui.straightDiameterEdit, 'length')])
			p.append([L,			"CutLength",		VAL.toSystemValue(ui.straightCutLengthEdit, 'length')])
			p.append([L,			"ToolLength",		VAL.toSystemValue(ui.straightToolLengthEdit, 'length')])
			p.append([L,			"ShaftDiameter",	VAL.toSystemValue(ui.straightShaftDiameterEdit, 'length')])
		elif tooltype == "Tapered":
			p.append([L,			"TopDiameter",		VAL.toSystemValue(ui.taperedTopDiameterEdit, 'length')])
			p.append([L,			"BottomDiameter",	VAL.toSystemValue(ui.taperedBottomDiameterEdit, 'length')])
			p.append([L,			"CutLength",		VAL.toSystemValue(ui.taperedCutLengthEdit, 'length')])
			p.append([L,			"ToolLength",		VAL.toSystemValue(ui.taperedToolLengthEdit, 'length')])
			p.append([L,			"ShaftDiameter",	VAL.toSystemValue(ui.taperedShaftDiameterEdit, 'length')])
		elif tooltype == "Conical":
			p.append([L,			"TopDiameter",		VAL.toSystemValue(ui.conicalTopDiameterEdit, 'length')])
			p.append([A,			"CutAngle",			VAL.toSystemValue(ui.conicalCutAngleEdit, 'angle')])
			p.append([L,			"ToolLength",		VAL.toSystemValue(ui.conicalToolLengthEdit, 'length')])						          	
			p.append([L,			"ShaftDiameter",	VAL.toSystemValue(ui.conicalShaftDiameterEdit, 'length')])
		elif tooltype == "Ball":
			p.append([L,			"BallDiameter",		VAL.toSystemValue(ui.ballDiameterEdit, 'length')])
			p.append([L,			"ToolLength",		VAL.toSystemValue(ui.ballToolLengthEdit, 'length')])
			p.append([L,			"ShaftDiameter",	VAL.toSystemValue(ui.ballShaftDiameterEdit, 'length')])
		elif tooltype == "TaperedBall":
			p.append([L,			"TopDiameter",		VAL.toSystemValue(ui.taperedBallTopDiameterEdit, 'length')])
			p.append([L,			"BallDiameter",		VAL.toSystemValue(ui.taperedBallDiameterEdit, 'length')])
			p.append([L,			"CutLength",		VAL.toSystemValue(ui.taperedBallCutLengthEdit, 'length')])
			p.append([L,			"ToolLength",		VAL.toSystemValue(ui.taperedBallToolLengthEdit, 'length')])
			p.append([L,			"ShaftDiameter",	VAL.toSystemValue(ui.taperedBallShaftDiameterEdit, 'length')])

		self.tool.setProperties(p, obj)				
		
	def Activated(self):
		self.setUnits()
		if self.selectedObject.ObjectType == "ToolTable":
			self.reset()
		elif self.selectedObject.ObjectType in self.toolTypes:
			self.getToolProperties(self.selectedObject)
		else:
			return False
		self.createToolUi.show()       
		return True
        
	def accept(self):
		ui = self.createToolUi
		ui.hide()
		if self.selectedObject.ObjectType == "ToolTable":
			self.tool = Tool(self.createToolUi, self.selectedObject)
			self.setToolProperties(self.selectedObject)
			return True
		elif self.selectedObject.ObjectType in self.toolTypes:
			self.tool = self.selectedObject.Proxy
			self.setToolProperties(self.selectedObject)
			
			return True
		return False
		
	def reject(self):
		self.createToolUi.hide()
		return False

	def IsActive(self):
		"""Here you can define if the command must be active or not (greyed) if certain conditions
		are met or not. This function is optional."""
		mw = FreeCADGui.getMainWindow()
		tree = mw.findChildren(QtGui.QTreeWidget)[0]
		if len(tree.selectedItems()) != 1: return False
		item = tree.selectedItems()[0]
		obj = FreeCAD.ActiveDocument.getObjectsByLabel(item.text(0))[0]
		if obj.ObjectType in ["ToolTable","StraightTool", "TaperedTool","ConicalTool", "BallTool", "TaperedBallTool"]:
			self.selectedObject = obj
			return True
		return False

FreeCADGui.addCommand('New_Tool',ToolGui())
