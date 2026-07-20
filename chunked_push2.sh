#!/usr/bin/env bash
set -e
cd /c/Users/WIN10/STEELCHINA

# Start from a clean orphan branch with an empty index but all files on disk
if git show-ref --verify --quiet refs/heads/chunked2; then
    git branch -D chunked2
fi
git checkout main
git checkout --orphan chunked2
git rm --cached -rf .

# Helper: commit then push, retry once on network error
push_batch() {
    msg="$1"
    shift
    git add "$@"
    git commit -m "$msg"
    if ! git push origin chunked2:main; then
        echo "Retrying push..."
        sleep 5
        git push origin chunked2:main
    fi
}

# 1. small project files
push_batch "chore: project tools" .gitignore *.py *.log chunked_push2.sh

# 2. root and top-level AEETHER pages
push_batch "content: root and top-level pages" \
  www/index.html \
  www/AEETHER/*.html www/AEETHER/*.js www/AEETHER/*.css www/AEETHER/*.php \
  www/AEETHER/favicon.ico

# 3. grades, solutions, tools, gallery pages
push_batch "content: grades solutions tools gallery" \
  www/AEETHER/grades www/AEETHER/solutions www/AEETHER/tools www/AEETHER/gallery

# 4. catalog PDFs
push_batch "content: catalog" www/AEETHER/catalog

# 5. product pages and detail
push_batch "content: product pages" www/AEETHER/products

# 6. product images
push_batch "content: product images" www/AEETHER/image/products

# 7. gallery images
push_batch "content: gallery images" www/AEETHER/image/gallery

# 8. other general images
push_batch "content: general images" \
  www/AEETHER/image/solutions www/AEETHER/image/contact-us \
  www/AEETHER/image/about-us www/AEETHER/image/grades \
  www/AEETHER/image/index www/AEETHER/image/logos \
  www/AEETHER/image/faq www/AEETHER/image/tools \
  www/AEETHER/image/countries www/AEETHER/image/*.jpg \
  www/AEETHER/image/*.svg

# 9. large media folders one at a time
for d in www/AEETHER/media/media-129 www/AEETHER/media/media-128; do
    name=$(basename "$d")
    push_batch "content: media ${name}" "$d"
done

# 10. remaining media
push_batch "content: remaining media" www/AEETHER/media

# Catch anything left
if [ -n "$(git status --porcelain)" ]; then
    git add .
    git commit -m "content: remaining files"
    git push origin chunked2:main
fi

echo "CHUNKED PUSH COMPLETE"
