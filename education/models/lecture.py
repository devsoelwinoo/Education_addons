from odoo import models, fields

class educationLecture(models.Model):
    _name = "education.lecture"
    _description = "Lecture"

    title = fields.Char(string="Name",required=True)
    lectureCode = fields.Char(string="Code",required=True,unique=True)
    batch_id = fields.Many2one("education.batch",string = "Batch ID")
    startDate = fields.Date(string="Start Date")
    endDate = fields.Date(string="End Date")
    duration = fields.Integer(string="Duration")
    location = fields.Char(string="Location")
    type = fields.Selection([
        ("theory","Theory"),
        ("pratical","Pratical")
    ],string = "Type")
    description = fields.Text(string="Description",required=True)