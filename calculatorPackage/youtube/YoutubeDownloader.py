from base64 import main

import click


@click.group()
def apis():  # TODO: A cli for getting transcription of youtube videos
    def main():
        apis(prog_name='apis')


if __name__ == '__main__':
    main()
