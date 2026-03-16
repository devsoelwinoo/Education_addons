from odoo import models, fields

class educationStudent(models.Model):
    _name = 'education.student'
    _description = 'Student'

    name = fields.Char(string='Name',required=True)
    code = fields.Char(string='Code',required=True,unique=True)
    batch_id = fields.Many2one('education.batch',string="Batch")
    age = fields.Integer(string='Age')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string='Gender')
    address = fields.Text(string='Address')
    course_id = fields.Many2one('education.course',string="Course")
    parent_id = fields.Many2one('education.parent',string="Gurdian")

