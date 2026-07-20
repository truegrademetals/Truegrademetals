#!/usr/bin/env bash
set -e
cd /c/Users/WIN10/STEELCHINA

REMOTE=truegrademetals
TARGET_BRANCH=main

# Create a fresh orphan branch for chunked deployment
if git show-ref --verify --quiet refs/heads/deploy; then
    git branch -D deploy
fi
git checkout --orphan deploy
git rm --cached -rf . >/dev/null 2>&1 || true

push_batch() {
    msg="$1"
    shift
    if [ $# -eq 0 ]; then
        echo "Skipping empty batch: $msg"
        return
    fi
    echo "Committing: $msg"
    git add "$@"
    git commit -m "$msg" >/dev/null
    echo "Pushing: $msg"
    if ! git push --force "$REMOTE" deploy:"$TARGET_BRANCH"; then
        echo "Retrying: $msg"
        sleep 5
        git push --force "$REMOTE" deploy:"$TARGET_BRANCH"
    fi
}

echo "=== Starting chunked push to $REMOTE/$TARGET_BRANCH ==="

# 1. Root project files + workflow
push_batch "chore: project tools and workflow" \
  .gitignore \
  .github/workflows/static.yml \
  *.py *.sh *.log

# 2. docs root and top-level non-media assets
push_batch "content: docs root and site core" \
  docs/index.html docs/tgm/favicon.ico \
  docs/tgm/*.html docs/tgm/*.css docs/tgm/*.js docs/tgm/*.svg \
  docs/tgm/nav.css docs/tgm/nav.js docs/tgm/chemical-all.css

# 3. Product shared/detail files and generic form pages
push_batch "content: generic product pages and shared assets" \
  docs/tgm/products/products-all.css \
  docs/tgm/products/products-all.js \
  docs/tgm/products/detail \
  docs/tgm/products/nickel-alloy-*.html

# 4. Monel product pages
push_batch "content: monel product pages" \
  docs/tgm/products/monel-*.html

# 5. Inconel product pages
push_batch "content: inconel product pages" \
  docs/tgm/products/inconel-*.html

# 6. Incoloy product pages
push_batch "content: incoloy product pages" \
  docs/tgm/products/incoloy-*.html

# 7. Hastelloy product pages
push_batch "content: hastelloy product pages" \
  docs/tgm/products/hastelloy-*.html

# 8. Catalog PDFs
push_batch "content: catalog pdfs" \
  docs/tgm/catalog

# 9. Product images
push_batch "content: product images" \
  docs/tgm/image/products

# 10. Gallery images
push_batch "content: gallery images" \
  docs/tgm/image/gallery

# 11. Other general images
push_batch "content: general images" \
  docs/tgm/image/solutions \
  docs/tgm/image/contact-us \
  docs/tgm/image/about-us \
  docs/tgm/image/grades \
  docs/tgm/image/index \
  docs/tgm/image/logos \
  docs/tgm/image/faq \
  docs/tgm/image/tools \
  docs/tgm/image/countries \
  docs/tgm/image/*.jpg \
  docs/tgm/image/*.svg

# 12. Large media folders split in halves to keep pushes small
split_push_media() {
    folder="$1"
    name=$(basename "$folder")
    files=$(git ls-files "$folder" | sort)
    total=$(echo "$files" | wc -l)
    half=$(( (total + 1) / 2 ))
    first=$(echo "$files" | head -n "$half")
    second=$(echo "$files" | tail -n +$((half + 1)))
    if [ -n "$first" ]; then
        push_batch "content: media ${name} part 1" $(echo "$first")
    fi
    if [ -n "$second" ]; then
        push_batch "content: media ${name} part 2" $(echo "$second")
    fi
}

split_push_media docs/tgm/media/media-128
split_push_media docs/tgm/media/media-129

# 13. Remaining media folders
push_batch "content: remaining media" \
  docs/tgm/media/alloy-knowledge \
  docs/tgm/media/applications \
  docs/tgm/media/chemical-element \
  docs/tgm/media/element-video \
  docs/tgm/media/leads \
  $(git ls-files docs/tgm/media | grep -vE '^docs/tgm/media/(media-128|media-129)/' | xargs -r echo)

# 14. Anything left (should be empty, but just in case)
remaining=$(git status --porcelain | awk '{print $2}')
if [ -n "$remaining" ]; then
    push_batch "content: remaining files" $remaining
fi

echo "=== CHUNKED PUSH COMPLETE ==="
