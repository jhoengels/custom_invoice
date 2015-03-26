# -*- coding: utf-8 -*-
from openerp import fields, models, api, exceptions

class custom_invoice(models.Model):
	_inherit = 'account.invoice'

	#nuevas columnas
	def run_sql(self):
		query = "SELECT date_invoice AS fecha FROM account_invoice WHERE id IN (%s)"
		self._cr.execute(query, (self.id,))
		res = self._cr.dictfetchall()
		return res[0]['fecha']
	def run_sql1(self):
		query = """SELECT dc.name AS name, ai.date_invoice AS fecha
					FROM account_invoice ai
					LEFT JOIN  sale_order so ON ai.origin = so.name
					LEFT JOIN  delivery_carrier dc ON so.carrier_id = dc.id
					WHERE ai.id IN (%s)"""
		self._cr.execute(query, (self.id,))
		res = self._cr.dictfetchall()
		return (res[0]['name'] + ' ' + res[0]['fecha'])