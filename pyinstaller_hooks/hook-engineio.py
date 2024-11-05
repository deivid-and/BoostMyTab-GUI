from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules('engineio') + ['engineio.async_drivers.eventlet']
