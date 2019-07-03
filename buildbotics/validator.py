from PySide import QtGui, QtCore
import FreeCAD, FreeCADGui

		
class MyIntValidator(QtGui.QIntValidator):
   def __init__(self, parent=None):
      super(MyIntValidator, self).__init__(1,999999)

   def validate(self, text, pos):
      if (pos == 1):
         if text == "0":
            return(QtGui.QValidator.Invalid)
      return super(MyIntValidator,self).validate(text,pos)

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

 
