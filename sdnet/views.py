# -*- coding: utf-8 -*-


from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.http.response import HttpResponseServerError
from sdnet.exceptions.ccnet_exceptions import *
from sdnet.ops import *

import logging
import json

logger = logging.getLogger(__name__)


def health(request):
    logger.info("Health Check")
    return HttpResponse("OK")

# Just Support Post Action
# Interface:
#   {
#       'Action': 'interface',
#       'kwargs': {
#           },
#   }

def fallback(request):
    try:
        import pdb
        #pdb.set_trace()
        if request.method != 'POST':
            raise CcnetException(6100)
        req_data = request.body
        body_json = json.loads(req_data.decode(encoding="utf-8"))
        ret = actions[body_json['Action']](request,body_json["kwargs"])
    except KeyError:
        logger.info("Invaild Request")
        err = {"Error": {"Code": "InvalidParameter","Message": "参数不正确"}, "RequestId": ""}
        return HttpResponseBadRequest(json.dumps(err,ensure_ascii=False),content_type="application/json;charset=utf-8")
    except CcnetException as e:
        logger.error("Unsupport Http Method. Request: %s" % request.get_host())
        err = {"Error": {"Code": e.code,"Message": e.message}, "RequestId": ""}
        return HttpResponseBadRequest(json.dumps(err,ensure_ascii=False),content_type="application/json;charset=utf-8")
    except:
        logger.error("Unkonw ERR")
        err = {"Error": {"Code": "InternalError","Message": "内部错误"}, "RequestId": ""}
        return HttpResponseServerError(json.dumps(err,ensure_ascii=False),content_type="application/json;charset=utf-8")
    return ret