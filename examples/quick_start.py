"""Inspect the installed pack identity."""

from ssot_pack_gs1_product_link_event_data import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:gs1-product-link-event-data"
print(metadata["origin"]["id"])
