# Copyright (c) 2023, quantdairy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import date


class Test(Document):
	def before_save(self):
		today=date.today()
		doc_list=frappe.get_all("Standard Deduction",filters={"name":"DCS-03Jamrunda - BDF","first_date":['<=',today],"last_date":['>=',today]},fields=["name"])
		frappe.msgprint(str(doc_list))
			
		