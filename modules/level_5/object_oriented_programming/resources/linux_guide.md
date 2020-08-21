# OOP - Setup guide for Linux users

One of the best parts about this module is it can be done on all 3 major operating systems. The goal of this document is to provide all relevant knowledge required to setup tooling for this module on Linux-based computers. Do note that all "optional" configurations listed here are totally optional and can be safely ignored.

## First half of module - MerkleRex

### General setup

First half of this course does not use any special package. All you need is a modern compiler.

On Ubuntu-based systems, the `build-essential` package provides everything we need, which is a modern C++ compiler (gcc/g++) and `make` for defining project build process.

    sudo apt install build-essential

If you're using any other distribution you need to install `GNU C/C++ Compiler` packages.

### Set up code completion for Visual Studio Code

1. Install Visual studio or [VSCodium](https://vscodium.com/) (MS-free version of VS Code).
2. Install [C/C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) to get code completion.

### Set up code completion for Vim

1. Install `vim` or `neovim` through your package manager.
2. Install [Node.js LTS version](https://nodejs.org/en/).
3. Install [coc.nvim](https://github.com/neoclide/coc.nvim) package with your preferred package manager. We recommend [vim-plug](https://github.com/junegunn/vim-plug).
4. Install [coc-clangd](https://github.com/clangd/coc-clangd) which provides clangd Language Server Protocol ([LSP](https://microsoft.github.io/language-server-protocol/)) integration in coc/vim.

### Optional configurations

- Create `Makefile` for your project. A make file defines your project dependencies and does the least possible amount of work required to compile your project: [GNU Make documentation](https://www.gnu.org/software/make/manual/html_node/Simple-Makefile.html).
- Install `clang-format` for autoformatting C++ files. Clang format uses a `.clang-format` file in root for understanding your preferences. A sample file that follows code style in lectures is present here: [amenat/dotfiles/.clang-format](https://github.com/amenat/dotfiles/blob/master/.clang-format). You can configure "format on save" in [VS Code from settings](https://code.visualstudio.com/docs/cpp/cpp-ide#_code-formatting); or in Vim by adding C++ extensions to `coc.preferences.formatOnSaveFiletypes` in `coc-settings.json` ([example](https://github.com/amenat/dotfiles/blob/master/.config/nvim/coc-settings.json#L8)).
- Setup `cppcheck` and `clang-tidy` for static analysis of your code. These tools help spot common errors.
- Install `valgrind` for checking memory leaks. Ideally you should not be doing any memory management on your own at this stage.
- Install `gdb` for debugging.
- Install and use `git`. The git sections of REPL ([YouTube], [websites], [courses]) have lots of video suggestions and links for learning git.

[youtube]: ../../../../youtube/README.md#git--github
[websites]: ../../../../websites/README.md#git--github
[courses]: ../../../../online_courses/free/README.md#git--github

## Second half of module - JUCE app

-- work in progress --

General recommendation: If you're new to Linux, try the [missing-semester](https://missing.csail.mit.edu/) series of lectures from MIT.

If you ever get stuck, post in `#linux` Slack channel.
