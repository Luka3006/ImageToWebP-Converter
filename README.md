# ImageToWebp-Converter
A python tool to convert unlimited images (.png, .jpg) to .webp images.

WebP is a modern image format that provides superior lossless and lossy compression for images on the web. Using WebP can create smaller, richer images that make the web faster.

The easiest way to convert images to WebP is to use Online Converters. But there you always have a limit of (for example) 10 images per day... Another way is to import every single image to Photoshop or Gimp (with an extra Plugin) and export it as WebP or to use tools for WebP images. But if you want to convert some images to WebP quickly these aren't good options. For that case: here you go! :)

## How to use it
1. Download the files
2. Put your images (.png or .jpg) into the "input" folder
3. Run the Python Script (Python 3.9)
4. Your converted images are located in the "output" folder

## How it works
The python script uses the _[WebP Conversion Tool](https://developers.google.com/speed/webp)_ and just runs this tool over every file in the "input" folder.
