# Aquarion Scripts

Scripts designed to assist with managing and modifying SCSS files within the Aquarion theme. These scripts help with tasks like replacing shorthand variables, removing invalid selectors, and converting raw CSS to placeholders. They are intended for use with the Aquarion project but can be modified for individual use cases.

---

## Table of Contents
- [Scripts Overview](#scripts-overview)
- [Detect and Replace](#detect-and-replace) | [Usage](#detect-and-replace-usage)
- [Remove Invalids](#remove-invalids) | [Usage](#remove-invalids-usage)
- [Replace Raw CSS](#replace-raw-css) | [Usage](#replace-raw-css-usage)

---

## Scripts Overview
The Aquarion Scripts help automate certain tasks within the theme, such as replacing shorthand variables, cleaning up obsolete selectors, and converting raw CSS into placeholder names. Below is an overview of each script and its purpose:

- **Detect and Replace:** Scans SCSS files for shorthand references that can be replaced with variables defined in the `variables.scss` file.
- **Remove Invalids:** Scans SCSS files for placeholder selectors that no longer exist, helping to clean up outdated or orphaned code.
- **Replace Raw CSS:** Replaces raw CSS selectors with placeholders, making it easier to manage styles across projects and reduce duplication.

---

## Detect and Replace
This script aids in finding references that can be shorthand and replacing them with the appropriate variable from the `variables.scss` file.

**Maintained by [Snow](https://github.com/babyboysnow)**

<details>
<summary>Usage</summary>
<a id="detect-and-replace-usage"></a>

```bash
python detect_and_replace.py
```

Modify the `variables.scss` file to ensure all your shorthands are defined. Run the script to automatically replace any shorthand references in your SCSS files.

**Note:** This script was designed for use with the Aquarion variables and may need modification for other use cases.
</details>

---

## Remove Invalids
This script scans SCSS files for selectors that no longer exist, helping to clean up invalid placeholders.

**Maintained by [Snow](https://github.com/babyboysnow)**

<details>
<summary>Usage</summary>
<a id="remove-invalids-usage"></a>

```bash
python remove_invalids.py
```

Make sure to adjust the `selector_file_path` and `scss_directory` in the script to fit your project structure. Running the script will remove any invalid or obsolete selectors from your SCSS files.

**Note:** This script was designed specifically for Aquarion, so some adjustments may be necessary for other projects.
</details>

---

## Replace Raw CSS
This script replaces raw CSS selectors with placeholders, making the code more modular and easier to manage.

**Maintained by [Snow](https://github.com/babyboysnow)**

<details>
<summary>Usage</summary>
<a id="replace-raw-css-usage"></a>

```bash
python replace_raw_css.py
```

Ensure that the `selector_file_path` and `ignore_files` are set correctly for your project. This script will generate placeholders for CSS selectors, using the class name without any suffixes.

**Example:** The class `.archivedDivider_a6d69a` will be replaced with the placeholder `%archivedDivider`.
</details>

---
