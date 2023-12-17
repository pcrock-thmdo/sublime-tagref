## sublime-tagref

[tagref](https://github.com/stepchowfun/tagref) integration for sublime text

**wip learning project**

### features

* [x] tag autocomplete
* [ ] go to tag

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
    {
        "folders": [
            /* ... */
        ],
        "build_systems": [
            {
                "name": "Test sublime-tagref",
                "target": "unit_testing",
                "package": "sublime-tagref"
            }
        ]
    }
    ```
    this will allow you to run tests in your current editor window using the
    `Build With: Test sublime-tagref` command in your command pallette.
