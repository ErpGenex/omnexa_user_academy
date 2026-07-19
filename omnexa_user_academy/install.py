import frappe

from omnexa_user_academy.seed import seed_user_assistant_guides


MODULE_NAME = "Omnexa User Academy"


def _ensure_module_def():
	"""Ensure Module Def exists so DocType controllers can be imported during migrate."""
	try:
		if frappe.db.exists("Module Def", MODULE_NAME):
			return
		doc = frappe.new_doc("Module Def")
		doc.module_name = MODULE_NAME
		doc.app_name = "omnexa_user_academy"
		doc.custom = 0
		doc.insert(ignore_permissions=True)
		frappe.db.commit()
	except Exception:
		# Never break migrate due to onboarding content.
		frappe.log_error(frappe.get_traceback(), "User Academy: ensure module def")


def after_install():
	_ensure_module_def()
	try:
		seed_user_assistant_guides()
	except Exception:
		frappe.log_error(frappe.get_traceback(), "User Academy: seed after_install")


def after_migrate():
	_ensure_module_def()
	try:
		seed_user_assistant_guides()
	except Exception:
		# Do not block migrations for guide seeding issues.
		frappe.log_error(frappe.get_traceback(), "User Academy: seed after_migrate")
