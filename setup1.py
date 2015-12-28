from cx_Freeze import setup, Executable
import sys

exe = Executable(
    script="Program_roman_number.py",
    base="Win32GUI",
    )
    
setup(
    name = "Program_roman_number",
    version = "0.1",
    description = "Translit",
    executables = [exe]
)
