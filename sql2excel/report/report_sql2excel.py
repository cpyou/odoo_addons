# -*- encoding: utf-8 -*-
from openerp.report.interface import report_int
from cStringIO import StringIO
import xlsxwriter
import openerp


class ReportSqlToExcel(report_int):
    """
    报表测试
    """

    def create(self, cr, uid, ids, datas, context=None):
        registry = openerp.registry(cr.dbname)
        # registry['stock.warehouse'].search(cr, uid, [])[0]
        cr.execute(datas['sql'])
        fp = StringIO()
        wbk = xlsxwriter.Workbook(fp, {'in_memory': True})
        sheet = wbk.add_worksheet('sheet1')
        row = 0
        sheet.write_row(row, 0, [d.name for i, d in enumerate(cr._obj.description)])
        try:
            while True:
                row += 1
                print row
                val = cr.next()
                sheet.write_row(row, 0, val)
        except StopIteration:
            pass

        wbk.close()
        fp.seek(0)
        pdf = fp.read()
        return pdf, 'xlsx'

ReportSqlToExcel('report.report.sql.to.excel')
