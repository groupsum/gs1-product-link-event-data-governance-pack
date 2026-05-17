from __future__ import annotations

import unittest

from ssot_pack_gs1_product_link_event_data import (
    __pypi_package_name__,
    __ssot_package_name__,
    load_document_manifest,
    load_pack_manifest,
    load_pack_metadata,
    load_pack_schema_version,
    read_packaged_document_text,
)


class GovernancePackManifestTests(unittest.TestCase):
    def test_pack_metadata_contract_is_exposed(self) -> None:
        metadata = load_pack_metadata()
        self.assertEqual("ssot-pack-gs1-product-link-event-data", __ssot_package_name__)
        self.assertEqual("ssot-pack-gs1-product-link-event-data", __pypi_package_name__)
        self.assertEqual("1.0.0", metadata["schema_version"])
        self.assertEqual("ssot-pack-gs1-product-link-event-data", metadata["ssot_package_name"])
        self.assertEqual("pack:gs1-product-link-event-data", metadata["origin"]["id"])
        self.assertEqual("ssot_pack_gs1_product_link_event_data", metadata["origin"]["import_name"])
        self.assertEqual("governance-pack", metadata["origin"]["kind"])
        self.assertEqual("extension-pack", metadata["trust"]["origin"])
        self.assertEqual("extension-pack:ssot-pack-gs1-product-link-event-data", metadata["trust"]["reservation_owner"])
        self.assertFalse(metadata["trust"]["trusted_by_default"])
        self.assertEqual("1.0.0", load_pack_schema_version())

    def test_pack_manifest_contract_is_exposed(self) -> None:
        manifest = load_pack_manifest()
        self.assertEqual("ssot-pack-gs1-product-link-event-data", manifest["metadata"]["origin"]["package_name"])
        self.assertEqual(5, len(manifest["documents"]["adr"]))
        self.assertEqual(4, len(manifest["documents"]["spec"]))

    def test_packaged_documents_are_readable(self) -> None:
        adr_manifest = load_document_manifest("adr")
        spec_manifest = load_document_manifest("spec")
        self.assertEqual("adr:gs1-digital-link-uri-policy", adr_manifest[0]["id"])
        self.assertEqual("spc:gs1-digital-link-contract", spec_manifest[0]["id"])
        self.assertIn("GS1 Digital Link URI Policy", read_packaged_document_text("adr", adr_manifest[0]["filename"]))
        self.assertIn("GS1 Product Link And Visibility Events", read_packaged_document_text("spec", spec_manifest[0]["filename"]))

    def test_packaged_adr_documents_are_downstream_portable(self) -> None:
        forbidden_terms = [
            "pack:",
            "This pack",
            "extension-pack",
            "governance-pack",
            "ssot-pack",
        ]
        for row in load_document_manifest("adr"):
            text = read_packaged_document_text("adr", row["filename"])
            for term in forbidden_terms:
                self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
