import frappe


DEFAULT_GUIDES = [
	{
		"guide_key": "list-add-general",
		"context_type": "List",
		"operation_type": "Add",
		"sequence": 10,
		"audience": "Beginner",
		"translations": [
			{
				"language_code": "ar",
				"is_default": 1,
				"title": "إضافة سجل جديد",
				"short_help": "اضغط New ثم املأ النموذج ثم Save.",
				"detailed_help": "استخدم هذه العملية عند إدخال بيانات جديدة لأول مرة.",
				"conditions": "يشترط صلاحية Create على نفس نوع المستند.",
				"steps": "- اضغط New\n- املأ الحقول الإلزامية\n- راجع البيانات\n- اضغط Save"
	},
			{
				"language_code": "en",
				"title": "Add a New Record",
				"short_help": "Click New, fill the form, then Save.",
				"detailed_help": "Use this operation to create a record for the first time.",
				"conditions": "Requires Create permission on this DocType.",
				"steps": "- Click New\n- Fill mandatory fields\n- Review data\n- Click Save"
	},
		]},
	{
		"guide_key": "form-edit-general",
		"context_type": "Form",
		"operation_type": "Edit",
		"sequence": 20,
		"audience": "Beginner",
		"translations": [
			{
				"language_code": "ar",
				"is_default": 1,
				"title": "تعديل سجل موجود",
				"short_help": "افتح السجل، عدل البيانات، ثم اضغط Save.",
				"detailed_help": "التعديل يستخدم لتصحيح أو تحديث البيانات الموجودة.",
				"conditions": "يشترط صلاحية Write، وقد تمنع حالة المستند المعتمد بعض التعديلات.",
				"steps": "- افتح السجل\n- عدل الحقول المطلوبة\n- تحقق من الرسائل\n- اضغط Save"
	},
			{
				"language_code": "en",
				"title": "Edit an Existing Record",
				"short_help": "Open the record, update fields, then Save.",
				"detailed_help": "Editing is used to correct or update existing data.",
				"conditions": "Requires Write permission; submitted records may restrict edits.",
				"steps": "- Open the record\n- Update needed fields\n- Check validation messages\n- Click Save"
	},
		]},
	{
		"guide_key": "form-delete-general",
		"context_type": "Form",
		"operation_type": "Delete",
		"sequence": 30,
		"audience": "Beginner",
		"translations": [
			{
				"language_code": "ar",
				"is_default": 1,
				"title": "حذف سجل",
				"short_help": "من قائمة الإجراءات اختر Delete عند الحاجة.",
				"detailed_help": "الحذف يجب استخدامه بحذر لأنه قد يؤثر على التقارير والربط.",
				"conditions": "يشترط صلاحية Delete، وألا يكون السجل مرتبطًا أو ممنوعًا بالحالة.",
				"steps": "- افتح السجل\n- افتح Actions/Menu\n- اختر Delete\n- أكد العملية"
	},
			{
				"language_code": "en",
				"title": "Delete a Record",
				"short_help": "Use Actions/Menu then choose Delete.",
				"detailed_help": "Delete carefully as it may impact reporting and links.",
				"conditions": "Requires Delete permission and no blocking linked records/state.",
				"steps": "- Open record\n- Open Actions/Menu\n- Choose Delete\n- Confirm"
	},
		]},
	{
		"guide_key": "form-submit-general",
		"context_type": "Form",
		"operation_type": "Submit",
		"sequence": 40,
		"audience": "Beginner",
		"translations": [
			{
				"language_code": "ar",
				"is_default": 1,
				"title": "اعتماد المستند",
				"short_help": "بعد المراجعة اضغط Submit لاعتماد المستند.",
				"detailed_help": "الاعتماد يحول المستند من مسودة إلى حالة رسمية.",
				"conditions": "يشترط صلاحية Submit واستكمال الحقول الإلزامية والتحقق من القيود.",
				"steps": "- راجع البيانات\n- تأكد من اكتمال الحقول\n- اضغط Submit\n- راجع الحالة الجديدة"
	},
			{
				"language_code": "en",
				"title": "Submit Document",
				"short_help": "After review, click Submit to approve the document.",
				"detailed_help": "Submit moves a draft into an official state.",
				"conditions": "Requires Submit permission and all mandatory validations passed.",
				"steps": "- Review data\n- Ensure required fields are complete\n- Click Submit\n- Verify new status"
	},
		]},
]


def ensure_user_assistant_manager_role():
	if not frappe.db.exists("Role", "User Assistant Manager"):
		role = frappe.get_doc({"doctype": "Role", "role_name": "User Assistant Manager"
	})
		role.insert(ignore_permissions=True)


def seed_user_assistant_guides():
	if not frappe.db.exists("DocType", "Omnexa User Assistant Guide"):
		return

	ensure_user_assistant_manager_role()
	for guide_data in DEFAULT_GUIDES:
		if frappe.db.exists("Omnexa User Assistant Guide", guide_data["guide_key"]):
			continue

		doc = frappe.get_doc(
			{
				"doctype": "Omnexa User Assistant Guide",
				"guide_key": guide_data["guide_key"],
				"is_active": 1,
				"allow_client_edit": 1,
				"context_type": guide_data["context_type"],
				"operation_type": guide_data.get("operation_type"),
				"sequence": guide_data.get("sequence", 10),
				"audience": guide_data.get("audience", "Beginner")}
		)

		for tr in guide_data.get("translations", []):
			doc.append("translations", tr)

		doc.insert(ignore_permissions=True)

	frappe.db.commit()
