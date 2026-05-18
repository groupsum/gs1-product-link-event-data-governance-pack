# gs1-product-link-event-data-governance-pack

Installable SSOT governance pack for GS1 Digital Link, GS1 resolver behavior, EPCIS/CBV visibility events, product identifiers, and product master data.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:gs1-product-link-event-data`
- Priority: `P4.2`
- PyPI package: `gs1-product-link-event-data-governance-pack`
- Import package: `ssot_pack_gs1_product_link_event_data`
- GitHub repository: `groupsum/gs1-product-link-event-data-governance-pack`
- Reservation owner: `extension-pack:gs1-product-link-event-data-governance-pack`

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

- `spc:gs1-digital-link-uri-syntax-requirements` - GS1 Digital Link URI Syntax Requirements
- `spc:gs1-digital-link-identifier-requirements` - GS1 Digital Link Identifier Requirements
- `spc:gs1-conformant-resolver-requirements` - GS1 Conformant Resolver Requirements
- `spc:gs1-web-vocabulary-product-requirements` - GS1 Web Vocabulary Product Requirements
- `spc:gs1-web-vocabulary-organization-location-requirements` - GS1 Web Vocabulary Organization Location Requirements
- `spc:epcis-event-envelope-requirements` - EPCIS Event Envelope Requirements
- `spc:epcis-event-type-requirements` - EPCIS Event Type Requirements
- `spc:cbv-business-step-disposition-requirements` - CBV Business Step Disposition Requirements
- `spc:gs1-product-master-data-attribute-requirements` - GS1 Product Master Data Attribute Requirements
- `spc:gs1-general-specifications-identifier-requirements` - GS1 General Specifications Identifier Requirements
- `spc:gdsn-product-data-synchronization-requirements` - GDSN Product Data Synchronization Requirements
- `spc:gs1-product-link-event-audit-evidence-requirements` - GS1 Product Link Event Audit Evidence Requirements

## Install With uv

```bash
uv add gs1-product-link-event-data-governance-pack
uv add ssot-registry gs1-product-link-event-data-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install gs1-product-link-event-data-governance-pack
uvx --from ssot-registry ssot pack sync . gs1-product-link-event-data-governance-pack
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
- PyPI package: https://pypi.org/project/gs1-product-link-event-data-governance-pack/
- SSOT Registry: https://pypi.org/project/ssot-registry/
