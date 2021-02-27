#!/bin/sh
for lang in $(find . -maxdepth 1 -type d -regex './.._..'); do
    po=$lang/LC_MESSAGES/unobot.po
    msgmerge -o $po --no-wrap $po unobot.pot
done
