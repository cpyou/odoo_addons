# -*- encoding: utf-8 -*-

from openerp import models, fields, api, exceptions


class SqlData(models.Model):
    """
        sql 数据
    """
    _name = 'sql.data'

    name = fields.Char('名称', required=True)
    header = fields.Text('表头字段名')
    sql = fields.Text('sql语句', required=True)
    description = fields.Text('描述')

    @api.multi
    def report_print(self):
        datas = {'sql': self.sql}
        name = self.name
        return {
            'name': name,
            'type': 'ir.actions.report.xml',
            'report_name': 'report.sql.to.excel',
            'datas': datas,
        }
