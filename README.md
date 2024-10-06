中文说明
代码 1: 提取文件并保存为 YAML 格式
此代码用于从指定目录中提取支持的文件格式（如 AAMP、BYML 和 MSBT），并将它们转换为 YAML 格式文件。

使用步骤：

确保已安装所需的库（pyyaml, oead, pymsyt）。

将代码保存为 extract_to_yaml.py 文件。

在命令行中运行以下命令：

bash
复制代码
python extract_to_yaml.py <输入目录> <输出目录>
<输入目录>: 包含需要提取的文件的目录路径。
<输出目录>: 要保存转换后 YAML 文件的目录路径。
运行后，程序会遍历输入目录中的所有文件，并将每个文件提取为单独的 YAML 文件，保存在输出目录中。

代码 2: 一键安装所需库
此代码用于一键安装所需的 Python 库。

使用步骤：

将代码保存为 install_packages.py 文件。

在命令行中运行以下命令：

bash
复制代码
python install_packages.py
程序将自动安装 pyyaml、oead 和 pymsyt 等库。如果有其他需要安装的库，可以将它们添加到 required_packages 列表中。

English Instructions
Code 1: Extract Files and Save as YAML Format
This code is used to extract supported file formats (such as AAMP, BYML, and MSBT) from a specified directory and convert them into YAML format files.

Usage Steps:

Ensure the required libraries (pyyaml, oead, pymsyt) are installed.

Save the code as extract_to_yaml.py.

Run the following command in the terminal:

bash
复制代码
python extract_to_yaml.py <input_directory> <output_directory>
<input_directory>: The path of the directory containing the files to be extracted.
<output_directory>: The path of the directory where the converted YAML files will be saved.
After running, the program will traverse all files in the input directory and extract each file as a separate YAML file, saving it in the output directory.

Code 2: One-Click Installation of Required Libraries
This code is used to install the required Python libraries with a single command.

Usage Steps:

Save the code as install_packages.py.

Run the following command in the terminal:

bash
复制代码
python install_packages.py
The program will automatically install libraries such as pyyaml, oead, and pymsyt. If there are other libraries you want to install, you can add them to the required_packages list.
