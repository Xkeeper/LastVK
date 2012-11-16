import os
import shutil
from setuptools import setup


os.system("rm -rf dist")
os.system("rm -rf build")

NAME = 'LastVK'
VERSION = '0.0.1'
APP = ['LastVK.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': False,
 'iconfile': 'icons/LastVK.icns',
 'compressed': 2,
 'includes': ['sip', 'PyQt4', 'mutagen', 'pylast', 'requests',],
 'packages': ['lxml', 'certifi'],
 'qt_plugins': ['imageformats/libqgif*'],
 'plist'   : {'CFBundleName': NAME,
              'CFBundleVersion': VERSION,
              'CFShortVersionString': VERSION,
              'CFBundleGetInfoString': ' '.join([NAME, VERSION]),
              'CFBundleExecutable': NAME,
              'CFBundleIdentifier': 'com.testsoft.LastVK',
              'NSHumanReadableCopyright': 'testsoft (c)2012',
              'LSUIElement': 1}
}

setup(
app=APP,
data_files=DATA_FILES,
options={'py2app': OPTIONS},
setup_requires=['py2app'],
)
#file = open('dist/' + appName + '/Contents/Resources/qt.conf', 'w')
#file.write('[Paths]\nPrefix = .\nBinaries = .\n')
#
#appPath = thisPath + '/dist/' + appName + '/Contents'
#
## Need to copy JPEG and GIF plugins
#os.mkdir(appPath + '/plugins')
#os.mkdir(appPath + '/plugins/imageformats')
#shutil.copy(qtPath + '/plugins/imageformats/libqgif.dylib', appPath + '/plugins/imageformats')
## Set the path to the Qt frameworks in the plugins
#pluginPath = appPath + '/plugins/imageformats'
#os.system(
#    'install_name_tool -change ' + qtPath + '/lib/QtGui.framework/Versions/4/QtGui ' +
#    '@executable_path/../Frameworks/QtGui.framework/Versions/4/QtGui ' +
#    pluginPath + '/libqgif.dylib'
#)
#os.system(
#    'install_name_tool -change ' + qtPath + '/lib/QtGui.framework/Versions/4/QtCore ' +
#    '@executable_path/../Frameworks/QtCore.framework/Versions/4/QtCore ' +
#    pluginPath + '/libqgif.dylib'
#)
