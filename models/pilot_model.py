# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pilot_user_model(models.Model):
    _inherit = "race_app.pilot_model"

    odoo_user = fields.Many2one("res.users", string="Odoo user: ")