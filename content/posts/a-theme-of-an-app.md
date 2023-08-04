---
title: "How to Create a Theme of an App"
date: 2023-08-04T15:30:12+08:00
categories: Coding
tags:
  - Web
  - Design
description: "I'm a programmer rather than a designer. But when you develop an App by yourself, you have to play a role in UI design. Here are some insights about creating a theme, aka, color system for an app."
draft: true
---

Recently I'm developing my [Timeline](https://github.com/crupest/Timeline) app. One of the goals is to refactor the theme, aka, color system.

I used to try to implement a color system like this. User can choose a color as the primary color, and the app will generate a series of colors (palette) based on the primary color, which then are used to colorize the UI components. But I found it's not a good idea. The generated colors are not harmonious, so it's not good-looking. Maybe it's because I'm not a color expert.

So I'm going to remove the custom color system and turn to use a fixed color palette. It will largely reduce the complexity. And I can implement the dark mode more easily.

However, it's still a problem to design the colors in the palette. After I chose the primary color, which is most likely to be *blue*, I have to create other variants of the primary color and use them to colorize the UI components.

So how to derive a palette from a primary color? How many colors do I need? Which color should be used on which UI component? What about different states of a component? These all become problems. And I have struggled on this for a long time.

After a lot of tries, I come up with a rather easy process. First, I need to list all the colors I will use for all components and mark those that need to have both light and dark variants. Then I create colors for them, and do the test to ensure they are beautiful.
