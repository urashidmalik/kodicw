#!/bin/bash
find /Users/umair/ -name ".DS_Store" -depth -exec rm {} \;
rm -rf /Users/umair/software/opensource/kodicw/plugin.video.umairthecw*.zip
zip -r plugin.video.umairthecw-$(date +"%Y%m%d-%H%m%s").zip  plugin.video.umairthecw