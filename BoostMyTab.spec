# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules

pathex = ['BoostMyTab']
hookspath = ['pyinstaller_hooks'] 
hiddenimports = collect_submodules('PyQt5') + collect_submodules('qtwidgets')

a = Analysis(
    ['.\gui\widgets\main.py'],
    pathex=pathex,
    binaries=[],
    datas=[
        ('gui', 'gui'),
        ('scripts', 'scripts'),
        ('scrcpy-win64-v2.6.1', 'scrcpy-win64-v2.6.1'),
    ],
    hiddenimports=hiddenimports,
    hookspath=hookspath,
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=1,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='BoostMyTab',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True, 
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
