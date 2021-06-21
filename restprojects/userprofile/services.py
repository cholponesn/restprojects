def sale_count(profile):
    if 100 > profile.count_order > 50:
        profile.sale = 0.1
    elif profile.count_order > 100:
        profile.sale = 0.2
    profile.save()