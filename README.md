# Downtown
A Python SSG for building websites and web applications from Markdown files.


## Overview
Downtown is a lightweight static site generator (SSG) written in Python that allows you to create websites from Markdown files. It provides a simple way to convert your Markdown content into HTML, with support for custom templates, CSS, and JavaScript. The framework is designed to be easy to use and highly configurable, making it suitable for a variety of web development projects.

## What is an SSG?
A Static Site Generator (SSG) is a tool that generates a full static HTML website based on raw data and a set of templates. Unlike dynamic websites that generate pages on-the-fly using server-side code, SSGs pre-build the entire site, resulting in faster load times and improved security. SSGs are particularly popular for blogs, documentation sites, and portfolios. Some well-known SSGs include Jekyll, Hugo, and Gatsby with each having its own unique features and use cases respectively.


## Features
- Convert Markdown files to HTML.
- Easy configuration through a simple `Sitefile/.Site` JSONC file.
- Use Javascript and CSS for enhanced interactivity and styling.
- Customizable HTML templates for consistent site layout.
- Supports additional configuration files for specific pages.
- Simple command-line interface for building the site.

## Installation
You can install Downtown by cloning the repository, installing dependencies using pip:

```bash
git clone https://github.com/MOHAPY24/downtown.git
cd downtown
pip install -r requirements.txt
```

## Usage
1. Edit the `Sitefile` in the config directory to customize your site settings.
2. Place your Markdown files in the `build/mark` directory.
3. Optional: Create additional `.Site` configuration files in the `build/configs` directory for specific pages.
4. Optional: Add a README for your site in the `build` directory.
5. Optional: Edit the template HTML file in the `src/template` directory to change the basic layout of your site.
6. Optional: Add any custom Javascript or CSS files in the `src/js` and `src/css` directories respectively and add them to your Sitefile/.Site file/s.
7. Run the main script to generate your website:
For POSIX systems:
```bash
bash cmd/build.sh
```
For Windows systems:

```batch
cmd\build.bat
```
7. The generated HTML files alongside the copied optional CSS or JS files will be available in the `build/out` directory.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the BSD-3-Clause License. See the [LICENSE](LICENSE) file for details.
Free for use and modification. Attribution is appreciated but not required. No warranty is provided.
