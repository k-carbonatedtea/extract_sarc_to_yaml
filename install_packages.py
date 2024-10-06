import subprocess
import sys

def install(package):
    """安装指定的库"""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

if __name__ == "__main__":
    # 需要安装的库列表
    required_packages = [
        'pyyaml',
        'oead',
        'pymsyt',
    ]
    
    for package in required_packages:
        try:
            install(package)
            print(f"成功安装 {package}")
        except Exception as e:
            print(f"安装 {package} 时发生错误: {str(e)}")
