#!/usr/bin/env bash
set -e
cd /c/Users/WIN10/STEELCHINA

# Pull in the GitHub Pages workflow commit that GitHub added
git fetch origin
git merge -m "Merge GitHub Pages workflow" origin/main

push_batch() {
    msg="$1"
    shift
    git add "$@"
    git commit -m "$msg"
    if ! git push origin chunked2:main; then
        echo "Retrying push..."
        sleep 5
        git pull --no-edit origin main || true
        git push origin chunked2:main
    fi
}

# General images (excluding gallery and already-pushed products)
push_batch "content: general images" \
  www/AEETHER/LOGO.svg \
  www/AEETHER/image/about-us \
  www/AEETHER/image/contact-us \
  www/AEETHER/image/countries \
  www/AEETHER/image/faq \
  www/AEETHER/image/grades \
  www/AEETHER/image/index \
  www/AEETHER/image/logos \
  www/AEETHER/image/media \
  www/AEETHER/image/solutions \
  www/AEETHER/image/tools \
  www/AEETHER/image/*.jpg \
  www/AEETHER/image/*.svg

# Gallery images
push_batch "content: gallery images" www/AEETHER/image/gallery

# Large media folders one at a time
for d in www/AEETHER/media/media-129 www/AEETHER/media/media-128; do
    name=$(basename "$d")
    push_batch "content: media ${name}" "$d"
done

# Remaining media
push_batch "content: remaining media" www/AEETHER/media

# Any leftover project files
if [ -n "$(git status --porcelain)" ]; then
    git add .
    git commit -m "content: remaining files"
    git push origin chunked2:main
fi

echo "CONTINUE PUSH COMPLETE"
