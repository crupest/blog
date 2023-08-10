---
title: "How to Create a Theme for an App"
date: 2023-08-04T15:30:12+08:00
categories: Coding
tags:
  - Web
  - Design
description: "A method to create a theme of an app by the developer himself/herself."
draft: true
---

Recently I'm developing my [Timeline](https://github.com/crupest/Timeline) app. One of the goals is to refactor the theme, aka, color system.

I used to try to implement a color system like this. User can choose a color as the primary color, and the app will generate a series of colors (palette) based on the primary color, which then are used to colorize the UI components. But I found it's not a good idea. The generated colors are not harmonious, so it's not good-looking. Maybe it's because I'm not a color expert.

So I'm going to remove the custom color system and turn to use a fixed color palette. It will largely reduce the complexity. And I can implement the *dark mode* more easily.

However, it's still a problem to design the colors in the palette. After I chose the primary color, which is most likely to be *blue*, I have to create other variants of the primary color and use them to colorize the UI components.

So how to derive a palette from a primary color? How many colors do I need? Which color should be used on which UI component? What about different states of a component? These all become problems. And I have struggled on this for a long time.

After a lot of tries, I come up with a rather easy process. First, I need to list all the colors I will use for all components and mark those that need to have both light and dark variants. Then I create colors for them, and do the test to ensure they are beautiful.

1. List all components and the colors used by them (including colors for different states of components). At the same time, mark the colors that need to have both a dark and a light variant.
2. Merge the colors that can be used at different places.
3. Choose real colors for the colors needed.

## Key Color

Some colors are key color based. Some are not. Key color indicates the action type of a component. Basic key colors are:

- *Primary*, the default color, used for primary action, or you don't know which key color should be used/.
- *Secondary*, used for non-primary action.
- *Create*, used for creating, success, or anything that you think is good.
- *Danger*, used for deleting, or anything that you think is dangerous.

## List All Colors

By default, colors need a light and a dark variant unless explicitly noted.

### Common

``` plain
- body.background
- text.primary
- text.secondary
```

### Button

*push button*, the most commonly used buttons, used as the button for primary action, or you don't know the type of button you should use.

``` plain
- push-button.[key].background.normal
- push-button.[key].background.hover
- push-button.[key].background.focus
- push-button.[key].background.active
- push-button.[key].text
- push-button.disabled.background
- push-button.disabled.text
```

*outline button*, the outline version of push button, used for second action, or where push button is not suitable.

``` plain
- outline-button.[key].border.normal
- outline-button.[key].border.hover
- outline-button.[key].border.focus
- outline-button.[key].border.active
- outline-button.[key].text
- outline-button.disabled.border
- outline-button.disabled.text
```

*flat button*, button embed in background, used when button should not be so, showy?

``` plain
- flat-button.[key].background.normal
- flat-button.[key].background.hover
- flat-button.[key].background.focus
- flat-button.[key].background.active
- flat-button.[key].text
- flat-button.disabled.background
- flat-button.disabled.text
```

*icon button*, button with an icon.

``` plain
- icon-button.[key].color.normal
- icon-button.[key].color.hover
- icon-button.[key].color.focus
- icon-button.[key].color.active
- icon-button.disabled.color
```

*summary for button*, merge all colors that can be commonly used.

``` plain
- button.[key].normal
  - push-button.[key].background.normal
  - outline-button.[key].border.normal
  - icon-button.[key].color.normal
  - flat-button.[key].text
- button.[key].hover
  - push-button.[key].background.hover
  - outline-button.[key].border.hover
  - icon-button.[key].color.hover
- button.[key].focus
  - push-button.[key].background.focus
  - outline-button.[key].border.focus
  - icon-button.[key].color.focus
- button.[key].active
  - push-button.[key].background.active
  - outline-button.[key].border.active
  - icon-button.[key].color.active
- button.disabled
  - push-button.disabled.background
  - push-button.disabled.text
  - outline-button.disabled.border
  - outline-button.disabled.text
  - icon-button.disabled.color
  - flat-button.disabled.text
```
