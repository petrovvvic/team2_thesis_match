from app import app
from db import db, Faculty, DegreeProgram


DEGREE_PROGRAMS = [
    {
        "name": "Business Administration (Vollzeit)",
        "degree": "B.A.",
    },
    {
        "name": "Business Administration (Teilzeitform)",
        "degree": "B.A.",
    },
    {
        "name": "Entrepreneurship",
        "degree": "B.Sc.",
    },
    {
        "name": "International Business Management",
        "degree": "B.A.",
    },
    {
        "name": "International Digital Business",
        "degree": "B.Sc.",
    },
    {
        "name": "International Sustainability Management",
        "degree": "B.Sc.",
    },
    {
        "name": "Unternehmensgründung und -nachfolge",
        "degree": "B.A.",
    },
    {
        "name": "Volkswirtschaftslehre (VWL)",
        "degree": "B.A.",
    },
    {
        "name": "Wirtschaftsinformatik",
        "degree": "B.Sc.",
    },
    {
        "name": "Wirtschaftsingenieur/in - Umwelt und Nachhaltigkeit",
        "degree": "B.Eng.",
    },
    {
        "name": "Wirtschaftsrecht",
        "degree": "LL.B.",
    },
]


def seed_degree_programs():
    """Insert the selected FB1 bachelor programmes without duplicates."""

    with app.app_context():
        faculty = db.session.execute(
            db.select(Faculty).where(Faculty.code == "FB1")
        ).scalar_one_or_none()

        if faculty is None:
            raise RuntimeError(
                "Der Fachbereich FB1 ist nicht vorhanden. "
                "Bitte zuerst den Fachbereich anlegen."
            )

        created_count = 0
        updated_count = 0

        for program_data in DEGREE_PROGRAMS:
            degree_program = db.session.execute(
                db.select(DegreeProgram).where(
                    DegreeProgram.faculty_id == faculty.id,
                    DegreeProgram.name == program_data["name"],
                )
            ).scalar_one_or_none()

            if degree_program is None:
                degree_program = DegreeProgram(
                    faculty_id=faculty.id,
                    name=program_data["name"],
                    degree=program_data["degree"],
                )
                db.session.add(degree_program)
                created_count += 1

            elif degree_program.degree != program_data["degree"]:
                degree_program.degree = program_data["degree"]
                updated_count += 1

        db.session.commit()

        degree_programs = db.session.execute(
            db.select(DegreeProgram)
            .where(DegreeProgram.faculty_id == faculty.id)
            .order_by(DegreeProgram.name)
        ).scalars().all()

        print(f"{created_count} Studiengänge erstellt.")
        print(f"{updated_count} Studiengänge aktualisiert.")
        print("\nGespeicherte Studiengänge:")

        for degree_program in degree_programs:
            print(
                f"- {degree_program.name} "
                f"({degree_program.degree})"
            )


if __name__ == "__main__":
    seed_degree_programs()
