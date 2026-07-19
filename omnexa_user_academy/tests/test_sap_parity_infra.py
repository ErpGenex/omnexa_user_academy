# Copyright (c) 2026, ErpGenEx
from frappe.tests.utils import FrappeTestCase
from omnexa_core.omnexa_core.infra_parity import preview_infra

class TestSapParityInfraApp(FrappeTestCase):
	def test_infra_kpi(self):
		out = preview_infra("user_academy", published_guides=5)
		self.assertEqual(out["vertical"], "user_academy")
