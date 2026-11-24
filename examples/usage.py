"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_gs1_product_link_event_data import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:gs1-digital-link-uri-syntax-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-gs1-digital-link-uri-syntax-requirements.yaml"
