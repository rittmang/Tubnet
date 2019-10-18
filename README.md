# Tubnet

On cloning this repository to your PC, run it as :

```sh
$ npm start
```

in the project directory (where src, package etc is present)

------

&nbsp;

In case CTRL+Shift+I shows version error that is was compiled using Node 64 or something, run:

```sh
$ ./node_modules/.bin/electron-rebuild
```

------

### Packaging the application:

Till the time I figure out why it can't be added to $PATH,

```sh
~/.local/bin/pyinstaller src/scripts/python_scripts/sn-api.py --distpath tubnetdist

rm -rf build/
rm -rf api.spec
```

```shell
./node_modules/.bin/electron-packager . --overwrite --ignore="./src/scripts/python_scripts$"
```

