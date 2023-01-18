import argparse
import pathlib
import logging
from __init__ import make_report

def html_path(string):
    path = pathlib.Path(string)

    if path.suffix == '.html':
        return path
    elif path.is_dir():
        return path / 'weather.html'
    else:
        raise ValueError('Must be an HTML file or directory')


def main():
    parser = argparse.ArgumentParser(prog='Weather Report Summarizer',
                                     description='Creates a compiled weather \
        report to be send in emails or displayed as a static site.'
                                     )
    parser.add_argument('output', help='Path to html file', type=html_path,
                        default='.', nargs='?')
    parser.add_argument('--log', help='Log path', type=pathlib.Path)
    args = parser.parse_args()

    if 'log' in args:
        logging.basicConfig(filename=args.log, encoding='utf-8',
            level=logging.WARNING, format='%(asctime)s %(message)s')

    # Create the report
    html = make_report()

    # Write the report
    try:
        f = open(args.output, 'w')
    except IOError:
        parser.error('Cannot write to ' f'{args.output}')

    f.write(html)
    f.close()

if __name__ == '__main__':
    main()