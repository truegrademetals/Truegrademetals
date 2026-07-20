#!/usr/bin/env bash
set -e
cd /c/Users/WIN10/STEELCHINA

# Create a fresh orphan branch so we can build history in small commits
if git show-ref --verify --quiet refs/heads/chunked; then
    git branch -D chunked
fi
git checkout --orphan chunked

# Commit 1: project scripts / logs / gitignore
git add .gitignore *.py *.log
git commit -m "chore: project tools"
git push -u origin chunked:main

# Commit 2: root index and top-level AEETHER HTML/JS/CSS/PHP files
git add www/index.html www/AEETHER/*.html www/AEETHER/*.js www/AEETHER/*.css www/AEETHER/*.php www/AEETHER/favicon.ico
git commit -m "content: aeether html/js/css/php core"
git push

# Commit 3: grades, solutions, tools, gallery pages
git add www/AEETHER/grades www/AEETHER/solutions www/AEETHER/tools www/AEETHER/gallery
git commit -m "content: grades, solutions, tools, gallery"
git push

# Commit 4: catalog PDFs
git add www/AEETHER/catalog
git commit -m "content: catalog pdfs"
git push

# Commit 5: product pages and product images
git add www/AEETHER/products www/AEETHER/image/products
git commit -m "content: product pages and images"
git push

# Commit 6: gallery images + smaller image folders
git add www/AEETHER/image/gallery www/AEETHER/image/solutions www/AEETHER/image/contact-us \
       www/AEETHER/image/about-us www/AEETHER/image/grades www/AEETHER/image/index \
       www/AEETHER/image/logos www/AEETHER/image/faq www/AEETHER/image/tools \
       www/AEETHER/image/countries www/AEETHER/image/*.jpg www/AEETHER/image/*.svg
git commit -m "content: gallery and general images"
git push

# Commit 7: large media folders split individually
for d in www/AEETHER/media/media-129 www/AEETHER/media/media-128; do
    if [ -d "$d" ]; then
        name=$(basename "$d")
        git add "$d"
        git commit -m "content: media ${name}"
        git push
    fi
done

# Commit 8: remaining media
git add www/AEETHER/media
git commit -m "content: remaining media"
git push

# Commit 9: anything left (should be empty, but just in case)
if [ -n "$(git status --porcelain)" ]; then
    git add .
    git commit -m "content: remaining files"
    git push
fi

echo "CHUNKED PUSH COMPLETE"
