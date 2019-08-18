import re


class CheckUserInfo:

    def check_mail(self, mail):
        flag = False
        str = '^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        if re.match(str, mail):
            flag = True

        return flag

    def check_pwd_len(self, pwd):
        '''密码长度不超过8位'''
        return len(pwd)>=8

    def check_pwd_contain_leter(self, pwd):
        '''密码包含大小写英文字母'''
        flag = False
        pattern = re.compile('[A-Z][a-z]+')
        match = pattern.findall(pwd)

        if match:
            flag = True
        return flag

    def check_pwd_contain_num(self, pwd):
        '''密码包含数字'''
        flag = False
        pattern = re.compile('[0-9]+')
        match = pattern.findall(pwd)
        if match:
            flag = True
        return flag
