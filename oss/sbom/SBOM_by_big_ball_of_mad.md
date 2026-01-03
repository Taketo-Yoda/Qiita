# Software Bill of Materials (SBOM)

## Component Inventory

A comprehensive list of all software components and libraries included in this project.

| Package | Version | License | Description |
|---------|---------|---------|-------------|
| annotated-types | 0.7.0 | MIT License | Reusable constraint types to use with typing.Annotated |
| colorama | 0.4.6 | BSD License | Cross-platform colored terminal text. |
| exceptiongroup | 1.3.1 | MIT License | Backport of PEP 654 (exception groups) |
| iniconfig | 2.3.0 | MIT | brain-dead simple config-ini parsing |
| ja-complete | 0.1.0 | MIT | Lightweight offline Japanese input completion library |
| janome | 0.5.0 | AL2 | Japanese morphological analysis engine. |
| packaging | 25.0 | Apache Software License | Core utilities for Python packages |
| pluggy | 1.6.0 | MIT | plugin and hook calling mechanisms for python |
| pydantic | 2.12.5 | MIT | Data validation using Python type hints |
| pydantic-core | 2.41.5 | MIT | Core functionality for Pydantic validation and serialization |
| pygments | 2.19.2 | BSD-2-Clause | Pygments is a syntax highlighting package written in Python. |
| pytest | 9.0.2 | MIT | pytest: simple powerful testing with Python |
| ruff | 0.14.10 | MIT License | An extremely fast Python linter and code formatter, written in Rust. |
| tomli | 2.3.0 | MIT | A lil' TOML parser |
| typing-extensions | 4.15.0 | PSF-2.0 | Backported and Experimental Type Hints for Python 3.9+ |
| typing-inspection | 0.4.2 | MIT | Runtime typing introspection tools |

## Direct Dependencies

Primary packages explicitly defined in the project configuration(e.g., pyproject.toml).

| Package | Version | License | Description |
|---------|---------|---------|-------------|
| janome | 0.5.0 | AL2 | Japanese morphological analysis engine. |
| pydantic | 2.12.5 | MIT | Data validation using Python type hints |
| pytest | 9.0.2 | MIT | pytest: simple powerful testing with Python |
| ruff | 0.14.10 | MIT License | An extremely fast Python linter and code formatter, written in Rust. |

## Transitive Dependencies

Secondary dependencies introduced by the primary packages.

### Dependencies for pydantic

| Package | Version | License | Description |
|---------|---------|---------|-------------|
| annotated-types | 0.7.0 | MIT License | Reusable constraint types to use with typing.Annotated |
| pydantic-core | 2.41.5 | MIT | Core functionality for Pydantic validation and serialization |
| typing-extensions | 4.15.0 | PSF-2.0 | Backported and Experimental Type Hints for Python 3.9+ |
| typing-inspection | 0.4.2 | MIT | Runtime typing introspection tools |

### Dependencies for pytest

| Package | Version | License | Description |
|---------|---------|---------|-------------|
| colorama | 0.4.6 | BSD License | Cross-platform colored terminal text. |
| exceptiongroup | 1.3.1 | MIT License | Backport of PEP 654 (exception groups) |
| typing-extensions | 4.15.0 | PSF-2.0 | Backported and Experimental Type Hints for Python 3.9+ |
| iniconfig | 2.3.0 | MIT | brain-dead simple config-ini parsing |
| packaging | 25.0 | Apache Software License | Core utilities for Python packages |
| pluggy | 1.6.0 | MIT | plugin and hook calling mechanisms for python |
| pygments | 2.19.2 | BSD-2-Clause | Pygments is a syntax highlighting package written in Python. |
| tomli | 2.3.0 | MIT | A lil' TOML parser |

