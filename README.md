#Who Contributes?

This is a simple Python script that helps determine who edited a given
wiki page. Often I get asked by folks "Who has edited <group of pages>
on our wiki?" I get a list of pages (either by gathering them from a
Category or from a quervy via the ReplaceText extension). For example,
someone asked if I could find out who has contributed to all pages that
mention a particular phrase. I'd run the string through ReplaceText, and
put the list of titles into this script.

**whoContributes.py** - the actual script itself. Nothing fancy.

**page-titles.txt** - Add a list of all pages you want to check. Each page
title should be on it’s own line.

**output.txt** - Your output will go here. Re-running the script will overwrite this file!