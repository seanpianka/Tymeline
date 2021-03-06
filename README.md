# Tymeline

Image organization tool.

## Usage

`$ python tymeline.py <directory>`

The directory is the only argument and specifies the top-level directory where sorting of pictures should be done.

It will create top-level directories denoting the `Year` which images within that directory were taken. A maximum of 12 sub-directories will be created for each of the top-level `Year` directories, each denoting the `Month` which the picture was taken (numerically). Finally, images are then moved into their corresponding folders.

If there are directories or other non-image files at the specified `directory`, they will be moved into a folder called `unsorted` at the top-level `directory`.

Moving new pictures into the top-level `directory`, outside of any of the `Year` folders, and re-executing `tymeline.py` will sort the remaining pictures into their corresponding `Year` directory or `unsorted`.

## Example

```
~/test » tree # unsorted images at the top-level directory
.
├── 20150621_143458.JPG
├── 20160704_125048.JPG
├── 20161028_235123.JPG
├── 20161029_144521.JPG
└── 20170624_143638.JPG

0 directories, 5 files
------------------------------------------------------------
~/test » python ~/Development/Tymeline/tymeline.py . # '.' is my top-level directory
------------------------------------------------------------
~/test » tree # all images are sorted according to their EXIF data (or creation/last modified as fallback if EXIF is not available)
.
├── 2015
│   └── 06
│       └── 20150621_143458.JPG
├── 2016
│   ├── 07
│   │   └── 20160704_125048.JPG
│   └── 10
│       ├── 20161028_235123.JPG
│       └── 20161029_144521.JPG
└── 2017
    └── 06
        └── 20170624_143638.JPG

7 directories, 5 files
------------------------------------------------------------
```
