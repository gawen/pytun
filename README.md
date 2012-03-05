# pytun

`pytun` is a Python module to manage tun/tap IP tunnel in the same way you would manipulate a file handler.

For now, it is only compatible with Linux, probably Unix, maybe MacOsX, and in the future Windows.

`pytun` is under the MIT license.

## How to use

First of all, clone this repos or use `easy_install` or `pip`.

    pip install pytun
    easy_install pytun

Quite easy. Use the `open()` function.

    import pytun

    tun = pytun.open()  # Open a TUN mode tunnel

For a TAP tunnel, add the `"tap"` argument.

    tun = pytun.open("tap")

`tun` is the handler for the newly created tunnel and is manipulated like a file.

To read/write, use the standard methods `recv([size = 1500])` and `send(buf)`

    buf = tun.recv()
    tun.send(buf)

tun is also `select()` compatible to make your network reactor asynchronous.

    import select

    fds = select.select([tun, ...], [...], [...])

Finally, you can close the tunnel using the method `close()`.

    tun.close()

The tunnel automatically closes when the object is not referenced anymore and the garbage collector destroys the handler.


