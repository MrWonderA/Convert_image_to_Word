# Convert_image_to_Word

# 基本运行方式

## 1. 最简单的用法（输出到当前目录的output.pdf）
python convert_images_to_pdf.py "图片文件夹路径"

## 2. 指定输出PDF文件名
python convert_images_to_pdf.py "图片文件夹路径" -o "自定义文件名.pdf"

## 3. 指定完整的输出路径
python convert_images_to_pdf.py "图片文件夹路径" -o "完整路径/文件名.pdf"

# 详细参数说明
usage: convert_images_to_pdf.py [-h] [-o OUTPUT] input_dir

将指定文件夹内的图片按顺序合并为一个 PDF 文件（不改变图片内容，仅封装为 PDF）。

positional arguments:
  input_dir             图片所在的文件夹路径，例如：f:\\images

optional arguments:
  -h, --help            显示帮助信息
  -o OUTPUT, --output OUTPUT
                        输出 PDF 文件名或路径（默认：output.pdf）
