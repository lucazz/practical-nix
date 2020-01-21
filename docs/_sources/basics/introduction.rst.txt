************
Introduction
************

Nix is a a package manager for Linux and other Unix systems, and it solves two
issues that are inherent to most other package managers. In addition to being a
package manager, Nix is also the programming language you use to write package
specifications (called derivations) for the Nix package manager.

In this chapter, you'll see what those issues are and how Nix addresses them.

The Problem
===========

Say you are working on a web application, and you have a relational database
running on PostgreSQL, and your application expects a PostgreSQL 10 server to
be available in order to function. If you are on an Ubuntu Linux computer, you
probably ran ``apt-get install postgresql-11`` which installed, among different
files, a binary at ``/usr/local/bin/postgres`` which you can use to start the
database server.

PostgreSQL 12 has been around for a while, and it has some interesting features
that you want to try out. If you are on a recent version of Ubuntu Linux, you
can run ``apt-get install postgresql-12`` to upgrade the database server.

APT (the Ubuntu package manager) will fetch the metadata for the new PostgreSQL
package and notice it has a conflict with the previous version. It will then
remove all files associated with the previous version, update its internal
database that there's no longer a conflicting PostgreSQL installed, and finally
proceed with installing the new version with a new bynary at ``/usr/local/bin/postgres``.

What if we want to have the two versions installed at the same time? It's
possible but brittle. Some package managers will, for example, installs Python
2 as ``/usr/local/bin/python`` and Python 3 at ``/usr/local/bin/python3``, and
you will have to adjust your programs and scripts to be aware of the different
binary names.

Nested Package Management
-------------------------

If you work on a high-level programming language such as Ruby or JavaScript,
you are probably are not using just the operating system package manager.
Because packages in these languages are generally smaller in size and developed
at a faster pace, developers of the these languages end up installing a single
OS-level package which is also a package manager for other langauge-specific
packages.

To make things worse, these high-level languages have package managers for
managing different versions of the language. If you are a Ruby developer on
macOS, you probably use homebrew for managing OS-level packages, something like
RVM for managing different versions of Ruby, and finally RubyGems for managing
your Ruby-specific packages.

Why Nix?
========

Nix makes package management purely functional and immutable.

That installed packages no longer mutate the global state of the operating
system. There is no ``/usr/local/bin`` in the Nix store (where Nix package are
installed). If can't just install Flash and have Firefox suddenly playing Flash
content unless you made Flash one of the inputs when building Firefox.

Also, there are no more dynamic libraries such as glibc and zlib that are
globally shared by packages that expect them to exist at certain locations.
Each package determines its own inputs and can only see them. In practice, you
can not break the installation of a package but making changes to another
package.
