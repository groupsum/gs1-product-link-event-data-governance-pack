"""Resolve and read a packaged specification without synchronizing it."""

from ssot_pack_gs1_product_link_event_data import load_document_manifest, read_packaged_document_text

spec = next(row for row in load_document_manifest("spec") if row["id"] == "spc:gs1-digital-link-uri-syntax-requirements")
document = read_packaged_document_text("spec", spec["filename"])
assert spec["id"] in document
