# Copyright (c) 2023, quantdairy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Test(Document):
	def before_save(self):
		# frappe.throw("hi")
		pi = frappe.new_doc("Purchase Invoice")
		pi.supplier=self.supplier
		pri=frappe.get_doc('Purchase Receipt',"MAT-PRE-2023-45753")
		pi.set_posting_time = 1
		for itm in pri.items:
			pi.append(
				"items",
				{
					'item_code': itm.item_code,
					'item_name': itm.item_name,
					'description': itm.description,
					'received_qty': 1,
					'qty': 1,
					'uom': itm.stock_uom,
					'stock_uom': itm.stock_uom,
					'rate': itm.rate,
					'warehouse':"DCS-03Jamrunda - BDF",
					'purchase_receipt':"MAT-PRE-2023-45753",
					'pr_detail':itm.name,
					'fat': itm.fat,
					'snf': itm.clr,
					'snf_clr': itm.snf,
					'fat_per': itm.fat_per_ ,
					'snf_clr_per':itm.clr_per ,
					'snf_per':itm.snf_clr_per,
				
				}
			)
		tax_row = pi.append("taxes", {})
		tax_row.charge_type="On Net Total"
		tax_row.account_head="Deduction Payable - BDF"
		tax_row.category="Total"
		tax_row.add_deduct_tax="Deduct"
		tax_row.description="hi"
		tax_row.rate = 1 
	
		pi.save(ignore_permissions = True)
		pi.submit()
