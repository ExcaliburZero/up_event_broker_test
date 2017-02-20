#!/usr/bin/python

from flask import Flask, request
import lsstbroker

from classifiers import *

app = Flask(__name__)
handler = None

@app.route("/post", methods=['POST'])
def post():
    #print request.data
    json = request.get_json()
    print json
    observation = parse_observ_json(json)
    handler.run(observation)
    return str(observation)

def parse_observ_json(json):
    object_id = json["id"]
    time = json["time"]
    magnitude = json["magnitude"]
    error = json["error"]

    return lsstbroker.Observation(object_id, time, magnitude, error)

if __name__ == "__main__":
    handler = create_handler()
    app.run()
