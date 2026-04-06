---
{"dg-publish":true,"permalink":"/90-slipbox/bootstrap/","tags":["notes"],"created":"2026-03-27T09:57:51.493+10:30","updated":"2026-03-27T09:57:51.493+10:30","dg-note-properties":{"created":"2023-09-25","references":null,"tags":"notes","related":["[[90_slipbox/CSS\|CSS]]","[[90_slipbox/HTML\|HTML]]","[[Programming]]"],"orgs":null,"modified":"2026-03-03"}}
---


Bootstrap is a free and [[Open Source Software\|Open Source Software]] web development framework, consisting of [[HTML]], [[90_slipbox/CSS\|CSS]] and [[JavaScript\|JavaScript]] based scripts. Using Bootstrap offers reasonable styling defaults, premade classes for different assets (Cards, Pills, Images), as well as a 12 Column grid system that adaptively scales to the viewport dimensions based on breakpoints.

## General Tips

- Using a [[CSS]] class to set a `min-width` will stop a Column from causing the content to wrap funny when resizing.

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
