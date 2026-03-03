from odoo import fields,models

class educationProgram(models.Model):
    _name = "education.program"
    _description = "Program"

    programName = fields.Char(string="Program Name",required=True)
    programCode = fields.Char(string="Program Code",required=True)
    programText = fields.Text(string="Program Text")
    programDuration = fields.Float(string='Duration (Years)')
    programLevel = fields.Selection([
        ('ug', 'Undergraduate'),
        ('pg', 'Postgraduate'),
        ('phd', 'PhD')
    ], string='Level', default='ug')
    programActive = fields.Boolean(string='Active', default=True)