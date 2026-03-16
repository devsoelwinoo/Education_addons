# Copyright 2017-24 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Education Management",
    "summary": "Education management system for schools and universities.",
    "version": "18.0.1.1.0",
    "category": "Education",
    "website": "https://github.com/",
    "author": "psodoo18",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [],
    "data": [
        "security/ir.model.access.csv",
        "views/education_student_view.xml",
        "views/education_batch_view.xml",
        "views/education_program_view.xml",
        "views/education_course_view.xml",
        "views/education_student_inherit_view.xml",
        "views/education_parent_view.xml"
    ],
}
