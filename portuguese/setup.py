import cx_Freeze
executables = [cx_Freeze.Executable("run_game.py")]
cx_Freeze.setup(
    name="Living With",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": [
                            "imagens",
                            "audio"
                           ]}},
    executables=executables
)
