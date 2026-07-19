from frappe.tests.utils import FrappeTestCase

from omnexa_user_academy import hooks


class TestUserAcademySmoke(FrappeTestCase):
	def test_hooks_are_present(self):
		self.assertEqual(hooks.app_name, "omnexa_user_academy")

