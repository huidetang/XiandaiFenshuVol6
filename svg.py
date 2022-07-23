import glob
from os import getcwd
from os.path import basename, join
from io import BytesIO

from PIL import Image
from cairosvg import svg2png


def convert(dir):
    path_list = []

    path_file = join(dir, "*.svg")
    filename = glob.glob(path_file)
    path_list.extend(filename)

    for file in path_list:
        converted_file_name = join(dir, (basename(file).split('.', 1)[0] + ".png"))
        print(file + "を" + converted_file_name + "に変換します。")
        png = svg2png(url=file)
        img = Image.open(BytesIO(png)).convert('RGBA')
        img.save(converted_file_name)
        print(converted_file_name + "を出力しました。")
    return


def main():
    image_path = getcwd() + '/images'
    print(image_path + 'のファイルが対象です。')
    convert(image_path)


if __name__ == "__main__":
    main()