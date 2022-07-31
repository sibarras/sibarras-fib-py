import os
import pathlib
import requests # type: ignore

def get_latest_version_number() -> str:
    # dynamic repo name based on folder
    repo_name = pathlib.Path(__file__).parent.name
    req = requests.get(
      f"https://pypi.org/pypi/{repo_name}/json")
    
    return req.json()["info"]["version"]

def unpack_version_number(version_str: str) -> tuple[int, int, int]:
    version_buffer = version_str.split('.')
    v1, v2, v3 = version_buffer
    return int(v1), int(v2), int(v3)

def increase_version_number(version_buffer: tuple[int, int, int]) -> tuple[int, int, int]:
    first, second, third = version_buffer
    third += 1
    if third >= 10:
        third = 0
        second += 1
        if second >= 10:
            second = 0
            first += 1
    return first, second, third

def pack_version_number(version_buffer: tuple[int, int, int]) -> str:
    return ".".join(str(i) for i in version_buffer)

def write_version_to_file(version_number: str) -> None:
    version_file_path = pathlib.Path(__file__).parent / "sibarras_fib_py" / "version.py"
    if version_file_path.exists():
        os.remove(version_file_path)
    with open(version_file_path, "w") as f:
        f.write(f"VERSION='{version_number}'")
    
if __name__ == "__main__":
    ver_nbr = get_latest_version_number()
    buff = unpack_version_number(ver_nbr)
    new_buff = increase_version_number(buff)
    new_ver_nbr = pack_version_number(new_buff)
    write_version_to_file(new_ver_nbr)
