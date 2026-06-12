#!/bin/bash
# Compile the P2P Open Distribution edition of Book 3 and generate torrent files
set -e

WORKSPACE="/home/user0/git/publishing"
BOOK_DIR="${WORKSPACE}/200_amazon_kdp/03_survival_physics/kdp"
MANUSCRIPT_DIR="${BOOK_DIR}/manuscript"
HANDOFF_DIR="${BOOK_DIR}/handoff"
TORRENT_DIR="${WORKSPACE}/published/torrents/03_survival_physics"

mkdir -p "${TORRENT_DIR}"

# 1. Back up original copyright file
echo "Backing up original copyright file..."
cp "${MANUSCRIPT_DIR}/copyright.md" "${MANUSCRIPT_DIR}/copyright.md.bak"

# 2. Write the Open Distribution copyright file
echo "Writing P2P Open Distribution notice to copyright.md..."
cat << 'EOF' > "${MANUSCRIPT_DIR}/copyright.md"
OPEN DISTRIBUTION NOTICE

Copyright © 2026 Charles J. DiBella

This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0).

Digital Rights Management is disabled. Digital distribution via BitTorrent networks, IPFS, and public directories is explicitly authorized and encouraged. Local printing for personal study and non-commercial educational use is permitted.

Official Torrent Info Hash: [Self-referential hash omitted from binary to prevent cryptographic loops]

Published by Charles J. DiBella
Los Angeles, California

First edition, 2026
EOF

# 3. Compile the P2P EPUB
echo "Compiling P2P EPUB..."
if [ -f "${HANDOFF_DIR}/the_moral_physics_of_survival.epub" ]; then
  echo "Backing up original EPUB file..."
  cp "${HANDOFF_DIR}/the_moral_physics_of_survival.epub" "${HANDOFF_DIR}/the_moral_physics_of_survival.epub.bak"
fi

python3 "${WORKSPACE}/scripts/200_amazon_kdp/compile_book.py" --book 3 --format epub

# Rename compiled EPUB to indicate P2P edition
mv "${HANDOFF_DIR}/the_moral_physics_of_survival.epub" "${HANDOFF_DIR}/the_moral_physics_of_survival_p2p.epub"
echo "P2P EPUB compiled: ${HANDOFF_DIR}/the_moral_physics_of_survival_p2p.epub"

if [ -f "${HANDOFF_DIR}/the_moral_physics_of_survival.epub.bak" ]; then
  echo "Restoring original EPUB file..."
  mv "${HANDOFF_DIR}/the_moral_physics_of_survival.epub.bak" "${HANDOFF_DIR}/the_moral_physics_of_survival.epub"
fi

# 4. Compile the P2P booklet PDF
echo "Compiling P2P Booklet PDF..."
"${WORKSPACE}/scripts/_archive/compile_any_booklet.sh" "${MANUSCRIPT_DIR}/epub_source.md" the_moral_physics_of_survival_p2p

# Move generated booklet PDF to handoff
mv "${MANUSCRIPT_DIR}/the_moral_physics_of_survival_p2p_booklet-book.pdf" "${HANDOFF_DIR}/"
echo "P2P Booklet PDF compiled: ${HANDOFF_DIR}/the_moral_physics_of_survival_p2p_booklet-book.pdf"

# 5. Restore original copyright file
echo "Restoring original copyright file..."
mv "${MANUSCRIPT_DIR}/copyright.md.bak" "${MANUSCRIPT_DIR}/copyright.md"

# 6. Generate Torrents using helper script
echo "Generating torrent files..."
python3 "${WORKSPACE}/scripts/create_torrent.py" \
  "${HANDOFF_DIR}/the_moral_physics_of_survival_p2p.epub" \
  "${TORRENT_DIR}/the_moral_physics_of_survival_p2p.epub.torrent"

python3 "${WORKSPACE}/scripts/create_torrent.py" \
  "${HANDOFF_DIR}/the_moral_physics_of_survival_p2p_booklet-book.pdf" \
  "${TORRENT_DIR}/the_moral_physics_of_survival_p2p_booklet-book.pdf.torrent"

echo "Torrent setup complete!"
