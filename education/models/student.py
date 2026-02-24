from odoo import models, fields

class StudentInfo(models.Model):
    _name = 'education.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    age = fields.Integer(string='Age')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    address = fields.Text(string='Address')
