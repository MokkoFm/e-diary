from datacenter.models import Schoolkid
from datacenter.models import Mark

schoolkid = Schoolkid.objects.filter(full_name__contains="Фролов Иван")[0]


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])

    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()

fix_marks(schoolkid)