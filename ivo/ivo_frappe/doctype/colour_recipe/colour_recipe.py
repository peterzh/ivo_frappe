# -*- coding: utf-8 -*-
# Copyright (c) 2021, Peter Zatka-Haas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Colourrecipe(Document):
	def validate(self):
		#Check that the proportions of child recipe items add up to 100%
		recipe = self.as_dict()['recipe']
		proportions = [x['proportion'] for x in recipe]
		if sum(proportions) != 100.0:
			frappe.throw('Proportions must sum to 100%!')
