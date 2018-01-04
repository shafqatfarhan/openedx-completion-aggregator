# -*- coding: utf-8 -*-
"""
Database models for completion_aggregator.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class AggregateCompletion(TimeStampedModel):
    """
    TODO: replace with a brief description of the model.
    """

    # TODO: add field definitions

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<AggregateCompletion, ID: {}>'.format(self.id)
