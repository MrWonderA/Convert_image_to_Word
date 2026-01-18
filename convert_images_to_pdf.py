import os
import re
from pathlib import Path

from PIL import Image


SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}


def extract_number_from_name(name: str) -> int:
    match = re.search(r"(\d+)", name)
    if match:
        return int(match.group(1))
    return float("inf")


def find_images_in_directory(directory: Path):
    images = []
    for entry in directory.iterdir():
        if entry.is_file() and entry.suffix.lower() in SUPPORTED_EXTENSIONS:
            images.append(entry)
    images.sort(key=lambda p: (extract_number_from_name(p.stem), p.name))
    return images


def images_to_pdf(image_paths, output_pdf: Path):
    if not image_paths:
        raise ValueError("该文件夹中没有找到支持格式的图片。")

    pil_images = []
    for path in image_paths:
        img = Image.open(path)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        pil_images.append(img)

    first_image, *rest_images = pil_images
    first_image.save(
        output_pdf,
        save_all=True,
        append_images=rest_images
    )


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="将指定文件夹内的图片按顺序合并为一个 PDF 文件（不改变图片内容，仅封装为 PDF）。"
    )
    parser.add_argument(
        "input_dir",
        type=str,
        help="图片所在的文件夹路径，例如：f:\\images"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="output.pdf",
        help="输出 PDF 文件名或路径（默认：output.pdf）"
    )

    args = parser.parse_args()

    input_dir = Path(args.input_dir).expanduser().resolve()
    if not input_dir.exists() or not input_dir.is_dir():
        raise SystemExit(f"输入路径不存在或不是文件夹: {input_dir}")

    images = find_images_in_directory(input_dir)
    if not images:
        raise SystemExit("该文件夹中没有找到图片，请确认文件扩展名为 jpg/jpeg/png/bmp/tif/tiff/webp。")

    output_pdf = Path(args.output)
    if not output_pdf.is_absolute():
        output_pdf = Path.cwd() / output_pdf

    images_to_pdf(images, output_pdf)
    print(f"已生成 PDF 文件: {output_pdf}")


if __name__ == "__main__":
    main()
