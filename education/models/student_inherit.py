from odoo import models, fields

class educationStudentInherit(models.Model):
    _inherit = "education.student"

    studentGpa = fields.Integer(string="GPA")