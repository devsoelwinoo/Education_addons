from odoo import models,fields

class educationCourse(models.Model):
    _name = "education.course"
    _description = "Course"

    courseName = fields.Char(string = "Course Name",required=True)
    courseTeacher = fields.Char(string="Teacher",required=True)
    courseDuration = fields.Char(string="Duration")

    subject_ids = fields.One2many('education.subject','course_id',string="Subject")
    student_ids = fields.One2many('education.student','course_id',string="Student")

    