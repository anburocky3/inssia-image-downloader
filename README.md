# Forum Image Grabber (Inssia)

Simple tool, which will download all images based on the URL provided.

> Some of the elements found on the below platform contains +18 content and if you are under-aged, STOP IT. Its not for you.
## Screenshots

## How to use it?

1. [Fork the repository]() and run the `main.py` using the following command

```shell
python main.py # you have to have python 3 installed.
```

2. It will ask you which directory, output folder name etc. input those information correctly.

| Inputs  | Sample | DataType |
   | ------------- | ------------- | ----|
| - Enter your **URL**, where you want to grab the images:  | Any Post thread link from inssia.com   | _string_ |
| - In Which **directory**, you want to put the images?  | Appropriate folder title | _string_  |
| - From which page to grab **START**? (default: 0):  | Any numeric value or skip (defaults to '0') | _integer_ |
| - Till which page to grab: **END**?  | Any numeric value | _integer_ |
| - Page Per Items count (default: 10):  | Any numeric value or skip (defaults to '10') | _integer_ |

3. It will download it for you. Automatically.

**Sample download end:**
| Status Legend:
   (OK):download completed.(ERR):error occurred. |

**Note:** Download completed mentions on sucessfull downloads with including error occuered contains invalid or broken media (can be ignored).

### Windows:

> No change required in code.
### Linux 

```shell
sudo apt install aria2 # You should make aria2c installed.
aria2c                 # Check with cmd 
```

> Check imgdownloader() in main.py


### License: MIT + (use it with care)

### Tested platforms

- inssia.com

### Authors & Maintainer

- [Anbuselvan Rocky](https://fb.me/anburocky3)