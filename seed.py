#Seed-Daten für Thesis Match.

#Legt Referenzdaten (Fachbereich FB1, Facheinheiten, Studiengaenge) und ein paar
#Demo-Accounts inkl. Anfragen an, mehrfaches Ausfuehren erzeugt keine Duplikate. Aufruf: flask --app app seed

from werkzeug.security import generate_password_hash

from db import (db, Faculty, Facheinheit, DegreeProgram, User,
                StudentProfile, ProfessorProfile, SupervisionRequest, RequestMessage)

DEMO_PASSWORD = 'demo1234'

FACHEINHEITEN = [
    'Unternehmensführung / Personal / Organisation', 'Marketing', 'Finanzwirtschaft',
    'Steuern', 'Rechnungswesen', 'Supply Chain und Operations Management',
    'Quantitative Methoden', 'Wirtschaftsinformatik', 'Volkswirtschaftslehre',
    'Gesellschaftswissenschaften', 'Wirtschaftsrecht',
]

DEGREE_PROGRAMS = [
    ('Business Administration (Vollzeit)', 'B.A.'),
    ('Business Administration (Teilzeitform)', 'B.A.'),
    ('Entrepreneurship', 'B.Sc.'),
    ('International Business Management', 'B.A.'),
    ('International Digital Business', 'B.Sc.'),
    ('International Sustainability Management', 'B.Sc.'),
    ('Unternehmensgründung und -nachfolge', 'B.A.'),
    ('Volkswirtschaftslehre (VWL)', 'B.A.'),
    ('Wirtschaftsinformatik', 'B.Sc.'),
    ('Wirtschaftsingenieur/in - Umwelt und Nachhaltigkeit', 'B.Eng.'),
    ('Wirtschaftsrecht', 'LL.B.'),
]

PROFESSORS = [
    {'email': 'anna.schneider@hwr-berlin.de', 'first': 'Anna', 'last': 'Schneider',
     'title': 'Prof. Dr.', 'facheinheit': 'Wirtschaftsinformatik',
     'research_areas': 'Datenanalyse, digitale Geschäftsmodelle, KI im Mittelstand',
     'requirements': 'Grundkenntnisse in Python und Statistik'},
    {'email': 'thomas.becker@hwr-berlin.de', 'first': 'Thomas', 'last': 'Becker',
     'title': 'Prof. Dr.', 'facheinheit': 'Marketing',
     'research_areas': 'Konsumentenverhalten, digitales Marketing, Markenführung',
     'requirements': 'Interesse an empirischer Forschung'},
]

STUDENTS = [
    {'email': 'max.mustermann@stud.hwr-berlin.de', 'first': 'Max', 'last': 'Mustermann'},
    {'email': 'lena.fischer@stud.hwr-berlin.de', 'first': 'Lena', 'last': 'Fischer'},
]

REQUESTS = [
    {'student': 'max.mustermann@stud.hwr-berlin.de', 'prof': 'anna.schneider@hwr-berlin.de',
     'examiner_role': 'erst', 'title': 'Einsatz von KI-Chatbots im Kundenservice',
     'description': 'Untersuchung, wie KI-Chatbots die Servicequalität kleiner Unternehmen beeinflussen.',
     'period': 'WS 2026/27'},
    {'student': 'lena.fischer@stud.hwr-berlin.de', 'prof': 'anna.schneider@hwr-berlin.de',
     'examiner_role': 'zweit', 'title': 'Datengetriebene Preisoptimierung im E-Commerce',
     'description': 'Analyse datenbasierter Preisstrategien anhand eines Online-Shops.',
     'period': 'SS 2027'},
    {'student': 'max.mustermann@stud.hwr-berlin.de', 'prof': 'thomas.becker@hwr-berlin.de',
     'examiner_role': 'erst', 'title': 'Einfluss von Social-Media-Werbung auf Kaufentscheidungen',
     'description': 'Empirische Studie zum Einfluss von Instagram-Werbung auf junge Zielgruppen.',
     'period': 'WS 2026/27'},
]


def _get_or_create(model, defaults=None, **filters):
    obj = db.session.execute(db.select(model).filter_by(**filters)).scalar_one_or_none()
    if obj is not None:
        return obj
    obj = model(**{**filters, **(defaults or {})})
    db.session.add(obj)
    return obj


def seed_all():
    fb1 = _get_or_create(Faculty, code='FB1', defaults={'name': 'Wirtschaftswissenschaften'})
    db.session.flush()

    fe_by_name = {name: _get_or_create(Facheinheit, faculty_id=fb1.id, name=name)
                  for name in FACHEINHEITEN}
    for name, degree in DEGREE_PROGRAMS:
        _get_or_create(DegreeProgram, faculty_id=fb1.id, name=name, defaults={'degree': degree})
    db.session.flush()

    for p in PROFESSORS:
        user = _get_or_create(User, email=p['email'], defaults={
            'password_hash': generate_password_hash(DEMO_PASSWORD),
            'first_name': p['first'], 'last_name': p['last'],
            'role': 'professor', 'account_status': 'active'})
        db.session.flush()
        if user.professor_profile is None:
            db.session.add(ProfessorProfile(
                user_id=user.id, facheinheit_id=fe_by_name[p['facheinheit']].id,
                title=p['title'], research_areas=p['research_areas'],
                requirements=p['requirements'], accepting_requests=1))

    for s in STUDENTS:
        user = _get_or_create(User, email=s['email'], defaults={
            'password_hash': generate_password_hash(DEMO_PASSWORD),
            'first_name': s['first'], 'last_name': s['last'],
            'role': 'student', 'account_status': 'active'})
        db.session.flush()
        if user.student_profile is None:
            db.session.add(StudentProfile(user_id=user.id, faculty_id=fb1.id))
    db.session.flush()

    def user_id(email):
        return db.session.execute(db.select(User).filter_by(email=email)).scalar_one().id

    for r in REQUESTS:
        student_id, prof_id = user_id(r['student']), user_id(r['prof'])
        exists = db.session.execute(db.select(SupervisionRequest).filter_by(
            student_id=student_id, professor_id=prof_id, proposed_title=r['title'])
        ).scalar_one_or_none()
        if exists is None:
            db.session.add(SupervisionRequest(
                student_id=student_id, professor_id=prof_id, examiner_role=r['examiner_role'],
                proposed_title=r['title'], short_description=r['description'],
                preferred_period=r['period'], status='submitted'))

    db.session.commit()

    # Eine Beispiel-Nachricht im ersten Chat (idempotent).
    first = db.session.execute(db.select(SupervisionRequest).filter_by(
        proposed_title=REQUESTS[0]['title'])).scalar_one_or_none()
    if first is not None and not first.messages:
        db.session.add(RequestMessage(
            request_id=first.id, sender_id=first.professor_id,
            message_text='Hallo, danke für Ihre Anfrage. Können Sie den geplanten Methodenteil kurz umreißen?'))
        db.session.commit()

    print(f'Seed abgeschlossen: {len(PROFESSORS)} Profs, {len(STUDENTS)} Studis, '
          f'{len(REQUESTS)} Anfragen (idempotent).')
