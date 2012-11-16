# -*- mode: python -*-
import sys
a = Analysis(['LastVK.py'],
             pathex=['.'],
             hiddenimports=[],
             hookspath=None)
a.datas.append((os.path.join('ssl','cacert.pem'), os.path.join('ssl','cacert.pem'), 'DATA'))
if sys.platform == 'win32':
  exename = os.path.join('build', 'pyi.win32', 'LastVK', 'LastVK.exe')
elif sys.platform == 'darwin':
  exename = os.path.join('build', 'pyi.darwin', 'LastVK', 'LastVK')
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=exename,
          debug=False,
          strip=None,
          upx=False,
          console=False,
          icon=os.path.join('icons', 'lastvk.ico'))
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'LastVK'))
app = BUNDLE(coll,
             name=os.path.join('dist', 'LastVK.app'),
             icon=os.path.join('icons','lastvk.icns'))
