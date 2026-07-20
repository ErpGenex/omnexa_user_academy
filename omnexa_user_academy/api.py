import re

import frappe


def _pick_translation(translations, lang):
	if not translations:
		return None

	for tr in translations:
		if tr.language_code == lang:
			return tr

	for tr in translations:
		if tr.is_default:
			return tr

	for fallback in ("en", "ar"):
		for tr in translations:
			if tr.language_code == fallback:
				return tr

	return translations[0]


def _as_steps(step_text):
	if not step_text:
		return []
	lines = re.split(r"[\r\n]+", step_text)
	cleaned = []
	for line in lines:
		line = re.sub(r"^\s*[-*]\s*", "", (line or "").strip())
		if line:
			cleaned.append(line)
	return cleaned


@frappe.whitelist()
def get_user_assistant_guides(context_type=None, reference_doctype=None, workspace_name=None, route_str=None):
	lang = frappe.local.lang or "en"
	if not frappe.db.exists("DocType", "Omnexa User Assistant Guide"):
		return []

	filters = {"is_active": 1
	}
	if context_type:
		filters["context_type"] = context_type

	names = frappe.get_all(
		"Omnexa User Assistant Guide",
		filters=filters,
		pluck="name",
		order_by="sequence asc, modified desc",
	)

	result = []
	for name in names:
		doc = frappe.get_doc("Omnexa User Assistant Guide", name)

		if doc.reference_doctype and reference_doctype and doc.reference_doctype != reference_doctype:
			continue
		if doc.reference_doctype and not reference_doctype:
			continue

		if doc.workspace_name and workspace_name:
			if doc.workspace_name != workspace_name:
				continue
		elif doc.workspace_name and not workspace_name:
			continue

		if doc.route_pattern and route_str:
			if doc.route_pattern not in route_str:
				continue
		elif doc.route_pattern and not route_str:
			continue

		tr = _pick_translation(doc.translations or [], lang)
		if not tr:
			continue

		result.append(
			{
				"id": f"db-{doc.name
	}",
				"t": tr.title,
				"k": f"{doc.context_type} {doc.operation_type or ''} {doc.reference_doctype or ''
	}",
				"b": tr.short_help,
				"d": tr.detailed_help or tr.conditions or "",
				"steps": _as_steps(tr.steps)
	}
		)

	return result
@frappe.whitelist()
def preview_infra_kpi(scenario: str | None = None, params: str | None = None) -> dict:
	from omnexa_core.omnexa_core.parity_api import preview_infra_kpi as _p
	return _p("user_academy", scenario=scenario, params=params)
