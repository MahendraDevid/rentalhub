def is_admin(user):
    return user.groups.filter(name='Admin').exists()
