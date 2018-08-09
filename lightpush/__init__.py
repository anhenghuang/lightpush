import warnings
import requests


class lightpush(object):
    single_push_url = "https://sc.ftqq.com"
    single_push_key = ''
    group_push_url = "https://pushbear.ftqq.com/sub"
    group_push_key = ''

    def set_single_push(self, key, url=None):
        self.single_push_key = key
        if url:
            self.single_push_url = url

    def set_group_push(self, key, url=None):
        self.group_push_key = key
        if url:
            self.group_push_url = url

    def _get_msg(self, title=None, content=None):
        if title is None:
            raise TypeError("Requires a string format title to push.")
        elif content is None:
            warnings.warn("Did not input content.", Warning)
        msg = {'text':title,'desp':content}
        return msg

    def single_push(self, title=None, content=None):
        msg = self._get_msg(title,content)
        r = requests.post('%s/%s.send' % (self.single_push_url, self.single_push_key), msg)
        return r

    def group_push(self, title=None, content=None):
        msg = self._get_msg(title,content)
        r = requests.post("%s?sendkey=%s"%(self.group_push_url,self.group_push_key), msg)
        return r

    def push(self, title=None, content=None, mode='single'):
        if mode == 'single':
            return self.single_push(title,content)
        elif mode == 'group':
            return self.group_push(title,content)
        else:
            raise ValueError("Please choose mode from single or group.")
