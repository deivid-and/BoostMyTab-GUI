# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules

pathex = ['C:\\Users\\Dale\\Efficiency\\BoostMyTab']
hookspath = ['pyinstaller_hooks'] 

a = Analysis(
    ['entry.py'],
    pathex=pathex,
    binaries=[],
    datas=[
        ('templates', 'templates'), 
        ('static', 'static'), 
        ('scripts', 'scripts'), 
        ('scrcpy-win64-v2.6.1', 'scrcpy-win64-v2.6.1')
    ],
    hiddenimports=collect_submodules('eventlet') + collect_submodules('engineio') + collect_submodules('socketio') + collect_submodules('flask_socketio'),
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
    console=True,            
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,  
    entitlements_file=None,  # Entitlements file for macOS, not used on Windows
)
