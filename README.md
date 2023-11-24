## sublime-tagref

[tagref](https://github.com/stepchowfun/tagref) integration for sublime text

**wip learning project:** nothing implemented yet

### getting started with development

i plan to keep this codebase dependency-free (besides `tagref` of course). that means no `pip
install`, no virtual environments, etc.

assuming you want to work on this project using _your favorite text editor..._ 😉

1. clone this repo
2. run `make install` to symlink this repo to your sublime packages
3. make sure you have [UnitTesting](https://github.com/SublimeText/UnitTesting) installed from
    Package Control
4. create a `.sublime-project` file with this build system:
    ```json
    "build_systems": [
        {
            "name": "Test sublime_tagref",
            "target": "unit_testing",
            "package": "sublime_tagref"
        }
    ]
    ```
    this will allow you to run tests in your current editor window.
