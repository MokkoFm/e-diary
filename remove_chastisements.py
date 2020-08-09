from datacenter.models import Schoolkid
from datacenter.models import Chastisement

schoolkid = Schoolkid.objects.filter(full_name__contains="Голубев Феофан")[0]


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()

remove_chastisements(schoolkid)