# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.utils.translation import ugettext_lazy as _
import logging
from django.forms import models
from django import forms
from ..models import Database, Credential, Project
from physical.models import Plan, Environment, DatabaseInfra, Engine
from util import make_db_random_password

from .database import DatabaseForm
from .credential import CredentialForm

LOG = logging.getLogger(__name__)


class ProjectForm(models.ModelForm):
    
    class Meta:
        model = Project
        widgets = {
            'slug': forms.HiddenInput(),
        }