from odoo import models,fields

class educationSubject(models.Model):
    _name = "education.subject"
    _description = "Subject"

    subjName = fields.Char(string="Subject", required=True)
    learningHour = fields.Char(string="Hour", required=True)
    room = fields.Char(string="Room")
    teacher = fields.Char(string="Teacher")

    course_id = fields.Many2one('education.course', string="Course")