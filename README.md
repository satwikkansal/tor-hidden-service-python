# tor-hidden-service-python

> A simple boilerplate of creating a `.onion` website for Tor using Flask and Python.

## Instructions

- Download Tor browser from the official site ([link](https://www.torproject.org/download/download))
- Configure your hidden service.
    + Go to the Tor browser directory.
    + Open the "torrc" file in an editor. (Probably located in `Browser/TorBrowser/Data/Tor` directory)
    + Add the following lines to the file
    ```
    HiddenServiceDir /any/path/where/you/want/config/to/be/stored
    HiddenServicePort 80 127.0.0.1:5000
    ```
    + Save and close the file.
- Clone this repository in your local system
```sh
$ git clone https://github.com/satwikkansal/tor-hidden-service-python.git
$ cd tor-hidden-service
```
- Install the pypi requirements
```sh
$ pip -r requirements.txt
```
- Run the server
```sh
$ python run.py
```
- Launch the Tor Browser
- Copy the url generated in the `hostname` file
```sh
$ cat /path/to/config/directory/hostname
>>> some-obfuscated-url.onion
```
- Open this url in the Tor Browser and it should work :tada:

## Contributing

All patches welcome!

## License

MIT License - see the [LICENSE](https://github.com/satwikkansal/readme_styles/blob/master/LICENSE) file for details.
