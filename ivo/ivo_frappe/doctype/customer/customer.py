# -*- coding: utf-8 -*-
# Copyright (c) 2021, Peter Zatka-Haas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class Customer(Document):
	def autoname(self):
		self.name = make_autoname(self.customer_name[0].upper() + ".###")
