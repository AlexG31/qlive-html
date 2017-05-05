#encoding:utf8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
import json
import os, sys, logging
import time


def index(request):
    '''Default page'''
    template = loader.get_template('html/index.html')
    context = {
        'data_list': [
            'haha',
            'gpf',
            'said',
            'ok'],
    }
    return HttpResponse(template.render(context, request))
