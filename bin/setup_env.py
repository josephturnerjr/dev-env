#!/usr/bin/python

import subprocess
import os

    
class Install:
    def __init__(self):
        pass

    def init_packaging(self):
        print "Updating packaing info"
        subprocess.call(['apt-get', 'update'])

    def install_package(self, package_name):
        print "Installation package %s via apt-get" % package_name
        subprocess.call(['apt-get', 'install', package_name])

    def install_custom(self):
        print "Performing custom install actions"
        pass

    def install(self):
        try:
            'test' in self.package_list
            self.init_packaging()
            for p in self.package_list:
                self.install_package(p)
            self.install_custom()
        except AttributeError:
            print "The Install class should be subclassed, with the child at least defining package_list." 
            print "The child may also override the install_custom command with non-apt package installation methods."
    

class BaseInstall(Install):
    def __init__(self):
        self.package_list = ['thunderbird', 'pidgin', 'flashplugin-installer', 'curl']

    def install_custom(self):
        self.install_chrome()
        self.install_skype()
        self.setup_home()
    
    def install_chrome(self):
        print "Opening browser to Chrome download page"
        subprocess.call(['firefox', 'http://www.google.com/chrome/eula.html'])

    def install_skype(self):
        print "Opening browser to Skype download page"
        subprocess.call(['firefox', 'http://www.skype.com/intl/en-us/get-skype/on-your-computer/linux/'])

    def setup_home(self):
        ''' Checkout git repo with vimrc etc, put things in place, fix paths in bashrc '''
        pass

class DevInstall(Install):
    def __init__(self):
        self.package_list = ['g++', 'vim', 'subversion', 'make', 'python2.6-dev', 'git-core']
        self.third_dir = '/opt/miserware-libs'
        self.thirdparty_url = 'https://slug.internal.miserware.com/svn/mw-3rdparty-lib/trunk'

    def install_custom(self):
        self.install_3rdparty_libs()

    def install_3rdparty_libs(self):
        print "Installing 3rdparty libraries from MiserWare repo"
        os.chdir('/tmp')
        os.mkdir('3rdparty')
        os.chdir('3rdparty')
        subprocess.call(('svn co %s' % self.thirdparty_url).split(' '))
        os.chdir('trunk')
        subprocess.call(['make', 'install'])
        

class WebDevInstall(Install):
    def __init__(self, web_dir = '/opt/web'):
        self.package_list = ['libssl-dev', 'git-core']
        self.web_dir = web_dir
        self.npm_url = 'http://npmjs.org/install.sh'
        self.node_url = 'git://github.com/joyent/node.git'

    def install_custom(self):
        self.setup_web_dir()
        self.install_node()
        self.install_npm()
        self.install_django()

    def setup_web_dir(self):
        os.mkdir(self.web_dir)
        os.chown(self.web_dir, os.getuid(), os.getgid())
        with open('~/.bashrc', 'a') as bashrc:
            bashrc.write('export PATH=$PATH:%s' % self.web_dir)

    def install_node(self):
        os.chdir('/tmp')
        subprocess.call(('git clone --depth 1 %s' % self.node_url).split(' '))
        os.chdir('node')
        subprocess.call('git checkout origin/v0.4'.split(' '))
        subprocess.call(('./configure --prefix=%s' % self.web_dir).split(' '))
        subprocess.call(['make'])
        subprocess.call(['make', 'install'])

    def install_npm(self):
        p1 = subprocess.Popen(['curl', self.npm_url], stdout=PIPE)
        p2 = subprocess.Popen(['sh'], stdin=p1.stdout, stdout=PIPE)
        p1.stdout.close()
        print p2.communicate()[0]
        
if __name__ == "__main__":
    print "This script will set up your development environment."
    a = WebDevInstall()
    a.install_node()

