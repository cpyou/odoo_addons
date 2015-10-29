# -*- encoding: utf-8 -*-
from openerp.report.interface import report_int
from cStringIO import StringIO
import xlsxwriter
import openerp


class ReportTest(report_int):
    """
    报表测试
    """

    def create(self, cr, uid, ids, datas, context=None):
        registry = openerp.registry(cr.dbname)
        # registry['stock.warehouse'].search(cr, uid, [])[0]
        fp = StringIO()
        wbk = xlsxwriter.Workbook(fp, {'in_memory': True})
        sheet = wbk.add_worksheet('cpy')
        sheet.write(0, 0, '报表测试')
        wbk.close()
        fp.seek(0)
        pdf = fp.read()
        return pdf, 'xlsx'

ReportTest('report.report.test')
