---
source_url: https://en.wikipedia.org/wiki/Software_testing
ingested: 2026-07-09
---

# Software Testing — Wikipedia

## Key Definitions

**Software testing** is the act of checking whether software meets its intended objectives and satisfies expectations. It can provide objective, independent information about the quality of software and the risk of its failure.

**Fundamental limitation:** Testing cannot determine correctness for all scenarios. It cannot find all bugs.

## Core Concepts

### Oracle Problem
Software testing employs principles and mechanisms to recognize a problem. Examples of oracles include:
- Specifications
- Contracts (Design by Contract)
- Comparable products
- Past versions of the same product
- User or customer expectations
- Relevant standards and applicable laws

### Test Pyramid
The "test pyramid" suggests:
1. **Unit tests** — most tests (base of pyramid)
2. **Integration tests** — smaller set
3. **End-to-end (E2E) tests** — fewest at top

### Static vs Dynamic Testing
- **Static testing**: Reviews, walkthroughs, inspections — verifying without running code
- **Dynamic testing**: Executing programmed code with test cases
- **Passive testing**: Verifying system behavior without interaction, looking at logs/traces

### Exploratory Testing (Cem Kaner, 1984)
"A style of software testing that emphasizes the personal freedom and responsibility of the individual tester to continually optimize the quality of his/her work by treating test-related learning, test design, test execution, and test result interpretation as mutually supportive activities that run in parallel throughout the project."

### White-Box vs Black-Box vs Grey-Box
- **White-box** (clear/glass/structural): Tester uses internal perspective + programming skills to design test cases. Tests paths through the code. Usually done at unit level.
- **Black-box**: Tests functionality without knowledge of internal structure.
- **Grey-box**: Hybrid approach combining aspects of both.

### Testing Levels
1. **Unit testing** — isolated source code, component/module level
2. **Integration testing** — multiple components/modules tested together, focusing on interactions and data exchange
3. **System testing** — complete integrated system tested
4. **Acceptance testing** — validating end-to-end behavior

### NIST 2002 Study
Software bugs cost the U.S. economy $59.5 billion annually. More than one-third of this cost could be avoided with better software testing.

## Related Concepts
- Test oracle
- Test case design
- Combinatorics for maximizing coverage
- Non-functional requirements: testability, scalability, maintainability, performance, security

## Source
https://en.wikipedia.org/wiki/Software_testing
Published: 2001-12-05
