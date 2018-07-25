import warnings
import requests

sigle_push_url = "https://sc.ftqq.com"
sigle_push_key = None
group_push_url = "https://pushbear.ftqq.com/sub"
group_push_key = None


def set_sigle_push(key,url=None):
	sigle_push_key = key
	if url:
		sigle_push_url = url


def set_group_push(key,url=None):
	group_push_key = key
	if url:
		group_push_url = url


def _get_msg(title=None,content=None):
	if title is None:
		raise TypeError("Requires a string format title to push.")
	elif content is None:
		warnings.warn("Did not input content.", Warning)
	msg = {'text':title,'desp':content}
	return msg


def single_push(title=None,content=None):
	msg = _get_msg(title,content)
	r = requests.post('%s/%s.send'%(sigle_push_url,sigle_push_key), msg)
	return r


def group_push(title=None,content=None):
	msg = _get_msg(title,content)
	r = requests.post("%s?sendkey=%s"%(group_push_url,group_push_key), msg)
	return r


def push(title=None,content=None,mode='single'):
	if mode=='single':
		return single_push(title,content)
	elif mode=='group':
		return group_push(title,content)
	else:
		raise ValueError("Please choose mode from signle or group.")
