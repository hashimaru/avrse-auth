# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.utils.timezone import now

from timerboard.models import Timer



def index(request):
    context = {
        "timers": filter(
                lambda x: x.user_in_groups(request.user),
                Timer.objects.filter(
                    date__gte=now() - timedelta(minutes=60),
                    visible_to_level__lte=request.user.profile.level,
                    deleted=False
                ).order_by(
                    'date'
                )
            ),
        "archive": filter(
                lambda x: x.user_in_groups(request.user),
                Timer.objects.filter(
                    date__lt=now() - timedelta(minutes=60),
                    date__gt=now() - timedelta(days=30),
                    visible_to_level__lte=request.user.profile.level,
                    deleted=False
                ).order_by(
                    '-date'
                )
            ),
        "now": now()
    }

    return render(request, "timerboard/index.html", context)


def delete(request, id):
    timer = Timer.objects.get(id=id)

    if timer.user_can_edit(request.user):
        timer.delete(request.user)
        messages.success(request, "Successfully deleted timer")
        return redirect("timerboard:index")