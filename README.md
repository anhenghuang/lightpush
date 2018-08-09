### lightpush

这是对[**ServerChan**](http://sc.ftqq.com/) 和 [**PushBear**](https://pushbear.ftqq.com/admin/#)服务的一个简单封装，能够通过微信向用户或用户组推送消息提醒。

适用的场景有异常警报、事件提醒、消息推送等。之所以做这个封装是因为py里每次调用requests有点丑 :)

---

This is a simple package for [**ServerChan**](http://sc.ftqq.com/) and [**PushBear**](https://pushbear.ftqq.com/admin/#).

**ServerChan** and **PushBear** are free services for you to push notifications to WeChat.

**lightpush** is a simple wrapper for those services.

You can install lightpush by

```shell
pip install lightpush --user
```

And it is very convenient to use lightpush (like ServerChan)

```python
from lightpush import lightpush

lgp = lightpush()

# For ServerChan
lgp.set_single_push("Your Key")
lgp.single_push("Hello World","This is a msg from lightpush.")

# For PushBear
lgp.set_group_push("Your Key")
lgp.group_push("Hello World","This is a msg from lightpush.")
```

---

[Blog for lightpush](https://www.huanganheng.com/lightpush.html)


