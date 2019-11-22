#!/usr/bin/python3

"""This example will create a basic fedora container that is made with hardcoded options, and delete it upon exit."""

import podman

client = podman.Client()
pull = client.images.pull("fedora:latest")
image = client.images.get(pull)

opts = {
    'memory': '1G',
    'memory-reservation': '750M',
    'Memory-swap': '1.5G',
    'detach': True,
    'tty': True,
    'command': '/bin/bash'
    }
container = image.create(**opts)
container.attach(eot=4)

try:
    container.start()
    print()
except (BrokenPipeError, KeyboardInterrupt):
    print('\nContainer disconnected.')
    container.remove(force=True)
