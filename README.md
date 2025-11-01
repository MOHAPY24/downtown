# Downtown
A Python framework for building websites and web applications from Markdown files.

## Features
- Convert Markdown files to HTML.
- Support for custom CSS files and JavaScript scripts.
- Easy configuration through a simple `Sitefile` JSONC file.

## Installation
You can install Downtown by cloning the repository and running the setup python script to install dependencies, project files, and create a virtual environment.:

```bash
git clone https://github.com/MOHAPY24/Downtown.git
cd Downtown
python setup.py
```

## Usage
1. Edit the `Sitefile` in the config directory to customize your site settings.
2. Place your Markdown files in the `build/mark` directory.
3. Optional: Add custom CSS files to the `build/css` directory and JavaScript files to the `build/js` directory.
4. Optional: Add a README for your site in the `build` directory.
5. Run the main script to generate your website:
```bash
python src/build.py
```
6. The generated HTML files will be available in the `build/out` directory.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the BSD-3-Clause License. See the LICENSE file for details.