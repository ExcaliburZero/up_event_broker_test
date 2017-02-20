##from lsstbroker.binary_classifier import *
#from lsstbroker.classifier import *
#from lsstbroker.classifier_box import *
#from lsstbroker.handler import *
#from lsstbroker.observation import *

from lsstbroker import *

import upsilonextract as up

import getpass
import sys

def create_handler():
    classifiers = create_classifiers()

    host = "localhost"
    database = raw_input("Database: ")
    username = raw_input("Username: ")
    password = getpass.getpass()
    handler = MySqlDatabaseHandler(host, database, username, password)
    handler.set_classifier_box(classifiers)

    return handler

def create_classifiers():
    cb = ClassifierBox()

    rr_lyrae_ab = create_rr_lyrae_ab()
    cb.add_classifier(rr_lyrae_ab)

    return cb

def create_rr_lyrae_ab():
    def f(x):
        if len(x) > 80:
            time = map(lambda a: a.time, x)
            light = map(lambda a: a.light, x)
            error = map(lambda a: a.error, x)

            e_features = up.ExtractFeatures(time, light, error)
            e_features.run()
            features = e_features.get_features()
            return features["period"]
        else:
            return 0.0

    name = "RR Lyrae ab"
    c = Classifier(name, f)
    return c
