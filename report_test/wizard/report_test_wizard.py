# -*- coding: utf-8 -*- #
import logging
from openerp import models, fields, api

_logger = logging.getLogger(__name__)


class ReportTestWizard(models.TransientModel):
    _name = "report.test.wizard"
    _order = "id desc"

    from_date = fields.Datetime('开始日期')
    to_date = fields.Datetime('结束日期')

    @api.multi
    def report_print(self):
        datas = {'a': 'a'}
        return {
            'name': '测试报表',
            'type': 'ir.actions.report.xml',
            'report_name': 'report.test',
            'datas': datas,
        }
