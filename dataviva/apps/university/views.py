# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g
from dataviva.apps.general.views import get_locale
from dataviva.api.hedu.services import University, UniversityMajors
from dataviva.api.attrs.models import Course_hedu

mod = Blueprint('university', __name__,
                template_folder='templates/university',
                url_prefix='/<lang_code>/university',
                static_folder='static')

@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.locale = values.pop('lang_code')

@mod.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', get_locale())

@mod.route('/<university_id>')
def index(university_id):

    #Use Example /university/00575

    university_service = University(university_id)
    majors_service = UniversityMajors(university_id)

    header = {
        'university_id' : university_id,
        'sector_id' : university_id[0],
        'name' : university_service.name(),
        'type' : university_service.university_type(),
        'enrolled' : university_service.enrolled(),
        'entrants' : university_service.entrants(),
        'graduates' : university_service.graduates(),
        'year' : university_service.year()
    }

    body = {
        'major_with_more_enrollments' : majors_service.major_with_more_enrollments(),
        'highest_enrollment_number_by_major' : majors_service.highest_enrolled_number(),
        'major_with_more_entrants' : majors_service.major_with_more_entrants(),
        'highest_entrant_number_by_major' : majors_service.highest_entrants_number(),
        'major_with_more_graduates' : majors_service.major_with_more_graduates(),
        'highest_graduate_number_by_major' : majors_service.highest_graduates_number()
    }
    return render_template('index.html', header=header, body=body)


