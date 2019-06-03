from zabbix.models import Machines



def get_machines():
    machines = Machines.objects.all()
    return machines


def check_for_special_chars_in_name(name):
    special_characters = ['/', '\\']
    for member in special_characters:
        if member in name:
            return False
        else:
            return True