# Vibe: Static Pages & Clean Architecture

This skill enforces a clean, modular architecture for HTML static sites to ensure they remain maintainable, organized, and scalable.

## Architecture Guidelines

1. **Separation of Concerns**:
   - **HTML**: Files should only contain semantic structural code. Avoid inline `<style>` and `<script>` blocks whenever possible.
   - **CSS**: All styling must reside in standalone `.css` files located entirely within the `css/` directory.
   - **JS**: All logical interactions must reside in standalone `.js` files located entirely within the `js/` directory.
   - **Image**: All image assets (PNG, JPG, SVG, etc.) must be stored within the `image/` directory.

2. **Data Decoupling (JSON)**:
   - Data structures, dictionaries, lists, or large arrays that feed into the application should not be hard-coded into the logic blocks (JS) or structure (HTML).
   - Variables containing extensive data must be extracted into their own `.json` files.
   - Save these to the `json/` directory (e.g., if the HTML file is named `app.html`, save data in `json/app.json`).
   - Dynamically load JSON data via `fetch` before initializing JavaScript logic that relies on it.

3. **Break and Combine**:
   - Break giant files into smaller ones where necessary.
   - The HTML file acts as the anchor piece combining these specialized assets (via `<link rel="stylesheet">` and `<script src="...">`).

4. **Directory Rules**:
   - `[filename].html`
   - `css/[filename].css`
   - `js/[filename].js`
   - `json/[filename].json`
   - `image/[image_name].extension`
