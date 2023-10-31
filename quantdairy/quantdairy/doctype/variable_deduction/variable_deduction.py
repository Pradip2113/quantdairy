# Copyright (c) 2023, quantdairy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VariableDeduction(Document):
	def before_save(self):
		payment=frappe.new_doc("Payment Entry")
		payment.payment_type="Pay"
		payment.mode_of_payment="Cash"
		payment.party_type="Supplier"
		payment.party=self.farmer_code
		payment.paid_amount=self.deduction_amount
		payment.received_amount=self.deduction_amount
		payment.source_exchange_rate=1
		payment.paid_from="1121 - HDFC OD Bank-1200 - BDF"
		payment.insert()
		self.payment_entry_doc=payment.name
		payment.docstatus=1
		payment.save()

	def on_trash(self):
		doc=frappe.get_doc("Payment Entry",self.payment_entry_doc)
		doc.cancel()
		frappe.delete_doc("Payment Entry",self.payment_entry_doc,force=True)
