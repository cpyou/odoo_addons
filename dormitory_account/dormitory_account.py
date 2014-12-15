# -*- coding: utf-8 -*-

from openerp.osv import fields, orm

import time

class dormitory_account(orm.Model):
    _name = 'dormitory.account'
    _columns = {
        'user_id': fields.many2one('res.users', '用户'),
        'cost': fields.float('费用'),
        'note': fields.text('备注'),
        'date': fields.date('日期'),
    }
    _defaults = {
        'user_id': lambda self, cr, uid, context: uid,
        'date': fields.date.today(),
    }
