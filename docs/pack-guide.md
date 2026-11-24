# GS1 Product Link And Visibility Events pack guide

Installable SSOT governance pack for GS1 Digital Link, GS1 resolver behavior, EPCIS/CBV visibility events, product identifiers, and product master data.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `gs1-product-link-event-data-governance-pack` is an installable SSOT governance pack for GS1 Product Link And Visibility Events. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern gs1 product link and visibility events, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`gs1-product-link-event-data-governance-pack`](https://pypi.org/project/gs1-product-link-event-data-governance-pack/)
- GitHub package repository: [`groupsum/gs1-product-link-event-data-governance-pack`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack)
- Import package: `ssot_pack_gs1_product_link_event_data`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:gs1-product-link-event-data`
- PyPI package: `gs1-product-link-event-data-governance-pack`
- Import package: `ssot_pack_gs1_product_link_event_data`
- GitHub repository: [groupsum/gs1-product-link-event-data-governance-pack](https://github.com/groupsum/gs1-product-link-event-data-governance-pack)
- Reservation owner: `extension-pack:gs1-product-link-event-data-governance-pack`

## Domain Focus

GS1 Product Link And Visibility Events

## Authority Sources

- [GS1 Web Vocabulary](https://www.gs1.org/gs1-web-vocabulary)
- [GS1 Digital Link](https://www.gs1.org/standards/gs1-digital-link)
- [GS1 Digital Link URI Syntax](https://ref.gs1.org/standards/digital-link/uri-syntax/)
- [GS1 Conformant Resolver](https://ref.gs1.org/standards/resolver/)
- [EPCIS](https://ref.gs1.org/standards/epcis/) and [CBV](https://ref.gs1.org/standards/cbv/)
- [GS1 General Specifications](https://www.gs1.org/standards/barcodes-epcrfid-id-keys/gs1-general-specifications)
- [GS1 Global Data Model](https://www.gs1.org/standards/gs1-global-data-model)
- [GDSN](https://www.gs1.org/services/gdsn)

## Included ADRs

- [`adr:gs1-digital-link-uri-policy`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/adr/ADR-1001-gs1-digital-link-uri-policy.yaml) - GS1 Digital Link URI Policy
- [`adr:gs1-resolver-behavior-policy`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/adr/ADR-1002-gs1-resolver-behavior-policy.yaml) - GS1 Resolver Behavior Policy
- [`adr:gs1-web-vocabulary-publication-policy`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/adr/ADR-1003-gs1-web-vocabulary-publication-policy.yaml) - GS1 Web Vocabulary Publication Policy
- [`adr:epcis-cbv-visibility-event-policy`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/adr/ADR-1004-epcis-cbv-visibility-event-policy.yaml) - EPCIS CBV Visibility Event Policy
- [`adr:gs1-product-master-data-policy`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/adr/ADR-1005-gs1-product-master-data-policy.yaml) - GS1 Product Master Data Policy

## Included SPECs

- [`spc:gs1-digital-link-uri-syntax-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2001-gs1-digital-link-uri-syntax-requirements.yaml) - GS1 Digital Link URI Syntax Requirements
- [`spc:gs1-digital-link-identifier-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2002-gs1-digital-link-identifier-requirements.yaml) - GS1 Digital Link Identifier Requirements
- [`spc:gs1-conformant-resolver-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2003-gs1-conformant-resolver-requirements.yaml) - GS1 Conformant Resolver Requirements
- [`spc:gs1-web-vocabulary-product-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2004-gs1-web-vocabulary-product-requirements.yaml) - GS1 Web Vocabulary Product Requirements
- [`spc:gs1-web-vocabulary-organization-location-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2005-gs1-web-vocabulary-organization-location-requirements.yaml) - GS1 Web Vocabulary Organization Location Requirements
- [`spc:epcis-event-envelope-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2006-epcis-event-envelope-requirements.yaml) - EPCIS Event Envelope Requirements
- [`spc:epcis-event-type-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2007-epcis-event-type-requirements.yaml) - EPCIS Event Type Requirements
- [`spc:cbv-business-step-disposition-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2008-cbv-business-step-disposition-requirements.yaml) - CBV Business Step Disposition Requirements
- [`spc:gs1-product-master-data-attribute-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2009-gs1-product-master-data-attribute-requirements.yaml) - GS1 Product Master Data Attribute Requirements
- [`spc:gs1-general-specifications-identifier-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2010-gs1-general-specifications-identifier-requirements.yaml) - GS1 General Specifications Identifier Requirements
- [`spc:gdsn-product-data-synchronization-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2011-gdsn-product-data-synchronization-requirements.yaml) - GDSN Product Data Synchronization Requirements
- [`spc:gs1-product-link-event-audit-evidence-requirements`](https://github.com/groupsum/gs1-product-link-event-data-governance-pack/blob/master/src/ssot_pack_gs1_product_link_event_data/templates/specs/SPEC-2012-gs1-product-link-event-audit-evidence-requirements.yaml) - GS1 Product Link Event Audit Evidence Requirements

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

- GitHub package repository: [groupsum/gs1-product-link-event-data-governance-pack](https://github.com/groupsum/gs1-product-link-event-data-governance-pack)
- PyPI package: [gs1-product-link-event-data-governance-pack](https://pypi.org/project/gs1-product-link-event-data-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative ownership boundary

Declared canonical GS1 ownership relative to commerce semantics.
