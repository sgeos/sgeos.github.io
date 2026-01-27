---
layout: post
mathjax: false
comments: true
title:  "WASM on a Jekyll Blog with Rust and wasm-bindgen"
date:   2026-01-26 04:19:39 +0000
categories: [rust, wasm, jekyll]
---
Jekyll generates static pages from templates.
It is often used for blogs, like this one.
Sometimes you want to include interactive elements, like calculators.

This post documents how web assembly (WASM) driven UI widget
can be included in a Jekyll blog post with Rust
and `wasm-bindgen`.
It is a tutorial on getting the WASM to work, not a deep dive
into `wasm-bindgen`.

The post largely documents the steps taken to get the following
UI-widget up and running on this page.

<style>
  .wasm-greeting-ui {
    max-width: 300px;
    font-family: sans-serif;
    border: 2px solid red;   /* red outline */
    padding: 0.75rem;        /* some space inside the box */
    border-radius: 4px;      /* optional: slightly rounded corners */
    background-color: #fff;  /* optional: white background */
  }

  .wasm-greeting-ui .line1 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
  }

  .wasm-greeting-ui .line2 {
    font-weight: bold;
  }
</style>
<script type="module" id="wasm_ui">
  import init, { inject_ui } from "/assets/wasm/post_webasm_on_jekyll/post_webasm_on_jekyll.js";
  async function run() {
    await init();
    inject_ui("wasm_ui");
  }
  run();
</script>


## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-01-26 04:19:39 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

# Hardware Information
$ system_profiler SPHardwareDataType | sed -n '8,10p'
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 32 GB

# Shell and Version
$ echo "${SHELL}"
/bin/bash

$ "${SHELL}" --version  | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)

# Rust Installation Versions
$ cargo --version
cargo 1.93.0 (083ac5135 2025-12-15)
```

## Instructions

First, create a new library project.

```sh
PROJECT_NAME="post_webasm_on_jekyll"
cargo new --lib "${PROJECT_NAME}"
cd "${PROJECT_NAME}"
```

Next, add the `js-sys`, `wasm-bindgen`, and `web-sys` dependencies for this project.

```sh
cargo add js-sys
cargo add wasm-bindgen
cargo add web-sys \
  -F Document -F Element -F Event -F EventTarget \
  -F HtmlElement -F HtmlInputElement -F Node -F Window
```

WASM needs to be packaged as a dynamic library, so
set the library type to a C dynamic library using your editor of choice.

`Cargo.toml` partial listing
```toml
[lib]
crate-type = ["cdylib"]
```

Your complete `Cargo.toml` should look something like this.

`Cargo.toml` full listing
```toml
[package]
name = "post_webasm_on_jekyll"
version = "0.1.0"
edition = "2024"

[lib]
crate-type = ["cdylib"]

[dependencies]
js-sys = "0.3.85"
wasm-bindgen = "0.2.108"
web-sys = { version = "0.3.85", features = ["Document", "Element", "Event", "EventTarget", "HtmlElement", "HtmlInputElement", "Node", "Window", ] }
```

Replace `src/lib.rs` with the following contents.

`src/lib.rs` full listing
```rust
use wasm_bindgen::prelude::*;
use wasm_bindgen::JsCast;
use web_sys::{HtmlElement, HtmlInputElement, Event};

#[wasm_bindgen]
pub fn inject_ui(anchor_id: &str) {
    let document = web_sys::window()
        .unwrap()
        .document()
        .unwrap();

    let anchor = document
        .get_element_by_id(anchor_id)
        .expect("anchor element not found");

    let parent = anchor
        .parent_node()
        .expect("anchor has no parent");

    let container = document
        .create_element("div")
        .unwrap();
    container.set_class_name("wasm-greeting-ui");

    // --- Line 1: label + input ---
    let line1 = document.create_element("div").unwrap();
    line1.set_class_name("line1");

    let label = document.create_element("label").unwrap();
    label.set_text_content(Some("Name: "));
    label.set_attribute("for", "name-input").unwrap();

    let input: HtmlInputElement = document
        .create_element("input")
        .unwrap()
        .dyn_into()
        .unwrap();
    input.set_type("text");
    input.set_id("name-input");
    input.set_placeholder("Enter your name");

    // append label + input to line1 container
    line1.append_child(&label).unwrap();
    line1.append_child(&input).unwrap();

    // --- Line 2: message ---
    let message: HtmlElement = document
        .create_element("div")
        .unwrap()
        .dyn_into()
        .unwrap();
    message.set_class_name("line2");

    update_message(&message, None);

    // Append line1 and line2 to the main container
    container.append_child(&line1).unwrap();
    container.append_child(&message).unwrap();

    // Replace the anchor with the new UI
    parent.replace_child(&container, &anchor).unwrap();

    // --- Event listener ---
    let message_clone = message.clone();
    let input_clone = input.clone();
    let closure = Closure::wrap(Box::new(move |_event: Event| {
        let value = input_clone.value();
        if value.trim().is_empty() {
            update_message(&message_clone, None);
        } else {
            update_message(&message_clone, Some(&value));
        }
    }) as Box<dyn FnMut(Event)>);

    input
        .add_event_listener_with_callback("input", closure.as_ref().unchecked_ref())
        .unwrap();

    closure.forget();
}

fn update_message(message: &HtmlElement, name: Option<&str>) {
    let name = name.unwrap_or("USERNAME");
    message.set_text_content(Some(&format!("Hello, {}!", name)));
}
```

Install `wasm-pack` with `cargo` if you need to.

```sh
cargo install wasm-pack
```

Build the WASM with the following command.

```sh
wasm-pack build --target web
```

`wasm-pack` produces files in `pkg/`, which Jekyll will not serve automatically.

```sh
tree pkg/
```

**Expected Output**
```sh
pkg/
├── post_webasm_on_jekyll.d.ts
├── post_webasm_on_jekyll.js
├── post_webasm_on_jekyll_bg.wasm
├── post_webasm_on_jekyll_bg.wasm.d.ts
└── package.json

1 directory, 5 files
```

To serve these files, they need to be copied into
`${JEKYLL_PATH}/assets`, ideally in something like the
`wasm/${PROJECT_NAME}` subdirectory to keep things organized.
Note that you probably do not want to copy the generated `.gitignore`.
Using `pkg/*` ensures we copy all build artifacts while ignoring the hidden
`.gitignore` file that wasm-pack creates, which would otherwise hide your
WASM files from `git` and complicate deployment.
Use the following command to copy the files.

```sh
PROJECT_NAME="post_webasm_on_jekyll"
JEKYLL_PATH="/path/to/jekyll/blog"
mkdir -p "${JEKYLL_PATH}/assets/wasm/${PROJECT_NAME}"
cp -r pkg/* "${JEKYLL_PATH}/assets/wasm/${PROJECT_NAME}/"
```

If you want to **overwrite** existing files automatically, add `-f`.

```sh
cp -rf pkg/* "${JEKYLL_PATH}/assets/wasm/${PROJECT_NAME}/"
```

After copying, all files should be present in the `assets` directory.

```sh
ls -1 "${JEKYLL_PATH}/assets/wasm/${PROJECT_NAME}/"
```

**Expected Output**
```sh
package.json
post_webasm_on_jekyll.d.ts
post_webasm_on_jekyll.js
post_webasm_on_jekyll_bg.wasm
post_webasm_on_jekyll_bg.wasm.d.ts
```

Inline an HTML `script` tag in the blog post to load the WASM. 
Note that the `id` of the `script` tag is used as an anchor, 
which the Rust code will replace with the WASM-driven UI. 
Alternatively, you can use an empty `div` (`<div id="wasm_ui"></div>`) 
or a self-closing tag like `<input type="hidden" id="wasm_ui" />` 
as your anchor if you prefer to keep the script logic and the 
UI placement separate.

```html
<script type="module" id="wasm_ui">
  import init, { inject_ui } from "/assets/wasm/post_webasm_on_jekyll/post_webasm_on_jekyll.js";
  async function run() {
    await init();
    inject_ui("wasm_ui");
  }
  run();
</script>
```

Also, you can add CSS in a `style` block above the `script` tag,
or put it in an included external file if you want to style your UI.

```css
<style>
  .wasm-greeting-ui {
    max-width: 300px;
    font-family: sans-serif;
    border: 2px solid red;   /* red outline */
    padding: 0.75rem;        /* some space inside the box */
    border-radius: 4px;      /* optional: slightly rounded corners */
    background-color: #fff;  /* optional: white background */
  }

  .wasm-greeting-ui .line1 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
  }

  .wasm-greeting-ui .line2 {
    font-weight: bold;
  }
</style>
```

## Future Reading

If you want to explore more about WebAssembly, Rust, and integrating dynamic
UIs in static sites, these resources are highly recommended:

- **Rust and WASM Fundamentals:**
Learn how Rust compiles to WebAssembly, how to use `wasm-bindgen`, and best
practices for building interactive web apps. See the official
[Rust and WebAssembly Book][rust_wasm_book].

- **Jekyll Assets & Static Sites:**
Tips on structuring static assets in Jekyll, managing JavaScript/CSS, and
optimizing for WASM loading can be found in the
[Jekyll Assets Documentation][jekyll_assets].

## References:

- [Rust and WebAssembly Book][rust_wasm_book]
- [Jekyll Assets][jekyll_assets]

[rust_wasm_book]: https://rustwasm.github.io/docs/book/
[jekyll_assets]: https://jekyllrb.com/docs/assets/

