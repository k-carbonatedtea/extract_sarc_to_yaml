from functools import lru_cache
from pathlib import Path
from typing import Union
import yaml  # 导入 pyyaml 库
import oead
from pymsyt import Msbt
from oead.aamp import get_default_name_table

@lru_cache(1)
def _init_deepmerge_name_table():
    table = get_default_name_table()
    for i in range(10000):
        table.add_name(f"File{i}")

def open_yaml(file: Path) -> dict:
    """读取文件并返回 YAML 格式的数据和对象类型"""
    yaml_str: str
    big_endian: bool
    obj: Union[oead.byml.Hash, oead.byml.Array, oead.aamp.ParameterIO, Msbt]
    obj_type: str

    try:
        data = file.read_bytes()
        if data[0:4] == b"Yaz0":
            data = oead.yaz0.decompress(data)

        if data[0:4] == b"AAMP":
            obj = oead.aamp.ParameterIO.from_binary(data)
            big_endian = False
            _init_deepmerge_name_table()
            yaml_str = obj.to_text()
            obj_type = "aamp"
        elif data[0:2] in {b"BY", b"YB"}:
            obj = oead.byml.from_binary(data)
            big_endian = data[0:2] == b"BY"
            yaml_str = oead.byml.to_text(obj)
            obj_type = "byml"
        elif data[0:8] == b"MsgStdBn":
            obj = Msbt.from_binary(data)
            big_endian = data[0x08:0x0A] == b"\xfe\xff"
            yaml_str = obj.to_yaml()
            obj_type = "msbt"
        else:
            raise ValueError("Unsupported file format.")
    except Exception as e:
        raise ValueError(f"Error processing file {file}: {str(e)}")

    return {"yaml": yaml_str, "big_endian": big_endian, "obj": obj, "type": obj_type}

def save_yaml(yaml_str: str, output_file: Path) -> None:
    """直接将 YAML 数据保存为文件"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(yaml_str)  # 直接保存未处理的 YAML 字符串

def extract_files_from_directory(input_directory: Path, output_directory: Path) -> None:
    """提取指定目录内所有文件并保存为单独的 YAML 文件"""
    for item in input_directory.iterdir():
        if item.is_dir():
            # 递归处理子目录
            new_output_directory = output_directory / item.relative_to(input_directory)
            new_output_directory.mkdir(parents=True, exist_ok=True)
            extract_files_from_directory(item, new_output_directory)  
        else:
            try:
                data = open_yaml(item)
                yaml_data = data['yaml']
                
                # 创建输出文件的路径
                output_file_name = f"{item.stem}.yaml"  # 使用原文件名
                output_file_path = output_directory / item.relative_to(input_directory).with_suffix('.yaml')
                
                # 保存原始 YAML 数据到单独的文件
                save_yaml(yaml_data, output_file_path)  
                
                print(f"成功将 {item.name} 转换并保存为 {output_file_path}")

            except Exception as e:
                print(f"处理文件 {item.name} 时发生错误: {str(e)}")

def main(input_directory: Path, output_directory: Path):
    """主函数，处理输入目录并保存输出文件"""
    try:
        output_directory.mkdir(parents=True, exist_ok=True)  # 创建输出目录
        extract_files_from_directory(input_directory, output_directory)

    except Exception as e:
        print(f"处理目录时发生错误: {str(e)}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("用法: python script.py <输入目录> <输出目录>")
        sys.exit(1)
    
    input_directory_path = Path(sys.argv[1])
    output_directory_path = Path(sys.argv[2])
    
    main(input_directory_path, output_directory_path)
