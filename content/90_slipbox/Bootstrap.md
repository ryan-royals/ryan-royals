---
{"dg-publish":true,"dg-path":"Slipbox Notes/Bootstrap.md","permalink":"/slipbox-notes/bootstrap/","tags":["notes"],"created":"2023-09-25","updated":"2025-11-28"}
---

Bootstrap is a free and [[Open Source Software\|Open Source Software]] web development framework, consisting of [[90_slipbox/HTML\|HTML]], [[90_slipbox/CSS\|CSS]] and [[90_slipbox/JavaScript\|JavaScript]] based scripts. Using Bootstrap offers reasonable styling defaults, premade classes for different assets (Cards, Pills, Images), as well as a 12 Column grid system that adaptively scales to the viewport dimensions based on breakpoints.

## General Tips

- Using a [[90_slipbox/CSS\|CSS]] class to set a `min-width` will stop a Column from causing the content to wrap funny when resizing.

```css
.whatIDo {
  border-radius: 13px;
  border: 2px solid #353535;
  padding-top: 18px;
  padding-right: 12px;
  padding-left: 12px;
  margin-right: 10px;
  margin-left: 10px;
  margin-top: 10px;
  font-size: 16px;
  min-width: 140px;
  max-width: 140px;
}
```
