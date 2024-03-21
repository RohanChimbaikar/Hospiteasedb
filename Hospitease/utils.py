def is_doctor(user):
    return user.groups.filter(name='Doctors').exists()