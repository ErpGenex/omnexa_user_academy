# Copyright (c) 2026, ErpGenEx
# Auto-generated Global Excellence report pack

import frappe
from frappe import _


def execute(filters=None):
	data = frappe.db.sql(
		"""
		SELECT `name`, `guide_key`, `is_active`, `context_type`, `operation_type`, `reference_doctype`
		FROM `tabOmnexa User Assistant Guide`
		ORDER BY modified DESC
		LIMIT 500
		""",
		as_dict=True,
	)
	columns = [
		{"label": _("Name"), "fieldname": "name", "fieldtype": "Link", "width": 140},
		{"label": _("Guide Key"), "fieldname": "guide_key", "fieldtype": "Data", "width": 120},
		{"label": _("Is Active"), "fieldname": "is_active", "fieldtype": "Check", "width": 120},
		{"label": _("Context Type"), "fieldname": "context_type", "fieldtype": "Select", "width": 120},
		{"label": _("Operation Type"), "fieldname": "operation_type", "fieldtype": "Select", "width": 120},
		{"label": _("Reference DocType"), "fieldname": "reference_doctype", "fieldtype": "Link", "width": 120}
	]
	return columns, data
