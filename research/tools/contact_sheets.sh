#!/usr/bin/env bash
# Contact sheets per ad: full ad at 1 fps (6x12 grid) + first 3 s at 3 fps (3x3),
# with burned-in timestamps. Also prints scene-cut times.
# Usage: research/tools/contact_sheets.sh competitor_ads research/contact_sheets
set -euo pipefail
src=${1:-competitor_ads}; out=${2:-research/contact_sheets}; mkdir -p "$out"
F=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
i=1
for f in "$src"/*.mp4; do
  n=C$(printf %02d $i)
  ffmpeg -v error -y -i "$f" -vf "fps=1,scale=240:240,drawtext=fontfile=$F:text='%{pts\:hms}':x=4:y=4:fontsize=16:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=6x12" -frames:v 1 "$out/${n}_full_1fps.jpg"
  ffmpeg -v error -y -i "$f" -t 3 -vf "fps=3,drawtext=fontfile=$F:text='%{pts\:hms}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=3x3" -frames:v 1 "$out/${n}_hook_0-3s.jpg"
  echo "$n cuts: $(ffmpeg -v info -i "$f" -vf "select='gt(scene,0.28)',showinfo" -an -f null - 2>&1 | grep -o 'pts_time:[0-9.]*' | cut -d: -f2 | awk '{printf "%.1f ",$1}')"
  i=$((i+1))
done
