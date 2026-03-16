from odoo import models,fields

class educationBatch(models.Model):
    _name = "education.batch"
    _description = "Student"
    _rec_name = "batchName"

    batchName = fields.Char(string="Batch Name",required=True)
    batchCode = fields.Char(string="Batch Code",required=True, unique=True)
    student_ids = fields.One2many(
        'education.student',
        'batch_id',
        string="Students"
    )
    batchStartDate = fields.Date(string="Start Date")
    batchEndDate = fields.Date(string="End Date")
    batchCapicity = fields.Integer(string="Batch Limit")
    batchDescription = fields.Text(string="Batch Description")
    batchActive = fields.Boolean(string="Active Batch",default=False)
    