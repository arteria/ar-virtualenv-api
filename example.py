#!/usr/bin/python

from virtualenvapi.manage import VirtualEnvironment
import shutil

def example(path='/tmp/virtualenv.test'):
    env = VirtualEnvironment(path)

    print 'django 1.5 installed?', env.is_installed('django==1.5')

    print 'mezzanine installed?', env.is_installed('mezzanine')
    env.install('mezzanine')
    print 'mezzanine installed?', env.is_installed('mezzanine')

    print env.installed_packages

    payments_repo = 'git+git://github.com/sjkingo/cartridge-payments.git'
    print 'cartridge-payments installed?', env.is_installed(payments_repo)
    env.install(payments_repo)
    print 'cartridge-payments installed?', env.is_installed(payments_repo)
    print env.installed_packages

    env.uninstall('mezzanine')
    print 'mezzanine installed?', env.is_installed('mezzanine')
    print env.installed_packages

    pkgs = env.search('requests')
    print 'search for \'requests\':'
    print len(pkgs), 'found:'
    print pkgs

    shutil.rmtree(path)

if __name__ == '__main__':
    example()
