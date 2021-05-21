def load_privx_api_lib_path():
    import sys
    from pathlib import Path

    _dir_path: Path = Path(__file__).parent.absolute()
    _lib_path: Path = _dir_path.parent.absolute()
    sys.path.append(str(_lib_path))
