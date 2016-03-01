# -*- encoding: utf-8 -*-

from openerp import models, fields, api, exceptions


class SqlToExeclWizard(models.TransientModel):
    """
    sql 转excel
    """
    _name = 'sql.to.excel.wizard'

    sql_data_id = fields.Many2one('sql.data', '导出报表名称')

    @api.multi
    def report_print(self):
        datas = {'sql': self.sql_data_id.sql}
        name = self.sql_data_id.name
        return {
            'name': name,
            'type': 'ir.actions.report.xml',
            'report_name': 'report.sql.to.excel',
            'datas': datas,
        }
