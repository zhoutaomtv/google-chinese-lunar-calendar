from fabric.api import env, cd, run


env.hosts = ['zhigang@yamaha.dreamhost.com']


def init():
    run('git clone git://github.com/zhigang/google-chinese-lunar-calendar.git /home/zhigang/zhigang.org/public/google-chinese-lunar-calendar')


def deploy():
    with cd('/home/zhigang/zhigang.org/public/google-chinese-lunar-calendar'):
        run('git pull')
