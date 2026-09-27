# Extended family tree

A sourced, editable first pass at one extended family tree, transcribed from seven photographed sheets. Open [`family_tree.html`](family_tree.html) locally for the full connected tree. All 158 people appear on one canvas. Drag and zoom to explore, use the minimap or branch list to move around, and search to jump directly to a person. Select a person for details, source photos, and ancestor or descendant highlighting. The viewer works offline when the `photos/` folder stays beside it.

## Contents

- `master_family.json`: person records, relationships, source photos and confidence flags.
- `people.csv` and `relationships.csv`: spreadsheet friendly exports.
- `branch_*.json`: separate transcriptions for each photo. The 3618–3620 images show overlapping versions of one handwritten sheet.
- `photos/`: seven source images.
- `REVIEW_QUEUE.csv` and `REVIEW.md`: candidate identity matches, nicknames, and unresolved relationships.
- `viewer_template.html` and `build_view.py`: build the standalone visual tree from `master_family.json` (`python3 build_view.py`).
- `build_tree.py` and `curate.py`: reproduce the original first transcription. Do not rerun these after editing the master JSON; they would overwrite subsequent corrections.

**Status:** 158 people, 203 relationships. This is an initial transcription, not verified genealogy. A `tentative` relationship requires checking the photograph or asking family. Names shared between photos were merged only when the branch context supported the match; the review queue records the remaining questions. Nicknames appear in `aliases` without inventing full names.

## Editing

Use stable person IDs. Update `master_family.json` for a corrected person or relationship, cite a photo or family source, and regenerate CSV/viewer outputs as needed. Do not replace a tentative edge with a clear edge until its relationship is confirmed. Some people here are living, including children; use care when sharing excerpts outside this repository.
