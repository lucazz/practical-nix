Practical Nix
=============

This is a practical guide on how to build, package, and deploy software using
Nix.

If you don't know what Nix is or why you should use it, read
:doc:`basics/introduction` first. :doc:`basics/getting-started` will get you
through installation and basic usage of Nix.
:doc:`basics/anatomy-of-a-derivation` shows what a package specification in Nix
looks like.

Once you are done with the basics, jump over to the build environment that is
relevant to you, and pick an appropriate deployment target. That should cover
the overall process of building and shipping a software package using Nix.

.. toctree::
   :caption: Basics
   :maxdepth: 2
   :hidden:

   basics/introduction
   basics/getting-started
   basics/anatomy-of-a-derivation

.. toctree::
   :caption: Build Environments
   :maxdepth: 2
   :hidden:

   build-environments/c-and-cpp
   build-environments/javascript
   build-environments/python
   build-environments/ruby

.. toctree::
   :caption: Deployment
   :maxdepth: 2
   :hidden:

   packaging-and-deployment/nixos
   packaging-and-deployment/docker-images
   packaging-and-deployment/ci-services
