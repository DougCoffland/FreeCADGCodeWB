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
import math

class ViewCut:
	def __init__(self,obj):
		obj.Proxy = self
		
	def attach(self,obj):
		self.ViewObject = obj
		self.Object = obj.Object
		return
		
	def attach(self, vobj):
		self.standard = coin.SoGroup()
		vobj.addDisplayMode(self.standard,"Standard");
		
	def getDisplayModes(self,obj):
		return ["Standard"]
	
	def getDefaultDisplayMode(self):
		return "Standard"
	
	def __getstate__(self):
		return None
		
	def __setstate__(self,state):
		return

	def getIcon(self):
		return ""
					
class Cut():
	def __init__(self,selectedObject):
		obj = FreeCAD.ActiveDocument.addObject('App::FeaturePython', "Cut")
		obj.Proxy = self
		self.obj = obj
		selectedObject.addObject(self.obj)
		self.outputUnits = ""
		
	def getObject(self):
		return self.obj
		
	def writeGCodeLine(self,line):
		self.fp.write(line + '\n')
		try:
			lc = int(self.ui.lcL.text())
		except:
			lc = 0
		self.ui.lcL.setText(str(lc + 1))		
		
	def run(self):
		print "running cut"
		
	def cut(self,x=None,y=None,z=None):
		line = 'G1'
		if x != None: line = line + 'X' + str(self.toOutputUnits(x,'length') + self.xOff)
		if y != None: line = line + 'Y' + str(self.toOutputUnits(y,'length') + self.yOff)
		if z != None: line = line + 'Z' + str(self.toOutputUnits(z,'length') + self.zOff)
		self.writeGCodeLine(line)

	def rapid(self,x=None,y=None,z=None):
		line = 'G0'
		if x != None: line = line + 'X' + str(self.toOutputUnits(x,'length') + self.xOff)
		if y != None: line = line + 'Y' + str(self.toOutputUnits(y,'length') + self.yOff)
		if z != None: line = line + 'Z' + str(self.toOutputUnits(z,'length') + self.zOff)
		self.writeGCodeLine(line)
		
	def setProperties(self,p,obj):
		if hasattr(obj,'PropertiesList'):
			for prop in obj.PropertiesList:
				obj.removeProperty(prop)
		for prop in p:
			newprop = obj.addProperty(prop[0],prop[1])
			setattr(newprop,prop[1],prop[2])
		obj.Label = obj.CutName

		ViewCut(obj.ViewObject)

		for prop in obj.PropertiesList:
			obj.setEditorMode(prop,("ReadOnly",))
		FreeCAD.ActiveDocument.recompute()
		
	def setUserUnits(self):
		userPref = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema")
		def setUnits(l,t,v):
			self.userLengthUnit = l
			self.userTimeUnit = t
			self.userVelocityUnit = v
		if userPref in [0,1]: setUnits('mm','s','mm/s')
		elif userPref == 2: setUnits('m', 's', 'm/s')
		elif userPref in [3,4]: setUnits('in','min','ipm')
		elif userPref == 6: setUnits('mm','min','mm/min')
		else:
			print "WARNING: units unknown"
			setUnits('mm','s','mm/s')
			
	def toOutputUnits(self,s,form):
		if hasattr(s,"UserString") == False: return s
		s = s.UserString
		sUnit = s.lstrip('-+0123456789.e\ ')
		sValue = eval(s[:len(s) - len(sUnit)])
		sUnit = sUnit.strip()
		if sUnit == "":
			if form == 'velocity': sUnit = self.userVelocityUnit
			elif form == 'length': sUnit = self.userLengthUnit
			elif form == 'time': sUnit = self.userTimeUnit
		if self.outputUnits == 'METRIC':
			if form == 'length':
				if sUnit in ['"','in']: sValue = sValue * 25.4
				elif sUnit in ["'",'f','ft']: sValue = sValue * 25.4 * 12
				elif sUnit == 'm': sValue = SValue * 1000
			elif form == 'velocity':
				if sUnit in ['mm/sec', 'mm/s', 'mmps']: sValue = sValue / 60
				elif sUnit in ['m/min', 'm/m', 'mpm']: sValue = sValue * 1000
				elif sUnit in ['m/s', 'm/sec', 'mps']: sValue = sValue * 1000 * 60
				elif sUnit in ['in/m','in/min', '"/m','"/min', 'ipm']: sValue = sValue * 25.4
				elif sUnit in ['in/sec','in/s','"/s','"/sec', 'ips']: sValue = sValue * 25.4 * 60
				elif sUnit in ['f/s', 'ft/sec', 'fps']: sValue = sValue * 12 * 25.4 * 60
				elif sUnit in ['ft/m', 'ft/min', 'fpm']: sValue = sValue * 12 * 25.4
				elif sUnit == 'kph': sValue = sValue * 1,000,000 / 60
				elif sUnit == 'mph': sValue = sValue * 5280 * 12 * 25.4 / 60
		else:
			if form == 'length':
				if sUnit == 'mm': sValue = sValue / 25.4
				elif sUnit == 'm': sValue = sValue * 39.37
				elif sUnit in ['f', 'ft', "'"]: sValue = sValue * 12
			elif form == 'velocity':
				if sUnit in ['mm/min','mm/m','mmpm']: sValue = sValue / 25.4
				elif sUnit in ['mm/sec', 'mm/s', 'mmps']: sValue = sValue / 25.4 * 60
				elif sUnit in ['m/min', 'm/m', 'mpm']: sValue = sValue * 39.37
				elif sUnit in ['m/s', 'm/sec', 'mps']: sValue = sValue * 39.37 * 60
				elif sUnit in ['in/sec','in/s','"/s','"/sec', 'ips']: sValue = sValue * 60
				elif sUnit in ['f/s', 'ft/sec', 'fps']: sValue = sValue * 12 * 60
				elif sUnit in ['ft/m', 'ft/min', 'fpm']: sValue = sValue * 12
				elif sUnit == 'kph': sValue = sValue * 1000 * 39.37 / 60
				elif sUnit == 'mph': sValue = sValue * 5280 * 12 / 60
		if form == 'time':
			if sUnit in ['s', 'sec']: sValue = sValue / 60
			if sUnit in ['hr', 'hour']: sValue = sValue * 60			
		elif form == 'angularVelocity':
			if sUnit in ['rps', 'r/s', 'r/sec', 'rev/s', 'rev/sec']: sValue = sValue / 60
		elif form == 'angle':
			if sUnit in ['rad', 'r', 'radian', 'radians']: sValue = sValue / math.pi
		return sValue
				
	def resetOffset(self):
		self.xOff = 0.
		self.yOff = 0.
		self.zOff = 0.

	def setOffset(self, origin):
		self.xOff = self.toOutputUnits(origin[0],'length')
		self.yOff = self.toOutputUnits(origin[1],'length')
		self.zOff = self.toOutputUnits(origin[2],'length')		
		
	def __getstate__(self):
		state = {}
		state["props"] = []
		return state
		
	def __setstate__(self, state):
		return		
	
	def IsActive(self):
		return True
		
	def execute(self,obj):
		return True
