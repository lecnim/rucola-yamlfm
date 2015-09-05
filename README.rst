=======================
rucola-yamlfm
=======================

A Rucola plugin used to load YAML front matters from files.

Installation
------------

Install with a ``pip`` command:

::

    $ pip install rucola-yamlfm

Dependencies
~~~~~~~~~~~~

Plugin requires ``pyyaml`` package.

Usage
-----

Load yaml frontmatter from all ``.md`` files:

.. code-block:: python

    from rucola_yamlfm import YamlFrontmatter

    app = Rucola('.')
    app.use(
        YamlFrontmatter()
    )

Load frontmatter from specified files:

.. code-block:: python

    app.use(
        YamlFrontmatter('path/to/file')
        YamlFrontmatter('path/to/dir/*.md')
    )


Options
~~~~~~~

pattern:
    Try to load frontmatter from all files that matches a pattern. Default is ``**/*.md``

limiter:
    Frontmatter limiter. Default is ``---``


License
-------

MIT