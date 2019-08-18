import re


class CheckUserInfo:

    def check_mail(self, mail):
        flag = False
        str = '^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        if re.match(str, mail):
            flag = True

        return flag

    def check_pwd_len(self, pwd):
        '''password too short'''
        return len(pwd)>=8

    def check_pwd_contain_leter(self, pwd):
        '''contains upper case and lower case'''
        flag = False
        pattern = re.compile('[A-Z][a-z]+')
        match = pattern.findall(pwd)

        if match:
            flag = True
        return flag

    def check_pwd_contain_num(self, pwd):
        '''contains number'''
        flag = False
        pattern = re.compile('[0-9]+')
        match = pattern.findall(pwd)
        if match:
            flag = True
        return flag
