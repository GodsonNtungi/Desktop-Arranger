# This is a sample Python script.
import shutil
from pathlib import Path

desktop = Path('')  # Enter path to your desktop
manyFiles = Path(Path.joinpath(desktop, 'ManyFiles'))


def allDict():
    for x in desktop.iterdir():
        print(x)


def Arranger(status):
    if not Path.exists(Path.joinpath(manyFiles, 'Pictures')):
        Path.mkdir(Path.joinpath(manyFiles, 'Pictures'))
        excelPath = Path(Path.joinpath(manyFiles, 'Pictures'))
    else:
        excelPath = Path(Path.joinpath(manyFiles, 'Pictures'))
    for fileformat in ['*.png', '*.png', '*.drawio']:  # Enter format of pictures you wish to arrange
        for x in desktop.glob(fileformat):
            print(x)
            shutil.move(x, excelPath)

    if not Path.exists(Path.joinpath(manyFiles, 'TextFiles')):
        Path.mkdir(Path.joinpath(manyFiles, 'TextFiles'))
        excelPath = Path(Path.joinpath(manyFiles, 'TextFiles'))
    else:
        excelPath = Path(Path.joinpath(manyFiles, 'TextFiles'))
    print(excelPath)
    for fileformat in ['*.txt', '*.docx', '*.pptx', '*.dart']:  # Format for text files
        for x in desktop.glob(fileformat):
            print(x)
            shutil.move(x, excelPath)

    if not Path.exists(Path.joinpath(manyFiles, 'PDFiles')):
        Path.mkdir(Path.joinpath(manyFiles, 'PDFiles'))
        excelPath = Path(Path.joinpath(manyFiles, 'PDFiles'))
    else:
        excelPath = Path(Path.joinpath(manyFiles, 'PDFiles'))
    print(excelPath)
    for fileformat in ['*.pdf']:
        for x in desktop.glob(fileformat):
            print(x)
            shutil.move(x, excelPath)

    for x in desktop.iterdir():  # All others except shortcuts
        if x not in desktop.glob('*.lnk'):
            if x != manyFiles:
                if not x in manyFiles.iterdir():
                    shutil.move(x, manyFiles)

    print(f'Arranging is , {status}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Arranger('DONE')
    # allDict()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
