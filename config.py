import os
# 找到文件的目录，即project跟目录，作为BASE_DIR
BASE_DIRS = os.path.dirname(__file__)

# options

options = {
    'port': 8080
}

# settings
# settings in web.py, Application.__init__(),
# template_path
# static_path
#debug
# static_url_prefix
# autoreload
#...

settings = {
    # 开发时开启debug, 1）每次保存都重启服务 2) 不使用缓存
    'debug': True,
    # 设置绝对路径，避免每次都要写具体绝对路径
    'template_path': os.path.join(BASE_DIRS, "templates"),
    'static_path': os.path.join(BASE_DIRS, "statics")
}