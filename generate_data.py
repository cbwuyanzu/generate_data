# -*- coding: utf-8 -*-
import sys
import requests
import codecs
import json

import time


def get_data(x):
    url = "https://cdz-inquiry-timeseries-service.run.aws-usw02-pr.ice.predix.io/services/pm25services/hourly_data/sensor_id/"
    point = x
    para = "?starttime=1466740800000&endtime=1467219600000"
    print int(time.time() * 1000)

    # noinspection PyBroadException
    try:
        msg = {}
        body0 = {}
        att = {}
        response = requests.get(url + point + para)
        js = response.json()
        # return json.dumps(js)
        # print js[u'tags'][0][u'name']

        att[u'lat'] = js[u'tags'][0][u'results'][0][u'attributes'][u'lat'][0]
        att[u'lng'] = js[u'tags'][0][u'results'][0][u'attributes'][u'lng'][0]
        datapoints = js[u'tags'][0][u'results'][0][u'values']
        for data_point in datapoints:
            data_point[0] += 2592000000
        body0[u'attributes'] = att
        body0[u'name'] = js[u'tags'][0][u'name']
        body0[u'datapoints'] = datapoints
        # print type(body0[u'datapoints'])
        bodies = [body0]
        msg[u'body'] = bodies
        msg[u'messageId'] = int(time.time() * 1000)

        return json.dumps(msg)

    except:
        e = sys.exc_info()[0]
        print "exception"
        print e


def write(x):
    f = open(x + ".json", "w+")
    f.write((get_data(x)))
    f.close()


if __name__ == '__main__':
    # print type(unicode(get_data('1141A'), "utf-8"))
    for node_id in range(41, 51):
        write("11" + str(node_id) + "A")
    write("61726")
    write("61728")
