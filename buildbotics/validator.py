from PySide import QtGui, QtCore
import FreeCAD, FreeCADGui

def setLabel(label,color):
	label.setStyleSheet("QLabel {background-color: " + color + "}")
	
def isfloat(s):
	try:
		float(s)
		return True
	except:
		return False
		
def validate(edit, label, args):
	s = edit.text().lower().strip()
	if len(s) == 0:
		setLabel(label,'red')
		return "INVALID"
	i = len(s)
	while i > 0:
		if isfloat(s[0:i]) is True: break
		else: i = i - 1
	val = s[0:i]
	if val == "":
		setLabel(label,'red')
		return "INVALID"
	s = s.strip()[i:]
	if len(s) == 0:
		setLabel(label,'white')
		return 'VALID'
	try:
		args.index(s)
		setLabel(label,'white')
		return 'VALID'
	except:
		setLabel(label,'red')
		return 'INVALID'

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

"""		
class MyDoubleValidator(QtGui.QDoubleValidator):
   def __init__(self, parent=None):
      super(MyDoubleValidator, self).__init__()
      super(MyDoubleValidator,self).setBottom(0.0)

   def validate(self, text, pos):
      if (pos == 1):
         if text == "-":
            return(QtGui.QValidator.Invalid)
      return super(MyDoubleValidator,self).validate(text,pos)
      
def setComboBoxLabelBG(combo, label):
	if combo.currentIndex() == 0:
		label.setStyleSheet("QLabel {background-color: red}")
		return False
	label.setStyleSheet("QLabel {background-color: rgb(238, 238, 236)}")
	return True

def setLineEditLabelBG(edit, label):
	if edit.text().strip() == "":
		label.setStyleSheet("QLabel {background-color: red}")
		return False
	label.setStyleSheet("QLabel {background-color: rgb(238, 238, 236)}")
	return True
"""
 
