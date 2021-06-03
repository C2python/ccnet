# -*- coding: utf8 -*-

INVALID_PARA = 4000
INVALID_AUTH = 4100

DUPLICATE_SW = 4101

error_code = {
    4000: "请求参数非法",
    4100: "身份认证失败",
    4101: "资源已存在"
}

'''
error_code = {
    4000: "请求参数非法",
    4100: "身份认证失败",
    4101: "未授权访问接口",
    4102: "未授权访问资源",
    4103: "未授权访问当前接口所操作的资源",
    4104: "密钥不存在",
    4105: "token 错误",
    4106: "MFA 校验失败",
    4110: "其他 CAM 鉴权失败",
    4300: "拒绝访问",
    4400: "超过配额",
    4500: "重放攻击",
    4600: "协议不支持",
    5000: "资源不存在",
    5100: "资源操作失败",
    5200: "资源购买失败",
    5300: "余额不足",
    5400: "部分执行成功",
    5500: "用户资质审核未通过",
    6000: "服务器内部错误",
    6100: "版本暂不支持",
    6200: "接口暂时无法访问"
}
'''

class CcnetConnectionTimeoutException(Exception):
    '''处理ccnet的超时异常'''
    def __init__(self,code,message=None):
        self.code = code
        if message is not None:
            self.message = error_code[code]
    def __str__(self):
        return "{code: %s, message: %s}" % (self.code,self.message)

class CcnetException(Exception):
    '''ccnet的Except'''
    def __init__(self,code):
        self.code = code
        self.message = error_code[code]
    def __str__(self):
        return "{code: %s, message: %s}" % (self.code,self.message)
    
class CcnetInvalidRequestException(Exception):
    def __init__(self,code):
        self.code = code
        self.message = error_code[code]
    def __str__(self):
        return "{code: %s, message: %s}" % (self.code,self.message)