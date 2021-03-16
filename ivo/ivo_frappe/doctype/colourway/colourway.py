# -*- coding: utf-8 -*-
# Copyright (c) 2021, Peter Zatka-Haas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Colourway(Document):
	def validate(self):
		#Check that the number of colours matches the num colours given in the design
		num_colours = len(self.colours)
		design = frappe.get_doc('Design',self.design)
		num_colours_design = design.number_of_colours
		if num_colours != num_colours_design:
			frappe.throw(f"Colourway has {num_colours} however design states {num_colours_design}")
