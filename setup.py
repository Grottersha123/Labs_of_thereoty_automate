from cx_Freeze import setup, Executable

setup(
    name = "Program_roman_number",
    version = "0.1",
    description = "Translit",
    executables = [Executable("Program_roman_number.py")]
)
