from odoo import models, fields

class educationParent(models.Model):
    _name = 'education.parent'
    _description = 'Parent'

    name = fields.Char(string='Name',required=True)
    phone = fields.Char(string='Phone',required=True)
    address = fields.Text(string='Address')
    student_ids = fields.One2many('education.student','parent_id',string = "Children")