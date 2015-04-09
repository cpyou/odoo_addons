# -*- coding: utf-8 -*-

from openerp import fields, api
from openerp.osv import orm


class MigrateUSer(orm.Model):
    _name = 'migrate.user'
    _description = 'migrate user'
    _rec_name = 'old_email_address'

    email_server = fields.Char('邮箱服务器')
    old_email_address = fields.Char('旧邮箱')
    new_email_address = fields.Char('新邮箱')
    # need_handle_sum = fields.Float('')
    # handled_sum = fields.Float('')
    handling_server = fields.Char('当前A处理服务器')
    messages = fields.One2many('email.message', 'user', '邮件')

MigrateUSer()


class EmailMessage(orm.Model):
    _name = 'email.message'
    _description = 'email message'

    message_id = fields.Integer('消息id')
    user = fields.Many2one('migrate.user', '用户')
    handle_state = fields.Selection([('wait_handle', '等待处理'),
                                     ('handled', '以处理')], '处理状态')
    handle_history = fields.One2many('message.handle.history', 'message_id', '处理历史')


EmailMessage()


class MessageHandleHistory(orm.Model):
    _name = 'message.handle.history'
    _description = 'message handle history'

    message_id = fields.Many2one('email.message', '邮件id')
    handle_server = fields.Many2one('handle.server', '处理服务器')
    handle_state = fields.Selection([('success', '成功'),
                                     ('fail', '失败')], '处理状态')

MessageHandleHistory()


class HandleServer(orm.Model):
    _name = 'handle.server'
    _description = 'handle server'

    server_ip = fields.Char('服务器ip')
    work_state = fields.Selection([('wait_work', '等待工作'),
                                   ('working', '工作中')], '工作状态')
    handling_message_id = fields.Many2one('email.message', '处理消息id')
    handled_message_history = fields.One2many('message.handle.history',
                                              'handle_server', '以处理处理消息历史')

    handling_email_address = fields.Many2one('migrate.user', '处理中的用户')
    handled_email_address = fields.Many2many('migrate.user', 'handle_server_migrate_user_rel',
                                             'handle_server_id', 'email_address_id', '已处理的用户')


HandleServer()