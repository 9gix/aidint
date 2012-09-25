from fabric.api import env, local, abort, cd, run, sudo
from django.conf import settings

def to(server):
    """Where do you want the fab to be applied"""
    global conf
    conf = settings.FAB_CONFIGS[server]
    if conf and conf['HOST']:
        env.host_string = conf['HOST']
        env.hosts.append(conf['HOST'])
        print "Targeting %s at %s" %(server, conf['HOST'])
    else:
        abort("Please configure your FAB_CONFIGS in your local settings file")


def restart_httpd():
    sudo('service httpd restart')

def deploy(server=None):
    if server:
        to(server)
    try:
        env.key_filename = conf['SSH_KEY']
        env.user = conf['USER']
        path = conf['PATH']
    except:
        abort("Configuration Not Complete")
    with cd(path):
        run("git stash")
        run("git pull origin %s" %conf['BRANCH'])
        restart_httpd()
