# Copyright (c) 2023, quantdairy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StandardDeduction(Document):
	@frappe.whitelist()
	def get_supplier_list(self):
		
		farmer_list=[]
		doc=frappe.db.get_list('Supplier',filters={"dcs_id":self.warehouse__branch,"disabled":False,'supplier_group':"Farmer -Milk Collection"},
							fields=["name","supplier_name"]
							) 
		for d in doc:
			if(d.name not in farmer_list):
				farmer_list.append(d.name)
				# far_name=frappe.get_value("Supplier",d.member,["supplier_name"],as_dict=True)
				self.append(
					"frm_items",
					{
						"farmer_id": d.name,
						# "milk_type":d.milk_type,
						"farmer_name":d.supplier_name,
						
					},
				)
	#Select All        
	@frappe.whitelist()
	def checkall(self):
		children = self.get('frm_items')
		if not children:
			return
		all_selected = all([child.check for child in children])  
		value = 0 if all_selected else 1 
		for child in children:
			child.check = value 
   
	#To Create collection Dictionary
	@frappe.whitelist()
	def get_document(self):
		litre_wise_amt=0
		per_wise_amt=0
		bill_wise_amt=0
		for type in self.get("items"):
			if(type.deduction_type=="Litre Wise"):
				litre_wise_amt=int(type.amount)
			if(type.deduction_type=="Percentage Wise"):
				per_wise_amt=int(type.amount)
			if(type.deduction_type=="Bill Wise"):
				bill_wise_amt=int(type.amount)
		for i in self.get("frm_items"):  # first child table
			if(i.check):
				doc=frappe.db.get_list('Supplier',filters={"dcs_id":self.warehouse__branch,"disabled":False,'supplier_group':"Farmer -Milk Collection"},
							fields=["name","supplier_name"]
							) 
				for d in doc:
					if(i.farmer_id==d.name):
						# if(i.milk_type=="Cow"):
						
						# far_name=frappe.get_value("Supplier",d.member,["supplier_name"],as_dict=True)
						self.append(
							"deduction",{
								"farmer_code":d.name,
								"supplier_name":d.supplier_name,
								# "milk_type":d.milk_type,
								"litre_wise":litre_wise_amt,
								"percentage_wise":per_wise_amt,
								"bill_wise":bill_wise_amt,
								"status":True
							}
						)
	
       
						
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
    
# #To Create collection Dictionary
# 	@frappe.whitelist()
# 	def get_document(self):
# 		collection_dict=[]
# 		for i in self.get("frm_items"):  # first child table
# 			if (i.check):
# 				doc=frappe.db.get_list('Milk Entry',filters={"dcs_id":self.warehouse__branch,"date":["between",[self.first_date,self.last_date]],"status":"Billed"},
# 							fields=["name",'member','milk_type']
# 							) 
# 				for d in doc:
# 					if(d.member not in collection_dict):
# 						collection_dict.append(d.member)
# 						if(i.farmer_id==d.member and i.milk_type==d.milk_type):
# 							if(i.milk_type=="Cow"):
# 								litre_wise_amt=0
# 								per_wise_amt=0
# 								bill_wise_amt=0
# 								for type in self.get("items"):
# 									if(type.deduction_type=="Litre Wise"):
# 										litre_wise_amt=int(type.amount)
# 									if(type.deduction_type=="Percentage Wise"):
# 										per_wise_amt=int(type.amount)
# 									if(type.deduction_type=="Bill Wise"):
# 										bill_wise_amt=int(type.amount)
# 								far_name=frappe.get_value("Supplier",d.member,["supplier_name"],as_dict=True)
# 								self.append(
# 									"deduction",{
# 										"farmer_code":d.member,
# 										"supplier_name":far_name.supplier_name,
# 										"milk_type":d.milk_type,
# 										"litre_wise":litre_wise_amt,
# 										"percentage_wise":per_wise_amt,
# 										"bill_wise":bill_wise_amt,
# 										"status":True
# 									}
# 								)