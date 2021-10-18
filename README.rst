This is a sample project for demonstrating a bug in Sphinx's handling of attrs_'
`"next generation" API`__.  When a class is defined with ``@attr.s``, type
annotations on the attributes appear in the documentation, but they do not
appear when the class is defined with ``@attr.define``.

.. _attrs: https://www.attrs.org
__ https://www.attrs.org/en/stable/api.html#next-generation-apis
