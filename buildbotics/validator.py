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
from PySide import QtGui, QtCore
import FreeCAD, FreeCADGui

ANGULAR_VELOCITY = ['rpm', 'r/m', 'rev/m','rev/min', 'rps', 'r/s', 'r/sec', 'rev/s', 'rev/sec']
VELOCITY = ['mm/min','mm/m','mmpm',
			'mm/sec', 'mm/s', 'mmps',
			'm/min', 'm/m', 'mpm',
			'm/s', 'm/sec', 'mps',
            'in/m','in/min', '"/m','"/min', 'ipm',
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

def setLabel(label,valid):
	if valid == 'INVALID':
		label.setStyleSheet("QLabel {background-color: red;}")
	else:
		label.setStyleSheet("")
	
def isfloat(s):
	try:
		float(s)
		return True
	except:
		return False
		
def validate(edit, label, required, valid, args):
	s = edit.text().lower().strip()
	if len(s) == 0 and required == True:
		setLabel(label,'INVALID')
		return False
	elif len(s) == 0 and required == False:
		setLabel(label, 'VALID')
		return valid
	i = len(s)
	while i > 0:
		if isfloat(s[0:i]) is True: break
		else: i = i - 1
	val = s[0:i]
	if val == "":
		setLabel(label,'INVALID')
		return False
	s = s.strip()[i:]
	if len(s) == 0:
		setLabel(label,'VALID')
		return valid
	try:
		args.index(s)
		setLabel(label,'VALID')
		return valid
	except:
		setLabel(label,'INVALID')
		return False

def fromSystemValue(form,value):
	if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema") in [0, 1, 4, 6]:
		userPref = 'METRIC'
	else:
		userPref = 'IMPERIAL'
	if form == 'velocity':
		if userPref == 'METRIC': return str(value)
		value = eval(str(value).split()[0])
		return str(round(value * 60 / 25.4, 2)) + ' in/min'
	elif form == 'length':
		if userPref == 'METRIC': return str(value)
		value = eval(str(value).split()[0])
		return str(round(value / 25.4,4)) + ' in'
	elif form == 'angle': return str(value)

def toSystemValue(edit,form):
	if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema") in [0, 1, 4, 6]:
		userPref = 'METRIC'
	else:
		userPref = 'IMPERIAL'
	s = edit.text().lower()
	s = ''.join(s.split())
	i = len(s)
	while i > 0:
		if isfloat(s[0:i]) is True: break
		else: i = i - 1
	val = s[0:i].strip()
	units = s[i:].strip()
	if form == "angularVelocity":
		if units in ['rps', 'r/s', 'r/sec', 'rev/s', 'rev/sec']:
			val = str(eval(val) * 60)
		return val + ' ' + 'rpm'
	elif form == "velocity":
		val = eval(val)
		if units in ['mm/min','mm/m','mmpm']: val = val / 60.
		elif units in ['m/min', 'm/m', 'mpm']: val = val * 1000 / 60.
		elif units in ['m/s', 'm/sec', 'mps']: val = val * 1000.
		elif units in ['in/m','in/min', '"/m','"/min', 'ipm']: val = val * 25.4 / 60
		elif units in ['in/sec','in/s','"/s','"/sec', 'ips']: val = val * 25.4
		elif units in ['f/s', 'ft/sec', 'fps']: val = val * 304.8
		elif units in ['ft/m', 'ft/min', 'fpm']: val = val * 304.8 / 60
		elif units == 'kph': val = val * 1,000,000 / 3600.
		elif units == 'mph': val = 5280 * 304.8 / 3600
		elif units == '' and userPref == 'IMPERIAL': val = val * 25.4 / 60
		return val
	elif form == "length":
		val = eval(val)
		if units == 'm': val = val * 1000.
		elif units in ['in', '"']: val = val * 25.4
		elif units in ['f', 'ft', "'"]: val = val * 304.8
		elif units == '' and userPref == 'IMPERIAL': val = val * 25.4
		return val
	elif form == "angle":
		val = eval(val)
		if units in ['rad', 'r', 'radian', 'radians']: val = val * 57.2958
		return val

class MyIntValidator(QtGui.QIntValidator):
   def __init__(self, parent=None):
      super(MyIntValidator, self).__init__(1,999999)

   def validate(self, text, pos):
      if (pos == 1):
         if text == "0":
            return(QtGui.QValidator.Invalid)
      return super(MyIntValidator,self).validate(text,pos)

 
