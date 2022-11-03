import os
import threading

import click


def list_files(base):
    files = []
    if os.path.isdir(base):
        for dir_name in os.listdir(base):
            files += list_files(os.path.join(base, dir_name))
        return files
    else:
        if base.endswith(".c") or base.endswith(".h"):
            return [base]
        else:
            return []


def do_operate(file, output_dir, encoding):
    with open(os.path.join(file), 'r', encoding=encoding) as i:
        with open(os.path.join(output_dir, os.path.basename(file)), 'w+') as o:
            o.write(i.read())


def operate(file, output_dir, encoding):
    try:
        do_operate(file, output_dir, encoding)
    except UnicodeDecodeError as e:
        try:
            do_operate(file, output_dir, 'utf-8')
        except UnicodeDecodeError:
            click.echo(f"Error: skipping {file} cause {e}")


@click.group()
@click.version_option(version='1.0.0')
def main():
    """Extract keil project files into common C project's"""
    pass


@click.command()
@click.argument('root', type=str)
@click.argument('output', type=str)
@click.option('--encoding', default='utf-8', help='Encoding of the files to be read')
def extract(root, output, encoding):
    if not os.path.exists(output):
        os.mkdir(output)
    elif len(os.listdir(output)) > 0:
        click.echo('Warning: output dir is not empty.')

    lib_dir = os.path.join(root)
    files = list_files(lib_dir)
    jobs = []
    for file in files:
        job = threading.Thread(target=operate, args=[file, output, encoding])
        job.start()
        jobs.append(job)

    for job in jobs:
        job.join()


main.add_command(extract)

if __name__ == "__main__":
    main()
