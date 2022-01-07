import datetime
from pathlib import Path

import click
import PyPDF2


def combine(src: Path, dst: Path) -> None:
    merger = PyPDF2.PdfFileMerger()

    for p in sorted(src.glob('*.pdf')):
        merger.append(str(p))

    merger.write(str(dst))
    merger.close()


@click.command()
@click.argument('src', type=click.Path(exists=True))
@click.option('--dst', type=click.Path(exists=True), help='出力ディレクトリ',
              default=Path(__file__).parents[3] / 'output')
def main(src: str, dst: str):
    """対象ディレクトリ以下のPDFを1つにまとめる"""
    src = Path(src)
    dst = Path(dst)
    file_path = dst / f'merged_{datetime.datetime.now()}.pdf'

    combine(src, dst=file_path)

    click.echo(f'Combined {file_path}')


if __name__ == '__main__':
    main()
