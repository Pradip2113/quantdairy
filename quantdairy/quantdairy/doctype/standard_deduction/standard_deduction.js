// Copyright (c) 2023, quantdairy and contributors
// For license information, please see license.txt

frappe.ui.form.on('Standard Deduction', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('Standard Deduction', {
    refresh: function(frm) {
        $('.layout-side-section').hide();
        $('.layout-main-section-wrapper').css('margin-left', '0');
    }
});

frappe.ui.form.on('Standard Deduction', {
	last_date: function (frm) {
		frm.clear_table("frm_items")
		frm.refresh_field('frm_items')
		frm.clear_table("deduction")
		frm.refresh_field('deduction')
		frm.call({
			method: 'get_supplier_list',//function name defined in python
			doc: frm.doc, //current document
		});
	},
	check_all: function (frm) {
		frm.call({
			method: 'checkall',//function name defined in python
			doc: frm.doc, //current document
		});
	},
	show: function(frm) {
		frm.clear_table("deduction")
		frm.refresh_field('deduction')
		frm.call({
			method: 'get_document',//function name defined in python
			doc: frm.doc, //current document
		});	
	}
});

