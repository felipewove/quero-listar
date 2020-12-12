""" Script to import data given a database exported in JSON
    
    This is the structure:

    [
        {
            "full_price": float,
            "price_with_discount": float,
            "discount_percentage": float,
            "start_date": string,
            "enrollment_semester": string,
            "enabled": boolean,
            "course": {
                "name": string,
                "kind": string,
                "level": string,
                "shift": string
            },
            "university": {
                "name": string,
                  "score": float,
              "logo_url": string
            },
            "campus": {
                "name": string,
                "city": string
            }
        },
    ...
    ]
"""
import json
from quero.offer.models import Offer, Campus, University, Course


with open('scripts/db.json') as file_data:
    data = json.load(file_data)
    for offer in data:
        university = University.objects.get_or_create(
            name=offer['university']['name'],
            score=offer['university']['score'],
            logo_url=offer['university']['logo_url'],
        )[0]  # because get_or_create() returns a tuple (obj, bool)

        campus = Campus.objects.get_or_create(
            name=offer['campus']['name'],
            city=offer['campus']['city'],
            university=university,
        )[0]  # because get_or_create() returns a tuple (obj, bool)

        course = Course.objects.get_or_create(
            name=offer['course']['name'],
            kind=offer['course']['kind'],
            level=offer['course']['level'],
            shift=offer['course']['shift'],
            campus=campus,
        )[0]  # because get_or_create() returns a tuple (obj, bool)

        Offer.objects.create(
            full_price=offer['full_price'],
            price_with_discount=offer['price_with_discount'],
            discount_percentage=offer['discount_percentage'],
            start_date=offer['start_date'],
            enrollment_semester=offer['enrollment_semester'],
            enabled=offer['enabled'],
            course=course
        )
