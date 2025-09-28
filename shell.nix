let 
  pkgs = import <nixpkgs> { };
in
  pkgs.mkShell {
    packages = with pkgs;  [
      inetutils
      jetbrains.pycharm-professional
      poetry
      libcdada
    ];
}
