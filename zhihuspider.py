import json
from urllib.request import Request


def start_requests(self):
    return [Request('https://www.zhihu.com/# signin',
                    callback=self.start_login,
                    meta={'cookiejar': 1})
            ]


def start_login(self, response):
    self.xsrf = Selector(response).xpath(
        '//input[@name="_xsrf"]/@value').extract_first()
    return [FormRequest(
        'https://www.zhihu.com/login/email',
        method='POST',
        meta={'cookiejar': response.meta['cookiejar']},
        formdata={
            '_xsrf': self.xsrf,
            'email': 'haihui_blessed@163.com',
            'passeword': 'hui1215cong',
            'captcha_type': 'cn'}
        callback=self.after_login
    )]

    def after_login(self, response):
        if json.loads(response.body)['msg'.encode('utf8'] == "登录成功"：
        self.logger.info(str(response.meta['cookiejar'])
        return [Request(
            self.start_urls[0],
            meta={'cookiejar': response.meta['cookiejar']},
            callback=self.parse_user_info,
            errback=self.parse_err,
        )]