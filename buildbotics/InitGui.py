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
import os
import FreeCADGui

class BuildboticsWorkbench (Workbench):
	MenuText = "Buildbotics"
	ToolTip = "Buildbotics G-Code Path Maker"
	Icon = """
						/* XPM */
						static char * logo_only_XPM[] = {
						"16 15 35 1",
						" 	c None",
						".	c #F0A836",
						"+	c #EFA93D",
						"@	c #F0A838",
						"#	c #F0A837",
						"$	c #EDAB4B",
						"%	c #EFA839",
						"&	c #DD9936",
						"*	c #BC7D36",
						"=	c #C58436",
						"-	c #EEA636",
						";	c #EEA93E",
						">	c #ECAC52",
						",	c #EFA93B",
						"'	c #EEAA48",
						")	c #ECAD5B",
						"!	c #BD8145",
						"~	c #BE8A5B",
						"{	c #C8BBB1",
						"]	c #AEAAA7",
						"^	c #D99E5B",
						"/	c #C1B1A8",
						"(	c #A6A4A3",
						"_	c #D8B492",
						":	c #C5AF9D",
						"<	c #DB9B46",
						"[	c #C0A797",
						"}	c #B4A79F",
						"|	c #EFA93F",
						"1	c #DA9737",
						"2	c #C88D45",
						"3	c #D89436",
						"4	c #DB9736",
						"5	c #EFA940",
						"6	c #D49237",
						"  ..........+   ",
						" .           @  ",
						"+#$%...&*=-.;>. ",
						".    ..&***   . ",
						".   ,..&***   . ",
						".   .')&!~*   . ",
						".    {]^/(    . ",
						".    _:<[}    . ",
						".    ..&**    . ",
						".    |,12     . ",
						".    & 3      . ",
						".    4 3 .    . ",
						"5      6      . ",
						" .           @  ",
						"  ..........@   "};
						"""

	def Initialize(self):
		"This function is executed when FreeCAD starts"
		# import here all the needed files that create your FreeCAD commands
		import GCodeProject, ToolTable, ToolGui
		self.list = ["New_Project", "New_Tooltable", "New_Tool"] # A list of command names created in the line above
		self.appendToolbar("My Commands",self.list) # creates a new toolbar with your commands
		self.appendMenu("Actions",self.list) # creates a new menu
		#self.appendMenu(["An existing Menu","My submenu"],self.list) # appends a submenu to an existing menu
		
	def Activated(self):
		"This function is executed when the workbench is activated"
		return
	
	def Deactivated(self):
		"This function is executed when the workbench is deactivated"
		return
		
	def ContextMenu(self, recipient):
		"This is executed whenever the user right-clicks on screen"
		# "recipient" will be either "view" or "tree"
		self.appendContextMenu("My commands",self.list) # add commands to the context menu
		
	def GetClassName(self):
		# this function is mandatory if this is a full python workbench
		return "Gui::PythonWorkbench"

FreeCADGui.addWorkbench(BuildboticsWorkbench())
