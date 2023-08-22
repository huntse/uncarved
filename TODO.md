# Some things still to sort out

## I-Ching server
[ ] Make a container-based server to serve hexagrams. The idea will be to run
this on fargate and it will generate hexagrams lazily using a timed cache. I
want to make 3 endpoints:
- /hex1 (redirect to the current static hexagram)
- /hex2 (redirect to the current hexagram with moving lines inverted)
- /hexes (return a json structure for 2 hexagrams with urls  to the images, alt text and the
  proper name of the hexagrams and maybe even the hex itself as utf8).  This
  would be for use if I write javascript to rewrite the in-page hexes.

## Sundry small tasks
[ ] Sync AWS lambda rewrite to git
[ ] clean up the zola branch and move to devel
[ ] maybe write a git hook to rclone when pushing to devel
