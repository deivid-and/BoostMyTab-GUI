from PyInstaller.utils.hooks import collect_data_files, collect_submodules

datas = collect_data_files('eventlet')
hiddenimports = collect_submodules('eventlet')
