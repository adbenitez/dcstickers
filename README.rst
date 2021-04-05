.. image:: https://github.com/adbenitez/dcstickers/raw/master/screenshot.png
   :align: center
   :height: 500
   :alt: screenshot


------

.. image:: https://img.shields.io/github/v/release/adbenitez/dcstickers
   :target: https://pypi.org/project/dcstickers

.. image:: https://img.shields.io/pypi/pyversions/dcstickers.svg
   :target: https://pypi.org/project/dcstickers

.. image:: https://pepy.tech/badge/dcstickers
   :target: https://pepy.tech/project/dcstickers

.. image:: https://img.shields.io/github/license/adbenitez/dcstickers
   :target: https://github.com/adbenitez/dcstickers/blob/master/LICENSE

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

A tool to install sticker packs in your Delta Chat Desktop application.

Install
-------

To install this tool, execute::

  pip install dcstickers


Usage
-----

Once it is installed go to https://signalstickers.com/ search for the sticker pack you want, take the pack URL (the "+ Add to Signal" button), then execute:

```
dcsticker "https://signal.art/addstickers/#pack_id=ffdd9e8ec5dc149aef15aadd38789643&pack_key=5508033752beca5ce1cdf3de8c3039f263c167e594a9748c40c04d707bed188b"
```

Another example with ``sgnl://`` schema URL:

```
dcsticker "sgnl://addstickers/?pack_id=07386433ec62c1ee34cb1d8146bf5b13&pack_key=b8a65656ca79c5cc4e9ea9ba2d4e141188ef2fa964b10c640d00ff148acb8763"
```

You can pass several URLs at the same time.

Then restart your Delta Chat and press the emoji button, now you should see the "Stickers" tab with your stickers. Enjoy!
