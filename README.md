# Downtown
A Python framework for building websites and web applications from Markdown files.

## Features
- Convert Markdown files to HTML.
- Easy configuration through a simple `Sitefile` JSONC file.

## Installation
You can install Downtown by cloning the repository and running the setup python script to install dependencies, project files, and create a virtual environment.:

```bash
git clone https://github.com/MOHAPY24/Downtown.git
cd Downtown
pip install -r requirements.txt
```

## Usage
1. Edit the `Sitefile` in the config directory to customize your site settings.
2. Place your Markdown files in the `build/mark` directory.
3. Optional: Add a README for your site in the `build` directory.
4. Optional: Edit the template HTML file in the `src/template` directory to change the basic layout of your site.
5. Run the main script to generate your website:
For POSIX systems:
```bash
bash cmd/build.sh
```
For Windows systems:

```batch
cmd\build.bat
```
6. The generated HTML files will be available in the `build/out` directory.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the BSD-3-Clause License. See the [LICENSE](LICENSE) file for details.