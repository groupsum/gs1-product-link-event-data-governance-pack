# ssot-pack-gs1-product-link-event-data

Installable SSOT governance pack for GS1 Digital Link, GS1 resolver behavior, EPCIS/CBV visibility events, product identifiers, and product master data.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:gs1-product-link-event-data`
- Priority: `P4.2`
- PyPI package: `ssot-pack-gs1-product-link-event-data`
- Import package: `ssot_pack_gs1_product_link_event_data`
- GitHub repository: `groupsum/gs1-product-link-event-data-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-gs1-product-link-event-data`

## Domain Focus

GS1 Product Link And Visibility Events

## Authority Sources

- GS1 Web Vocabulary
- GS1 Digital Link
- GS1 Digital Link URI Syntax
- GS1 Conformant Resolver
- EPCIS and CBV
- GS1 General Specifications
- GS1 Global Data Model
- GDSN

## Included ADRs

- `adr:gs1-digital-link-uri-policy` - GS1 Digital Link URI Policy
- `adr:gs1-resolver-behavior-policy` - GS1 Resolver Behavior Policy
- `adr:gs1-web-vocabulary-publication-policy` - GS1 Web Vocabulary Publication Policy
- `adr:epcis-cbv-visibility-event-policy` - EPCIS CBV Visibility Event Policy
- `adr:gs1-product-master-data-policy` - GS1 Product Master Data Policy

## Included SPECs

- `spc:gs1-digital-link-contract` - GS1 Digital Link Contract
- `spc:gs1-resolver-contract` - GS1 Resolver Contract
- `spc:epcis-cbv-event-contract` - EPCIS CBV Event Contract
- `spc:gs1-product-master-data-contract` - GS1 Product Master Data Contract

## Install With uv

```bash
uv add ssot-pack-gs1-product-link-event-data
uv add ssot-registry ssot-pack-gs1-product-link-event-data
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-gs1-product-link-event-data
uvx --from ssot-registry ssot pack sync . ssot-pack-gs1-product-link-event-data
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_gs1_product_link_event_data import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/gs1-product-link-event-data-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-gs1-product-link-event-data/
- SSOT Registry: https://pypi.org/project/ssot-registry/
