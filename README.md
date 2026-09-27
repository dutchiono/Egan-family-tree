# Extended family tree

A sourced, editable first pass at one extended family tree, transcribed from seven photographed sheets. Open [`family_tree.html`](family_tree.html) locally to browse a person’s parents, partners, and children. The viewer works offline.

## Contents

- `master_family.json`: person records, relationships, source photos and confidence flags.
- `people.csv` and `relationships.csv`: spreadsheet friendly exports.
- `branch_*.json`: separate transcriptions for each photo. The 3618–3620 images show overlapping versions of one handwritten sheet.
- `photos/`: seven source images.
- `REVIEW_QUEUE.csv` and `REVIEW.md`: candidate identity matches, nicknames, and unresolved relationships.
- `build_tree.py`, `curate.py`, `build_view.py`: the scripts that reproduce the first pass (`python3 build_tree.py && python3 curate.py && python3 build_view.py`). The master JSON is the working source for subsequent corrections.

**Status:** 158 people, 203 relationships. This is an initial transcription, not verified genealogy. A `tentative` relationship requires checking the photograph or asking family. Names shared between photos were merged only when the branch context supported the match; the review queue records the remaining questions. Nicknames appear in `aliases` without inventing full names.

## Editing

Use stable person IDs. Update `master_family.json` for a corrected person or relationship, cite a photo or family source, and regenerate CSV/viewer outputs as needed. Do not replace a tentative edge with a clear edge until its relationship is confirmed. Some people here are living, including children; use care when sharing excerpts outside this repository.
