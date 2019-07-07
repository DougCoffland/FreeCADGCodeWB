
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
import validator

class ToolGui():
	def __init__(self):			
		self.createToolUi = FreeCADGui.PySideUic.loadUi(os.path.dirname(__file__) + "/resources/ui/tool.ui")
		
		self.straightToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/straightBitPic.png")				
		self.taperedToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/taperedBitPic.png")				
		self.conicalToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/conicalBitPic.png")				
		self.ballToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/ballBitPic.png")				
		self.taperedBallToolPic = QtGui.QPixmap(os.path.dirname(__file__) + "/resources/png/taperedBallBitPic.png")
		
		ui = self.createToolUi
		iv = validator.MyIntValidator()
		dv = validator.MyDoubleValidator()
		ui.numberEdit.setValidator(iv)
		ui.feedRateEdit.setValidator(dv)
		ui.plungeRateEdit.setValidator(dv)
		ui.spindleSpeedEdit.setValidator(dv)
		ui.stepOverEdit.setValidator(dv)
		ui.depthOfCutEdit.setValidator(dv)
		ui.straightDiameterEdit.setValidator(dv)
		ui.straightCutLengthEdit.setValidator(dv)
		ui.straightToolLengthEdit.setValidator(dv)
		ui.straightShaftDiameterEdit.setValidator(dv)
		ui.taperedTopDiameterEdit.setValidator(dv)
		ui.taperedBottomDiameterEdit.setValidator(dv)
		ui.taperedCutLengthEdit.setValidator(dv)
		ui.taperedToolLengthEdit.setValidator(dv)
		ui.taperedShaftDiameterEdit.setValidator(dv)
		ui.conicalTopDiameterEdit.setValidator(dv)
		ui.conicalCutAngleEdit.setValidator(dv)
		ui.conicalToolLengthEdit.setValidator(dv)
		ui.conicalShaftDiameterEdit.setValidator(dv)
		ui.ballDiameterEdit.setValidator(dv)
		ui.ballToolLengthEdit.setValidator(dv)
		ui.ballShaftDiameterEdit.setValidator(dv)
		ui.taperedBallTopDiameterEdit.setValidator(dv)
		ui.taperedBallDiameterEdit.setValidator(dv)
		ui.taperedBallCutLengthEdit.setValidator(dv)
		ui.taperedBallToolLengthEdit.setValidator(dv)
		ui.taperedBallShaftDiameterEdit.setValidator(dv)
							
		ui.buttonBox.accepted.connect(self.accept)
		ui.buttonBox.rejected.connect(self.reject)
		
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
		if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema") in [0, 1, 4, 6]: self.units = 'mm'
		else: self.units = 'in'

		ui.feedRateL.setText("Feed Rate (" + self.units + "/min)")
		ui.plungeRateL.setText("Plunge Feed Rate (" + self.units + "/min)")
		ui.stepOverL.setText("Step Over (" + self.units + "/min)")
		ui.docL.setText("Depth of Cut (" + self.units + ")")
			
		ui.straightDiameterL.setText("Diameter (" + self.units + ")")
		ui.straightCutLenL.setText("Cut Length (" + self.units + ")")
		ui.straightToolLenL.setText("Tool Length (" + self.units + ")")
		ui.staightShaftDiameterL.setText("Shaft Diameter (" + self.units + ")")
			
		ui.taperedTopDiameterL.setText("Top Diameter (" + self.units + ")")
		ui.taperedBottomDiameterL.setText("Bottom Diameter (" + self.units + ")")
		ui.taperedCutLengthL.setText("Cut Length (" + self.units + ")")
		ui.taperedToolLengthL.setText("Tool Length (" + self.units + ")")
		ui.taperedShaftDiameterL.setText("Shaft Diameter (" + self.units + ")")
			
		ui.conicalTopDiameterL.setText("Top Diameter (" + self.units + ")")
		ui.conicalCutAngleL.setText("Cut Angle (degrees)")
		ui.conicalToolLengthL.setText("Tool Length (" + self.units + ")")
		ui.conicalShaftDiameterL.setText("Shaft Diameter (" + self.units + ")")
			
		ui.ballDiameterL.setText("Ball Diameter (" + self.units + ")")
		ui.ballToolLengthL.setText("Tool Length (" + self.units + ")")
		ui.ballShaftDiameterL.setText("Shaft Diameter (" + self.units + ")")

		ui.taperedBallTopDiameterL.setText("Top Diameter (" + self.units + ")")
		ui.taperedBallBallDiameterL.setText("Ball Diameter (" + self.units + ")")
		ui.taperedBallCutLengthL.setText("Cut Length (" + self.units + ")")
		ui.taperedBallToolLengthL.setText("Tool Length (" + self.units + ")")
		ui.taperedBallShaftDiameterL.setText("Shaft Diameter (" + self.units + ")")
			

	def Activated(self):
		self.setUnits()
		self.createToolUi.toolTypeCB.currentIndexChanged.connect(self.changeToolTypeWidget) 
		self.createToolUi.stackedWidget.setCurrentIndex(0)       
		self.createToolUi.show()       
		return
        
	def accept(self):
		ui = self.createToolUi
		ui.hide()
		tool = Tool(self.createToolUi, self.ToolTable)
		return True
		
	def reject(self):
		self.createToolUi.hide()
		return False

	def IsActive(self):
		"""Here you can define if the command must be active or not (greyed) if certain conditions
		are met or not. This function is optional."""
		mw = FreeCADGui.getMainWindow()
		tree = mw.findChildren(QtGui.QTreeWidget)[0]
		numberOfInstances = 0
		for item in tree.selectedItems():
			obj = FreeCAD.ActiveDocument.getObjectsByLabel(item.text(0))[0]
			if obj.ObjectType == "ToolTable": 
				numberOfInstances += 1
				self.ToolTable = obj
		if numberOfInstances != 1: return False
		return True

FreeCADGui.addCommand('New_Tool',ToolGui())
