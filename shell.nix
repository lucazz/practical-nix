{ pkgs ? import (fetchTarball https://github.com/nixos/nixpkgs-channels/archive/5d59133d968ab97668e0eaabb65d7cefdb6f10f2.tar.gz) {} }:

let
  pythonEnv = pkgs.python37.buildEnv.override {
    extraLibs = with pkgs.python37Packages; [
      sphinx
    ];
  };
in

pkgs.stdenv.mkDerivation {
  name = "practical-nix";

  buildInputs = [ pythonEnv ];
}
