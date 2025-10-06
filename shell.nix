let 
  pkgs = import <nixpkgs> { };
in
  pkgs.mkShell {
    packages = with pkgs;  [
      inetutils
      jetbrains.pycharm-professional
      poetry
    ];
  env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
    pkgs.stdenv.cc.cc.lib
    pkgs.libz
    ];
}
