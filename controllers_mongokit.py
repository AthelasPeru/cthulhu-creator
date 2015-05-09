from __future__ import print_function
import os
import uuid
import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, json


from models import User, Character

api2 = Blueprint("api2", __name__)